# Generated by Django 3.0.7 on 2023-03-27 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20230327_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='linkedin_profile',
        ),
        migrations.AddField(
            model_name='team',
            name='facebook_link',
            field=models.URLField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='team',
            name='google_plus_link',
            field=models.URLField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='team',
            name='twitter_link',
            field=models.URLField(blank=True, max_length=100),
        ),
    ]
