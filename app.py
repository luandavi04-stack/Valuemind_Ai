# Lógica do Backend ValueMind AI
def filtrar_jogos_amanha(grade_jogos):
    sugestoes = []
    for jogo in grade_jogos:
        # Regra 1: Apenas Odd até 3.00
        # Regra 2: Apenas Confiança Alta (>90%)
        if jogo['odd'] <= 3.00 and jogo['confianca'] >= 90:
            sugestoes.append(jogo)
    return sugestoes

def enviar_whatsapp(mensagem, tipo="sinal"):
    # Aqui conectamos com a API do WhatsApp (Z-API ou Evolution)
    print(f"Enviando para o grupo: {mensagem}")

# Exemplo de Mensagem de Abertura (06:00)
abertura = "🧠 ValueMind AI\n📖 Salmos 37:5\n🛡️ Gestão: 1% da banca."