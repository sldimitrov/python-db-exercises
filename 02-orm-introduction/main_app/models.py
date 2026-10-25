from django.db import models
from datetime import date

class Employee(models.Model):
    name = models.CharField(max_length=30)
    email_address = models.EmailField()
    photo = models.URLField()
    birth_date = models.DateField()
    work_full_time = models.BooleanField()
    created_now = models.DateTimeField(auto_now_add=True)

class Department(models.Model):
    class Cities(models.TextChoices):
        SF = 'S', 'Sofia'
        PD = 'P', 'Plovdiv'
        V = 'V', 'Varna'
        BS = 'Bs', 'Burgas'

    code = models.CharField(max_length=4, primary_key=True, unique=True)
    name = models.CharField(max_length=50, unique=True)
    employees_count = models.PositiveIntegerField(default=1, verbose_name='Employees Count')
    location = models.CharField(
        max_length=20,
        choices=Cities.choices,
        null=True,
        blank=True
    )
    last_edited_on = models.DateTimeField(auto_now_add=True, editable=False)

class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2,  blank=True, null=True)
    duration_in_days = models.PositiveIntegerField(null=True, blank=True, verbose_name="Duration in Days")
    estimated_hours = models.FloatField(null=True, blank=True, verbose_name="Estimated Hours")
    start_date = models.DateField(null=True, blank=True, verbose_name="Start Date", default=date.today())
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    last_edited_on = models.DateTimeField(auto_now_add=True, editable=False)
