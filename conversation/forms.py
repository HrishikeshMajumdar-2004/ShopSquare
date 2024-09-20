from django import forms

# Importing the ConversationMessage model from the current app
from .models import ConversationMessage

# Defining a form class for ConversationMessage
class ConversationMessageForm(forms.ModelForm):
    class Meta:
        # Specify the model to use for the form
        model = ConversationMessage
        
        # Specify which fields from the model should be included in the form
        fields = ('content',)
        
        # Define widgets to customize the form field's appearance and behavior
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'  # CSS classes for styling the Textarea
            })
        }
