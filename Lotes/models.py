from django.db import models

# Create your models here.
class Development(models.Model):
    name = models.CharField(max_length=300)
    address = models.TextField()
    total_lots = models.IntegerField()
    total_available = models.IntegerField()

    def __str__(self):
        return self.name


class DevelopmentImage(models.Model):
    development = models.ForeignKey(Development, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='developments/')

    def __str__(self):
        return f"Image of {self.development.name}"

