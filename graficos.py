"""
Graficos
========

Esse módulo tem como objetivo agrupar as funções que imprimem a interface ASCII no prompt do usuário


"""
# Grupo: Ana Carolina Erthal Fernandes, Eduardo Adame Salles, Murilo Calegari de Souza, Tiago Barradas Figueiredo, Rodrigo Gomes Hutz Pintucci e Vinícius Hedler
# Documentação Sphinx: https://graficoforcaascii.readthedocs.io/en/latest/


import os
import estados
import sys

# Criação da variável this que recebe o módulo graficos e servirá para ter controle dentro das funções sobre as variáveis que estão fora delas:
this = sys.modules[__name__]


# Definição das variáveis globais iniciais:
this.vidas_remanescentes = 7
this.palavra_secreta = ""
this.lista_letras_erradas = []
this.tema = ""

separador = "---------------------------------------------------------------------"


def cls():
    """Limpa o texto do terminal."""
    print()
    os.system("clear")


def tela_inicio():
    """Exibe a tela de início do jogo e espera um input qualquer. Não está vinculado a ``inicializar_jogo`` para possibilitar a escolha de apresentar a tela apenas quando o programa for iniciado ou após cada jogo."""
    cls()
    print("""                                                              
                                                                 
    ______________________                                
   |  __________________X̲_|    \\  |  |  /                  
   | |                    |   \\  _________  /                          
   | |                    |  \\  /  ◕ u ◕  \\  /                       
___| |____________________|____/___________\\________________/\\../\\___
   | |                    |   v                             > || <
   | |_______________     |                                 \\/  \\/
   |  _______________|    =                                   
   | |                   _=_        _  __      ______      ______
   | |                  / _ \\      | |/ _|    /  ___ \\     \\____ \\
   | |                 / / \\ \\     | | /     |  /   \\_|     ____\\ \\ 
   | |             v  | |   | |    |  /      | |     _     /  ___  \\
   | |                 \\ \\_/ /     | |       |  \___/ |   |  |___|  \\
   | |__                \\___/      |_|        \\______/     \\______/\\_\\
  /| | /                                                               
 /____/                            v                        
                     v                                     v          
                                                                   v
        v                    _________________
                            |x               x|
                            |   Aperte Enter  |
                            |      para       |
                            |   Inicializar   |       
                            |x̲_______________x̲|
""")
    input()


def inicializar_jogo(palavra_secreta_inicial, tema="", print_input=False):
    """Inicializa o jogo para o módulo gráfico dada a palavra_secreta_inicial, resetando as variáveis do módulo.

      :param str palavra_secreta_inicial: A palavra a ser advinhada

      :param str tema: Tema para a palavra a ser advinhada. (Opcional)

      :type tema: str, optional

      :param bool print_input: Determina se deve ou não exibir a mensagem requisitando o input de letras. (Opcional)

      :type print_input: bool, optional

    """
    this.vidas_remanescentes = 7
    this.palavra_secreta = palavra_secreta_inicial
    this.lista_letras_erradas = []
    this.tema = tema
    this.print_input = print_input
    atualizar_tela()


def atualizar_tela():
    """Atualiza a interface gráfica por completo, utilizando os estados atuais de cada container"""
    print()
    cls()

    # Imprime a lista das letras erradas
    print("Letras incorretas")
    print(separador)
    for letra_errada in this.lista_letras_erradas:
        print(letra_errada, end=" ")
    print("")
    print(separador)
    # Imprime a imagem da forca
    print(estados.vidas_remanescentes(this.vidas_remanescentes))

    # Imprime a palavra secreta
    print(separador)
    print(this.palavra_secreta)
    print(separador)
    if this.tema != "":
        print("Tema:", this.tema)
        print(separador)

    if this.print_input:
        if this.vidas_remanescentes != 0:
            print("Insira uma letra: ", end="")
        else:
            print("Aperte enter para recomeçar ou insira \"S\" para sair: ", end="")


def atualizar_forca(vidas):
    """Atualiza a imagem da forca (globalmente) e a interface com a nova imagem. Deve ser utilizada quando o usuário perde uma vida.

    :param int vidas: Quantidade de vidas remanescentes do jogador
    """
    this.vidas_remanescentes = vidas
    atualizar_tela()


def atualizar_palavra(palavra):
    """Atualiza a palavra sendo adivinhada (globalmente) e a interface com o novo estado da palavra. Deve ser utilizada quando o usuário acerta uma letra.

    :param str palavra: O novo estado da palavra a ser adivinhada, com mais letras impressas.
    """
    this.palavra_secreta = palavra
    atualizar_tela()


def atualizar_erros(letras_erradas):
    """Atualiza a lista das letras erradas (globalmente) e a interface com a nova lista de letras erradas. Deve ser utilizada quando o usuário erra uma letra.

    :param list letras_erradas: Lista contendo todas as letras que o usuário digitou mas não estavam contidas na palavra secreta.
    """

    this.lista_letras_erradas = letras_erradas
    atualizar_tela()


def imprimir_vitoria(palavra_secreta):
    """Atualiza a tela com uma mensagem de vitória.

    :param str palavra_secreta: A palavra adivinhada.
    """
    cls()
    print("""
                                                 /\\               
                                _____________    | |                
                                |x          x|   | |                 
                                |Você venceu!|   | |      \\  |  |  /           
                                |x̲__________x̲|   | |   \\  _________  /
                                                 | |  \\  / -▉ u ▉- \\  /
_________________________________________________| |____/___________\\
            / ¬▊.▊\\______________________________| |________         
            Գ___u̲_/ ___________________________  | |        /| 
   v       //    \\\\/             /             / | |       / |
          ///|___|\\\\            /             /  | |__    /  /
         /// || || \\\\ ________ /             /  /| | /   /  /
        (_)  || || (_) _______<             /  /____/   /  /
       /    (_|/|_) / /      /             /           /  /
      /       /____/ /______/_____________/           /  /
     /            / /                                /  /
    /            / /                                /  /
   /____________/ /________________________________/  /
   |           /x/                                 | /    v
   |_________ /_/|_________________________________|/
                  \\_______                 _____
                          \\___________,,,,/     \\
                                          \\_____/
""")
    print(f"Parabéns você adivinhou {palavra_secreta}!!!")
    input("Aperte enter para continuar")
