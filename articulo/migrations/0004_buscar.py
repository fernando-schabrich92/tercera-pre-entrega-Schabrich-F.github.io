# Generated by Django 5.0.2 on 2024-02-21 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0003_programaciona'),
    ]

    operations = [
        migrations.CreateModel(
            name='buscar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
    ]
