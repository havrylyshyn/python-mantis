def test_login(app_auth):
    if app_auth.session.is_logged_in():
        app_auth.session.logout()
    app_auth.session.login("administrator","root")
    assert app_auth.session.is_logged_in_as("administrator")