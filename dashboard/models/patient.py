from django.db import models


class Patient(models.Model):
    name = models.CharField('Bemorning Ismi', max_length=128)
    first_name = models.CharField('Bemorning Familiyasi', max_length=128)
    father_name = models.CharField('Otasining ismi',max_length=128,null=True,blank=True)
    age = models.CharField('Bemorning tug\'ilgan yili', max_length=10)
    phone = models.CharField('Bemorning telefon raqami', max_length=16,null=True,blank=True)
    date = models.DateField(auto_now=True)
    diagnoz = models.TextField('Tashxis')
    recommendation = models.TextField('Tavsiya')
    """Comment faqat bazaga yoziladi, qog'ozda chiqarilmaydi"""
    comment = models.TextField("Izox",null=True,blank=True)


    def __str__(self):
        return f"{self.name} {self.first_name}"
