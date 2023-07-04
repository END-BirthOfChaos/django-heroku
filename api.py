from PIL import Image

import engine

class BroadcastTerminal:

    WARNING = '\033[93m[ENGINE - WARNING]'
    FAILURE = '\033[93m[ENGINE - FAILURE]'
    SUCCESS = '\033[92m[ENGINE - SUCCESS]'

    def __init__(self, message, type):
        self.message = message

        if type == "warning": self.type = self.WARNING
        if type == "failure": self.type = self.FAILURE
        if type == "success": self.type = self.SUCCESS

    def __str__(self):
        print(self.type + " " + self.message)


def getMenu(module_id: str, theme_id: str, titre_menu: str, taille_menu: int) -> Image:
    """
    Renvoie l'image terminé contenant le menu demandé
    Renvoie None si une erreur (voir ci dessous) a été détecté
    - Module inconnu
    - Theme inconnu
    """
    if module_id in engine.getRegisteredModules():
        if theme_id in engine.getModuleThemes(module_id):

            BroadcastTerminal("Le menu '" + titre_menu + "' a été généré avec succès", "success").__str__()
            return engine.getFinalMenu(module_id, theme_id, titre_menu, taille_menu)

        else:
            BroadcastTerminal("Le thème '"+ theme_id  +"' n'existe pas", "warning").__str__()
            return None
    else:
        BroadcastTerminal("Le module '"+ module_id  +"' n'existe pas", "warning").__str__()
        return None


#                              MODULE      THEME       WORD     HEIGHT
#                                |           |          |         |
#                                v           v          v         v

#           image = getMenu("seasonskyV3", "noel", "nom du menu", 6)

getMenu("seasonskyV3", "noel", "aaaaaaaaadddddd", 5).save("generate.png")