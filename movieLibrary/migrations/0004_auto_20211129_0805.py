# Generated by Django 3.2.9 on 2021-11-29 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieLibrary', '0003_auto_20211129_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movieLogo',
            field=models.FileField(upload_to='movieLibrary/static/video_logo'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_file',
            field=models.FileField(upload_to='movieLibrary/static/videos'),
        ),
    ]
