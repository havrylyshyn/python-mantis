from model.project import Project
import random
import string


def test_add_new_project(app):
    project = Project(name="new project2")
    old_projects_list = app.soap.get_projects_list(app.config['webadmin']['username'], app.config['webadmin']['password'])
    if project in old_projects_list:
        project.name = random_string("name", 5)
    app.project.create(project)
    new_projects_list = app.soap.get_projects_list(app.config['webadmin']['username'], app.config['webadmin']['password'])
    old_projects_list.append(project)
    assert sorted(new_projects_list, key=Project.id_or_max) == sorted(old_projects_list, key=Project.id_or_max)
#    assert project in app.project.get_projects_list()


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])