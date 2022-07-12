from django.shortcuts import render
from app_gestion.models import Persona
from app_gestion.models import Vacunatorio
from django.http import HttpResponse
from django.db.models import Q

def ingreso_persona(request):
    return render(request,"ingreso_persona.html")

def busqueda_persona(request):
    return render(request,"busqueda_persona.html")

def eliminacion_persona(request):
    return render(request,"eliminacion_persona.html")

def listado_persona(request):
    return render(request,"listado_persona.html")

def home(request):
    return render(request,"home.html")

##### EXAMEN

def ingreso_vacunatorio(request):
    return render(request,"ingreso_vacunatorio.html")

def listado_vacunatorio(request):
    return render(request,"listado_vacunatorio.html")

def actualizado_vacunatorio(request):
    return render(request,"actualizado_vacunatorio.html")

# Create your views here.

# INGRESAR PERSONA
def ingresar_persona(request):
    nombre=request.GET["txt_nombre"]
    appaterno=request.GET["txt_appaterno"]
    apmaterno=request.GET["txt_apmaterno"]
    rut=request.GET["txt_rut"]
    edad=request.GET["num_edad"]
    nom_vacuna=request.GET["sel_vacuna"]
    fecha=request.GET["dt_fecha"]

    if len(nombre)>0 and len(appaterno)>0 and len(apmaterno)>0 and len(rut)>7 and len(rut)<10 and len(edad)>0:
        pro=Persona(nombre=nombre,appaterno=appaterno,apmaterno=apmaterno,rut=rut,edad=edad,nom_vacuna=nom_vacuna,fecha=fecha)
        pro.save()
        mensaje="Datos guardados correctamente en la Base de Datos."
    else:
        mensaje="Ha habido un error en el inggreso de los datos."
    return HttpResponse(mensaje)


def buscar_persona(request):
    if request.GET["txt_rut"]:
        rut_persona = request.GET["txt_rut"]
        personas = Persona.objects.filter(
            Q(nombre__icontains = rut_persona) | 
            Q(appaterno__icontains=rut_persona) | 
            Q(apmaterno__icontains=rut_persona) | 
            Q(edad__icontains=rut_persona) | 
            Q(nom_vacuna__icontains=rut_persona) | 
            Q(fecha__icontains=rut_persona)
        )
        return render(request,"listar.html",{"Persona":personas , "query":rut_persona})
    else:
        mensaje = "El rut ingresado no existe en la Base de Datos"
        return HttpResponse(mensaje)

# ELIMINAR PERSONA
def eliminar_persona(request):
    if request.GET["txt_rut"]:
        rut_persona = request.GET["txt_rut"]
        personas = Persona.objects.filter(rut=rut_persona)
        if personas:
            pro=Persona.objects.get(rut=rut_persona)
            pro.delete()
            mensaje = "Los registros de la persona han sido eliminados."
                
        else:
            mensaje = "El rut ingresado no existe en la Base de Datos"
    else:
        mensaje = "Debe ingresar un rut"
    return HttpResponse(mensaje)

# LISTAR PERSONAS
def listar_persona(request):
    datos = Persona.objects.all()  
    return render(request,"listado_persona.html",{'personas':datos})

#######################

# INGRESAR VACUNATORIO
def ingresar_vacunatorio(request):
    nom_consultorio=request.GET["txt_nom_consultorio"]
    nom_enfermero=request.GET["txt_nom_enfermero"]
    rut_enfermero=request.GET["txt_rut_enfermero"]
    nro_dosis=request.GET["num_dosis"]
    id_atencion=request.GET["num_id_atencion"]
    if len(nom_consultorio)>0 and len(nom_enfermero)>0 and len(rut_enfermero)>0 and len(nro_dosis)>0 and len(id_atencion)>0:
        pro=Vacunatorio(nom_consultorio=nom_consultorio, nom_enfermero=nom_enfermero, rut_enfermero=rut_enfermero, nro_vacuna=nro_dosis, id_atencion=id_atencion)
        pro.save()
        mensaje="Datos ingresados correctamente"
    else:
        mensaje="Faltan campos por completar"
    return HttpResponse(mensaje)

# LISTAR VACUNATORIO
def listar_vacunatorio(request):
    datos = Vacunatorio.objects.all()  
    return render(request,"listado_vacunatorio.html",{'vacunatorios':datos})

# ACTUALIZAR
def actualizar_vacunatorio(request):
    nom_consultorio=request.GET["txt_nom_consultorio"]
    nom_enfermero=request.GET["txt_nom_enfermero"]
    rut_enfermero=request.GET["txt_rut_enfermero"]
    nro_dosis=request.GET["num_dosis"]
    id_atencion=request.GET["num_id_atencion"]

    if request.GET["num_id_atencion"]:
        id_atencion = request.GET["num_id_atencion"]
        vacunatorios = Vacunatorio.objects.filter(id_atencion=id_atencion)
        if vacunatorios:
            pro=Vacunatorio(nom_consultorio=nom_consultorio, nom_enfermero=nom_enfermero, rut_enfermero=rut_enfermero, nro_vacuna=nro_dosis, id_atencion=id_atencion)
            pro.save()
            mensaje="Datos actualizados"
        else:
            mensaje="Faltan campos por completar"
        return HttpResponse(mensaje)
    else:
        mensaje="La ID no concide con la base de datos"
    return HttpResponse(mensaje)