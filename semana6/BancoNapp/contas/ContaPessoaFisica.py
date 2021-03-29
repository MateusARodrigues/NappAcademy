from BancoNapp.contas.Conta import Conta


class ContaPessoaFisica(Conta):
    def __init__(self,  **kwargs):
        super(ContaPessoaFisica, self).__init__(**kwargs)
        self.profissao = kwargs.get('profissao', '')
