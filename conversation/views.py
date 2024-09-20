from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from item.models import Item  # Import Item model
from .forms import ConversationMessageForm  # Import ConversationMessageForm
from .models import Conversation  # Import Conversation model

@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)  # Get the Item object based on item_pk

    if item.created_by == request.user:
        return redirect('dashboard:index')  # Redirect to dashboard if user is the creator of the item
    
    # Check if there are existing conversations related to the item and involving the current user
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        return redirect('conversation:detail', pk=conversations.first().id)  # Redirect to the first conversation detail
    
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)  # Create a form instance with POST data

        if form.is_valid():
            # Create a new Conversation instance for the item
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)  # Add current user to the conversation
            conversation.members.add(item.created_by)  # Add item creator to the conversation
            conversation.save()

            # Save the conversation message linked to the new conversation
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            # this code snippet processes form data submitted by a user to create a new ConversationMessage. It first creates a new message instance (conversation_message) based on form data, assigns it to a specific conversation and sets the author, and then saves it to the database. 

            return redirect('item:detail', pk=item_pk)  # Redirect to item detail page after saving
    else:
        form = ConversationMessageForm()  # Create a new empty form instance
    
    return render(request, 'conversation/new.html', {
        'form': form  # Pass the form to the template for rendering
    })

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])  # Get conversations involving the current user

    return render(request, 'conversation/inbox.html', {
        'conversations': conversations  # Pass conversations to the template for rendering
    })

@login_required
def detail(request, pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)  # Get specific conversation involving the current user

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)  # Create a form instance with POST data

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()  # Save the conversation after adding the new message

            return redirect('conversation:detail', pk=pk)  # Redirect to the same conversation detail page
    else:
        form = ConversationMessageForm()  # Create a new empty form instance

    return render(request, 'conversation/detail.html', {
        'conversation': conversation,  # Pass the conversation object to the template
        'form': form  # Pass the form to the template for rendering
    })
