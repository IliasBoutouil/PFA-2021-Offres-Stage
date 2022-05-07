from django.urls import path
from . import views
urlpatterns=[
   path('',views.home_screen,name='home'),  
   path('login',views.Login,name='Login'),  
   path('inscription',views.Inscription,name='Inscription'),  
   path('logout',views.logout_view,name='Logout'),
   path('students',views.display_students,name='Etudiants'),  
   path('students/<int:pk>',views.display_student,name='Etudiant'),  
   path('profile',views.profile,name='profile'),  
]
