from flask import Flask, request
app = Flask(__name__)

def servico(peso,largura,espessura,altura):
  lista = [peso,largura,espessura,altura]
  d = {'Lala: Moto':[20,35,30,40],'Lala: Fiorino':[500,188,108,133],'Lala: Carreto':[1500,300,200,180],
       'Ogi: Moto':[20,52,52,36],'Ogi: SUV':[200,125,60,80]}
  
  #verificando se o valor inserido é muito grande
  for i in range(len(lista)):
    if lista[i]>d['Lala: Carreto'][i]:      
      return ('Nenhum serviço disponível,'+ str(lista[i])+ 
      ' é um número muito grande ')

    #removendo os servicos não disponíveis
    for j in list(d.keys()):
      if d[j][i] < lista[i]:
        del d[j]       

  d_Lala ={}; d_Ogi={}
   
  #criando um dicionario separado para cada empresa
  for i,j in d.items():
    if i[0] == 'L':             
      d_Lala[i]=d[i][0]    
    else:              
      d_Ogi[i]=d[i][0]  
  if not d_Ogi:    
    d_Ogi['não é possível utilizar o serviço Ogi'] = 0  
  
  #variaveis que contem os menores valores dentre os possiveis veiculos
  lala = min(d_Lala, key=d_Lala.get)
  ogi = min(d_Ogi, key=d_Ogi.get)   

  return '<h1>{} e {}</h1>'.format(lala,ogi)

#criando uma rota com a API
@app.route("/servicos",methods=['POST','GET'])
#pedindo as informacoes de peso,largura,espessura e altura para o usuario
def enviar():
  try:  
    if request.method=='POST':
      peso = int((request.form['peso']))  
      largura = int((request.form['largura']))  
      espessura = int((request.form['espessura']))  
      altura = int((request.form['altura']))                 
      return servico(peso,largura,espessura,altura)
    return '''<form method="POST">
        Peso (Kg): <input type='text' name='peso'>
        Largura (cm): <input type='text' name='largura'>
        Espessura (cm): <input type='text' name='espessura'>
        Altura (cm): <input type='text' name='altura'>
        <input type="submit">'''
  except ValueError:
    return "Escolha um número inteiro positivo"
        
if __name__ == "__main__":
  app.run()