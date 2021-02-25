from companies.models import Company
from entities.models import Object, SubObject, SubObjectTypeTwo


def generate_companies(count=1000, children_count=0, child_children_count=0, sub_objects_count=10):
    result = Company.objects.bulk_create([Company(name='Тестовая компания №%s' % i) for i in range(count)])
    if children_count > 0:
        for c in result:
            children = Object.objects.bulk_create([Object(company=c) for _ in range(children_count)])
            for obj in children:
                SubObject.objects.bulk_create([SubObject(object=obj) for _ in range(child_children_count)])
    return result


def clear_companies():
    Company.objects.all().delete()
    Object.objects.all().delete()
    SubObject.objects.all().delete()
    SubObjectTypeTwo.objects.all().delete()
