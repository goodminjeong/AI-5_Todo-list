from django.urls import path
from users import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('api/signup/', views.SignupView.as_view(), name='signup_view'),
    path('api/login/', views.CustomTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', views.LogoutView.as_view(), name='logout_view'),
    path('api/<int:user_id>/', views.ProfileView.as_view(), name='profile_view'),
]
