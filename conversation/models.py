from django.db import models

# Importing the User model provided by Django's authentication system
from django.contrib.auth.models import User

# Importing the Item model from another app named 'item'
from item.models import Item

# Conversation model
class Conversation(models.Model):
    # A conversation is associated with an Item using ForeignKey
    item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE)
    
    # Many-to-many relationship with User, as members can be multiple users
    members = models.ManyToManyField(User, related_name='conversations')
    
    # Automatically set the creation timestamp when an instance is created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Automatically update the modified timestamp when an instance is saved
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Ordering conversations based on the modified_at timestamp in descending order
        ordering = ('-modified_at',)


# ConversationMessage model
class ConversationMessage(models.Model):
    # A message is linked to a Conversation using ForeignKey
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    
    # Content of the message, stored as TextField
    content = models.TextField()
    
    # Automatically set the creation timestamp when an instance is created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # The user who created the message, linked via ForeignKey to the User model
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)
