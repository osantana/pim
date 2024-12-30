import pytest
from calendar.models import Calendar
from django.db.utils import IntegrityError  # <.>


pytestmark = pytest.mark.django_db


def test_create_basic_calendar(default_user):
    calendar = Calendar.objects.create(
        owner=default_user,
        name='Default Calendar',
    )
    assert calendar.name == 'Default Calendar'
    assert calendar.owner == default_user
    assert default_user.calendars.all().count() == 1


def test_fail_create_calendar_missing_owner():
    with pytest.raises(IntegrityError):  # <.>
        Calendar.objects.create(owner=None, name='Default Calendar')
