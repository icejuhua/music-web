# Generated by Django 3.2.8 on 2024-01-05 03:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Test3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Test_id', models.IntegerField(max_length=200)),
                ('Test_char', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Music_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.IntegerField(default=1)),
                ('photo_path', models.CharField(default='/test/', max_length=556)),
                ('info', models.TextField(default='该用户很懒，什么都没输入', max_length=5)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
