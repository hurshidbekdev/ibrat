from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class SivilNumber(models.Model):
    content = RichTextField()
class employes(models.Model):
    employes_img = models.ImageField(upload_to='')
    employes_name = models.CharField(max_length=64)
    employes_info = models.TextField()
    def __str__(self):
        return self.employes_name

    class Meta:
        verbose_name_plural = "hodimlar"

class NewVideo(models.Model):
    video_url = models.FileField(upload_to='video/')
    title = models.TextField()
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Video"
class YangiHodim(models.Model):
    ismi=models.CharField(max_length=60)
    haqida=models.TextField(max_length=200)
    rasmi=models.ImageField(upload_to='media/media/')
    def __str__(self):
        return self.ismi
class IbratRasm(models.Model):
    rasm=models.ImageField(upload_to='media/media/')

class Jamoa(models.Model):
    rasmi=models.ImageField(upload_to='media/media')
    ismi=models.CharField(max_length=60)
    TurarJoi=models.TextField(max_length=60)
    lavozimi=models.TextField(max_length=1000)
    def __str__(self):
        return self.lavozimi

class UzgarishYangiliklar(models.Model):
    uzgarish=models.TextField(max_length=200)
    def __str__(self):
        return self.uzgarish


class KomisHodim(models.Model):
    rasm=models.ImageField(upload_to='media/media')
    ismi = models.CharField(max_length=60)
    TurarJoi = models.TextField(max_length=60)
    lavozimi = models.TextField(max_length=1000)
    def __str__(self):
          return self.TurarJoi

class MaxallFuqorolar(models.Model):
    content = RichTextField()


class Contact (models.Model):
        name = models.CharField(max_length=36)
        email = models.EmailField(max_length=36)
        message = models.TextField()
        def __str__(self):
            return self.name



