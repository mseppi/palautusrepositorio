from urllib import request
from project import Project
import tomli

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        data = tomli.loads(content)

        name = data['tool']['poetry']['name']
        description = data['tool']['poetry']['description']
        authors = data['tool']['poetry']['authors']
        license = data['tool']['poetry']['license']
        dependencies = data['tool']['poetry']['dependencies']
        group_dependencies = data['tool']['poetry']['group']['dev']['dependencies']



        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, authors, license, dependencies, group_dependencies)
