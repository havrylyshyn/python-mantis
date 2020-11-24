import string
import random


def random_username(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_signup_new_account(app_auth):
    username = random_username("user_", 10)
    email = username + "@localhost"
    password = 'test'
    app_auth.james.ensure_user_exists(username, password)
    app_auth.signup.new_user(username, email, password)
    assert app_auth.soap.can_login(username, password)