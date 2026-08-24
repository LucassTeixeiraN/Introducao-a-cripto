ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cesar(texto, chave):
    texto_upper = texto.upper()
    cifra = ""

    for i in texto_upper: 
        if i in ALFABETO:
            idx = ALFABETO.index(i)
            carac_cifrado = ALFABETO[(idx + chave) % 26]
            cifra += carac_cifrado
        else:
            cifra += i
    return cifra
        

def decifrar(texto, chave):
    texto_upper = texto.upper()
    cifra = ""

    for i in texto_upper: 
        if i in ALFABETO:
            idx = ALFABETO.index(i)
            carac_cifrado = ALFABETO[(idx - chave) % 26]
            cifra += carac_cifrado
        else:
            cifra += i
    return cifra


def candidatas(texto_cifrado):
    opcoes = []
    PALAVRAS_ALVO = ["DE", "A", "QUE", "AO"]

    for i in range(26):
        texto_tentativa = decifrar(texto_cifrado, i)
        pontuacao = 0

        palavras_separadas = texto_tentativa.split()

        for j in PALAVRAS_ALVO:
            pontuacao += palavras_separadas.count(j)

        opcoes.append({
            'pontuacao': pontuacao,
            'chave': i,
            'texto': texto_tentativa
        })

        print(f"Chave: {i:2d} | Pontos: {pontuacao} | Tentativa: '{texto_tentativa}'")

    return sorted(opcoes, key=lambda x:x['pontuacao'], reverse=True)

mensagem_original = "AO QUE TUDO INDICA"
chave_secreta = 3

print("=== ETAPA 1: CIFRAÇÃO ===")
print("Teste 1")
print(f"Texto original: '{mensagem_original}'")
print(f"Aplicando algoritmo de César com chave {chave_secreta}")
texto_cifrado = cesar(mensagem_original, chave_secreta)
print(f"Resultado: '{texto_cifrado}'\n")

print("=== ETAPA 2: DECIFRAÇÃO LEGÍTIMA ===")
print(f"Texto cifrado recebido: '{texto_cifrado}'")
print(f"Revertendo com a chave correta conhecida ({chave_secreta})")
texto_recuperado = decifrar(texto_cifrado, chave_secreta)
print(f"Resultado: '{texto_recuperado}'\n")

print("=== ETAPA 3: ATAQUE DE BUSCA EXAUSTIVA ===")
print(f"Texto cifrado: '{texto_cifrado}'")
melhores = candidatas(texto_cifrado)
print("Exemplo de falha:")
texto_falho = "O REI"
print(f"Texto cifrado: '{texto_falho}'")
melhores = candidatas(texto_falho)

print("\n=== RESULTADO FINAL DO ATAQUE ===")
print("O algoritmo estatístico ordenou as opções e sugere:")
print(f" -> Chave Provável: {melhores[0]['chave']}")
print(f" -> Texto Recuperado: '{melhores[0]['texto']}'")
print(f" -> Pontuação de Confiança: {melhores[0]['pontuacao']}")