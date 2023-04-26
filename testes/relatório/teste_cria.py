import unittest
from relatorio.cria import Relatório

class TestCria(unittest.TestCase):
    def test_cria_relatorio(self):
        R=Relatório('Meu relatório', 'Eu mesmo')
        self.assertEqual(R.titulo, 'Meu relatório')
        