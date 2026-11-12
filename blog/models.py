from django.db import models
from django.utils.text import slugify

#category
class Category(models.Model):
   name=models.CharField(max_length=100)
    
   def __str__(self):
         return self.name

# Create your models here.
class Post(models.Model):
   title = models.CharField(max_length=100)
   content = models.TextField()
   image_url = models.URLField(null=True)
   created_at = models.DateTimeField(auto_now_add=True)
   slug=models.SlugField(unique=True)
   category=models.ForeignKey(Category,on_delete=models.CASCADE)

   def save(self, *args, **kwargs):
      self.slug=slugify(self.title)
      super().save( *args, **kwargs)
       
   
   def __str__(self):
      return self.title

#about us
class AboutUs(models.Model):
   content = models.TextField()

   def __str__(self):
      return "About Us"

#contact messages
class ContactMessage(models.Model):
   name = models.CharField(max_length=100)
   email = models.EmailField()
   message = models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)

   class Meta:
      ordering = ["-created_at"]

   def __str__(self):
      return f"{self.name} <{self.email}>"
