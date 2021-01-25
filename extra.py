from flask import Flask, request,redirect,url_for,render_template
from flask_httpauth import HTTPBasicAuth
import Ex2,Ex1


app = Flask(__name__)
auth = HTTPBasicAuth()

#crianco um usuario e senha
USER_DATA={
    'admin':'datamachina'
}

#verificando se o usuario e a senha foram inseridos corretamente
@auth.verify_password
def verify(username,password):
    if not(username and password):
        return False
    return USER_DATA.get(username)==password

#criando os botoes para redirecionamento
@app.route('/',methods=['POST','GET'])
@auth.login_required
def redireciona():       
    if request.method == 'POST':
        if request.form['submit_button'] == 'Fibonacci':
            return redirect(url_for('call_fib'))            
        elif request.form['submit_button'] == 'Servicos':
            return redirect(url_for('call_serv'))        

    return '''<form method="POST">    
    <input type="submit" name="submit_button" value="Fibonacci">
    <input type="submit" name="submit_button" value="Servicos">'''      
    
#chamando a funcao fibonacci criada
@app.route("/fibonacci",methods=['POST','GET'])
@auth.login_required
def call_fib():
    return Ex1.enviar()

#chamandoa  funcao servicos criada
@app.route("/servicos",methods=['POST','GET'])
@auth.login_required
def call_serv():
    return Ex2.enviar()

if __name__ == "__main__":
  app.run(debug=True)
