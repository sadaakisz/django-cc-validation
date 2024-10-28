import re

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse, reverse_lazy

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

class CreateView(generic.CreateView):
    model = Card
    template_name = "cc_validation_app/create.html"
    fields = ["number", "expires", "name", "cvv"]

    # https://stackoverflow.com/a/52823773
    def get_success_url(self):
        return reverse("cc_validation_app:index")

def validate(request, card_str):
    # https://stackoverflow.com/a/17337613
    plain_str = re.sub('[^0-9]', '', card_str)
    verification_digit = int(plain_str[-1])
    rev_str = "".join(reversed(plain_str))
    # 1 offset because of the verification digit
    even_pos_digits = [int(rev_str[i]) for i in range(len(rev_str)) if int(i)%2==1]
    odd_pos_digits = [int(rev_str[i]) for i in range(len(rev_str)) if int(i)%2==0 and i!=0]

    processed_even_digits = [1+(2*x)%10 if 2*x>=10 else 2*x for x in even_pos_digits]

    card_validity = (sum(processed_even_digits) + sum(odd_pos_digits) + verification_digit) % 10 == 0

    return HttpResponse(card_validity)
class UpdateView(generic.UpdateView):
    model = Card
    template_name = "cc_validation_app/update.html"
    fields = ["number", "expires", "name", "cvv"]

    # https://stackoverflow.com/a/52823773
    def get_success_url(self):
        # https://stackoverflow.com/a/66262635
        pk = self.kwargs["pk"]
        return reverse("cc_validation_app:detail", kwargs={"pk": pk})

class DeleteView(generic.DeleteView):
    model = Card
    template_name = "cc_validation_app/confirm_delete.html"
    success_url = reverse_lazy("cc_validation_app:index")