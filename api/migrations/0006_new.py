# Generated by Django 4.2.1 on 2023-05-31 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_contacts_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='', verbose_name='Yangilikga oid rasm')),
                ('title', models.CharField(max_length=512, verbose_name='Yangilikning Sarlavha')),
                ('short_desc', models.TextField(verbose_name="Yangilikning Qisqa ma'lumoti")),
                ('desc', models.TextField(verbose_name="Yangilikning To'liq ma'lumoti")),
                ('date', models.DateField(auto_now_add=True, verbose_name='Yangilikni saytga joylash vaqti')),
            ],
        ),
    ]