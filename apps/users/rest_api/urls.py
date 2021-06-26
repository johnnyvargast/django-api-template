from django.urls import path, include

from . import views

app_name = "users"

urlpatterns = [
    path('v1/', include([
        path('login/', views.LoginView.as_view(), name="v1-login"),
        path('token/refresh/', views.RefreshView.as_view(), name="v1-token-refresh"),
        path('logout/', views.LogoutView.as_view(), name="v1-logout"),
    ])),
]
