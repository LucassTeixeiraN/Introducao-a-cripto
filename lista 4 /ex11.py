from functools import reduce

def xor_bytes(*valores):
    return bytes([reduce(lambda x, y: x^y, coluna) for coluna in zip(*valores)])

m1 = b"pagar=1000"
m2 = b"pagar=9000"
fluxo_reutilizado = bytes.fromhex("00112233445566778899")

print ("=== CIFRAÇÃO E IMPLEMENTAÇÃO XOR ===")
c1 = xor_bytes(m1, fluxo_reutilizado)
c2 = xor_bytes(m2, fluxo_reutilizado)
print(f"M1 original: {m1}")
print(f"C1 gerado: {c1.hex()}")
print(f"M2 original: {m2}")
print(f"C2 gerado: {c2.hex()}\n")

print("=== DEMONSTRAR IDENTIDADE C1 XOR C2 == M1 XOR M2 ===")
c1_xor_c2 = xor_bytes(c1, c2)
m1_xor_m2 = xor_bytes(m1, m2)
print(f"Resultado de c1 xor c2: {c1_xor_c2.hex()}")
print(f"Resultado de m1 xor m2: {m1_xor_m2.hex()}")
print(f"A identidade é verdadeira? {'Sim' if c1_xor_c2 == m1_xor_m2 else 'Não'}\n")

recuperada = xor_bytes(c1, c2, m1)
print(f"Mensagem M2 intercepetada e recuperada: {recuperada}")

assert recuperada == m2
print("A execução passou pelo asset sem erros")
