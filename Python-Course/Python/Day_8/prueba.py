import unittest
import cambia_texto

class probarCambiaTexto(unittest.TestCase):

    def test_texto(self):
        palabra = 'buen dia'
        resultado = cambia_texto.todoMayusculas(palabra)
        self.assertEqual(resultado, 'buen DIA')

if __name__ == '__main__':
    unittest.main()


