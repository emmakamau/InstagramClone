# Generated by Django 4.0.5 on 2022-06-05 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_comment',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_caption',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
