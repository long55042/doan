# Generated by Django 4.1.4 on 2023-05-10 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_avatar_author_avatar_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='avatar',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]