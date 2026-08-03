import hashlib
import hmac
import secrets

def sha256(mensagem):
    return hashlib.sha256(mensagem).digest()

def criar_hmac(chave, mensagem):
    return hmac.new(chave, mensagem, hashlib.sha256).digest()

def verificar_hmac(chave, mensagem, etiqueta):
    etiqueta_calculada = criar_hmac(chave, mensagem)
    return hmac.compare_digest(etiqueta_calculada, etiqueta)

original = b"destino=ana; valor=100"
alterada = b"destino=ana; valor=900"

print("="*50)
print("CENARIO 1: SHA-256")
print("="*50)

# SHA-256 nao possui chave. O atacante consegue recalcular o resumo.
hash_original = sha256(original)
hash_forjado = sha256(alterada)
print(f"Mensagem Original: {original}")
print(f"Hash SHA-256 Original: {hash_original.hex()[:20]}...")
print("-" * 50)
print(f"Mensagem Interceptada e Alterada: {alterada}")
print(f"Novo Hash Forjado pelo Atacante: {hash_forjado.hex()[:20]}...")
assert hash_forjado == sha256(alterada)
print("\n> RESULTADO SHA-256: O atacante conseguiu recalcular o hash livremente, pois nao exige chave secreta\n")


print("="*50)
print("CENARIO 2: HMAC")
print("="*50)
# Servidor e o remetente compartilham esta chave; o atacante nao.
chave_legitima = secrets.token_bytes(32)
chave_atacante = secrets.token_bytes(32)

etiqueta_original = criar_hmac(chave_legitima, original)
print(f"Mensagem Original: {original}")
print(f"HMAC Legitimo: {etiqueta_original.hex()[:20]}...")
assert verificar_hmac(chave_legitima, original, etiqueta_original)
print("> Verificacao do Servidor para a mensagem original: AUTORIZADO (HMAC Valido)\n")

print("-" * 50)

etiqueta_atacante = criar_hmac(chave_atacante, alterada)
print(f"Mensagem Alterada pelo Atacante: {alterada}")
print(f"HMAC Forjado (Chave Errada): {etiqueta_atacante.hex()[:20]}...")
assert not verificar_hmac(chave_legitima, alterada, etiqueta_atacante)

mensagem_aceita = verificar_hmac(chave_legitima, alterada, etiqueta_atacante)
assert not mensagem_aceita

print(f"\n> Verificacao do Servidor para mensagem alterada: {'AUTORIZADO' if mensagem_aceita else 'REJEITADO (HMAC Invalido)'}")
print("> RESULTADO HMAC: O servidor percebeu a fraude! Somente quem possui a chave legitima consegue gerar um HMAC valido.")