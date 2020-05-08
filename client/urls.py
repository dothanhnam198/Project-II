from django.urls import path
from client.views import LoginView, LogoutView, registration_view
from users.views import password_reset_view, password_reset_confirm_view


urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('register/', registration_view),
    path('password_reset', password_reset_view),
    path('password_reset_confirm/', password_reset_confirm_view),
]
