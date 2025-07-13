from django.shortcuts import render

from rest_framework import generics, filters
from .models import BogieForm, WheelSpecification
from .serializers import BogieFormSerializer, WheelSpecificationSerializer

# ====== 1️⃣ POST /api/forms/bogie-checksheet ======

class BogieFormCreateAPIView(generics.CreateAPIView):
    queryset = BogieForm.objects.all()
    serializer_class = BogieFormSerializer


# ====== 2️⃣ GET /api/forms/wheel-specifications ======

class WheelSpecificationListAPIView(generics.ListAPIView):
    serializer_class = WheelSpecificationSerializer

    def get_queryset(self):
        queryset = WheelSpecification.objects.all()

        # Apply optional filters
        form_number = self.request.query_params.get('formNumber')
        submitted_by = self.request.query_params.get('submittedBy')
        submitted_date = self.request.query_params.get('submittedDate')

        if form_number:
            queryset = queryset.filter(formNumber=form_number)
        if submitted_by:
            queryset = queryset.filter(submittedBy=submitted_by)
        if submitted_date:
            queryset = queryset.filter(submittedDate=submitted_date)

        return queryset


# Create your views here.
