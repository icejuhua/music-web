# Generated by Django 3.2.8 on 2024-02-20 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_web', '0007_auto_20240220_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='music_path',
            field=models.URLField(default='/music/test/', null=True),
        ),
    ]