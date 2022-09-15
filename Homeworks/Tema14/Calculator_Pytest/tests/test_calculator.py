from Homeworks.Tema14.Calculator_Pytest.calculator_oop import Calculator


class Test_calculator:
    def setup_method(self):
        print('Se executa la inceput')
        self.calculator = Calculator(5, 5)

    def teardown_method(self):
        print('Se executa la final')

    def test_adunare(self):
        assert self.calculator.adunare() == 10, 'Adunarea nu este corecta'

    def test_scadere(self):
        assert self.calculator.scadere() == 1, 'Scaderea nu este corecta'

    def test_inmultire(self):
        assert self.calculator.inmultire() == 25, 'Inmultirea nu este corecta'

    def test_impartire(self):
        assert self.calculator.impartire() == 2, 'Impartirea nu este corecta'

    def test_init(self):
        assert self.calculator.a == 5, 'a incorect'
        assert self.calculator.b == 5, 'b incorect'
