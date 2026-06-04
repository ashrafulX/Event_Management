from django.db import models

#  category (ForeignKey)

class Category(models.Model):
    name=models.CharField(max_length=150,null=False)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.name


class Participant(models.Model):
    name=models.CharField(max_length=150,null=False)
    email=models.EmailField()
    
    def __str__(self):
        return f"{self.name}"

class Event(models.Model):
    name=models.CharField(max_length=150,null=False)
    description=models.TextField(blank=True)
    date=models.DateField()
    time=models.TimeField()
    location=models.CharField(max_length=200,default='unknown')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='events')
    participants=models.ManyToManyField(Participant,related_name='events')
    ticket=models.DecimalField(max_digits=10, decimal_places=2,default=5)

    def __str__(self):
        return f"{self.name} + {self.date} at {self.location}"
