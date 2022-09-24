from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=100)
    age =  models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name    # it will show name on user 

    

    


   