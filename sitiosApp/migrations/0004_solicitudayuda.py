# Generated by Django 3.2.4 on 2021-06-22 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitiosApp', '0003_solicitudtrabajo'),
    ]

    operations = [
        migrations.CreateModel(
            name='solicitudayuda',
            fields=[
                ('correo', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('telefono', models.IntegerField()),
                ('descripcion', models.TextField(max_length=350)),
                ('imagen', models.ImageField(null=True, upload_to='solitudesa')),
            ],
        ),
    ]
