from BancoNapp.contas.Conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, **kwargs):
        super(ContaPoupanca, self).__init__(**kwargs)
        self.limite = kwargs.get('limite', 0)

    def rendimento_aniversario(self, juros):
        if juros < 0 or juros > 1:
            raise ValueError('Os juros precisam ser entre 0 (0%) e 1 (100%).')
        self.saldo += self.saldo*juros
