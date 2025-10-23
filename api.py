from flask import Flask, request, jsonify
import threading

app = Flask(__name__)

# Este dicionário vai armazenar o estado atual da casa (em memória)
# Ele já começa com os valores do seu protótipo
estado_da_casa = {
    "quarto_principal": 0.0,
    "cozinha": 0.0,
    "chuveiro": 0.0,
    "iluminacao_geral": 0.0,
    "total": 0.0
}

# Lock para evitar problemas de concorrência ao atualizar o estado
data_lock = threading.Lock()

# Rota [POST] /update
# O Unity vai enviar dados para cá
@app.route('/update', methods=['POST'])
def update_data():
    with data_lock:
        circuito = request.form['circuito']
        wattage = float(request.form['wattage'])
        
        # Mapeia o circuito do Unity para o nosso estado
        if circuito == "chuveiro":
            estado_da_casa["chuveiro"] = wattage
        elif circuito == "quarto_principal":
            estado_da_casa["quarto_principal"] = wattage
        elif circuito == "cozinha":
            estado_da_casa["cozinha"] = wattage
        elif circuito == "iluminacao_geral":
            estado_da_casa["iluminacao_geral"] = wattage
            
        # Recalcula o total
        estado_da_casa["total"] = (
            estado_da_casa["chuveiro"] +
            estado_da_casa["quarto_principal"] +
            estado_da_casa["cozinha"] +
            estado_da_casa["iluminacao_geral"]
        )
        
    return jsonify({"status": "sucesso"})

# Rota [GET] /data
# O Streamlit vai ler os dados daqui
@app.route('/data', methods=['GET'])
def get_data():
    with data_lock:
        # Retorna uma cópia do estado atual
        return jsonify(dict(estado_da_casa))

# --- Como rodar esta API ---
# 1. Abra um terminal
# 2. Digite: flask --app api run
# 3. Deixe este terminal rodando
if __name__ == '__main__':
    app.run(debug=True)