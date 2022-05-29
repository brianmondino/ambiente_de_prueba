from django.shortcuts import render
from app_familia.models import miembros
# Create your views here.


def miembros_app(request):
    fam_1 = miembros.objects.create(
        nombre = 'Brian', 
        apellido = 'Mondino', 
        dni = '34111222', 
        fecha_nac = '18-10-88', 
        telefono = '478611111'
        )
    fam_2 = miembros.objects.create(
        nombre = 'pepe', 
        apellido = 'Lopez', 
        dni = '34111223', 
        fecha_nac = '19-10-88', 
        telefono = '478611166'
        )
    fam_3 = miembros.objects.create(
        nombre = 'Jose Luis', 
        apellido = 'Zabala', 
        dni = '34111224', 
        fecha_nac = '20-10-88', 
        telefono = '478611155'
        )
		

    fam_all = miembros.objects.all
    context = {'fam_1':fam_1, 'fam_2':fam_2, 'fam_3':fam_3, 'fam_all':fam_all}
    return render(request, 'miembros_familia.html', context = context)