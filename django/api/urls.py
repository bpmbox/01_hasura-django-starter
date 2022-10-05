from django.urls import path, include
from django.conf.urls import url, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .auth import HasuraTokenObtainPair, ValidateTokenRefreshView, RegisterUser, ChangePassword
from . import logic
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = (
    path('token/', HasuraTokenObtainPair.as_view(), name='token_obtain_pair'),
    path('token/refresh/', ValidateTokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('user/register/', RegisterUser.as_view(), name='register_user'),
    path('user/change_password/', ChangePassword.as_view(), name='change_password'),
    url('user/', include('django_rest_passwordreset.urls', namespace='password_reset')), 
            # + /reset_password/ 
            # + /reset_password/confirm/ 
            # + /reset_password/validate_token/
    # >>> Logic Samples
    path('logic/new_registration_email/', logic.new_registration_email, name='email_registration'),
    path('logic/reset_password_email/', logic.reset_password_email, name='email_reset_password'),
    path('logic/hotdog/', logic.is_hotdog, name='is_hotdog'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
)