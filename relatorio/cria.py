from jinja2 import Environment
import os

class Relatório:
    template_dir = "../dados"
    def __init__(self,titulo, autor, template='cabeçalho.tex') -> None:
        env = Environment(loader=PackageLoader("relatorio"))
        self.template = env.get_template(self.template_file)
        self.cabeçalho=None
        self.titulo = titulo
        self.autor = autor
  
    def render(self):
        return self.template.render(autor=self.autor, titulo=self.titulo)