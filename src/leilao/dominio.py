

class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        if self._valor_e_valido(valor):
            raise ValueError(
                'Não pode propor um lance com o valor maior que o valor da carteira')

        lance = Lance(self, valor)
        leilao.propoe(lance)

        self.__carteira -= valor

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def _valor_e_valido(self, valor):
        return valor > self.__carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao) -> None:
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    def propoe(self, lance: Lance):
        if self._lance_e_valido(lance):
            if self._tem_lances():
                self.menor_lance = lance.valor
            
            self.maior_lance = lance.valor

            self.__lances.append(lance)
        else:
            raise ValueError('Erro ao propor lance')

    @property
    def lances(self):
        return self.__lances[:]

    def _tem_lances(self) -> list:
        return self.__lances

    def _usuario_diferentes(self, lance):
        return self.__lances[-1].usuario != lance.usuario
    
    def _valor_maior_que_lance_anterior(self, lance):
        return lance.valor > self.__lances[-1].valor

    def _lance_e_valido(self, lance):
        return not self._tem_lances() or (self._usuario_diferentes(lance) and 
                                        self._valor_maior_que_lance_anterior(lance))
