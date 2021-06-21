from rh.classes.Departamento import Departamento
from datetime import date, timedelta


class TestDepartamento:
    def test_class_declared(self):
        objeto = Departamento('Departamento XYZ', 'Diego', 20, 6, 2001)
        assert isinstance(objeto, Departamento)

    def test_instanciar(self):
        objeto = Departamento('Departamento XYZ', 'Diego', 20, 6, 2001)
        assert objeto.nome == 'Departamento XYZ'
        assert objeto.responsavel == 'Diego'

    def test_str_repr(self):
        objeto = Departamento('Departamento XYZ', 'Diego', 20, 6, 2001)
        assert str(objeto) == 'Departamento XYZ'
        assert repr(objeto) == 'Departamento = Departamento XYZ'

    def test_setters(self):
        objeto = Departamento('Curadoria', 'Diego', 20, 6, 2001)
        assert objeto.nome == 'Curadoria'
        objeto.nome = 'ETL'
        assert objeto.nome == 'ETL'

    def test_properties(self):
        objeto = Departamento('Departamento XYZ', 'Diego', 20, 6, 2001)
        assert objeto.nome == 'Departamento XYZ'

    def test_responsavel(self):
        departamento = Departamento('Departamento XYZ', 'Diego', 20, 6, 2001)
        assert departamento.responsavel == 'Diego'
        departamento = Departamento('Departamento XYZ', 'Mateus', 6, 3, 2001)
        assert departamento.responsavel == 'Mateus'

    def test_responsavel_substituido(self):
        departamento = Departamento('Departamento XYZ', 'Diego', 20, 6, 2001)
        assert departamento.responsavel == 'Diego'
        departamento = Departamento('Departamento XYZ', 'Mateus', 6, 3, 2001)
        assert departamento.responsavel == 'Mateus'
        departamento = Departamento('Departamento XYZ', 'Will', 1, 1, 2002)
        assert departamento.responsavel == 'Will'

    def test_add_colaborador(self):
        departamento = Departamento('Departamento XYZ', 'Diego', 20, 6, 2001)
        departamento.add_colaborador('João Oliveira', 18, 3, 1992)
        departamento.add_colaborador('Pedro Mendonça', 18, 4, 1993)
        assert len(departamento.colaboradores) == 2

    def test_verificar_aniversariantes(self):
        retorno = [('João Oliveira', '1992-06-20', 'Departamento XYZ'),
                   ('Luis Fernando', '2000-06-20', 'Departamento XYZ'),
                   ('Diego', '2001-06-20', 'Departamento XYZ')]
        dt1 = date.today() - timedelta(days=4)
        hoje = date.today()
        depto = Departamento('Departamento XYZ', 'Diego', hoje.day, hoje.month, 2001)
        depto.add_colaborador('João Oliveira', hoje.day, hoje.month, 1992)
        depto.add_colaborador('Pedro Mendonça', dt1.day, dt1.month, 1993)
        depto.add_colaborador('Luis Fernando', hoje.day, hoje.month, 2000)
        depto.add_colaborador('Maurício Souza', dt1.day, dt1.month, 1085)
        aniversariantes = depto.verificar_aniversariantes()
        assert aniversariantes == retorno
        assert len(aniversariantes) == 3
        assert len(aniversariantes[0]) == 3
        assert type(aniversariantes[0]) == tuple
        assert type(aniversariantes) == list
