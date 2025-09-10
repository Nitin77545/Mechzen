from django.urls import path
from .views import ServiceListView, ServiceDetailView, MechanicDetailView, MechanicListView, PublicProfileUpdate
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView




urlpatterns = [
    path('services/', ServiceListView.as_view(), name='service-list'),
    path('services/<str:title>/', ServiceDetailView.as_view(), name='service-detail'),
    path("mechanics/", MechanicListView.as_view(), name="mechanic-list"),
    path("mechanics/<int:id>/", MechanicDetailView.as_view(), name="mechanic-detail"),
    path("profile/<int:user_id>/", PublicProfileUpdate.as_view(), name="profile-update"),
     path('user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path("user/profile/", PublicProfileUpdate.as_view(), name="profile"),
]
#"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1NzE1MTc1OCwiaWF0IjoxNzU3MDY1MzU4LCJqdGkiOiJjMDQ2Mjg0MjY5YTk0ZWRjODAyZDRiM2IwYTkzM2I1NyIsInVzZXJfaWQiOiIxIn0.MojsTWZRrqfgZzHLHRiNz8wkqv9AEpTmDW9_Cu1pBF8",
    # "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU3MDY1NjU4LCJpYXQiOjE3NTcwNjUzNTksImp0aSI6ImFhOWU5MTU5ZjkyMjQ3MDliNDNjNmY2NjkwYTAwOGNlIiwidXNlcl9pZCI6IjEifQ.ABTPudzbA9sqFsqtNHAJsnowGTQyJbw1td7IhJmjwc4"