# Generated by Django 5.0.2 on 2024-02-21 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('infocontacto', models.TextField(max_length=300)),
            ],
        ),
    ]
