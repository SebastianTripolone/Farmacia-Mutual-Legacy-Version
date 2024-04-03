# Generated by Django 4.2.4 on 2023-09-30 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.CharField(choices=[('cliente', 'cliente'), ('suscriptor', 'suscriptor'), ('moderador', 'moderador')], default='regular', max_length=100),
        ),
    ]
