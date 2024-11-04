from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.db import connection
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password



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
        cursor = connection.cursor()

        cursor.execute("SELECT password_estudiante FROM estudiantes WHERE correo_estudiante = %s", [correo])
        estudiante = cursor.fetchone()

        if estudiante:
            user_type = 'estudiante'
            stored_password = estudiante[0]  

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

            if user_type == 'empresa':
                request.session['nit'] = nit_empresa
                

            if user_type == 'estudiante':
                messages.success(request, "Inicio de sesión exitoso para estudiante")
                return redirect(reverse('Inicio'))  
            elif user_type == 'empresa':
                messages.success(request, "Inicio de sesión exitoso para empresa")
                return redirect(reverse('inicioE'))  
        else:
            messages.error(request, "Correo o contraseña incorrectos")

    return render(request, 'login/InicioS.html')
