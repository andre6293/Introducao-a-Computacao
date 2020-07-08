# Andre Pinto
# @Coursera - Introdução ao Python I (USP)

def converteSegundos(seg):
    segPorDia = 86400
    segPorHora = 3600
    segPorMinuto = 60

    dias = seg // segPorDia
    horas = (seg - dias * segPorDia) // segPorHora
    minutos = (seg - dias * segPorDia - horas * segPorHora) // segPorMinuto
    segundos = seg - dias * segPorDia - horas * segPorHora - minutos * segPorMinuto

    return "{} dias, {} horas, {} minutos e {} segundos.".format(dias, horas, minutos, segundos)

segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
print(converteSegundos(segundos))
