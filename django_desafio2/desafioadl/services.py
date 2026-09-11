from desafioadl.models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.filter(eliminada=False)

    # Devolvemos una lista
    todas = []
    for tarea in tareas:
        sub_tareas = SubTarea.objects.filter(tarea=tarea, eliminada=False)

        # Crea una tupla por cada tarea con su subtarea
        # Voy a utilizar esta opción
        todas.append((tarea, sub_tareas))

        # La alternativa es crear un diccionario
        # Pero mantengo el tema de la lista de
        # tuplas
        # todas.append({
        #     'tarea': tarea,
        #     'sub_tareas': sub_tareas
        # })

    return todas

def crear_nueva_tarea(descri: str = ''):
    tarea = Tarea.objects.create(
        descripcion=descri
    )

    return recupera_tareas_y_sub_tareas()

def crear_sub_tarea(tarea_id: int = 0, descri: str = ''):
    tarea = Tarea.objects.get( id = tarea_id, eliminada=False )

    sub_tarea = SubTarea.objects.create(
        descripcion=descri,
        tarea=tarea
    )

    return recupera_tareas_y_sub_tareas()

def elimina_tarea(tarea_id: int = 0):

    tarea = Tarea.objects.get( id = tarea_id, eliminada=False )
    tarea.eliminada = True
    tarea.save()

    return recupera_tareas_y_sub_tareas()

def elimina_sub_tarea(sub_tarea_id: int = 0):

    sub_tarea = SubTarea.objects.get( id = sub_tarea_id, eliminada=False )
    sub_tarea.eliminada = True
    sub_tarea.save()

    return recupera_tareas_y_sub_tareas()

def imprimir_en_pantalla(lista_tareas: list = []):

    for item in lista_tareas:
        tarea = item[0]
        sub = item[1]

        print( f"[{tarea.id}] {tarea.descripcion}" )

        for it in sub:
            print( f".... [{sub.id}] {sub.descripcion}"   )

    return True
