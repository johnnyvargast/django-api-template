from django.urls import reverse
from rest_framework.test import APITestCase

from apps.administrations.models import Tenant
from apps.users.models import DashboardUser


class BaseAPITestCase(APITestCase):

    def login(self):
        dashboard_user_data = {
            "username": "dashboard_user",
            "password": "password",
            "types": "dashboard_user",
            "email": "dashboard_user@django.com",
        }
        self.tenant = Tenant.objects.create(name="test_tenant")
        DashboardUser.objects.create(**dashboard_user_data, tenant=self.tenant)
        user_credentials = {
            "username": dashboard_user_data['username'],
            "password": dashboard_user_data['password'],
        }
        response_login = self.client.post(reverse('users:v1-login'), user_credentials)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response_login.data["access"])
