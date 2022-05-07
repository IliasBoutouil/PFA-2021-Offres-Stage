from django.conf import settings
User = settings.AUTH_USER_MODEL
from django.db import models

class Publication(models.Model):
    titre=models.CharField(max_length=100,null=False)
    description=models.TextField(max_length=800,null=False)
    domaine=models.CharField(max_length=100,null=False)
    date_publication=models.DateTimeField(auto_now_add=True)
    type_publication=models.CharField(max_length=100,null=False,default='Demande')
    periode=models.IntegerField(null=False)
    etat=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.titre
    def brief(self):
        return self.description[:100]