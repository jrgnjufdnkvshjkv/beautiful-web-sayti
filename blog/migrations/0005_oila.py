# Generated by Django 4.2.6 on 2023-10-13 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oila',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ismi', models.CharField(max_length=30)),
                ('familyasi', models.CharField(max_length=30)),
                ('yili', models.IntegerField()),
                ('yoshi', models.IntegerField()),
                ('bio', models.TextField()),
            ],
        ),
    ]