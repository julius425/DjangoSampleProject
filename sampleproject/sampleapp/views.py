from django.shortcuts import render, redirect, reverse, get_object_or_404
from . models import MySampleModel


def model_list_view(request):
    models = MySampleModel.objects.all()
    context = {
        'models': models
    }
    return render(request, 'sampleapp/model_list.html', context)


def model_detail_view(request, model_id):
    model = get_object_or_404(MySampleModel, pk=model_id)
    context = {
        'model': model
    }
    return render(request, 'sampleapp/model_detail.html', context)