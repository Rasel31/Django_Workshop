# Generated by Django 2.2.10 on 2020-04-30 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('desc', models.TextField(blank=True, verbose_name='Description')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=200)),
                ('contact_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
