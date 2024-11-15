from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.db import connection
from django.utils.dateparse import parse_date
import re  # Importa el módulo re para expresiones regulares
import os

def register(request):
    if request.method == 'POST':
        if 'nombre' in request.POST:  # Registro de estudiante
            try:
                # ... Código de registro de estudiante ...
                return redirect('inicioS')

            except Exception as e:
                error_message = f"Error en el registro de estudiante: {str(e)}"
                print(error_message)
                messages.error(request, error_message)
                return render(request, 'register.html')

        elif 'nombre_empresa' in request.POST:  # Registro de empresa
            try:
                nombre_empresa = request.POST['nombre_empresa']
                nit_empresa = request.POST['nit_empresa']
                email_empresa = request.POST['email_empresa']
                telefono_empresa = request.POST['telefono_empresa']
                direccion_empresa = request.POST['direccion_empresa']
                password = request.POST['password_empresa']
                password2 = request.POST['password2_empresa']

                if password != password2:
                    messages.error(request, "Las contraseñas no coinciden.")
                    return render(request, 'register.html')

                hashed_password = make_password(password)

                # Insertar datos de la empresa en la base de datos
                with connection.cursor() as cursor:
                    cursor.execute("""
                        INSERT INTO EMPRESAS (NIT, NOM_EMPRESA, DIRECCION, CORREO_EMP, PASSWORD_EMP, TELEFONO)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """, [nit_empresa, nombre_empresa, direccion_empresa, email_empresa, hashed_password, telefono_empresa])
                
                # Crear carpeta con el NIT de la empresa 
                folder_path = os.path.join('Data', 'OfertasExamenes', 'Examenes', nit_empresa)
                os.makedirs(folder_path, exist_ok=True)

                messages.success(request, "Registro de empresa exitoso.")
                return redirect('inicioS')

            except Exception as e:
                error_message = f"Error en el registro de empresa: {str(e)}"
                print(error_message)
                messages.error(request, error_message)
                return render(request, 'register.html')

    return render(request, 'register.html')
