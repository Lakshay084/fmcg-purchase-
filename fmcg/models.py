from django.db import models
from django.utils.timezone import now


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True, default='default_username')
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, default="ClassPure")
    mobile_number = models.CharField(max_length=15)
    address = models.TextField(default="Unknown Address")
    password = models.CharField(max_length=255, default="ClassPure#123")
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.username


class Tender(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="tenders")
    product_name = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    rate_per_tonne = models.DecimalField(max_digits=10, decimal_places=2)
    approved = models.BooleanField(default=False)
    delivery_date = models.DateField(null=True, blank=True)
    tender_id = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(
        max_length=10,
        choices=[
            ('Pending', 'Pending'),
            ('Accepted', 'Accepted'),
            ('Rejected', 'Rejected'),
        ],
        default='Pending'
    )

    def __str__(self):
        return f"Tender {self.tender_id} by {self.supplier.name}"
    
class ProductRate(models.Model):
    product_name = models.CharField(max_length=255, unique=True)
    rate_per_tonne = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product_name} - ₹{self.rate_per_tonne} per tonne"    

# Create your models here.
