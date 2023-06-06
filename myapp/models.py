from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# from django.contrib.auth.models import AbstractUser

class AdminUser(AbstractUser):
    mobile_number = models.CharField(max_length=20)
    city = models.CharField(max_length=100)

class Blog(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    image = models.ImageField(upload_to = 'media/blog')
    date_created = models.DateField(auto_now_add = True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"


class Choose(models.Model):
    titles = models.CharField(max_length = 50)
    contents = models.TextField()
   

    def __str__(self):
        return self.titles

    class Meta:
        verbose_name = "Choose"
        verbose_name_plural = "Choose"
        
class CustomerRegistration(models.Model):
    fullNames = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)    
    current_destination = models.CharField(max_length=50, choices=(('Bamenda', 'Bamenda'), ('Douala', 'Douala'), ('Yaounde', 'Yaounde'), ('Buea', 'Buea')))
    final_destination = models.CharField(max_length=50, choices=(('Bamenda', 'Bamenda'), ('Douala', 'Douala'), ('Yaounde', 'Yaounde'), ('Buea', 'Buea')))
    
    ID_Number = models.CharField(max_length = 50, blank=True, null=True)
    no_of_sites = models.IntegerField(default=1)
    
    def __str__(self):
        return self.fullNames
    
    class Meta:
        verbose_name = "CustomerRegistration"
        verbose_name_plural = "CustomerRegistration"
        
class SlideShow(models.Model):
    town = models.CharField(max_length = 50, default='Bamenda')
    text = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='media/slideshow')
    
    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = "SlideShow"
        verbose_name_plural = "SlideShow"