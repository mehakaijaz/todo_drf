# Generated by Django 4.2 on 2023-04-05 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('location', models.CharField(max_length=200)),
                ('rdocs', models.FileField(blank=True, upload_to='rdocs')),
            ],
        ),
    ]
