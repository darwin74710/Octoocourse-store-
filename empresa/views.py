from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from login.models import Conocimiento, TipoCont, OfertaEmpleo, Empresa, Estudiante
from estudiantes.models import Estudiantes, HojasDeVida, Idiomas, Aptitudes, LenguajesProg, FormacionesAcademicas, ExpLaborales
from datetime import date





@login_required
def crearOferta(request):
    if request.method == 'POST':
        nombre_oferta = request.POST.get('nombre_oferta')
        salario = request.POST.get('salario')
        descripcion = request.POST.get('descripcion')
        conocimientos_text = request.POST.get('conocimientos')
        tipo_cont = request.POST.get('tipo_cont')
        print(f'Tipo de contrato recibido: {tipo_cont}')

        estado = 1 if request.POST.get('estado') == 'on' else 0

        nit_empresa = request.session.get('nit')

        fecha_pub = date.today() 


        with connection.cursor() as cursor:
            cursor.execute("SELECT oferta_id_seq.NEXTVAL FROM dual")
            id_oferta = cursor.fetchone()[0]

        oferta = OfertaEmpleo(
            id_oferta=id_oferta,
            nit=nit_empresa, 
            nombre_oferta=nombre_oferta,
            salario=salario,
            descripcion=descripcion,
            estado=estado,
            fecha_pub=fecha_pub  

        )
        oferta.save()

        conocimientos_list = conocimientos_text.split(',')
        for conocimiento_nombre in conocimientos_list:
            if conocimiento_nombre.strip():
                Conocimiento.objects.create(
                    id_oferta=oferta,
                    nom_con=conocimiento_nombre.strip()
                )

        TipoCont.objects.create(
            id_oferta=oferta,
            tipo_cont=tipo_cont
        )

        return render(request, 'empresa/publicaro.html')

    return render(request, 'empresa/publicaro.html')


@login_required 
def inicioE(request):
    return render(request, 'empresa/inicioE.html')

@login_required 
def logout_view(request):
    logout(request)  
    messages.success(request, "Sesión cerrada correctamente.")
    return redirect('home')  

@login_required
def detalle_estudiante(request, id_estudiante):
    estudiante = get_object_or_404(Estudiantes, id_estudiante=id_estudiante)  
    Tablas = obtenerTablasHV(id_estudiante)  
    
    nit_empresa = request.session.get('nit')
    
    context = {
        'estudiante': estudiante,
        'nit_empresa': nit_empresa  
    }
    context.update(Tablas)  
    
    return render(request, 'empresa/aboutMeStudent.html', context)

def obtenerTablasHV(id_estudiante):
    estudiantes = Estudiantes.objects.filter(id_estudiante=id_estudiante)

    if estudiantes.exists():
        estudiante = estudiantes[0]
    else:
        estudiante = None

    if estudiante:
        hojasDeVida = HojasDeVida.objects.filter(id_estudiante=estudiante.id_estudiante)

        if hojasDeVida.exists():
            hojaDeVida = hojasDeVida[0]
        else:
            hojaDeVida = None

        idiomas = Idiomas.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida) if hojaDeVida else []
        aptitudes = Aptitudes.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida) if hojaDeVida else []
        lenguajesProg = LenguajesProg.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida) if hojaDeVida else []
        formaciones = FormacionesAcademicas.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida) if hojaDeVida else []
        expLaborales = ExpLaborales.objects.filter(id_hojavida=hojaDeVida.id_hoja_vida) if hojaDeVida else []
    else:
        idiomas = aptitudes = lenguajesProg = formaciones = expLaborales = []

    Datos = {
        'estudiante': estudiante,
        'hojasDeVida': hojaDeVida,
        'idiomas': idiomas,
        'aptitudes': aptitudes,
        'lenguajesProg': lenguajesProg,
        'formaciones': formaciones,
        'expLaborales': expLaborales,
    }

    return Datos


@login_required 
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

@login_required 
def ofertasE(request):
    nit_empresa = request.session.get('nit')
    ofertas = OfertaEmpleo.objects.filter(nit=nit_empresa)
    return render(request, 'empresa/ofertasE.html', {'ofertas': ofertas})


@login_required 
def detalle_oferta(request, id_oferta):
    oferta = get_object_or_404(OfertaEmpleo, id_oferta=id_oferta)
    
    datos_adicionales = obtener_tablas_tc(id_oferta)

    nit_empresa = request.session.get('nit')

    context = {
        'oferta': oferta,
        'tipo_contrato': datos_adicionales.get('tipo_contrato'),
        'conocimientos': datos_adicionales.get('conocimientos'),
    }
    
    return render(request, 'empresa/DetallesOferta.html', context)

@login_required
def eliminar_oferta(request, id_oferta):
    oferta = get_object_or_404(OfertaEmpleo, id_oferta=id_oferta)
    
    oferta.delete()
    
    return redirect('ofertasE')  

@login_required
def editar_oferta(request, id_oferta):
    oferta = get_object_or_404(OfertaEmpleo, id_oferta=id_oferta)
    
    if request.method == 'POST':
        oferta.nombre_oferta = request.POST.get('nombre_oferta', oferta.nombre_oferta)
        oferta.salario = request.POST.get('salario', oferta.salario)
        oferta.descripcion = request.POST.get('descripcion', oferta.descripcion)

        oferta.estado = '1' if 'estado' in request.POST else '0'
        
        
        oferta.save()
        
        return redirect('ofertasE')  
    
    return render(request, 'empresa/editar_oferta.html', {'oferta': oferta})

def obtener_tablas_tc(id_oferta):
    oferta = get_object_or_404(OfertaEmpleo, id_oferta=id_oferta)

    tipo_cont = TipoCont.objects.filter(id_oferta=oferta).values('tipo_cont')

    conocimientos = Conocimiento.objects.filter(id_oferta=oferta).values_list('nom_con', flat=True)  # Cambiado 'oferta' a 'id_oferta'

    datos = {
        'tipo_contrato': tipo_cont[0]['tipo_cont'] if tipo_cont else None,
        'conocimientos': list(conocimientos),  
    }

    return datos


def des_ofertas(request):
    return render(request, 'empresa/des_ofertas.html')

def listEAp(request):
    return render(request, 'empresa/listEAp.html')





