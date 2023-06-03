tuplaVogal = ('a','e','i','o','u')
try: 
  tuplaVogal[0] = 'b'
except: 
  print("Uma tupla é imutável")

dict = { 
  "nome": "Guilherme", 
  "idade": 25, 
  "sexo": "M", 
  "peso": 80.0, 
  "altura": 1.75
}

for key in dict: 
  print(" {} : {}".format(key, dict[key]))
