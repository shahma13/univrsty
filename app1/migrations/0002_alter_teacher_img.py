# Generated by Django 4.2.7 on 2023-11-29 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
