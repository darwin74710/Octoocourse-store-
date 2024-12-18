from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.db import connection
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError



def home(request):
    if request.user.is_authenticated:
        user_type = request.session.get('user_type')  
        if request.user.is_superuser:  
            return redirect('administratorAdmin') 
        elif user_type == 'estudiante':
            return redirect('Inicio')  
        elif user_type == 'empresa':
            return redirect('inicioE')  
    return render(request, 'login/home.html')


def inicioS(request):
    if request.method == 'POST':
        correo = request.POST['correo']
        password = request.POST['password']

        user_type = None
        id_estudiante = None
        nit_empresa = None
        cursor = connection.cursor()

        # Con esto validamos si es un correo lo que ingresamos.
        validarCorreo = True
        try:
            validate_email(correo)
        except ValidationError:
            validarCorreo = False

        # Con esto busco el superUsuario de django en caso de que no sea un correo lo que validamos.
        if not validarCorreo:
            try:
                usuario = User.objects.get(username=correo)
                if usuario.is_superuser and usuario.check_password(password):
                    login(request, usuario)
                    messages.success(request, "Inicio de sesión exitoso como administrador")
                    return redirect(reverse('administrator'))
            except User.DoesNotExist:
                pass

        if validarCorreo:
            cursor.execute("SELECT id_estudiante, password_estudiante FROM estudiantes WHERE correo_estudiante = %s", [correo])
            estudiante = cursor.fetchone()

            if estudiante:
                user_type = 'estudiante'
                id_estudiante = estudiante[0]  
                stored_password = estudiante[1]  
            else:
                cursor.execute("SELECT password_emp, nit FROM empresas WHERE correo_emp = %s", [correo])
                empresa = cursor.fetchone()
                if empresa:
                    user_type = 'empresa'
                    stored_password = empresa[0] 
                    nit_empresa = empresa[1] 

        if user_type and check_password(password, stored_password):
            user, created = User.objects.get_or_create(username=correo)

            if created:
                user.set_password(password)
                user.save()

            login(request, user)

            request.session['user_type'] = user_type

            if user_type == 'estudiante':
                request.session['id_estudiante'] = id_estudiante

            if user_type == 'empresa':
                request.session['nit'] = nit_empresa

            if user_type == 'estudiante':
                messages.success(request, "Inicio de sesión exitoso para estudiante")
                return redirect(reverse('Inicio'))
            elif user_type == 'empresa':
                messages.success(request, "Inicio de sesión exitoso para empresa")
                return redirect(reverse('inicioE'))
        else:
            error_message = "Correo electrónico o contraseña incorrectos. Por favor, inténtelo de nuevo."
            return render(request, 'login/InicioS.html', {'error_message': error_message})

    return render(request, 'login/InicioS.html')