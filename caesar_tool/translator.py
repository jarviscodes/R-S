import string
from collections import deque

class CaesarTranslator(object):

    @classmethod
    def translate_with_key(cls, text, key):
        all_symbols = [x for x in string.ascii_uppercase + string.ascii_lowercase + string.digits + ".!?:"]
        items_nokey = deque(all_symbols)
        items_nokey.rotate(key)
        all_symbols = str(all_symbols)
        all_items = str(list(items_nokey))
        my_translator = str.maketrans(all_symbols, all_items)
        return text.translate(my_translator)


