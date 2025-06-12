from flask import Flask, render_template, request, redirect, url_for
from cidade_escolhida import cidade_escolhida


app = Flask(__name__)
app.register_blueprint(cidade_escolhida, url_prefix='/cidade')

@app.route("/", methods=['GET', 'POST'])
def homepage():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        cidade = request.form['cidadeinput'].lower()
        return redirect(url_for('cidade_escolhida_bp.clima', cidade=cidade)) #passando a variavel cidade como parametro em cidade_escolhida.py, ou seja, passando variáveis não só entre funções, mas também entre arquivos diferentes com blueprints.



if __name__ == '__main__':
    app.run(debug=True)