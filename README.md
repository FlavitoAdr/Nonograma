# Nonograma
O algoritmo mais complexo que já desenvolvi até a data desta postagem, se baseia na resolução de um jogo de lógica e matemática da qual eu gosto de jogar.

O algoritmo mais complexo que já desenvolvi até a data desta postagem, se baseia na resolução de um jogo de lógica e matemática da qual eu gosto de jogar.
Há dois anos eu conheci um jogo chamado nonograma, é um quebra cabeça que consiste em usar a lógica para conseguir fazer um preenchimento em uma tabela até formar uma imagem, marcando preenchimento ou X para indicar que é uma posição vazia, as regras do jogo são, a tabela que é dividida em linhas e colunas e é dado diversos números ao lado da tabela, esses números indicam uma sequência de posições preenchidas, e deve haver ao menos uma posição marcada como vazia entre as sequências preenchidas, existem números que indicam o preenchimento nas linhas(horizontal) e colunas(vertical).

Após um tempo eu me aperfeiçoei no jogo e usei diversas estratégias para resolve-lo, até que percebi um algoritmo capaz de resolver o problema, primeiro deve definir quem são os termos para cada linha e também qual a quantidade de espaços excedentes do mínimo necessário para se poder resolver.

Por exemplo, se a tabela é 10x10, e é indicado que uma linha/coluna tem os termos 2 e 3 sabemos que tem dois espaços preenchidas ao menos uma posição vazia que separa os termos e em seguida três posições, o que no total dá seis, pois Efetivo = Soma dos termos mais Quantidade de termos menos um, Efetivo = 2 + 3 + 2 - 1 = 6, a necessidade da soma da Quantidade de termos menos 1 é devido a consideração que deve haver ao menos um espaço entre cada termo, em seguida o espaço restante é o Bônus, lembrando que é uma tabela de lado 10, e ao menos 6 espaços são necessário para montar a informação dada, há 4 espaços a mais que o necessário, logo o Bônus é 4.

Ao ter a Quantidade de termos e Bônus para cara linha podemos definir quantas possibilidades existem, pelo cálculo da combinação, isto é importante para o algoritmo resolver.

Após ter a quantidade de possibilidades, podemos criá-las, então o primeiro dos três algoritmos para resolver gera uma matriz, as quantidade de colunas é definido pela quantidade de termos mais um, e a quantidade de linhas é definida pela quantidade de possibilidades, a matriz é zerada, depois o algoritmo soma a última coluna da primeira linha o valor do bônus, após esse processo para cada linha seguinte o algoritmo subtrai 1 da ultima coluna que seja maior que zero e o restante volta para a ultima coluna, soma 1 na seguinte a subtraída, até que o valor da primeira coluna seja igual a bônus.

exemplo:

Termos = 2
Bônus = 3
possibilidades = (2+3)!/(2!*3!) = 10

 1º => 0 0 3
 
 2º => 0 1 2
 
 3º => 0 2 1
 
 4º => 0 3 0
 
 5º => 1 0 2
 
 6º => 1 1 1
 
 7º => 1 2 0
 
 8º => 2 0 1
 
 9º => 2 1 0
 
10º => 3 0 0

No segundo algoritmo ele irá somar 1 a todas as colunas com excessão da primeira e última coluna.

exemplo:

Termos = 2
Bônus = 3
possibilidades = (2+3)!/(2!*3!) = 10

 1º => 0 0 3 => 0 1 3
 
 2º => 0 1 2 => 0 2 2
 
 3º => 0 2 1 => 0 3 1
 
 4º => 0 3 0 => 0 4 0
 
 5º => 1 0 2 => 1 1 2
 
 6º => 1 1 1 => 1 2 1
 
 7º => 1 2 0 => 1 3 0
 
 8º => 2 0 1 => 2 1 1
 
 9º => 2 1 0 => 2 2 0
 
10º => 3 0 0 => 3 1 0

Por fim no terceiro algoritmo ele encaixa os termos entre a matriz resultante do segundo algoritmo.

exemplo:

Termos = 2
Bônus = 3
possibilidades = (2+3)!/(2!*3!) = 10

