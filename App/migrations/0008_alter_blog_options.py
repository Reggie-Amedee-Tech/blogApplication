# Generated by Django 4.0.10 on 2023-05-03 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_blog_slug_blog_status_alter_blog_created_on_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-created_on']},
        ),
    ]