# Generated by Django 3.2.8 on 2024-02-20 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_web', '0008_music_music_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='music_upload_user_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
