from transpose_cipher.translator import TransposeTranslator

translation = TransposeTranslator.encrypt_message("Hallo Test 123", 5)

print(translation)