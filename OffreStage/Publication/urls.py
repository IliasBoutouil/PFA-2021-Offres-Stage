from django.urls import path
from . import views
urlpatterns=[
   path('offres',views.OffreList,name='List Offres'),  
   path('offres/<int:pk>',views.ShowOffre,name='Offre'),  
   path('offres/create',views.CreateOffre,name='Create Offre'),  
   path('offres/edit/<int:pk>',views.EditOffre,name='Edit Offre'),  
   path('offres/update/<int:pk>',views.UpdateOffre,name='Update Offre'),  
   path('offres/delete/<int:pk>',views.DestroyOffre,name='Delete Offre'), 
   path('demandes',views.DemandeList,name='List demandes'),  
   path('demandes/<int:pk>',views.ShowDemande,name='Demande'),  
   path('demandes/create',views.CreateDemande,name='Create Demande'),  
   path('demandes/edit/<int:pk>',views.EditDemande,name='Edit Demande'),  
   path('demandes/update/<int:pk>',views.UpdateDemande,name='Update Demande'),  
   path('demandes/delete/<int:pk>',views.DestroyDemande,name='Delete Demande'),
   path('approve/<int:pk>',views.Approve,name='approve'),  

]
