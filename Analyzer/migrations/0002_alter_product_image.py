# Generated by Django 4.0 on 2024-03-10 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analyzer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
    ]
