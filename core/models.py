from django.db import models
from datetime  import datetime

# Create your models here.

class Poster(models.Model):

	titulo   	= models.CharField(max_length=255, null=False)

	descricao 	= models.CharField(max_length=500, null=False)

	imagem 		= models.CharField(max_length=255)

	data   		= models.DateField(default=datetime.now)

	ativo  		= models.BooleanField(default=True)

	deletado    = models.BooleanField(default=False)
