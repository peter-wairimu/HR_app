from django.db import models
# Create your models here.


class Employee(models.Model):
    """
    Employee model
    """
    STANDARD = 'STD'
    MANAGER = 'MGR'
    SUPERVISOR = 'SUP'
    PRESIDENT = 'PRE'

    EMPLOYEE_TYPES = (
        (STANDARD, 'base employee'),
        (MANAGER, 'manager'),
        (SUPERVISOR, 'supervisor'),
        (PRESIDENT, 'president'),


    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    employee_type = models.CharField(max_length=3, choices=EMPLOYEE_TYPES, default=STANDARD)
    def __str__(self):
        return self.first_name + ' ' + self.last_name