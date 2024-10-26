from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Card

# Create your views here.
class IndexView(generic.ListView):
    template_name = "cc_validation_app/index.html"
    context_object_name = "card_list"

    def get_queryset(self):
        return Card.objects.all()

class DetailView(generic.DetailView):
    model = Card
    template_name = "cc_validation_app/detail.html"

    def get_queryset(self):
        return Card.objects.all()