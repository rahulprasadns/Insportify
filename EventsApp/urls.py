"""Insportify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from django.views.generic import TemplateView

# from .views import CheckoutSessionView

app_name = 'EventsApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('show/', views.all_events, name="list-events"),
    path('individual/profile/', views.user_profile, name='user_profile'),
    path('organization/profile/', views.organization_profile, name='organization_profile'),
    path('create/', views.multistep, name='multistep'),
    path('<int:event_id>/', views.event_by_id, name='event_by_id'),
    path('invite/<int:event_id>/', views.invite_by_id, name='invite_by_id'),
    path('invite/', views.invite, name='invite'),
    path('delete/<int:event_id>/', views.delete_by_id, name='delete_by_id'),
    path('get_selected_sports_type/', views.get_selected_sports_type, name='get_selected_sports_type'),
    path('get_sports_category/', views.get_sports_category, name='get_sports_category'),
    path('get_sports_skill/', views.get_selected_sports_skill, name='get_selected_sports_skill'),
    path('get_sports_position/', views.get_selected_sports_positions, name='get_selected_sports_positions'),
    path('get_venue/', views.get_venue_details, name='get_venue'),
    path('add_availability/', views.add_availability, name='add_availability'),
    path('notifications/', views.notifications, name='notifications'),
    path('delete_availability/<int:id>/', views.delete_availability, name='delete_availability'),
    path('upload/', views.logo_upload_view, name='logo_upload'),
    path('event_details/<int:event_id>/', views.event_details, name='event_details'),
    path('cart_summary/', views.cart_summary, name='cart_summary'),

    # PAYMENT URL'S
    path('payment-success/', views.paymentSuccess, name='payment-success'),
    path('payment-cancel/', views.paymentCancel, name='payment-cancel'),
    path('create-checkout-session/<id>/', views.create_checkout_session, name='create-checkout-session'),
]
