# Generated by Django 4.2.2 on 2023-06-26 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_exclusivas_delete_exclusivos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mejores',
            name='calificacion',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
    ]