from django.contrib import admin
from django.urls import path
from core import views

# from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.IndexView.as_view(), name="index"),
    path("cadastro/", views.CadastroView.as_view(), name="cadastro"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView, name="logout"),
]
