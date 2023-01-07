from django.urls import path, include
from .views import RegisterUserView, EmployerView, JobsView
from rest_framework import routers
router = routers.DefaultRouter()
router.register('Employer/', EmployerView)
router.register('Jobs/', JobsView)
urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('emloyer/', include(router.urls))
]