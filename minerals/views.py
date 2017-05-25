from django.shortcuts import render

from .models import Mineral
from django.db.models import Q


def mineral_list(request):
    minerals = Mineral.objects.all()
    return render(request, 'minerals/mineral_list.html', {'minerals': minerals})


def mineral_detail(request, pk):
    mineral = Mineral.objects.get(pk=pk)
    return render(request, 'minerals/mineral_detail.html', {'mineral': mineral})


def mineral_letter(request, letter):
    minerals = Mineral.objects.filter(name__startswith=letter.lower())
    return render(request, 'minerals/mineral_list.html', {'minerals': minerals, 'active_letter':letter})


def search(request):
    term = request.GET.get("q")
    search = Mineral.objects.filter(name__icontains=term)
    return render(request, 'minerals/mineral_list.html', {'search': search})
