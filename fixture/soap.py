from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:
    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self, username, password):
        projects_list = []
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            for project in client.service.mc_projects_get_user_accessible(username, password):
                projects_list.append(Project(id=project.id, name=project.name))
            return projects_list
        except WebFault:
            return projects_list
