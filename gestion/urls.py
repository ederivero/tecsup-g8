from django.urls import path
from .views import ( endpointInicial, 
                     PruebaApiView, 
                     ImportanciasView, 
                     ImportanciaView, 
                     TareasView,
                     usandoVista,
                     EtiquetasView,
                     TareaEtiquetasView )

# importo absolutamente todo lo que esta contenido en ese archivo inclusive sus importaciones
# from .views import *


urlpatterns = [
    path('inicio', endpointInicial),
    path('prueba', PruebaApiView.as_view()),
    path('importancias', ImportanciasView.as_view()),
    path('importancia/<int:pk>', ImportanciaView.as_view()), # primary key
    path('tareas', TareasView.as_view()),
    path('prueba-view-bd', usandoVista),
    path('etiquetas', EtiquetasView.as_view()),
    path('tarea-etiqueta', TareaEtiquetasView.as_view())
]