from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    # The provided Django Meta class sets 2 options for a model called "Categories":
    # ordering = ('name','): Specifies the default ordering of model instances based on the 'name' field in ascending order when querying the database.
    # verbose_name_plural = 'Categories': Defines a custom plural name for the model, so it's referred to as 'Categories' when dealing with multiple instances in the application, rather than the automatically generated plural form.


    def __str__(self):
        return self.name

class Item(models.Model):
    # A foreign key relationship to the Category model.
    # Each item belongs to a category.
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)

    # A short text field to store the name of the item.
    name = models.CharField(max_length=255)

    # A text field for an optional item description.
    description = models.TextField(blank=True, null=True)

    # A field to store the price of the item as a floating-point number.
    price = models.FloatField()

    # An image field for uploading and storing item images.
    image = models.ImageField(upload_to='item_images', blank=True, null=True)

    # A boolean field to indicate whether the item has been sold or not.
    is_sold = models.BooleanField(default=False)

    # A foreign key relationship to the User model.
    # Indicates the user who created this item.
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)

    # A date and time field that records when the item was created.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # returns a name of the item.
        return self.name
