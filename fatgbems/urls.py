from django.urls import path

from fatgbems.views import PaymentNotification


urlpatterns = [
    path("pay", PaymentNotification.as_view())
]