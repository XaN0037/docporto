# Generated by Django 4.2.1 on 2023-05-31 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='adress',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name="Manzil so'z bilan"),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Email sissilka'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='facebook',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Facebook sissilka'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='instagramm',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Instagram sissilka'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='locatsiya',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Locatsiya sissilka'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='odnoklassniki',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ok.ru sissilka'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='telegram',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Telegram sissilka'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='twitter',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Twitter sissilka'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='youtube',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='YOUTUBE sissilka'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='about_doctor',
            field=models.TextField(blank=True, null=True, verbose_name='Shifokor haqida'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Shaxsiy Email sissilka'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='facebook',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Shaxsiy Facebook sissilka'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='instagramm',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Shaxsiy Instagram sissilka'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='motto',
            field=models.TextField(blank=True, null=True, verbose_name='Shifokor shiori'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='odnoklassniki',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Shaxsiy Ok.ru sissilka'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Shaxsiy Telefon raqam'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='telegram',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Shaxsiy Telegram sissilka'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='twitter',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Shaxsiy Twitter sissilka'),
        ),
    ]