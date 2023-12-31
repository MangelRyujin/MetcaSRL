from django.db import models

# Create your models here.
class Offer(models.Model):
    offer_name = models.CharField('Offer name ',max_length=50, null=False, blank=False)
    fecha_inicial_vigente = models.DateField()
    fecha_final_vigente = models.DateField()
    imagen = models.ImageField(upload_to = "offer" , null= False )
    
    def __str__(self) -> str:
        return self.offer_name

    class Meta:
        verbose_name_plural='ofertas'
       