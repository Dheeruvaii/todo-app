from django.db import models

# Create your models here.
class todo(models.Model):
    Title=models.CharField(max_length=100,blank=False)
    discription=models.TextField(blank=True)
    date=models.DateField(blank=True)
    completed =models.BooleanField(blank=True)
    
    def __str__(self):
        return self.Title
    
    
    