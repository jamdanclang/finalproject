from django.shortcuts import render

# Create your views here.

from .models import Campus, Building, Reports

def homepage(request):
    buildings = Building.objects.order_by('name')
    return render(request, 'reports/index.html', {'buildings' : buildings})

def buildingdetail(request, building_slug):
    building = Building.objects.get(name_slug=building_slug)
    reports = Reports.objects.filter(building=building).order_by("date")
    return render(request, 'reports/detail.html', {'building' : building, "reports": reports })

