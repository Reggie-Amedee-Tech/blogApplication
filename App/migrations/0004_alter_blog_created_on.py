# Generated by Django 4.0.10 on 2023-04-03 17:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_alter_blog_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 3, 17, 38, 11, 41093, tzinfo=utc)),
        ),
    ]
