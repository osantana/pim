def test_create_basic_agenda(default_user):
    agenda = Agenda.objects.create(
        owner=default_user,
        name="Default Agenda",
    )
    assert agenda.name == "Default Calendar"
    assert agenda.owner == default_user
    assert default_user.agendas.all().count() == 1
