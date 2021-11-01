from io import BytesIO
from PIL import Image
from django.core.files import Files

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

class Product(models.Model):
    models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    slug = models.SlugField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)    
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=False)

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        
        
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(300,200)):
        img = Image.open(image)
        img.convert('RGB')
        imb.thumbnail(size)

        thumb_io = BytesIO()

