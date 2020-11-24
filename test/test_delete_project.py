import random
from model.project import Project


def test_delete_project(app):
    if len(app.project.get_projects_list()) == 0:
        app.project.create(Project(name="new project to delete"))
    old_projects_list = app.soap.get_projects_list(app.config['webadmin']['username'], app.config['webadmin']['password'])
    project_to_delete = random.choice(old_projects_list)
    app.project.delete_project_by_id(project_to_delete.id)
    new_projects_list = app.soap.get_projects_list(app.config['webadmin']['username'], app.config['webadmin']['password'])
    old_projects_list.remove(project_to_delete)
    assert sorted(old_projects_list, key=Project.id_or_max) == sorted(new_projects_list, key=Project.id_or_max)
#    assert project_to_delete not in app.project.get_projects_list()