# Generated by Django 5.1.6 on 2025-03-02 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock_number',
            field=models.CharField(default='hxEQKV', max_length=100),
        ),
    ]
