n=input('Digite algo:')
print(f'O tipo primitivo desse valor é {type(n)}')
print(f'Tem espaço? {n.isspace()}')
print(f'Só tem número? {n.isnumeric()}')
print(f'Tem número com alfabéto? {n.isalnum()}')
print(f'É alfabético? {n.isalpha()}')
print(f'Está em maiúsculo? {n.isupper()}')
print(f'Está em minúsculo? {n.islower()}')
print(f'Tem letra em maiúsculo e minúsculo? {n.istitle()}')