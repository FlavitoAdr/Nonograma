
 
tamanho = numeros[0]
 
def calcularbonus():
  for i in linhas[:len(linhas)-1]:
    bonus.append(tamanho-(sum(i)+len(i)-2))
 
def calcularpossibilidades():
  global bonus
  global termos
  global possibilidades

  for i in range(0, tamanho*2):
    possibilidades.append(int(math.factorial(int(bonus[i]+termos[i]))/(math.factorial(bonus[i])*math.factorial(termos[i]))))
 
def algoritmo1de3():
  global a1
  global tamanho
  global bonus
  global termos
  global alternativa
 
  for i in range(0, tamanho*2):
    a1 = a1 + [[bonus[i]] + [0] * (termos[i])]
    alternativa = a1[i]
    al1.append([])
    al1[i] = al1[i] + [list(alternativa)]
    for j in range(0, possibilidades[i]-1):
      romper = 0
      k=0
      while romper == 0:
        if int(alternativa[k]) > 0:
          gravar = alternativa[k]-1
          alternativa[k] = 0
          alternativa[0] = gravar
          alternativa[k+1] += 1
          romper = 1
        k += 1
      al1[i] = al1[i] + [list(alternativa)]

def algoritmo2de3():
  global al1
  global al2

  for i in range(0, tamanho*2):
    al2.append([])
  posicao = -1
  for i in al2:
    posicao += 1
    for j in range(0, possibilidades[posicao]):
      i.append([])

  l = -1
  for i in al1:
    l += 1
    m = al2[l]
    n = -1
    for j in i:
      n += 1
      o = m[n]
      o.append(j[0])
      posicao = -1
      for k in j[1:-1]:
        posicao += 1
        o.append(k+1)
      o.append(j[-1])

def algoritmo3de3():
  global al2
  global al3

  for i in range(0, tamanho*2):
    al3.append([])
  posicao = -1
  for i in al3:
    posicao += 1
    for j in range(0, possibilidades[posicao]):
      i.append([])

  l = -1
  p = -1
  for i in al2:
    l += 1
    p += 1
    m = al3[l]
    q = linhas[p]
    n = -1
    for j in i:
      n += 1
      o = m[n]
      for k in range(0, len(j)*2-1):
        if k % 2 == 0:
          o.append(j[int(k/2)])
        else:
          o.append(q[int((k-1)/2)])

def gerartabelapossibilidades():
  global al3
  global tabelapossibilidades

  for i in range(0, tamanho*2):
    tabelapossibilidades.append([])
  posicao = -1
  for i in tabelapossibilidades:
    posicao += 1
    for j in range(0, possibilidades[posicao]):
      i.append([])

  l =-1
  for i in tabelapossibilidades:
    l += 1
    m = al3[l]
    n = -1
    for j in i:
      n += 1
      o = m[n]
      for k in range(0, len(o)):
        for a in range(0, o[k]):
          if k % 2 == 0:
            j.append(2)
          else:
            j.append(1)

  for i in range(0, tamanho*2):
    descarte.append([])
    tabela2.append([0]*tamanho)
  for i in range(0, tamanho):
    tabela.append([0]*tamanho)
  posicao = -1
  for i in descarte:
    posicao += 1
    for j in range(0, possibilidades[posicao]):
      i.append(1)

def encontrarconstante():
  global tabelapossibilidades
  global descarte
  global buscar

  for i in range(0, tamanho*2):
    for k in range(0, tamanho):
      buscar = 0
      constante = 1
      for j in range(0, possibilidades[i]):
        if buscar == 0:
          if descarte[i][j] == 1:
            buscar = tabelapossibilidades[i][j][k]
      for j in range(0, possibilidades[i]):
        if descarte[i][j] == 1:
          if buscar != tabelapossibilidades[i][j][k]:
            constante = 0
      if constante == 1:
        if i < tamanho:
          tabela[i][k] = buscar
        else:
          tabela[k][i-tamanho] = buscar
        
  for i in range(0, tamanho*2):
    if i < tamanho:
      tabela2[i] = tabela[i]
    else:
      for j in range(0, tamanho):
        tabela2[i][j] = tabela[j][i-tamanho]

def eliminarpossibilidades():
  global tabela
  global tabelapossibilidades

  posicao = -1
  for i in tabelapossibilidades:
    posicao += 1
    for j in range(0, tamanho):
      if tabela2[posicao][j] != 0:
        conferir = tabela2[posicao][j]
        for k in range(0, possibilidades[posicao]):
          if i[k][j] != conferir:
            descarte[posicao][k] = 0

def detalhes():
  for i in tabela:
    print("tabela: ", i)
  for i in tabelapossibilidades:
    print(i)
  print(tamanho)
  print(linha)
  print(bonus)
  print(termos)
  print(possibilidades)
  print(linhas)
  print(al1)
  print(al2)
  print(al3)

for i in linha:
  linha2.append(int(i))
  if i == str(0):
    termos.append(len(linha2)-1)
    linhas = linhas + [linha2]
    linha2 = []
 
calcularbonus()
calcularpossibilidades()
algoritmo1de3()
algoritmo2de3()
algoritmo3de3()
gerartabelapossibilidades()

while zeros == 1:
  encontrarconstante()
  eliminarpossibilidades()
  zeros = 0
  for i in tabela:
    for j in i :
      if j == 0:
        zeros = 1
for i in tabela:
  print(i)
