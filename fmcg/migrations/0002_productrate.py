# Generated by Django 5.0.10 on 2024-12-12 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmcg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255, unique=True)),
                ('rate_per_tonne', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]