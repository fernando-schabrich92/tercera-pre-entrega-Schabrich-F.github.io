# Generated by Django 5.0.2 on 2024-02-21 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0002_datos'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramacionA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('infocontacto', models.TextField(max_length=300)),
                ('conocimientos', models.TextField(max_length=300)),
            ],
        ),
    ]
