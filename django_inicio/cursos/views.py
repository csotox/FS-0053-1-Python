from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    login,
    logout
)

from cursos.models import Cursos

def get_cursos():
    return Cursos.objects.all()

def listado_cursos(request):
    cursos = get_cursos()

    print('-- -')
    print( request.user )
    print('-- -')

    context = {
        'cursos': cursos,
        'prueba': "Hola"
    }

    return render(
        request,
        'cursos/index.html',
        context
    )

def detalles_cursos(request, parametro_uuid):

    _cursos = None

    try:
        _cursos = Cursos.objects.get( uuid=parametro_uuid )
    except Cursos.DoesNotExist:
        print( f"El curso no existe {parametro_uuid}" )

    context = {
        'detalle': _cursos,
    }

    return render(
        request,
        'cursos/detalle.html',
        context
    )

def crear_cursos(request):
    print( 'Crear cursos' )

    if request.method == 'POST':
        nombre_curso = request.POST.get('nombre_curso', None)

        Cursos.objects.create(
            nombre = nombre_curso,
        )

        messages.success(request, "Curso creado.")

        return redirect('/cursos/')

    return render(
        request,
        'cursos/crear.html'
    )

def editar_cursos(request, parametro_uuid):

    _cursos = None

    try:
        _cursos = Cursos.objects.get( uuid=parametro_uuid )
    except Cursos.DoesNotExist:
        print( f"El curso no existe {parametro_uuid}" )

    if request.method == 'POST' and _cursos:
        _cursos.nombre = request.POST.get('nombre_curso', None)

        _cursos.save()

        messages.success(request, "Curso actualizado")

        return redirect('/cursos/')


    context = {
        'detalle': _cursos,
    }

    return render(
        request,
        'cursos/editar.html',
        context
    )

# Login
def iniciar_sesion(request):

    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        usuario = authenticate(
            request,
            username=username,
            password=password
        )

        # print( f"Usuario: {username} y contraseña {password}")
        # print( usuario )

        if usuario is not None:
            login( request, usuario )

            return redirect('/cursos/')
        else:
            messages.warning(
                request,
                "Usuario o contraseña incorrectos"
            )

    return render(
        request,
        'cursos/login.html',
    )



"""
Ciclo de vida de la petición Http
---------------------------------
GET /cursos/ (Navegador)
app/urls.py --> cursos/
cursos/views.py --> listado_cursos()
HttpResponse
Navegador
"""

