from flask import Flask, render_template
import os

# Aqui avisamos ao sistema para usar a pasta 'modelos'
app = Flask(__name__, template_folder='modelos')

@app.route('/')
def home():
    return render_template('painel.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
