import os

class Relatório:
    template_dir = "../dados"
    def __init__(self,title, author, template='cabeçalho.tex') -> None:
        self.template = template
        self.cabeçalho=None
        self.title = title
        self.author = author
        self.inicialize()

    def inicialize(self):
        with open(os.path.join(self.template_dir,'../dados/cabeçalho.tex')) as f:
            self.cabeçalho = f.head()