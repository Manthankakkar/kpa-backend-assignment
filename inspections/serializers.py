from rest_framework import serializers
from .models import (
    BMBCChecksheet, BogieChecksheet, BogieDetails, BogieForm,
    WheelSpecificationFields, WheelSpecification
)

# ===== Bogie Form Serializers =====

class BMBCChecksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BMBCChecksheet
        fields = '__all__'

class BogieChecksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BogieChecksheet
        fields = '__all__'

class BogieDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BogieDetails
        fields = '__all__'

class BogieFormSerializer(serializers.ModelSerializer):
    bmbcChecksheet = BMBCChecksheetSerializer()
    bogieChecksheet = BogieChecksheetSerializer()
    bogieDetails = BogieDetailsSerializer()

    class Meta:
        model = BogieForm
        fields = '__all__'

    def create(self, validated_data):
        bmbc_data = validated_data.pop('bmbcChecksheet')
        bogie_data = validated_data.pop('bogieChecksheet')
        details_data = validated_data.pop('bogieDetails')

        bmbc_obj = BMBCChecksheet.objects.create(**bmbc_data)
        bogie_obj = BogieChecksheet.objects.create(**bogie_data)
        details_obj = BogieDetails.objects.create(**details_data)

        return BogieForm.objects.create(
            bmbcChecksheet=bmbc_obj,
            bogieChecksheet=bogie_obj,
            bogieDetails=details_obj,
            **validated_data
        )

# ===== Wheel Specification Serializers =====

class WheelSpecificationFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelSpecificationFields
        fields = '__all__'

class WheelSpecificationSerializer(serializers.ModelSerializer):
    fields = WheelSpecificationFieldsSerializer()

    class Meta:
        model = WheelSpecification
        fields = '__all__'

    def create(self, validated_data):
        fields_data = validated_data.pop('fields')
        fields_obj = WheelSpecificationFields.objects.create(**fields_data)
        return WheelSpecification.objects.create(fields=fields_obj, **validated_data)
