from django.db import models

# Create your models here.
# Create company model

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100,
                            choices=(('IT', 'IT'), ('Non IT', 'Non IT'))
                            )
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Employe Model
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    position = models.CharField( max_length=50,choices=(('TL', 'TL'), ('SDE', 'SDE'),
                                       ('PO', 'PO'), ('PM', 'PM'))
                              )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)