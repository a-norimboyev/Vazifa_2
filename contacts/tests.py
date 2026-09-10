from django.test import TestCase, Client
from django.urls import reverse
from .models import ContactMessage


class ContactMessageTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.sample_message = ContactMessage.objects.create(
            first_name="Furqat",
            last_name="Yo‘ldoshev",
            phone_number="+998993554555",
            email="abcd@gmail.com",
            message="Assalomu alaykum, Sizning darslaringiz menga juda maʼqul kelyapti."
        )

    def test_contact_form_page_get(self):
        """Bosh sahifa ochilganda contact form ko'rinishi kerak."""
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts/contact_form.html')
        self.assertContains(response, 'Bog‘lanish Formasi')
        self.assertContains(response, 'Jo‘natish')

    def test_contact_form_submission_post_success(self):
        """Forma to'ldirilib POST qilinganda bazaga saqlanib, /xabarlar ga yo'naltirilishi kerak."""
        post_data = {
            'first_name': 'Ali',
            'last_name': 'Valiyev',
            'phone_number': '+998901112233',
            'email': 'ali@example.com',
            'message': 'Bu sinov xabari.'
        }
        response = self.client.post(reverse('contact'), data=post_data)
        
        # Redirection tekshiruvi (/xabarlar/ ga)
        self.assertRedirects(response, reverse('messages_list'))
        
        # Bazada yaratilganligini tekshirish
        self.assertTrue(ContactMessage.objects.filter(email='ali@example.com').exists())
        saved_msg = ContactMessage.objects.get(email='ali@example.com')
        self.assertEqual(saved_msg.first_name, 'Ali')
        self.assertEqual(saved_msg.last_name, 'Valiyev')
        self.assertEqual(saved_msg.phone_number, '+998901112233')
        self.assertEqual(saved_msg.message, 'Bu sinov xabari.')

    def test_messages_list_page(self):
        """Xabarlar jadvali sahifasi (/xabarlar/) to'g'ri ishlashi va xabarlarni ko'rsatishi kerak."""
        response = self.client.get(reverse('messages_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts/messages_list.html')
        self.assertContains(response, 'Furqat')
        self.assertContains(response, 'Yo‘ldoshev')
        self.assertContains(response, '+998993554555')
        self.assertContains(response, 'abcd@gmail.com')

    def test_messages_list_without_slash(self):
        """/xabarlar manziliga ham to'g'ridan-to'g'ri kirish mumkin bo'lishi kerak."""
        response = self.client.get('/xabarlar')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Furqat')

