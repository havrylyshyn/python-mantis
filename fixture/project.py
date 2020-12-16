from model.project import Project
import re


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def create(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_xpath("//input[@value = 'Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_class_name("button").click()
        self.open_projects_page()

    def get_projects_list(self):
        wd = self.app.wd
        projects_list = []
        self.open_projects_page()
        for element in wd.find_elements_by_xpath("//a[contains(@href,'manage_proj_edit_page.php?project_id')]"):
            name = element.text
            id = [int(s) for s in re.findall(r'\d+', element.get_attribute('href'))][-1]
            projects_list.append(Project(name=name, id=id))
        return projects_list

    def open_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(@href,'manage_proj_edit_page.php?project_id=%s')]" % id).click()

    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.open_projects_page()
        self.open_project_by_id(id)
        wd.find_element_by_xpath("//input[@value = 'Delete Project']").click()
        wd.find_element_by_xpath("//input[@value = 'Delete Project']").click()