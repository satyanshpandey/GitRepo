# Generated by Django 5.0.4 on 2025-03-24 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=111)),
                ('salary', models.IntegerField()),
                ('phoneNumber', models.CharField(max_length=222)),
            ],
        ),
    ]
