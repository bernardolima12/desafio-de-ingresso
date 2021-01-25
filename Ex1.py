from flask import Flask, request
app = Flask(__name__)

#fibonacci recursivo usando memorizacao
def fibonacci(n,dic={}):    
    if n in dic:
        return dic[n]
    if n<0:
        raise ValueError
    elif n ==0:
        return 0       
    elif n==1:
        return 1    
    else:
        resposta = fibonacci(n-1)+fibonacci(n-2)
        dic[n] = resposta
        return resposta

#criando rota com a API e pedindo ao usuario inserir o n-ésimo termo a ser calculado
@app.route("/fibonacci",methods=['POST','GET'])
def enviar():
    try:
        if request.method=='POST':
            n = request.form['n']      
            fibs = fibonacci(int(n))
            
            return '<h1> O {} número de Fibonacci é: {}</h1>'.format(n,fibs)

        return '''<form method="POST">
        Escolha o n-ésimo Fibonacci: <input type='text' name='n'>
        <input type="submit">
        '''
    except ValueError:
        return "Escolha um número inteiro positivo"

if __name__ == "__main__":
  app.run(debug=True)