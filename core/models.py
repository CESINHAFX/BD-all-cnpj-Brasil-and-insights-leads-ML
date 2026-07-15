from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Company(models.Model):
    cnpj = models.CharField(max_length=14, unique=True)
    legal_name = models.CharField(max_length=255)
    trade_name = models.CharField(max_length=255, blank=True, null=True)
    date_opened = models.DateField(blank=True, null=True)
    registration_status = models.CharField(max_length=100, blank=True, null=True)
    capital_social = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    legal_nature_code = models.CharField(max_length=20, blank=True, null=True)
    cnae_main = models.ForeignKey('CNAE', on_delete=models.PROTECT, blank=True, null=True,related_name='companies_main')
    cnae_secondary = models.ManyToManyField('CNAE', related_name='companies_secondary', blank=True)
    address = models.TextField()
    city = models.CharField(max_length=100, db_index=True)
    state = models.CharField(max_length=2, db_index=True)
    zip_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.legal_name} ({self.cnpj})"

class CNAE(models.Model):
    code = models.CharField(max_length=7, unique=True)
    description = models.TextField()
    class Meta:
        verbose_name = "CNAE"
        verbose_name_plural = "CNAEs"
        ordering = ['code']

    def __str__(self):
        return f"{self.code} - {self.description}"

class Partner(models.Model):

    Classification_choices = [
        ("22", 'Socio'),
        ("49", 'Socio-Administrador'),
    ]
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='partners')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    qualification_code = models.CharField(max_length=2, choices=Classification_choices)

    def __str__(self):
        return f"{self.name} - {self.company.legal_name}"
    
    