# Exercício 1

def converter_tempo(segundos_totais):
    horas = segundos_totais // 3600
    minutos = (segundos_totais % 3600) // 60
    segundos = segundos_totais % 60
    return horas, minutos, segundos

entry = int(input("Introduz o tempo em segundos: "))

h, m, s = converter_tempo(entry)

print(f"{entry} segundos correspondem a {h} hora(s), {m} minuto(s), {s} segundo(s).")