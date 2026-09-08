from django.urls import path

from cursos.views import (
    listado_cursos,
    detalles_cursos,
    crear_cursos,
    editar_cursos,
    iniciar_sesion,
    cerrar_sesion,
    listado_clasi
)

# [TODO] crear grupos de path
urlpatterns = [
    path('', listado_cursos),
    path('login/', iniciar_sesion),
    path('logout/', cerrar_sesion),
    path('crear/', crear_cursos),
    path('<uuid:parametro_uuid>/', detalles_cursos),
    path('<uuid:parametro_uuid>/editar/', editar_cursos),
    path('clasificacion/', listado_clasi, name="curso_clasi_index"),
]
