import random
from model.project import Project


def test_delete_project(app):
    if len(app.project.get_projects_list()) == 0:
        app.project.create(Project(name="new project to delete"))
    app.project.open_projects_page()
    old_projects_list = app.project.get_projects_list()
    project_to_delete = random.choice(app.project.get_projects_list())
    app.project.delete_project_by_id(project_to_delete.id)
    new_projects_list = app.project.get_projects_list()
    old_projects_list.remove(project_to_delete)
    assert sorted(old_projects_list, key=Project.id_or_max) == sorted(new_projects_list, key=Project.id_or_max)
#    assert project_to_delete not in app.project.get_projects_list()