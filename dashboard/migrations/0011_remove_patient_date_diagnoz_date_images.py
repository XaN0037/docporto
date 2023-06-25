# Generated by Django 4.1.7 on 2023-06-22 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_diagnoz_recommendation_delete_recommendation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='date',
        ),
        migrations.AddField(
            model_name='diagnoz',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('diagnoz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.diagnoz')),
            ],
        ),
    ]
