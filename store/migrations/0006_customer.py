# Generated by Django 3.2.12 on 2023-08-12 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_products_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('cemail', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(verbose_name=10)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
    ]
