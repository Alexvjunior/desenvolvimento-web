from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ContatosView.as_view(), name='home'),
    path('<int:contato_id>', views.ContatosView.as_view(), name='ver_contato'),
]