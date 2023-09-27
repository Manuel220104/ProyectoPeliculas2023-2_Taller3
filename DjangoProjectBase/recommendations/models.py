from django.db import models

# Create your models here.
class Recommendations(models.Model):
    prompt = models.CharField(max_length=200)
    image = models.ImageField(upload_to='recommendations_images/')

    def __str__(self):
        return self.headline