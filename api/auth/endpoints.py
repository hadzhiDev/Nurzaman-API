from django.urls import path

from .api import custom_login, logout, profile, change_password, test_email_send
from .generic_api import RegisterView, ProfileView, LoginView, ChangePasswordView, DeactivateAccountView


urlpatterns = [
    # path('login/', custom_login, name='login'),
    # path('logout/', logout, name='logout'),
    # path('profile/', profile, name="profile" ),
    # path('change-password/', change_password, name="change_password"),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name="profile" ),
    path('change-password/', ChangePasswordView.as_view(), name="change_password"),
    path('deactivate-account/', DeactivateAccountView.as_view()),
    path('send-test-email/', test_email_send, name='send_test_email'),
]