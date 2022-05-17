from reverse_cipher.translator import ReverseCipherTranslator

txt = "Jarvis is a s3cr3t sp33dc0d3r"

translation = ReverseCipherTranslator.reverse_string(txt)
print(translation)
