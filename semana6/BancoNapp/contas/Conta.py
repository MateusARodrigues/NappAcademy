class Conta:
    def __init__(self, **kwargs):
        self.extrato = []
        self.limite = kwargs.get('limite', 500)
        self.nome = kwargs.get('nome', None)
        self.saldo = kwargs.get('saldo', 0)
        if self.saldo < 0:
            raise ValueError('Saldo negativo')
        self.extrato.append(('I', self.saldo))
    def deposito(self, valor):
        if isinstance(valor, (float, int)):
            if valor <= 0:
                raise ValueError('Valor do depósito precisa ser maior que zero')
            self.saldo = self.saldo + valor
            self.extrato.append(('D', valor))
            return
        raise TypeError('O depósito precisa ser numérico')
    def saque(self, valor):
        if isinstance(valor, (float, int)):
            if self.limite:
                if valor > (self.saldo + self.limite):
                    raise ValueError('Valor do saque supera seu saldo e seu limite')
                    return
            else:
                if valor > self.saldo:
                    raise ValueError('Valor do saque supera seu saldo.')
                    return
            self.saldo = self.saldo - valor
            self.extrato.append(('S', valor))
            return valor
        raise TypeError('O valor do saque precisa ser numérico')
    def get_extrato(self):
        return self.extrato
