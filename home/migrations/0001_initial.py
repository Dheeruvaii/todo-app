# Generated by Django 4.0.4 on 2022-05-30 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('discription', models.TextField(blank=True)),
                ('date', models.DateField(blank=True)),
                ('completed', models.BooleanField(blank=True)),
            ],
        ),
    ]
