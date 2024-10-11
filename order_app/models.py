from django.db import models
from customer_app.models import Customer  # Import Customer model

class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Working', 'Working'),
        ('Complete', 'Complete'),
    ]
    ORDER_CUSTOM_CHOICES = [
        ('Head Shot', 'Head Shot'),
        ('Bust Up', 'Bust Up'),
        ('Half Body', 'Half Body'),
        ('Full Body', 'Full Body'),
        ('Personalize', 'Personalize'),
    ]

    order_no = models.AutoField(primary_key=True)
    order_date = models.DateField()
    due_date = models.DateField()
    category = models.CharField(max_length=20, choices=ORDER_CUSTOM_CHOICES, default='Bust Up')
    
    # Setting the default prices
    head_shot_price = models.DecimalField(max_digits=10, decimal_places=2, default=5.00)
    bust_up_price = models.DecimalField(max_digits=10, decimal_places=2, default=10.00)
    half_body_price = models.DecimalField(max_digits=10, decimal_places=2, default=15.00)
    full_body_price = models.DecimalField(max_digits=10, decimal_places=2, default=20.00)
    personalize_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    # Price field that reflects the current price based on the selected category
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='Pending')  # Status choices
    order_file = models.ImageField(upload_to='orders/')  # Assuming order_file is an image
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders', null=True)  # Foreign key to Customer

    def save(self, *args, **kwargs):
        # Update the price based on the selected category
        if self.category == 'Head Shot':
            self.price = self.head_shot_price
        elif self.category == 'Bust Up':
            self.price = self.bust_up_price
        elif self.category == 'Half Body':
            self.price = self.half_body_price
        elif self.category == 'Full Body':
            self.price = self.full_body_price
        elif self.category == 'Personalize':
            self.price = self.personalize_price
        super().save(*args, **kwargs)  # Call the original save method

    def __str__(self):
        return f"Order {self.order_no} for {self.customer.c_fname} {self.customer.c_mname} {self.customer.c_lname} - ID: {self.customer.customer_id}"
