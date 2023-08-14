

from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("", views.order, name="order"),
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
]
