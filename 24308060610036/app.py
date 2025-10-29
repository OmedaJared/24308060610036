from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

print("DEBUG: __file__ =", __file__)
print("DEBUG: app.root_path =", app.root_path)
print("DEBUG: app.template_folder (rel) =", app.template_folder)

@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    peso = float(request.form['peso'])
    altura = float(request.form['altura'])
    edad = int(request.form['edad'])
    genero = request.form['genero']
    actividad = request.form['actividad']

    if genero == 'hombre':
        tmb = 10 * peso + 6.25 * altura - 5 * edad + 5
    else:
        tmb = 10 * peso + 6.25 * altura - 5 * edad - 161

    
    factores = {
        'sedentario': 1.2,
        'ligera': 1.375,
        'moderada': 1.55,
        'alta': 1.725
    }

    get = tmb * factores[actividad]

    return render_template('resultado.html', tmb=tmb, get=get)

if __name__ == '__main__':
    app.run(debug=True)
