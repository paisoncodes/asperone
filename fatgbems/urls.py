from django.urls import path

from fatgbems.views import PaymentNotification, GetInformation


urlpatterns = [
    path("paymentnotification", PaymentNotification.as_view()),
    path("getinformation", GetInformation.as_view())
]