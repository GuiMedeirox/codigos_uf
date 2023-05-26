def voterIsValid(array, auxVar): 
    if ( array.count(auxVar) > 0 ): 
        print("Your CPF already is registtered in this votation") 

        return False
    else:
        array.append(auxVar)
        return True

cpf = "" 
citizens = []
citizenIsOk = True
vote = True
polA = 0
polB = 0
total = 0
maxnumber = int(input("Voters number: "))


while(vote): 
    aux = 0
    cpf = input("Input your CPF: ") 
    
    if(citizenIsOk == True): 
        voto = input("1 - Politician A || 2 - Politican B: ") 
        if(voto == '1' and voterIsValid(citizens, cpf) == True ): 
            polA += 1
        elif(voto == '2' and voterIsValid(citizens, cpf) == True): 
            polB += 1
            
    aux = polA + polB 
    total = aux
    print(citizens, polA, polB, aux)
#codigo feito por Guilherme\
    if(aux == maxnumber): 
        vote = False 
    

if(polA > polB): 
    print("Politician A wins with {}%".format( ( (polA/total) * 100) ))
elif(polB > polA): 
    print("Politician B wins with{}% ".format( ( (polB/total) * 100) ))
else: 
    print("Omg, it's a draw")
