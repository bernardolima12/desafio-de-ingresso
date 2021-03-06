from flask import Flask, request
app = Flask(__name__)

#fibonacci utilizando lista para guardar valores
def fibonacci(n):
    lista=[0,1]; i =2         
    if n<=0:
        raise ValueError             
    elif n==1:
        return lista[n]    
    else:
        while i <n+1:        
          lista.append(lista[i-1] + lista[i-2])
          i+=1
        return lista[n]
        
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