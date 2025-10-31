from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'login'
urlpatterns = [
    path(
        "",
        auth_views.LoginView.as_view(template_name="login/loginform.html"),
        name="login",  # ← name は path() の第3引数で指定
    ),
]
