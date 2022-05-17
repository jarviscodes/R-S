import string

class MorseTranslator(object):
    @classmethod
    def generate_morse_dict(cls):
        character_list = string.ascii_uppercase + string.digits
        morse_characters = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
            ".----",
            "..---",
            "...--",
            "....-",
            ".....",
            "-....",
            "--...",
            "---..",
            "----.",
            "-----",
        ]
        return {k: v for k,v in zip(character_list, morse_characters)}

    @classmethod
    def generate_character_dict(cls):
        character_list = string.ascii_uppercase + string.digits
        morse_characters = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
            ".----",
            "..---",
            "...--",
            "....-",
            ".....",
            "-....",
            "--...",
            "---..",
            "----.",
            "-----",
        ]
        return {v: k for k, v in zip(character_list, morse_characters)}

    @classmethod
    def character_to_morse(cls, character):
        return cls.generate_morse_dict().get(character, None)

    @classmethod
    def morse_to_character(cls, morse):
        return cls.generate_character_dict().get(morse, None)

    @classmethod
    def string_to_morse(cls, text, separator=" "):
        # Split into words:
        string_compounds = text.split(" ")
        translated_compounds = []
        for compound in string_compounds:
            translated_compounds.append(' '.join([MorseTranslator.character_to_morse(letter) for letter in compound]))

        return '\n'.join(translated_compounds)


    @classmethod
    def morse_to_string(cls, morse):
        # Inverse the above
        # 1. Get compounds by splitting on line breaks
        morse_words = morse.split("\n")
        translated_compounds = []
        for word in morse_words:
            word_compounds = word.split(" ")
            full_word = []
            for character in word_compounds:
                translated = MorseTranslator.morse_to_character(character)
                full_word.append(translated)
            translated_compounds.append(full_word)
        return ' '.join([''.join(x) for x in translated_compounds])
