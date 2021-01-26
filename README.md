# desafio-de-ingresso
Para utilizar a API do Ex1 (fibonacci) e Ex2 (servicos) basta inserir no URL do seu navegador localhost:5000/fibonacci ou localhost:5000/servicos, respectivamente.
No primeiro você deve inserir o n-ésimo termo da sequência de Fibonacci a ser calculado.
É importante notar que n precisa ser um número inteiro e positivo. Caso contrário, o site retorna uma mensagem pedindo para que o usuário insira um input válido.
A sequência original de Fibonacci se inicia com o número 0, mas alguns livros optam por omitir esse primeiro termo. Issp também foi feito no código do Ex1.
Para o Ex2, deve-se inserir, também, números inteiros e positivos para os valores de peso, largura, espessura e altura. Do contrário, o site também retorna a mesma mensagem que o exercício anterior.
Os valores para os atributos desse exercício precisam estar dentro de um certo limite, pois existem restrições para cada um dos serviços. Desse modo, caso o valor máximo de algum atributo seja excedido, a API retorna que nenhum serviço está disponível e qual o valor excedeu o limite imposto pelas empresas.
Por último, no arquivo denominado extra, foi proposto uma maneira simples de deixar a API um pouco mais segura. Para isso, foi criado um usuário e uma senha que devem ser preenchidos por quem acessa a plataforma. Nesse caso, o usuário é admin e a senha datamachina - gerados a partir de um dicionário denominado USER_DATA.
Após o preenchimento desses campos, o cliente deve escolher dentre os dois botões oferecidos. Dependendo da sua escolha, ele será redirecionado para a página do Ex1, caso escolha Fibonacci, ou do Ex2, caso escolha serviços.
