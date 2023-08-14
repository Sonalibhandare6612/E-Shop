

from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("", views.order, name="order"),
    path("signup", views.Signup.as_view(), name="Signup"),
    path("login", views.Login.as_view(), name="Login"),
]
