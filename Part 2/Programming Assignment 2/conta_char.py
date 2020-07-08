def conta_letras(frase, contar="vogais"):
    vogais = ["a", "á", "ã", "à", "e", "é", "ê", "i", "í", "o", "ô", "õ", "ó", "u", "ú"]
    letras = len(frase) - frase.count(" ")
    total_vogais = 0

    for i in range(len(frase)):
        if frase[i].lower() in vogais:
               total_vogais += 1
    if contar == "vogais":
        return total_vogais
    else:
        return letras - total_vogais
