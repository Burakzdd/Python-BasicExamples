
text = "deneyap"

print(text.upper())
print(text.lower())
print(text.isalpha())
print(text.find("e")) #baştan arar
print(text.rfind("e")) #sondan arar
text = "151"
print(text.isdigit())

text = "deneyap,151"
print(text.split(','))

print(text.replace("d","t"))

text = "{} ozdemir {} yasında"
print(text.format("Burak",20))
#text.endswith() en sonda hangi karakter olduğunu inceler
