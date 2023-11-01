from django.db import models

# Create your models here.
# Create company model

class Company(models.Model):
    company_id = models.AutoField(primary_field=True)
    name = models.CharField(max_length=1000)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100,
                            Choices=(('IT', 'IT'), ('Non IT', 'Non IT'))
                            )
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

# Employe Model