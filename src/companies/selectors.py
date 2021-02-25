from companies import models


def companies_all():
    return models.Company.objects.all()
