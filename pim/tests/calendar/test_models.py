def test_create_basic_calendar(default_user):
    calendar = Calendar.objects.create(
        owner=default_user,
        name="Default Calendar",
    )
    assert calendar.name == "Default Calendar"
    assert calendar.owner == default_user
    assert default_user.calendars.all().count() == 1
