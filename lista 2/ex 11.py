import secrets

def euclides_estendido(a, b):
    print(f"\n--- Iniciando Algoritmo de Euclides Estendido ---")
    print(f"Objetivo: encontrar mdc({a}, {b}) e coeficientes x, y")
    
    x0, x1, y0, y1 = 1, 0, 0, 1
    print(f"Estado inicial: a={a:2}, b={b:2} | x0={x0:2}, x1={x1:2} | y0={y0:2}, y1={y1:2}")
    
    passo = 1
    while b != 0:
        q = a // b
        resto = a % b
        print(f"\nPasso {passo}: Divisão inteira -> {a} = {b} * {q} + {resto} (Quociente: {q})")
        
        # Atualizando os valores
        a, b = b, resto
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
        
        print(f"Valores atualizados: a={a:2}, b={b:2} | x0={x0:2}, x1={x1:2} | y0={y0:2}, y1={y1:2}")
        passo += 1
        
    print(f"--- Fim Euclides Estendido: mdc = {a}, x = {x0}, y = {y0} ---\n")
    return a, x0, y0

def inverso_modular(a, n):
    print(f">>> Calculando inverso de {a} módulo {n}")
    mdc, x, y = euclides_estendido(a, n)
    if mdc != 1:
        raise ValueError(f"Inverso não existe: gcd({a}, {n}) é {mdc}, diferente de 1.")
    
    inverso = x % n
    print(f"O máximo divisor comum é 1. O coeficiente x é {x}.")
    print(f"Ajustando o módulo: {x} % {n} = {inverso}")
    print(f"Resultado: o inverso de {a} módulo {n} é {inverso}\n")
    return inverso

def xor_bytes(a, b):
    # Rejeita tamanhos diferentes e aplica XOR byte a byte.
    if len(a) != len(b):
        raise ValueError("As sequências de bytes devem ter o mesmo tamanho.")
    
    print(f">>> Calculando XOR byte a byte")
    print(f"Sequência A (Hex): {a.hex()}")
    print(f"Sequência B (Hex): {b.hex()}")
    print("-" * 40)
    
    resultado = bytearray()
    for i, (byte_a, byte_b) in enumerate(zip(a, b)):
        res_byte = byte_a ^ byte_b
        resultado.append(res_byte)
        
        # Formatando para mostrar em binário (8 bits)
        bin_a = bin(byte_a)[2:].zfill(8)
        bin_b = bin(byte_b)[2:].zfill(8)
        bin_r = bin(res_byte)[2:].zfill(8)
        
        print(f"Byte {i}:")
        print(f"  {bin_a} (0x{byte_a:02x})")
        print(f"^ {bin_b} (0x{byte_b:02x})")
        print(f"  {bin_r} (0x{res_byte:02x})")
        print("-" * 40)
        
    print(f"Resultado final (Hex): {resultado.hex()}\n")
    return bytes(resultado)


print("=" * 50)
print("TESTE 1: INVERSO MODULAR (SUCESSO)")
print("=" * 50)
assert inverso_modular(7, 26) == 15
print("=" * 50)
print("TESTE 2: INVERSO MODULAR (FALHA ESPERADA)")
print("=" * 50)
try:
    inverso_modular(6, 26)
except ValueError as e:
    print(f"EXCEÇÃO CAPTURADA: {e}")

print("=" * 50)
print("TESTE 3: OPERAÇÃO XOR")
print("=" * 50)
assert xor_bytes(bytes.fromhex("0f"), bytes.fromhex("f0")).hex() == "ff"


print("=" * 50)
print("TESTE 4: GERAÇÃO DE 1000 NONCES")
print("=" * 50)

nonces_gerados = set()
houve_repeticao = False
colisoes = 0

print("Iniciando a geração de 1000 nonces de 12 bytes...")

for i in range(1000):
    novo_nonce = secrets.token_bytes(12)
    
    if novo_nonce in nonces_gerados:
        houve_repeticao = True
        colisoes += 1
        print(f"  -> ATENÇÃO: Repetição encontrada no passo {i+1}!")
        print(f"     Valor repetido (Hex): {novo_nonce.hex()}")
    
    nonces_gerados.add(novo_nonce)

print("-" * 50)
print(f"Total de nonces gerados no loop: 1000")
print(f"Total de nonces ÚNICOS armazenados: {len(nonces_gerados)}")
print(f"Houve repetição entre os 1000 nonces? {'Sim' if houve_repeticao else 'Não'}")
print("=" * 50)