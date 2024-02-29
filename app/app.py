from flask import Flask,render_template 

#creamos una instancia de la clase flask

app = Flask(__name__)

#para ejecutar la aplicación

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar')
def saludo():
    return render_template('registrar.html')

#para ejecutar la aplicacion
if __name__ == '__main__':
    app.add_url_rule('/', view_func=index)
    app.run(debug=True,port=5005)
#definir rutas