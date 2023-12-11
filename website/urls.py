from . import views
from django.urls import path

urlpatterns=[
    path('', views.home, name='home'),  
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('logout_view/', views.logout_view, name='logout_view'),
    
    path('create/', views.create, name='create'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete')

]