from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required 
def inicioE(request):
    return render(request, 'empresa/inicioE.html')


def logout_view(request):
    logout(request)  
    messages.success(request, "Sesión cerrada correctamente.")
    return redirect('home')  

def aboutMe(request):
    return render(request, 'empresa/aboutMeStudent.html')


def estudiantesE(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT ID_ESTUDIANTE, TIPO_ID, NOM_ESTUDIANTE, APELLIDO, CORREO_ESTUDIANTE, FECHA_NAC FROM ESTUDIANTES")
        estudiantes = [
            {
                'id': row[0],
                'tipo_id': row[1],
                'nombre': row[2],
                'apellido': row[3],
                'correo': row[4],
                'fecha_nac': row[5]
            }
            for row in cursor.fetchall()
        ]
    return render(request, 'empresa/estudiantesE.html', {'estudiantes': estudiantes})


def configE(request):
    return render(request, 'empresa/configE.html')

def ofertasE(request):
    return render(request, 'empresa/ofertasE.html')


def des_ofertas(request):
    return render(request, 'empresa/des_ofertas.html')

def listEAp(request):
    return render(request, 'empresa/listEAp.html')

def publicaro(request):
    return render(request, 'empresa/publicaro.html')


def DetallesOferta(request):
    return render(request, 'empresa/DetallesOferta.html')

@login_required
def crearOferta(request):
    if request.method == 'POST':
        try:
            nit = request.session.get('nit')  
            if not nit:
                raise ValueError("NIT no encontrado en la sesión")
            
            nombre_oferta = request.POST['nombre_oferta']
            salario = request.POST['salario']
            tipo_cont = request.POST['tipo_cont']
            descripcion = request.POST['descripcion']
            conocimientos = request.POST['conocimientos']
            estado = 1 if request.POST.get('estado', 'off') == 'on' else 0

            with connection.cursor() as cursor:
                try:
                    # Create variable to store the generated ID_OFERTA
                    id_oferta_var = cursor.var(int)

                    # Insert into OFERTAS_EMPLEOS and return the generated ID_OFERTA
                    cursor.execute("""
                        INSERT INTO OFERTAS_EMPLEOS (ID_OFERTA, NIT, NOMBRE_OFERTA, SALARIO, DESCRIPCION, ESTADO)
                        VALUES (SEQ_OFERTAS_EMPLEOS.NEXTVAL, :nit, :nombre_oferta, :salario, :descripcion, :estado)
                        RETURNING ID_OFERTA INTO :id_oferta
                    """, {
                        'nit': nit,
                        'nombre_oferta': nombre_oferta,
                        'salario': salario,
                        'descripcion': descripcion,
                        'estado': estado,
                        'id_oferta': id_oferta_var
                    })
                    
                    id_oferta = id_oferta_var.getvalue()  # Get the value of the variable

                    # Insert into CONOCIMIENTOS
                    conocimiento_list = [c.strip() for c in conocimientos.split(',') if c.strip()]
                    for conocimiento in conocimiento_list:
                        cursor.execute("""
                            INSERT INTO CONOCIMIENTOS (ID_CONOCIMIENTO, ID_OFERTA, NOM_CON)
                            VALUES (SEQ_CONOCIMIENTOS.NEXTVAL, :id_oferta, :conocimiento)
                        """, {'id_oferta': id_oferta, 'conocimiento': conocimiento})

                    # Insert into TIPO_CONT
                    cursor.execute("""
                        INSERT INTO TIPO_CONT (ID_TIPO_CONT, ID_OFERTA, TIPO_CONT)
                        VALUES (SEQ_TIPO_CONT.NEXTVAL, :id_oferta, :tipo_cont)
                    """, {
                        'id_oferta': id_oferta,
                        'tipo_cont': tipo_cont
                    })

                except DatabaseError as e:
                    if 'ORA-02289' in str(e):
                        # Sequence doesn't exist, create it and retry
                        cursor.execute("CREATE SEQUENCE SEQ_OFERTAS_EMPLEOS START WITH 1 INCREMENT BY 1")
                        cursor.execute("CREATE SEQUENCE SEQ_CONOCIMIENTOS START WITH 1 INCREMENT BY 1")
                        cursor.execute("CREATE SEQUENCE SEQ_TIPO_CONT START WITH 1 INCREMENT BY 1")
                        # Retry the insertion
                        cursor.execute("""
                            INSERT INTO OFERTAS_EMPLEOS (ID_OFERTA, NIT, NOMBRE_OFERTA, SALARIO, DESCRIPCION, ESTADO)
                            VALUES (SEQ_OFERTAS_EMPLEOS.NEXTVAL, :nit, :nombre_oferta, :salario, :descripcion, :estado)
                            RETURNING ID_OFERTA INTO :id_oferta
                        """, {
                            'nit': nit,
                            'nombre_oferta': nombre_oferta,
                            'salario': salario,
                            'descripcion': descripcion,
                            'estado': estado,
                            'id_oferta': id_oferta_var
                        })
                        id_oferta = id_oferta_var.getvalue()

                        for conocimiento in conocimiento_list:
                            cursor.execute("""
                                INSERT INTO CONOCIMIENTOS (ID_CONOCIMIENTO, ID_OFERTA, NOM_CON)
                                VALUES (SEQ_CONOCIMIENTOS.NEXTVAL, :id_oferta, :conocimiento)
                            """, {'id_oferta': id_oferta, 'conocimiento': conocimiento})

                        cursor.execute("""
                            INSERT INTO TIPO_CONT (ID_TIPO_CONT, ID_OFERTA, TIPO_CONT)
                            VALUES (SEQ_TIPO_CONT.NEXTVAL, :id_oferta, :tipo_cont)
                        """, {
                            'id_oferta': id_oferta,
                            'tipo_cont': tipo_cont
                        })
                    else:
                        raise

            messages.success(request, '¡Oferta publicada con éxito!')
            return redirect('ofertasE')
        except ValueError as e:
            messages.error(request, str(e))
        except Exception as e:
            messages.error(request, f'Error al publicar la oferta: {str(e)}')

    return render(request, 'empresa/publicaro.html')