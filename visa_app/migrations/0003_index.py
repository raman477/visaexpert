# Generated by Django 3.1.3 on 2021-02-16 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visa_app', '0002_auto_20210210_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
    ]
