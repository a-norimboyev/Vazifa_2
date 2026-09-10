from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name='contact'),
    path('xabarlar/', views.messages_list_view, name='messages_list'),
    path('xabarlar', views.messages_list_view),  # trailing slashsiz ham ishlashi uchun
]
