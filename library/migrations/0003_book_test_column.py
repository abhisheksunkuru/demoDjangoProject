# Generated by Django 5.1.1 on 2024-10-11 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_book_publish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='test_column',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]