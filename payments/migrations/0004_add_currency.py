# Generated by Django 4.1.6 on 2023-02-14 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_add_discount_and_tax'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR')], default='USD', max_length=3),
        ),
    ]