"""
Estados
=======

Esse módulo tem como finalidade armazenar e retornar os estados referentes a quantidade atual de vida remanescente do jogador.

"""


def vidas_remanescentes(vidas):
    """ Retorna a arte em ASCII referente à quantidade de vidas que o jogador tem.

    :param int vidas: Quantidade de vidas que o jogador tem
    """
    return VIDAS_REMANESCENTES[vidas]


VIDAS_REMANESCENTES = list(range(0, 8))

VIDAS_REMANESCENTES[0] = """
█████████████████████████████████████████████████████████████████████
█████████████████████████|_X̲_____________________  |█████████████████
███████████████████████████|█████████████████████| |█████████████████
███████████████████████████|█████████████████████| |█████████████████
███████████████████████████|█████████████████████| |█████████████████
███████████████████████████|████|x          x|███| |█████████████████
███████████████████████████|████|   <3 = 0   |███| |█████████████████
███████████████████████████|████|x̲__________x̲|███| |█████████████████
███████████████████████████=█████████████████████| |█████████████████
████████████████████████/x̳. x̳ \██████████████████| |█████████████████
             ___________\_N̲____P_________________| |________
            /       _____'===' \_______________  | |        /| 
   v       /       / \████|___||\\██████████████/ | |       / |
          /       /   \███|\\\\\\\\█\\\\████████████/  | |__    /  /
         /       /     \██()\\\\\\\\(_)██████████/  /| | /   /  /
        /       /       \███(/(/████████████/  /____/   /  /
       /       /        /██████████████████/           /  /
      /       /________/██████████████████/           /  /
     /                                               /  /
    /                                               /  /
   /_______________________________________________/  /
   |                                               | /    v
   |_______________________________________________|/ 	
v
"""

VIDAS_REMANESCENTES[1] = """
█████████████████████████████████████████████████████████████████████
█████████████████████████|_X̲_____________________  |█████████████████
███████████████████████████|█████████████████████| |█████████████████
███████████████████████████|█████████████████████| |█████████████████
███████████████████████████|█████████████████████| |█████████████████
███████████████████████████|████|x          x|███| |█████████████████
███████████████████████████|████|   <3 = 1   |███| |█████████████████
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓|▓▓▓▓|x̲__________x̲|▓▓▓| |▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓=▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓| |▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓/Ó. Ò \▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓| |▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
             ___________\_o̲____P_________________| |________
            /       _____'===' \_______________  | |        /| 
   v       /       /    //|___|\\\\/             / | |       / |
          /       /    // || || \\\\            /  | |__    /  /
         /       /   (_)  || ||/(_)          /  /| | /   /  /
        /       /        (_| |_)            /  /____/   /  /
       /       /             /             /           /  /
      /       /_____________/_____________/           /  /
     /                                               /  /
    /                                               /  /
   /_______________________________________________/  /
   |                                               | /    v
   |_______________________________________________|/
v
"""

VIDAS_REMANESCENTES[2] = """
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓|_X̲_____________________  |▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓|▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓| |▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓|▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓| |▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓|▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓| |▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓|▓▓▓▓|x          x|▓▓▓| |▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓|▓▓▓▓|   <3 = 2   |▓▓▓| |▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓|▓▓▓▓|x̲__________x̲|▓▓▓| |▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓=▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓| |▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓/Ó. Ò \▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓| |▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
             ___________\_o̲____P_________________| |________
            /       _____'===' \_______________  | |        /| 
   v       /       /    //|___|\\\\/             / | |       / |
          /       /    // ||    \\\\            /  | |__    /  /
         /       /   (_)  ||   /(_)          /  /| | /   /  /
        /       /        (_|  /             /  /____/   /  /
       /       /             /             /           /  /
      /       /_____________/_____________/           /  /
     /                                               /  /
    /                                               /  /
   /_______________________________________________/  /
   |                                               | /    v
   |_______________________________________________|/
v
"""

VIDAS_REMANESCENTES[3] = """
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓|_X̲_____________________  |▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓|▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓| |▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓|▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓| |▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓|▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓| |▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓|▓▓▓▓|x          x|▓▓▓| |▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓|▓▓▓▓|   <3 = 3   |▓▓▓| |▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒|▒▒▒▒|x̲__________x̲|▒▒▒| |▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒=▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒| |▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒/Ó. Ò \▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒| |▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
             ___________\_o̲____P_________________| |________
            /       _____'===' \_______________  | |        /| 
   v       /       /    //|___|\\\\/             / | |       / |
          /       /    //       \\\\            /  | |__    /  /
         /       /   (_)       /(_)          /  /| | /   /  /
        /       /             /             /  /____/   /  /
       /       /             /             /           /  /
      /       /_____________/_____________/           /  /
     /                                               /  /
    /                                               /  /
   /_______________________________________________/  /
   |                                               | /    v
   |_______________________________________________|/
v
"""

