from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator, MinValueValidator,RegexValidator
from django.contrib.auth.models import User
    

class Tutor(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name
    phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")]  ,max_length=20, null = True)
    adress=models.TextField()
    email = models.EmailField()
    subject= models.CharField(max_length=100)
    image=models.ImageField(upload_to = "images//", null=True)
    
class Question(models.Model):
   
    question = models.TextField()
    cr_date = models.DateTimeField(auto_now_add=True)
    answer = models.TextField()

    

    
