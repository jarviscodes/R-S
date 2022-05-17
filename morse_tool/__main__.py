from morse_tool.translator import  MorseTranslator

text_to_translate = "CQ CQ CQ"
morse_to_translate = """-.-. --.-
-.-. --.-
-.-. --.-"""

translation = MorseTranslator.string_to_morse(text_to_translate)
print(translation)

translation = MorseTranslator.morse_to_string(morse_to_translate)
print(translation)


