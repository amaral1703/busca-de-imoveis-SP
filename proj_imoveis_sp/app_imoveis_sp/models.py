from django.db import models

# Create your models here.

class imovel (models.Model):
    
    num_contrib = models.CharField(max_length = 20)
    nome_logradoro_imovel = models.CharField(max_length = 255)
    num_imovel = models.FloatField()
    complemento_imovel = models.CharField(max_length = 255)
    bairro_imovel = models.CharField(max_length = 255)
    cep_imovel = models.CharField(max_length = 15)
    area_tereno = models.FloatField()
    metro_quad_terreno = models.FloatField()
 



 