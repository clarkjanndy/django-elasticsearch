from api import views
from django.urls import path

urlpatterns = [
    path('employers', views.EmployerListCreate.as_view()),
    path('employers/<int:id>', views.EmployerById.as_view()),
]
