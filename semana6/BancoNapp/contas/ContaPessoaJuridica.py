from BancoNapp.contas.Conta import Conta


class ContaPessoaJuridica(Conta):
    """
    Limite padrão da conta: R$ 1500,00
    Args:
        Conta ([type]): [description]
    """
    def __init__(self, **kwargs):
        """
        Construtor da classe PessoaJuridica.
        Extrai do dicionário kwargs, a empresa e define o limite
        """
        self.empresa = kwargs.get('empresa')
        super(ContaPessoaJuridica, self).__init__(**kwargs)
        self.limite = kwargs.get('limite', 1500)
