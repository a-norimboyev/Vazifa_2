from django.db import models


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Ism")
    last_name = models.CharField(max_length=100, verbose_name="Familiya")
    phone_number = models.CharField(max_length=30, verbose_name="Telefon raqam")
    email = models.EmailField(verbose_name="Email manzil")
    message = models.TextField(verbose_name="Yuborilgan xabar")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yuborilgan vaqti")

    class Meta:
        verbose_name = "Xabar"
        verbose_name_plural = "Xabarlar"
        ordering = ['id']

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

