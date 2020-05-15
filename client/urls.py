from django.urls import path
from client.views.auth import LoginView, LogoutView, registration_view
from client.views.schedule import schedule_view
from client.views.student import score_view
from client.views.teacher import lesson_view
from users.views import password_reset_view, password_reset_confirm_view


urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('register/', registration_view),
    path('password_reset', password_reset_view),
    path('password_reset_confirm/', password_reset_confirm_view),
    path('', schedule_view),
    path('score', score_view),
    path('lesson', lesson_view),

]
