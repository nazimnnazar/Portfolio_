# Generated by Django 4.1 on 2023-02-20 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=540)),
                ('Project_Discription', models.TextField()),
                ('images', models.ImageField(upload_to='Projects')),
            ],
        ),
    ]
