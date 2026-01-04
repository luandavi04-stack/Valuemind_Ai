from flask import Flask, render_template_string, request, jsonify
import os
import random

app = Flask(__name__)

# Lógica da IA para gerar jogos aleatórios (O cérebro da ValueMind)
def gerar_jogo():
    times = ["Real Madrid", "Barcelona", "Man. City", "Liverpool", "PSG", "Bayern", "Flamengo", "Palmeiras"]
    time1 = random.choice(times)
    time2 = random.choice([t for t in times if t != time1])
    return {
        "confronto": f"{time1} vs {time2}",
        "mercado": "Over 2.5 Gols",
        "odd": round(random.uniform(1.50, 2.10), 2),
        "confianca": f"{random.randint(75, 98)}%"
    }

@app.route('/')
def home():
    # Carrega o seu HTML diretamente (ajustado para ler o arquivo solto)
    with open('painel.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    return render_template_string(html_content)

# Rota para os botões funcionarem
@app.route('/api/acao', methods=['POST'])
def acao_ia():
    dados = request.json
    tipo = dados.get('tipo')
    # Aqui ele gera um novo jogo quando você clica em Aprovar ou Rejeitar
    novo_jogo = gerar_jogo()
    return jsonify({"status": "sucesso", "novo_jogo": novo_jogo})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
