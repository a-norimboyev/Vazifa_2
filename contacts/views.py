from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage
from .forms import ContactMessageForm


def contact_view(request):
    """Bosh sahifada kontakt formasini ko'rsatish va xabarni saqlash."""
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Xabaringiz muvaffaqiyatli yuborildi va saqlandi!")
            return redirect('messages_list')
    else:
        form = ContactMessageForm()

    context = {
        'form': form
    }
    return render(request, 'contacts/contact_form.html', context)


def messages_list_view(request):
    """Barcha foydalanuvchilardan kelgan xabarlarni jadval shaklida ko'rsatish."""
    contact_messages = ContactMessage.objects.all().order_by('id')
    context = {
        'messages_list': contact_messages
    }
    return render(request, 'contacts/messages_list.html', context)

