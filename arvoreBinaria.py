class Celula:

    def __init__(self, valor, fd=None, fe=None):
        self.valor = valor
        self.fd = fd
        self.fe = fe

    def __str__(self):
        return 'Nó(' + str(self.valor) + ')'


class arvoreBinaria:

    def __init__(self):
        self.raiz = Celula(None)
        self.raiz = None
        self.ultimo = None

    def buscar(self, valor):
        if self.raiz == None:
            return None
        else:
            aux = self.raiz

            while (valor != aux.valor):

                if valor < aux.valor:
                    aux = aux.fe
                else:
                    aux = aux.fd

                if valor == None:
                    return None

            return aux

    def ultimoNo(self):
        return self.ultimo

    def insercao(self, valor):

        novo = Celula(valor)

        if self.raiz is None:
            self.raiz = novo
        else:
            atual = self.raiz

            while True:
                anterior = atual

                if valor < atual.valor:
                    atual = atual.fe

                    if atual == None:
                        anterior.fe = novo
                        self.ultimo = novo
                        return
                else:
                    atual = atual.fd

                    if atual == None:
                        anterior.fd = novo
                        self.ultimo = novo
                        return

    # o sucessor é o No mais a esquerda da subarvore da direita do No que foi passado como parametro do metodo
    def nosucessor(self, apaga):  # o parâmetro é a referencia para o No que deseja-se apagar

        paisucessor = apaga
        sucessor = apaga
        atual = apaga.fd  # vai para subarvore da direita

        while atual != None:  # enquanto não for o Nó mais a esquerda não sai do while
            paisucessor = sucessor
            sucessor = atual
            atual = atual.fe  # ele caminhando para direita

            # **************************************************
            # quando sair do while, 'sucessor' será o No mais a esquerda da subarvore da direita
            # 'paisucessor' será o pai de sucessor e 'apaga' sera o No que devera ser apagado
            # **************************************************

            if sucessor != apaga.fe:  # se sucessor nao é o filho a direita do No que deve ser eliminado
                paisucessor.fe = sucessor.fd
                # * pai herda os filhos do sucessor que sempre serao a direita
                # * lembrando que o sucessor nunca podera ter filhos a esquerda, pois ele sempre sera o No mais a esquerda da subarvore
                # da direita do No que ira ser apagado
                # * lembrando tambem que o sucessor sempre sera o filho a esquerda do pai
                sucessor.fd = apaga.fd
                # guardando a referencia a direita do sucessor para quando ele assumir a posicao correta na arvore

        return sucessor

    def remover(self, valor):

        if self.raiz == None:
            return False  # Se a arvore for vazia

        atual = self.raiz
        pai = self.raiz
        filhoesquerdo = True

        # ********** VAMOS BUSCAR O VALOR **********

        while atual.valor != valor:  # enquanto ainda nao achou o valor
            pai = atual

            if valor < atual.valor:
                atual = atual.fe
                filhoesquerdo = True  # é filho a esquerda? sim
            else:
                atual = atual.fd
                filhoesquerdo = False  # é filho a esquerda? nao

            if atual == None:
                return False  # encontrou uma folha, e nao tem o valor na arvore -> sai

        # Fim do while para achar o valor

        # ***************************************************************

        # se nao possui nenhum filho (No folha), excluir
        if atual.fe == None and atual.fd == None:

            if atual == self.raiz:
                self.raiz = None  # Se for a raiz
            else:
                if filhoesquerdo:
                    pai.fe = None  # se for filho a esquerda do pai
                else:
                    pai.fd = None  # se for filho a direita do pai

        # ***************************************************************

        # se é pai e não possuir filho a direita, substitui pela subarvore a direita

        elif atual.fd == None:

            if atual == self.raiz:
                self.raiz = atual.fe  # se for a raiz
            else:
                if filhoesquerdo:
                    pai.fe = atual.fe  # se for filho a esquerda do pai
                else:
                    pai.fd = atual.fe  # se for filho a direita do pai

        # ***************************************************************

        # se é pai e não possuir filho a esquerda, substitui pela subarvore da esquerda

        elif atual.fe == None:

            if atual == self.raiz:
                self.raiz = atual.fd  # se for a raiz
            else:
                if filhoesquerdo:
                    pai.fe = atual.fd  # se for filho a esquerda do pai
                else:
                    pai.fd = atual.fd  # se for filho a direita do pai

        # ***************************************************************

        # se é pai e possui filho direito e filho esquerdo

        else:
            # o valor mais a esquerda da subarvore da direita
            sucessor = self.nosucessor(valor)
            # vamos usar o sucessor que é o nó mais a esquerda da subarvore da direita, a melhor opcao para substituir
            if atual == self.raiz:
                self.raiz = sucessor
            else:
                if filhoesquerdo:
                    pai.fe = sucessor
                else:
                    pai.fd = sucessor

            # colocando a continuacao da arvore com  a nova posicao desse No
            sucessor.fe = atual.fe

        return True


arv = arvoreBinaria()
arv.insercao(60)
arv.insercao(49)
arv.insercao(99)
arv.insercao(97)
arv.insercao(74)
arv.insercao(68)
arv.insercao(75)
arv.insercao(5)
arv.insercao(45)
arv.insercao(22)
arv.ultimoNo()
