# Generated by Django 5.0.10 on 2024-12-12 18:59

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='default_username', max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('company_name', models.CharField(default='ClassPure', max_length=255)),
                ('mobile_number', models.CharField(max_length=15)),
                ('address', models.TextField(default='Unknown Address')),
                ('password', models.CharField(default='ClassPure#123', max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rate_per_tonne', models.DecimalField(decimal_places=2, max_digits=10)),
                ('approved', models.BooleanField(default=False)),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('tender_id', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=10)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tenders', to='fmcg.supplier')),
            ],
        ),
    ]
