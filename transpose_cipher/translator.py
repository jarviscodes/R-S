class TransposeTranslator(object):
    @classmethod
    def encrypt_message(cls, text, key, padding="#"):
        if key > len(text) / 2:
            print(f"Key max length for this text is {int(len(text) / 2)}")
            exit()
        else:
            all_chunks = [text[i:i+key] for i in range(0, len(text), key)]
            for i in range(len(all_chunks)):
                all_chunks[i] += f'{padding}' * (key - len(all_chunks[i]))

            # We should now have n padded chunks of len = key each.
            full_cipher_padded = ""
            for j in range(key):
                for chunk in all_chunks:
                    full_cipher_padded += chunk[j]

            return full_cipher_padded.replace("#", "")




