import json
from estudiantes.models_Empresas import Conocimientos, OfertasEmpleos, TipoCont
from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def Ofertas(request):
    filtros = request.GET.get('filtros')
    ofertasEmpleos = OfertasEmpleos.objects.all()
    
    # Rangos de salarios según el dato recibido de filtros.
    salario_ranges = {
        "0_1": (0, 1000000),
        "1_2": (1000000, 2000000),
        "2_3": (2000000, 3000000),
        "3+": (3000000, None),
    }

    if filtros:
        lista_filtros = json.loads(filtros)
        q_objects = Q()  # Creamos un objeto Q para filtrar varias condiciones.

        # Agrego condiciones según los filtros seleccionados.
        if "fijo" in lista_filtros:
            q_objects |= Q(tipo_cont__id_tipo_cont=1)  # Utilizamos OR para multiples filtros.
        if "indefinido" in lista_filtros:
            q_objects |= Q(tipo_cont__id_tipo_cont=2)
        if "obra" in lista_filtros:
            q_objects |= Q(tipo_cont__id_tipo_cont=3)
        if "aprendizaje" in lista_filtros:
            q_objects |= Q(tipo_cont__id_tipo_cont=4)
        
        # Filtramos los salarios.
        salario_q_objects = Q()

        for filtro in lista_filtros:
            if filtro in salario_ranges:
                min_sal, max_sal = salario_ranges[filtro]
                
                # Verificar si tiene limite.
                if max_sal is not None:
                    salario_q_objects |= Q(salario__gte=min_sal, salario__lte=max_sal)
                else:
                    # Si no tiene limite.
                    salario_q_objects |= Q(salario__gte=min_sal)

        # Añadir la condición de salarios al objeto q_objects principal.
        if salario_q_objects:
            q_objects &= salario_q_objects

        # Aplicamos los filtros a la consulta.
        ofertasEmpleos = ofertasEmpleos.filter(q_objects)

        
    
    # Utilizo paginator para divitir 5 tablas por pagina.
    paginator = Paginator(ofertasEmpleos, 5) #Especifico que solo quiero 5 tablas en la pagina.
    num_pag = request.GET.get('page') #Obtengo el numero de pagina.
    ofertas_data = paginator.get_page(num_pag) #Obtengo la pagina.

    for oferta in ofertas_data:
        oferta.conocimientos = Conocimientos.objects.filter(id_oferta=oferta.id_oferta)
        oferta.tipoCont = TipoCont.objects.filter(id_oferta=oferta.id_oferta).first()

    filtros_java = json.dumps(lista_filtros) if filtros else ""

    Datos = {
        'ofertas_data': ofertas_data,
        'filtros': filtros_java,
    }

    return render(request, 'estudiantes/Ofertas.html', Datos)

@login_required
def OfertasInfo(request):
    idOferta = request.GET.get('idOferta')

    ofertasEmpleos = OfertasEmpleos.objects.filter(id_oferta=idOferta)

    if ofertasEmpleos.exists():
        ofertasEmpleo = ofertasEmpleos[0]
    
    conocimientos = Conocimientos.objects.filter(id_oferta=idOferta)
    tipoCont = TipoCont.objects.filter(id_oferta=idOferta)

    if tipoCont.exists():
        contrato = tipoCont[0]
    else:
        contrato = None

    Datos = {
        'ofertasEmpleos': ofertasEmpleo,
        'conocimientos': conocimientos,
        'contrato': contrato,
    }

    return render(request, 'estudiantes/OfertasInfo.html', Datos)