
from PIL import Image

import json


###################################################
#                                                 #
#              CONFIGURATION HANDLER              #
#                                                 #
###################################################


def getModuleConfiguration() -> dict:
    """
    Renvoie un dictionnaire avec le contenu du ficher 'module-config.json'
    """
    file = open("module-config.json")
    return json.load(file)


def getRegisteredModules() -> list:
    """
    Renvoie une liste contenant les modules enregistrés
    """
    modules_dict = getModuleConfiguration().keys()
    modules_list = []

    for module in modules_dict:
        modules_list.append(module)

    return modules_list


def getModule(module_id: str) -> dict:
    """
    Renvoie un dictionnaire contenant la configuration du module
    Renvoie None si aucune configuration n'a été trouvé
    """
    if getModuleConfiguration().get(module_id) is not None:
        return getModuleConfiguration().get(module_id)


def getModuleName(module_id: str) -> str:
    """
    Renvoie le nom du module choisi
    Renvoie None si aucun nom n'a été trouvé
    """
    if getModule(module_id).get("module-name") is not None:
        return getModule(module_id).get("module-name")


def getModuleThemes(module_id: str) -> list:
    """
    Renvoie une liste contenant les thèmes associés au module
    Renvoie None si aucun thème n'a été trouvé
    """
    if getModule(module_id).get("themes") is not None:
        return getModule(module_id).get("themes")


def getThemeConfiguration(module_id: str, theme_id: str) -> dict:
    """
    Renvoie un dictionnaire contenant la configuration du thème associé au module choisi
    Renvoie None si aucune configuration n'a été trouvé
    """
    try:
        file = open("modules/" + module_id + "/" + theme_id + "/config.json")
        return json.load(file)

    except FileNotFoundError:
        return None


def getAvailablesTemplateFormats(module_id: str, theme_id: str) -> list:
    """
    Renvoie une liste contenant les formats de templates enregistrés
    Renvoie une liste vide si aucun format de template n'est enregistré
    """
    formats_list = []
    theme_config: dict = getThemeConfiguration(module_id, theme_id).get("templates")

    for element in theme_config:
        if theme_config.get(element) is not None:
            formats_list.append(element)

    return formats_list


def getTemplatePath(module_id: str, theme_id: str, size: str) -> str:
    """
    Renvoie le chemin d'accès vers la template
    Renvoie None si le chemin d'accès n'est pas enregistré
    """
    formats_list = getAvailablesTemplateFormats(module_id, theme_id)

    if size in formats_list:
        return getThemeConfiguration(module_id, theme_id).get("templates").get(size)


def getImage(module_id: str, theme_id: str, size: str) -> Image:
    """
    Renvoie l'image demandée
    Renvoie None si aucune image n'a été trouvée
    """
    if size in getAvailablesTemplateFormats(module_id, theme_id):
        try:
            path = getTemplatePath(module_id, theme_id, size)
            return Image.open("modules/" + module_id + "/" + theme_id + "/" + path)

        except FileNotFoundError:
            return None


def getAllLettersPositions(module_id: str, theme_id: str) -> dict:
    """
    Renvoie un dictionnaire avec les coordonnées des pixels des lettre
    """
    return getThemeConfiguration(module_id, theme_id).get("letters-position")


def getLetterPositionTuple(module_id: str, theme_id: str, letter: str) -> tuple:
    """
    Renvoie un tuple avec les coordonnées des pixels de la lettre choisi
    Renvoie None si aucune coordonée n'a été trouvée
    """
    all_letters_pos = getAllLettersPositions(module_id, theme_id)

    if letter.upper() in all_letters_pos:
        return (
            all_letters_pos.get(letter)[0],
            all_letters_pos.get(letter)[1],
            all_letters_pos.get(letter)[2],
            all_letters_pos.get(letter)[3]
        )


def getAllLettersWidth(module_id: str, theme_id: str) -> dict:
    """
    Renvoie un dictionnaire avec les coordonnées des pixels des lettre
    """
    return getThemeConfiguration(module_id, theme_id).get("letters-width")


def getLetterWitdh(module_id: str, theme_id: str, letter: str) -> int:
    """
    Renvoie un entier avec la largeur en pixels de la lettre choisi
    Renvoie None si aucune largeur n'a été trouvée
    """
    all_letters_width = getAllLettersWidth(module_id, theme_id)

    if letter.upper() in all_letters_width:
        return all_letters_width.get(letter)


###################################################
#                                                 #
#                 CORE FUNCTIONS                  #
#                                                 #
###################################################


def crop_function(letterCoords):
    letters = getImage("seasonskyV3", "noel", "letters")
    return letters.crop(letterCoords)


def add_title(background, foreground, img_offset):
    background.paste(foreground, img_offset, foreground)
    return background


def getBlankBackground(x: int, y: int):
    return Image.new("RGBA", (x, y), (0, 0, 0, 0))


def getBlankCharacter():
    return Image.new("RGBA", (1, 5), (0, 0, 0, 0))


def createWordImage(module_id: str, theme_id: str, word: str) -> tuple[Image, int]:
    """
    Renvoie une image contenant le mot parfaitement découpé ainsi que le final_size
    """
    blankBackground = getBlankBackground(2000, 14)
    offset = 0
    generated_text = None

    for letter in word.upper():
        letter_pos_tuple = getLetterPositionTuple(module_id, theme_id, letter)
        generated_text = add_title(blankBackground, crop_function(letter_pos_tuple), (offset, 0))
        offset += getLetterWitdh(module_id, theme_id, letter) - 1

    final_size = offset + 1

    return (generated_text.crop((0, 0, final_size, 14)), final_size)


def getFinalMenu(module_id: str, theme_id: str, word: str, menu_height: int) -> Image:
    """
    Renvoie une image contenant le menu terminé
    """
    dynamicalX = 255
    generated_text = createWordImage(module_id, theme_id, word)[0]
    final_size = createWordImage(module_id, theme_id, word)[1]

    def getBackgroundBackground(size, height):
        if size <= 97 and height == 6:
            return getImage(module_id, theme_id, "small-6x9")

        elif size <= 128 and height == 6:
            return getImage(module_id, theme_id, "medium-6x9")

        elif size <= 182 and height == 6:
            return getImage(module_id, theme_id, "big-6x9")

        # 5X9

        elif size <= 97 and height == 5:
            return getImage(module_id, theme_id, "small-5x9")

        elif size <= 128 and height == 5:
            return getImage(module_id, theme_id, "medium-5x9")

        elif size <= 182 and height == 5:
            return getImage(module_id, theme_id, "big-5x9")

        # 4X9

        elif size <= 97 and height == 4:
            return getImage(module_id, theme_id, "small-4x9")

        elif size <= 128 and height == 4:
            return getImage(module_id, theme_id, "medium-4x9")

        elif size <= 182 and height == 4:
            return getImage(module_id, theme_id, "big-4x9")

        else:
            print("Mot trop long")

    def autocenterPosition() -> int:
        return int(dynamicalX / 2 - final_size / 2) + 1

    whiteBackground = add_title(getBackgroundBackground(final_size, menu_height), generated_text,
                                (autocenterPosition(), 27))
    return whiteBackground
