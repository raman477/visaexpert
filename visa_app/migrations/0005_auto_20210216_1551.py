# Generated by Django 3.1.3 on 2021-02-16 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visa_app', '0004_auto_20210216_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
    ]
