from django.db import models

# Create your models here.
class Catgory(models.Model):
       name = models.CharField(max_length=255)
       slug = models.SlugField()

       class Meta:
           ordering = ('name',)
        
        def __str__(self):
            return self.name

        def get_absolute_url(self):
            return f'/{self.slug}/'
            

            
