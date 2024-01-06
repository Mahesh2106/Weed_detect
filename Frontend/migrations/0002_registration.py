# Generated by Django 3.2.10 on 2023-11-19 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Password', models.CharField(blank=True, max_length=8, null=True)),
                ('Confirm_Password', models.CharField(blank=True, max_length=8, null=True)),
            ],
        ),
    ]
