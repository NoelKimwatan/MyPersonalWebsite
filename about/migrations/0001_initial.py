# Generated by Django 3.0.8 on 2020-07-27 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_image', models.ImageField(upload_to='uploads/images/mainpage/about')),
                ('description', models.TextField()),
            ],
        ),
    ]
