# Generated by Django 5.0.7 on 2024-07-19 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_author', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='author_kkk',
        ),
    ]
