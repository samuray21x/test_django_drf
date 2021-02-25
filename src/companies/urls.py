from django.urls import path

from companies import views

urlpatterns = [
    path('', views.CompanyListCreateAPIView.as_view(), name='list__create'),
    path('simple/', views.simple_companies_api, name='list__simple'),
    path('<int:pk>/', views.CompanyRetrieveUpdateDestroy.as_view(), name='retrieve__update__destroy')
]
