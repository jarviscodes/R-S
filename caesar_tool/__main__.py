# TBD: This is basically just rot13, made easy with codecs module.
# Let's have some fun though.

from caesar_tool.translator import CaesarTranslator

translation = CaesarTranslator.translate_with_key("This is a test for our caesar translator!!!", 2)
print(translation)

# Theoretically rotating to -2 should have the same plaintext
plain_text = CaesarTranslator.translate_with_key(translation, -2)
print(plain_text)