from django.shortcuts import render

from .models import Mineral


def mineral_list(request):
    minerals = Mineral.objects.all()
    return render(request, 'minerals/mineral_list.html', {'minerals': minerals})


def mineral_detail(request, pk):
    mineral = Mineral.objects.get(pk=pk)
    return render(request, 'minerals/mineral_detail.html', {'mineral': mineral})