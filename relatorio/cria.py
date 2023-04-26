class Relatório:
    def __init__(self,title, author, date) -> None:
        self.cabeçalho=None
        self.title = title
        self.author = author
        self.date = date
        self.inicialize()

    def inicialize(self):
        with open('../dados/cabeçalho.tex') as f:
            self.cabeçalho = f.head()