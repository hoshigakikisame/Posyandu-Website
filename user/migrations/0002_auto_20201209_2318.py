# Generated by Django 3.1.4 on 2020-12-09 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biodata',
            name='tgl_lahir_anak',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='biodata',
            name='tgl_lahir_ibu',
            field=models.DateField(),
        ),
    ]
