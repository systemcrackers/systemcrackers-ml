from django.db import models

def upload_path_handler(instance, filename): 
  n = len(filename)
  return "predict/{file}".format( file="modelimg" + filename[n-4:n] )

# Create your models here.
class Predictor(models.Model):
    image = models.ImageField(upload_to=upload_path_handler)