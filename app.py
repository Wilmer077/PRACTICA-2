from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

datos_formularios = {
    'inscripcion': [],
    'usuarios': [],
    'productos': [],
    'libros': []
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inscripcion', methods=['GET', 'POST'])
def inscripcion():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        curso = request.form['curso']
        datos_formularios['inscripcion'].append({
            'nombre': nombre,
            'apellido': apellido,
            'curso': curso
        })
        return redirect(url_for('mostrar'))
    return render_template('inscripcion.html')

@app.route('/registro_usuarios', methods=['GET', 'POST'])
def registro_usuarios():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        datos_formularios['usuarios'].append({
            'nombre': nombre,
            'apellido': apellido,
            'correo': correo,
            'contrasena': contrasena
        })
        return redirect(url_for('mostrar'))
    return render_template('registro_usuarios.html')

@app.route('/registro_productos', methods=['GET', 'POST'])
def registro_productos():
    if request.method == 'POST':
        producto = request.form['producto']
        categoria = request.form['categoria']
        existencia = request.form['existencia']
        precio = request.form['precio']
        datos_formularios['productos'].append({
            'producto': producto,
            'categoria': categoria,
            'existencia': existencia,
            'precio': precio
        })
        return redirect(url_for('mostrar'))
    return render_template('registro_productos.html')

@app.route('/registro_libros', methods=['GET', 'POST'])
def registro_libros():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        resumen = request.form['resumen']
        medio = request.form['medio']
        datos_formularios['libros'].append({
            'titulo': titulo,
            'autor': autor,
            'resumen': resumen,
            'medio': medio
        })
        return redirect(url_for('mostrar'))
    return render_template('registro_libros.html')

@app.route('/mostrar')
def mostrar():
    return render_template('mostrar.html', datos=datos_formularios)

if __name__ == '__main__':
    app.run(debug=True, port=8080)