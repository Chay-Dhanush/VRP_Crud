from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime
# Create your models here.


def current_time():
    return datetime.now().date()

class OrderModel(models.Model):
    Laptop_Choices=[
        ('Asus Laptop','Asus Laptop'),('Leonovo Laptop','Leonovo Laptop'),('Dell Laptop','Dell Laptop'),('Hp Laptop','Hp Laptop'),('Acer Laptop','Acer Laptop')
    ]

    ProductId=models.IntegerField()
    CustomerName=models.CharField(max_length=30)
    Product=models.CharField(max_length=20,choices=Laptop_Choices)
    Dateoforder=models.DateField(_('Date'),default=current_time)
    ProductPrice=models.IntegerField()
    CustomerPhone=models.BigIntegerField()
    CustomerEmail=models.EmailField()
    CustomerAddress=models.CharField(max_length=150)
    State=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.CustomerName
    