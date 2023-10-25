# Generated by Django 4.2.6 on 2023-10-23 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('adress', models.CharField(blank=True, max_length=200)),
                ('postal_code', models.CharField(blank=True, max_length=20)),
                ('city', models.CharField(blank=True, max_length=200)),
                ('state', models.CharField(blank=True, max_length=200)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('rfc', models.CharField(blank=True, max_length=50)),
                ('country', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