VIDAS_REMANESCENTES[4] = """
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒|_X̲_____________________  |▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒|▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒| |▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒|▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒| |▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒|▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒| |▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒|▒▒▒▒|x          x|▒▒▒| |▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒|▒▒▒▒|   <3 = 4   |▒▒▒| |▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒|▒▒▒▒|x̲__________x̲|▒▒▒| |▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒=▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒| |▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒/Ó. Ò \▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒| |▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
             ___________\_o̲____P_________________| |________
            /       _____'===' ________________  | |        /| 
   v       /       /    //|___|  /             / | |       / |
          /       /    //       /             /  | |__    /  /
         /       /   (_)       /             /  /| | /   /  /
        /       /             /             /  /____/   /  /
       /       /             /             /           /  /
      /       /_____________/_____________/           /  /
     /                                               /  /
    /                                               /  /
   /_______________________________________________/  /
   |                                               | /    v
   |_______________________________________________|/
v
"""

VIDAS_REMANESCENTES[5] = """
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒|_X̲_____________________  |▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒|▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒| |▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒|▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒| |▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒|▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒| |▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒|▒▒▒▒|x          x|▒▒▒| |▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒|▒▒▒▒|   <3 = 5   |▒▒▒| |▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
░░░░░░░░░░░░░░░░░░░░░░░░░░░|░░░░|x̲__________x̲|░░░| |░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░=░░░░░░░░░░░░░░░░░░░░░| |░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░/Ó. Ò \░░░░░░░░░░░░░░░░░░| |░░░░░░░░░░░░░░░░░
             ___________\_o̲____P_________________| |________
            /       _____'===' ________________  | |        /| 
   v       /       /      |___|  /             / | |       / |
          /       /             /             /  | |__    /  /
         /       /             /             /  /| | /   /  /
        /       /             /             /  /____/   /  /
       /       /             /             /           /  /
      /       /_____________/_____________/           /  /
     /                                               /  /
    /                                               /  /
   /_______________________________________________/  /
   |                                               | /    v
   |_______________________________________________|/
v
"""

VIDAS_REMANESCENTES[6] = """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░|_X̲_____________________  |░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░|░░░░░░░░░░░░░░░░░░░░░| |░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░|░░░░░░░░░░░░░░░░░░░░░| |░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░|░░░░░░░░░░░░░░░░░░░░░| |░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░|░░░░|x          x|░░░| |░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░|░░░░|   <3 = 6   |░░░| |░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░|░░░░|x̲__________x̲|░░░| |░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░=░░░░░░░░░░░░░░░░░░░░░| |░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░/Ó. Ò \░░░░░░░░░░░░░░░░░░| |░░░░░░░░░░░░░░░░░
             ___________\_o̲____P_________________| |________
            /       _____'===' ________________  | |        /| 
   v       /       /             /             / | |       / |
          /       /             /             /  | |__    /  /
         /       /             /             /  /| | /   /  /
        /       /             /             /  /____/   /  /
       /       /             /             /           /  /
      /       /_____________/_____________/           /  /
     /                                               /  /
    /                                               /  /
   /_______________________________________________/  /
   |                                               | /    v
   |_______________________________________________|/
v
"""

VIDAS_REMANESCENTES[7] = """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░|_X̲_____________________  |░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░|░░░░░░░░░░░░░░░░░░░░░| |░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░|░░░░░░░░░░░░░░░░░░░░░| |░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░|░░░░░░░░░░░░░░░░░░░░░| |░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░|░░░░|x          x|░░░| |░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░|░░░░|   <3 = 7   |░░░| |░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░|░░░░|x̲__________x̲|░░░| |░░░░░░░░░░░░░░░░░
                           =                     | |
__________________________ =_____________________| |_________________
             _____________/_\____________________| |________
            /       _____/___\_________________  | |        /| 
   v       /       /     \___/   /             / | |       / |
          /       /             /             /  | |__    /  /
         /       /             /             /  /| | /   /  /
        /       /             /             /  /____/   /  /
       /       /             /             /           /  /
      /       /_____________/_____________/           /  /
     /                                               /  /
    /                                               /  /
   /_______________________________________________/  /
   |                                               | /    v
   |_______________________________________________|/
v
"""
