# Generated by Django 4.1.6 on 2023-02-14 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_add_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='discounts',
            field=models.ManyToManyField(blank=True, to='payments.discount'),
        ),
        migrations.AddField(
            model_name='order',
            name='taxes',
            field=models.ManyToManyField(blank=True, to='payments.tax'),
        ),
    ]
