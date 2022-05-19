import textwrap

class TransposeTranslator(object):
    @classmethod
    def encrypt_message(cls, text, key):
        if key > len(text) / 2:
            print(f"Key max length for this text is {int(len(text) / 2)}")
            exit()
        else:
            all_chunks = [text[i:i+key] for i in range(0, len(text), key)]
            for chunk in all_chunks:
                chunk += '#' * (key - len(chunk))





