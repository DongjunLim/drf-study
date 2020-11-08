import pytest

import django

from django.contrib.auth import get_user_model

django.setup()


@pytest.mark.django_db
def test_create_uesr_with_email_successful():
    """Test creating a new user with an email is successful"""
    email = 'test@gmail.com'
    password = 'testpass123'

    user = get_user_model().objects.create_user(
        email=email,
        password=password
    )

    assert user.email == email
    assert user.check_password(password)


@pytest.mark.django_db
def test_new_user_email_normalized():
    """Test the email for a new user is normalized"""
    email = 'test@GMAIL.com'
    user = get_user_model().objects.create_user(email, 'teset123')

    assert user.email == email.lower()


@pytest.mark.django_db
def test_new_user_invalid_email():
    """Test creating user with no email raises error."""
    with pytest.raises(ValueError):
        get_user_model().objects.create_user(None, '123')


@pytest.mark.django_db
def test_create_super_user_with_email_successful():
    """Test creating a new superuser with an email is successful."""
    email = 'test@gmail.com'
    password = 'test123'
    user = get_user_model().objects.create_superuser(
        email=email,
        password=password
    )

    assert user.is_superuser
    assert user.is_staff
