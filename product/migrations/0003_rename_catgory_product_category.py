# Generated by Django 3.2.5 on 2021-07-12 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='catgory',
            new_name='category',
        ),
    ]