# Generated by Django 5.1.6 on 2025-04-18 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_customuser_bio_customuser_company_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='brand_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='industry',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
