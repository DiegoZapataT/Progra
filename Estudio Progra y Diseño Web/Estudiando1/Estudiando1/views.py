from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludito(request): #Vista 1

    nombre = "Diego"
    apellido = "Zapata"
    hora = datetime.datetime.now()
    temas_de_prueba = ["Plantillas","Modelos","Formularios","Vistas","Despliegue"]
    doc_externo = open('C:/Users/dzapa/OneDrive/Documentos/ProyectoPracticaDjango/Estudiando1/Estudiando1/plantillas/platilla1.html')
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"nombre_persona": nombre,
                   "apellido_persona": apellido,
                   "hora_actual": hora,
                   "temas": temas_de_prueba})

    documento = plt.render(ctx)
    return HttpResponse(documento)

def calculaMiEdad(request,edad, agno):

    periodo = agno - 2020
    edadFutura = edad + periodo
    documento = "<html><body><h2>En el año %s tendras %s años</h2></body></html" %(agno, edadFutura)

    return HttpResponse(documento)