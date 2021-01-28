#pip install container_packing
from flask import Flask, request
app = Flask(__name__)
from container_packing.shortcuts import pack_products_into_restrictions

#requisitando um JSON data type que pode ser:string, numero, array etc
@app.route("/servicos",methods=['POST','GET'])
def enviar():
  items = request.get_json()
  return servico(items)  

def servico(items):  
  d = {'Lala: Moto':[20,35,30,40],'Lala: Fiorino':[500,188,108,133],'Lala: Carreto':[1500,300,200,180],
       'Ogi: Moto':[20,52,52,36],'Ogi: SUV':[200,125,60,80]}
  
  #calculo do peso total dos itens
  peso_items =0  
  for i in range(len(items)):
    peso_items += items[i]['peso']
  #excluimos os servicos pelo peso max
  for v,k in list(d.items()):
    if peso_items >k[0]:
      del d[v]
  
  #usando a lib para verificar se os pacotes cabem nas dimensoes de cada veiculo
  #a funcao pack_products_into_restrictions calcula as dimensoes minimas necessarias para se organizar as caixas.
  #caso as dimensoes minimas excedam as dimensoes maximas (container_max_sizes) a funcao retorna None  
  for v,k in list(d.items()):
    container_max_sizes = (k[1],k[2],k[3])
    pack = pack_products_into_restrictions(items,container_max_sizes)
    if pack == None:
      del d[v]       

  #criamos um dicionario separado para cada uma das empresas
  #nesse caso, trocamos a chave por value e vice versa
  lala={}; ogi={}
  for v,k in list(d.items()):
    if v[0]=='L':
      lala[k[0]] = v
    else:
      ogi[k[0]] = v      

  if not lala and not ogi:
    return ('Não é possível utilizar nenhum serviço')
  elif not ogi:
    ogi[0] = 'não é possível utilizar o serviço Ogi'  

  return (str(lala[min(lala)])+' e ' + str(ogi[min(ogi)]))

app.run(debug=True)