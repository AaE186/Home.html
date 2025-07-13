from django.urls import path
from . import views

urlpatterns = [
    path('api/register/', views.register_user),
    path('api/login/', views.login_user),
    path('api/me/', views.current_user),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
]
