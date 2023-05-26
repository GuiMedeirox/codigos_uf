class Pessoa: 
    def __init__(self): 
      self._nome = ""
      self._numero = "00000000"
    
    def get_nome(self):
      return self._nome

    def set_nome(self, novo_nome): 
      self._nome = novo_nome

    def get_numero(self):
      return self._numero

    def set_numero(self, novo_numero): 
      self._numero = novo_numero

    def editar_nome(self, novo_nome): 
      self._nome = novo_nome
    
    def editar_numero(self, novo_numero):
      self._numero = novo_numero

agenda = []

def listar_contatos(contatos):
  for contato in contatos: 
    print("{} - {} - {}".format( contatos.index(contato), contato.get_nome(), contato.get_numero())) 
  
def adicionar_contato(contatos, nome, numero):
  contato = Pessoa()
  contato.set_nome(nome)
  contato.set_numero(numero)
  contatos.append(contato)

def pesquisar_por_nome(contatos, nome):
  for i in range(len(contatos)): 
    if(nome == contatos[i].get_nome()): 
      print(contatos[i].get_nome())
    else:
      print("Não há contato com esse nome")

def deletar_contato(id_contato, agenda):
  try:
    agenda.pop(id_contato)
    print("AGENDA ATUALIZADA: ")
    listar_contatos(agenda)
  except Exception:
    print("Erro. ")
 
senha_agenda = input("Usuário, insira uma senha para a sua agenda: ")
print("\n" * 100)
user_senha = input("Digita a senha definida pelo usuário: ")
while (senha_agenda != user_senha): 
  user_senha = input("Digite novamente a senha: ")
print("\n" * 100)

while True:
  print("\nAGENDA")
  print("1 - LISTAR OS CONTATOS  ")#
  print("2 - EDITAR O CONTATO    ") 
  print("3 - DELETAR O CONTATO   ")# 
  print("4 - PESQUISAR POR NOME  ")#
  print("5 - CADASTRAR UM CONTATO")#
  print("6 - SAIR\n              ")#
  option = int(input("DIGITE O QUE VOCÊ DESEJA: "))
 
  if (option ==1):
    print("\n" * 100)
    listar_contatos(agenda)
  
  elif (option == 2):
    print("\n" * 100)
    listar_contatos(agenda)
    try: 
      id_contato = int(input("Digita o ID do contato a ser editado: "))
      edit = input("\n  Selecione o campo desejado para editar (NO)nome ou (NU) número: \n ")
      if edit.lower() == "no":
        novo_nome = input("Insira o novo nome do contato: ")
        agenda[id_contato].set_nome(novo_nome)
      if edit.lower() == "nu":
        novo_numero = input("Insira o novo numero do contato: ")
        agenda[id_contato].set_nome(novo_numero)
      
    except IndexError: 
        print("Erro, id inválido, insira um válido! ")
    
  elif(option == 3):
    print("\n" * 100)
    listar_contatos(agenda)
    id_contato = input("Digita o ID do contato: ")
    deletar_contato(id_contato, agenda)
  
  elif(option == 4):
    print("\n" * 100)
    nome_contato = input("Nome do contato a ser pesquisado: ")
    pesquisar_por_nome(agenda, nome_contato)
  
  elif(option == 5):
    nome_contato = input("Nome do contato: ") 
    numero_contato = input("Numero do contato: ")
    adicionar_contato(agenda, nome_contato, numero_contato)
  
  elif(option == 6):
    print("See you :)")
    exit()