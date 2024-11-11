from django.urls import path

from . import views

app_name = "cc_validation_app"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("create/", views.CreateView.as_view(), name="create"),
    path("validate_http/<str:card_str>", views.validate_http, name="validate_http"),
    path("<int:pk>/update/", views.UpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.DeleteView.as_view(), name="delete"),
]
