# Generated by Django 4.1.4 on 2023-05-08 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_delete_post1_avatar_email_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='avatar',
            name='author',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='avatar',
            name='phone',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]