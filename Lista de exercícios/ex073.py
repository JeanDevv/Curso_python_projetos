times = ("Corinthians", "Palmeiras", "Santos", "Grêmio",
"Cruzeiro", "Flamengo", "Vasco", "Chapecoense", 
"Atlético", "Botafogo", " Atlético-PR", "Bahia",
"São Paulo", "Fluminense", "Sport Recife",
"EC vitória", "Coritiba", "Avaí", "Ponte Preta", "Atlético-GO")
print("-=" * 40)
print(f"Lista de times do Brasileirão {times}")
print("-=" * 40)
print(f"Os 5 primeiros times são {times[0:5]}")
print("-=" * 40)
print(f"Os últimos colocados são {times[-4:]}")
print("-=" * 40)
print(f"Times em ordem alfabética são: {sorted(times)}")
print("-=" * 40)
print(f"A Chapecoense está na {times.index('Chapecoense')+1}ª posição") 
print("-=" * 40)
