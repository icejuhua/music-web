# Generated by Django 3.2.8 on 2024-01-05 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_web', '0003_music_user_musername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music_user',
            name='musername',
            field=models.TextField(default='user', max_length=20),
        ),
    ]
