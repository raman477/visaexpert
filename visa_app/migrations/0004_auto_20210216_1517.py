# Generated by Django 3.1.3 on 2021-02-16 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visa_app', '0003_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
