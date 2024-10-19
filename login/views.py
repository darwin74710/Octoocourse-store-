from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from django.contrib.auth.hashers import check_password
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, 'login/home.html')

def inicioS(request):
    if request.method == 'POST':
        try:
            correo = request.POST['correo']
            password = request.POST['password']
        except KeyError as e:
            messages.error(request, f"Campo requerido faltante: {str(e)}")
            return render(request, 'login/InicioS.html')
        
        if correo.endswith('@elpoli.edu.co'):
            user_type = 'estudiante'
            table_name = 'ESTUDIANTES'
            email_field = 'CORREO_ESTUDIANTE'
            password_field = 'PASSWORD_ESTUDIANTE'
            redirect_url = reverse('Inicio')
        else:
            user_type = 'empresa'
            table_name = 'EMPRESAS'
            email_field = 'CORREO_EMP'
            password_field = 'PASSWORD_EMP'
            redirect_url = reverse('inicioE')

        try:
            with connection.cursor() as cursor:
                # Fetch user data
                cursor.execute(f"""
                    SELECT * FROM {table_name}
                    WHERE {email_field} = %s
                """, [correo])
                user = cursor.fetchone()
                
                if user:
                    # Get the index of the password field
                    desc = cursor.description
                    password_index = next(i for i, d in enumerate(desc) if d[0].lower() == password_field.lower())
                    
                    # Check password
                    if check_password(password, user[password_index]):
                        # Login successful
                        request.session['user_id'] = user[0]  # Assuming ID is the first field
                        request.session['user_type'] = user_type
                        messages.success(request, f"Bienvenido, {'estudiante' if user_type == 'estudiante' else 'empresa'}!")
                        return redirect(redirect_url)
                    else:
                        messages.error(request, "Contraseña incorrecta.")
                else:
                    messages.error(request, "Usuario no encontrado.")
        except Exception as e:
            messages.error(request, f"Error de inicio de sesión: {str(e)}")
            
    return render(request, 'login/InicioS.html')