Os termos são: 4 e 2 para um quadrado de tamanho 10

 1º => 0 0 3 => 0 1 3 => 0 4 1 2 3
 
 2º => 0 1 2 => 0 2 2 => 0 4 2 2 2
 
 3º => 0 2 1 => 0 3 1 => 0 4 3 2 1
 
 4º => 0 3 0 => 0 4 0 => 0 4 4 2 0
 
 5º => 1 0 2 => 1 1 2 => 1 4 1 2 2
 
 6º => 1 1 1 => 1 2 1 => 1 4 2 2 1
 
 7º => 1 2 0 => 1 3 0 => 1 4 3 2 0
 
 8º => 2 0 1 => 2 1 1 => 2 4 1 2 1
 
 9º => 2 1 0 => 2 2 0 => 2 4 2 2 0
 
10º => 3 0 0 => 3 1 0 => 3 4 1 2 0

O resultado serão todas as possibilidades de preenchimento da linha, um novo algoritmo cria estas linhas em lista, ele define os números de coluna na posição impar como 2 e os números de coluna na posição par como 1, o programa irá trabalhar como 1 para preenchido e 2 para espaço vazio e 0 quando não se tem o conhecimento do valor.

exemplo:

 1º => 0 0 3 => 0 1 3 => 0 4 1 2 3 => 1 1 1 1 2 1 1 2 2 2
 
 2º => 0 1 2 => 0 2 2 => 0 4 2 2 2 => 1 1 1 1 2 2 1 1 2 2
 
 3º => 0 2 1 => 0 3 1 => 0 4 3 2 1 => 1 1 1 1 2 2 2 1 1 2
 
 4º => 0 3 0 => 0 4 0 => 0 4 4 2 0 => 1 1 1 1 2 2 2 2 1 1
 
 5º => 1 0 2 => 1 1 2 => 1 4 1 2 2 => 2 1 1 1 1 2 1 1 2 2
 
 6º => 1 1 1 => 1 2 1 => 1 4 2 2 1 => 2 1 1 1 1 2 2 1 1 2
 
 7º => 1 2 0 => 1 3 0 => 1 4 3 2 0 => 2 1 1 1 1 2 2 2 1 1
 
 8º => 2 0 1 => 2 1 1 => 2 4 1 2 1 => 2 2 1 1 1 1 2 1 1 2
 
 9º => 2 1 0 => 2 2 0 => 2 4 2 2 0 => 2 2 1 1 1 1 2 2 1 1
 
10º => 3 0 0 => 3 1 0 => 3 4 1 2 0 => 2 2 2 1 1 1 1 2 1 1

Em seguida o programa irá trabalhar em um loop até que resolva o jogo, ele irá procurar por valores constantes nas possibilidades para descobrir preenchimentos e vazios na tabela, realizar o teste em todas as linhas e colunas ele tenta usar as constantes para eliminar possibilidades, por isso um loop encontrando constantes podemos diminuir possibilidades, diminuindo possibilidades pode-se encontrar mais constante, a tabela é inicialmente formada por zeros, quando encontrado alguma constante ele altera na tabela.


exemplo:

1 1 1 1 2 1 1 2 2 2

1 1 1 1 2 2 1 1 2 2

1 1 1 1 2 2 2 1 1 2

1 1 1 1 2 2 2 2 1 1

2 1 1 1 1 2 1 1 2 2

2 1 1 1 1 2 2 1 1 2

2 1 1 1 1 2 2 2 1 1

2 2 1 1 1 1 2 1 1 2

2 2 1 1 1 1 2 2 1 1

2 2 2 1 1 1 1 2 1 1

0 0 0 1 0 0 0 0 0 0 Na quarta coluna todos os números eram 1, por isso definir-se que só pode ser 1 independente de qual possibilidade seja.

O programa também trabalha com a relação de linhas e colunas, ao descobrir uma constante em uma linha elimina possibilidades em na coluna, e vice versa.

exemplo:
      3
      4

0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0
          
0 0 0 0 0 0 0 0 0 0
          
0 0 0 0 0 0 0 0 0 0   4 2
    
0 0 0 0 0 0 0 0 0 0
          
0 0 0 0 0 0 0 0 0 0
          
0 0 0 0 0 0 0 0 0 0
          
