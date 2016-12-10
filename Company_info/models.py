from django.db import models
from multiprocessing.managers import State
from email import email

# Create your models here.

class mas_countries(models.Model):
    country_name = models.CharField(max_length=50)
    def __str__(self):
        return self.country_name

class mas_states(models.Model):
    state_name = models.CharField(max_length=50)
    country = models.ForeignKey(mas_countries,default=2)
    def __str__(self):
        return self.state_name

class mas_company_profile(models.Model):
    company_name = models.CharField(max_length=30)
    company_caption = models.CharField(max_length=100,null=True,blank=True)
    company_reg_info = models.CharField(max_length=30,null=True,blank=True)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50,null=True,blank=True)
    address3 = models.CharField(max_length=50,null=True,blank=True)
    State = models.ForeignKey(mas_states)
    country = models.CharField(max_length=10)
    phone1  =  models.CharField(max_length=10)
    phone2  =  models.CharField(max_length=10,null=True,blank=True)
    website =  models.CharField(max_length=200)
    email   =  models.EmailField(null=True,blank=True)
    postcode = models.CharField(max_length=7)
    
    def __str__(self):
        return self.company_name

    
