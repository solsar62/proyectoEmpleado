# Generated by Django 3.0.4 on 2020-03-22 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0005_empleado_hoja_vida'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=160, verbose_name='Nombre Completo'),
        ),
    ]