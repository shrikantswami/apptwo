from django.db import models
class Topic(models.Model):
    webname = models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.webname

class data(models.Model):
    name = models.ForeignKey('Topic',on_delete=models.CASCADE,)
    date = models.DateField()
    url = models.URLField()
    def __str__(self):
        return str(self.url)

class sign_up(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password =models.CharField(max_length=10)
    def __str__(self):
        return self.name 


# Create your models here.
