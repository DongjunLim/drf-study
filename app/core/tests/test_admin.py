import pytest


from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient


@pytest.fixture(scope='session')
def client():
    return APIClient()


@pytest.mark.django_db
def test_users_listed(client):
    """Test that users are listed on user page."""
    user = get_user_model().objects.create_user(
        email="user123@gmail.com",
        password="password123",
        name="user name"
    )

    admin = get_user_model().objects.create_superuser(
        email="admin123@gmail.com",
        password="password123",
    )

    client.force_login(admin)

    url = reverse('admin:core_user_changelist')
    res = client.get(url)

    assert user.name in str(res.content)
    assert user.email in str(res.content)


@pytest.mark.django_db
def test_user_change_page(client):
    """Test that the user edit page works."""
    user = get_user_model().objects.create_user(
        email="user1234@gmail.com",
        password="password1234",
        name="user name"
    )

    admin = get_user_model().objects.create_superuser(
        email="admin1235@gmail.com",
        password="password1235",
    )

    client.force_login(admin)

    url = reverse('admin:core_user_change', args=[user.id])
    res = client.get(url)

    assert res.status_code == 200


@pytest.mark.django_db
def test_create_user_page(client):
    """Test that the create user page works"""
    get_user_model().objects.create_user(
        email="user1238@gmail.com",
        password="password123",
        name="user name"
    )

    admin = get_user_model().objects.create_superuser(
        email="admin1238@gmail.com",
        password="password123",
    )

    client.force_login(admin)

    url = reverse('admin:core_user_add')
    res = client.get(url)

    assert res.status_code == 200
