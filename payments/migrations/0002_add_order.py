# Generated by Django 4.1.6 on 2023-02-14 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_add_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.BooleanField(default=False)),
                ('stripe_session_id', models.CharField(blank=True, max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('items', models.ManyToManyField(to='payments.item')),
            ],
        ),
    ]