0 0 0 0 0 0 0 0 0 0
          
0 0 0 0 0 0 0 0 0 0
          
0 0 0 0 0 0 0 0 0 0

Encontrando as possibilidades da coluna com os termos 3 e 4.

Termos = 2
Bônus = 2
possibilidades = (2+2)!/(2!*2!) = 6

Os termos são: 4 e 2 para um quadrado de tamanho 10

 1º => 0 0 2 => 0 1 2 => 0 3 1 4 2 => 1 1 1 2 1 1 1 1 2 2
 
 2º => 0 1 1 => 0 2 1 => 0 3 2 4 1 => 1 1 1 2 2 1 1 1 1 2
 
 3º => 0 2 0 => 0 3 1 => 0 3 3 4 1 => 1 1 1 2 2 2 1 1 1 1
 
 4º => 1 0 1 => 1 1 1 => 1 3 1 4 1 => 2 1 1 1 2 1 1 1 1 2
 
 5º => 1 1 0 => 1 2 0 => 1 3 2 4 0 => 2 1 1 1 2 2 1 1 1 1
 
 6º => 2 0 0 => 2 1 0 => 2 3 1 4 0 => 2 2 1 1 1 2 1 1 1 1

Podemos encontrar as seguintes constantes:

1 1 1 2 1 1 1 1 2 2

1 1 1 2 2 1 1 1 1 2

1 1 1 2 2 2 1 1 1 1

2 1 1 1 2 1 1 1 1 2

2 1 1 1 2 2 1 1 1 1

2 2 1 1 1 2 1 1 1 1

0 0 1 0 0 0 1 1 0 0 <= encontrando constantes com 6 possibilidades, encontramos 3 constantes.

Ao descobrir a constante na quarta coluna na linha com os termos 4 e 2, pode se verificar que elimina possibilidades na coluna com os termos 3 e 4 em que define como possibilidade o 2 aonde já se sabe que tem a constante 1, logo podemos eliminar.

0 0 0 1 0 0 0 0 0 0

1 1 1 2 1 1 1 1 2 2 Tem um 2 aonde deveria ser 1

1 1 1 2 2 1 1 1 1 2 Tem um 2 aonde deveria ser 1

1 1 1 2 2 2 1 1 1 1 Tem um 2 aonde deveria ser 1

2 1 1 1 2 1 1 1 1 2

2 1 1 1 2 2 1 1 1 1

2 2 1 1 1 2 1 1 1 1

sobra então três possibilidades, que ao procurar constantes podemos encontrar mais por ter eliminado falsas possibilidades:

2 1 1 1 2 1 1 1 1 2

2 1 1 1 2 2 1 1 1 1

2 2 1 1 1 2 1 1 1 1


2 0 1 1 0 0 1 1 1 0 <= encontrando constantes com 3 possibilidades, encontramos 6 constantes.

Para que o programa saiba quais são as possibilidades eliminadas ele usa uma lista de mesmo tamanho que as possibilidades, inicialmente com tudo 1 substitui-se por 0 ao eliminar uma possibilidade.

coluna com os termos 3 e 4 e em seguida ao descobrir a constante da linha com os termos 4 e 2, elimina as três primeiras possibilidades:

1 1 1 1 1 1

0 0 0 1 1 1

Então quando em loop ele tenta resolver o desafio, por mais que eu ainda não tenha provado acredito que possa resolver qualquer fase que só tenha uma forma de resolver, jogos com mais de uma resolução não sairia do loop, nunca testado apenas teórico, mas todas as fases geralmente são feitas para que se tenho um único formato, por mais que exista formatos de diversas resoluções.

Para enviar os dados do jogo e obter a resolução é necessário enviar uma única frase com o tamanho do quadrado, em seguida separado por vírgula informar todas as linhas com os termos separados por vírgula e para finalizar a linha deve enviar um zero no final de cada linha, e depois o mesmo processo com as colunas e por fim mandar dois zeros separados por vírgula no final.

exemplo:

5, 3, 0, 2, 0, 1, 3, 0, 2, 1, 0, 3, 0, 1, 2, 0, 1, 2, 0, 3, 1, 0, 2, 1, 0, 2, 0, 0
