from rest_framework import serializers

from core.serializers import DynamicFieldsModelSerializer
from entities import models


class SubObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubObject
        fields = '__all__'


class ObjectSerializer(serializers.ModelSerializer):
    sub_objects = SubObjectSerializer(many=True, read_only=True)

    class Meta:
        model = models.Object
        fields = (
            'id',
            'name',
            'uuid',
            'boolean_1',
            'boolean_2',
            'boolean_3',
            'boolean_4',
            'boolean_5',
            'boolean_6',
            'boolean_7',
            'integer_1',
            'integer_2',
            'integer_3',
            'integer_4',
            'integer_5',
            'date_1',
            'date_2',
            'date_3',
            'date_4',
            'string_1',
            'string_2',
            'string_3',
            'string_4',
            'string_5',
            'sub_objects',
        )



