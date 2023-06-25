# Generated by Django 4.2.1 on 2023-06-02 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_doctor_motto_en_remove_doctor_motto_ru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_clinica',
            field=models.CharField(max_length=25, verbose_name='Telefon raqam clinica'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_mobile',
            field=models.CharField(max_length=25, verbose_name='Telefon raqam shaxsiy'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='about_doctor_en',
            field=models.TextField(default=1, verbose_name='Shifokor haqida ingliz tilida'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctor',
            name='about_doctor_ru',
            field=models.TextField(default=1, verbose_name='Shifokor haqida rus tilida'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctor',
            name='about_doctor_uz',
            field=models.TextField(default=1, verbose_name="Shifokor haqida o'zbek tilida"),
            preserve_default=False,
        ),
    ]
