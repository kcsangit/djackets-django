# Generated by Django 3.2.5 on 2021-07-13 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_catgory_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='person/')),
            ],
        ),
    ]
