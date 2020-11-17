# Generated by Django 3.1.3 on 2020-11-17 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20, unique=True)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]