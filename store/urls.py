

from django.urls import path
from . import views


urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("order", views.order, name="order"),
    path("signup", views.Signup.as_view(), name="Signup"),
    path("login", views.Login.as_view(), name="Login"),
    path("logout", views.logout, name="logout"),
    path("contact", views.Contact.as_view(), name="contact"),
]
