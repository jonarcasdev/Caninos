# Generated by Django 5.1.3 on 2024-11-17 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Correo', models.CharField(max_length=50)),
                ('Contraseña', models.CharField(max_length=50)),
            ],
        ),
    ]
