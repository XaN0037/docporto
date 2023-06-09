# Generated by Django 4.1.7 on 2023-06-22 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_files_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.CharField(max_length=4, verbose_name="Bemorning tug'ilgan yili"),
        ),
        migrations.AlterField(
            model_name='patient',
            name='comment',
            field=models.TextField(default=1, verbose_name='Izox'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='father_name',
            field=models.CharField(default=1, max_length=128, verbose_name='Otasining ismi'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(default=1, max_length=16, verbose_name='Bemorning telefon raqami'),
            preserve_default=False,
        ),
    ]
