from rest_framework import serializers

from core.serializers import DynamicFieldsModelSerializer
from companies import models
from entities.models import Object, SubObject
from entities import serializers as entities_serializers


class CompanySerializer(DynamicFieldsModelSerializer, serializers.ModelSerializer):
    entities_objects = entities_serializers.ObjectSerializer(many=True, read_only=True)

    class Meta:
        model = models.Company
        fields = '__all__'


def companies_inline_serializer(companies):
    return [{
        'id': company.id,
        'name': company.name,
        'uuid': company.uuid,
        'boolean_1': company.boolean_1,
        'boolean_2': company.boolean_2,
        'boolean_3': company.boolean_3,
        'boolean_4': company.boolean_4,
        'boolean_5': company.boolean_5,
        'boolean_6': company.boolean_6,
        'boolean_7': company.boolean_7,
        'integer_1': company.integer_1,
        'integer_2': company.integer_2,
        'integer_3': company.integer_3,
        'integer_4': company.integer_4,
        'integer_5': company.integer_5,
        'date_1': company.date_1,
        'date_2': company.date_2,
        'date_3': company.date_3,
        'date_4': company.date_4,
        'string_1': company.string_1,
        'string_2': company.string_2,
        'string_3': company.string_3,
        'string_4': company.string_4,
        'string_5': company.string_5,
        'objects': [company_object_inline_serializer(obj) for obj in company.entities_objects.all()]
    } for company in companies]


def company_object_inline_serializer(obj: Object):
    return {
        'name': obj.name,
        'uuid': obj.uuid,
        'boolean_1': obj.boolean_1,
        'boolean_2': obj.boolean_2,
        'boolean_3': obj.boolean_3,
        'boolean_4': obj.boolean_4,
        'boolean_5': obj.boolean_5,
        'boolean_6': obj.boolean_6,
        'boolean_7': obj.boolean_7,
        'integer_1': obj.integer_1,
        'integer_2': obj.integer_2,
        'integer_3': obj.integer_3,
        'integer_4': obj.integer_4,
        'integer_5': obj.integer_5,
        'date_1': obj.date_1,
        'date_2': obj.date_2,
        'date_3': obj.date_3,
        'date_4': obj.date_4,
        'string_1': obj.string_1,
        'string_2': obj.string_2,
        'string_3': obj.string_3,
        'string_4': obj.string_4,
        'string_5': obj.string_5,
        'sub_objects': [object_sub_objects_inline_serializer(sub_obj) for sub_obj in obj.sub_objects.all()]
    }


def object_sub_objects_inline_serializer(obj: SubObject):
    return {
        'name': obj.name,
        'uuid': obj.uuid,
        'boolean_1': obj.boolean_1,
        'boolean_2': obj.boolean_2,
        'boolean_3': obj.boolean_3,
        'boolean_4': obj.boolean_4,
        'boolean_5': obj.boolean_5,
        'boolean_6': obj.boolean_6,
        'boolean_7': obj.boolean_7,
        'integer_1': obj.integer_1,
        'integer_2': obj.integer_2,
        'integer_3': obj.integer_3,
        'integer_4': obj.integer_4,
        'integer_5': obj.integer_5,
        'date_1': obj.date_1,
        'date_2': obj.date_2,
        'date_3': obj.date_3,
        'date_4': obj.date_4,
        'string_1': obj.string_1,
        'string_2': obj.string_2,
        'string_3': obj.string_3,
        'string_4': obj.string_4,
        'string_5': obj.string_5,
    }
