"""
HMTAI PORT REWRITE - by @NMWIN_D (twitter)
Used original port made by NickSaltFoxu
HMTAI is an Anime / Hentai (NSFW) Image API which simplifies how you fetch random images from the official REST API!\n
"""
from hmtai.hmfull import hmfull

class CategoryNotFound(Exception):
    def __init__(self, categoryn):
        self.categoryn = categoryn
        self.message = f"I don't found '{categoryn}' in list of categories. Please, check docs for right names."
        super().__init__(self.message)

class SourceNotFound(Exception):
    def __init__(self, source):
        self.source = source
        self.message = f"I don't found {source} in list of categories. Please, check docs for right names."
        super().__init__(self.message)

class NoSourceEntered(Exception):
    def __init__(self):
        self.message = f"Source name is empty."
        super().__init__(self.message)

class NoCategoryEntered(Exception):
    def __init__(self):
        self.message = f"Category name is empty."
        super().__init__(self.message)

def get(source = None, category = None):
    if source == None:
        raise NoSourceEntered
    if category == None:
        raise NoCategoryEntered
    if source == "hmtai":
        res = hmfull.hmtai(category)
        if res == 0:
            raise CategoryNotFound(category)
        else:
            return res
    elif source == "nekobot":
        res = hmfull.nekobot(category)
        if res == 0:
            raise CategoryNotFound(category)
        else:
            return res
    elif source == "nekos":
        res = hmfull.nekos(category)
        if res == 0:
            raise CategoryNotFound(category)
        else:
            return res
    elif source == "freaker":
        res = hmfull.freaker(category)
        if res == 0:
            raise CategoryNotFound(category)
        else:
            return res
    elif source == "nekolove":
        res = hmfull.nekolove(category)
        if res == 0:
            raise CategoryNotFound(category)
        else:
            return res
    else:
        raise SourceNotFound(source)

def useHM(version = None, category = None):
    return get("hmtai",f"{category}")