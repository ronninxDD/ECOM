# Generated by Django 5.2 on 2025-05-02 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('name',), 'verbose_name_plural': 'Products'},
        ),
    ]
