from django.urls import path
from .views import BogieFormCreateAPIView, WheelSpecificationListAPIView

urlpatterns = [
    path('forms/bogie-checksheet/', BogieFormCreateAPIView.as_view(), name='bogie-form-create'),
    path('forms/wheel-specifications/', WheelSpecificationListAPIView.as_view(), name='wheel-specification-list'),
]

