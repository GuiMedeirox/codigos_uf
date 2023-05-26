
def tester(number):
    charArray = []

    for i in number:
        charArray.append(i)

    strNumA = charArray[0] + charArray[1]
    strNumB = charArray[2] + charArray[3]

    numA = int(strNumA)
    numB = int(strNumB)

    if((numA + numB) ** 2 == int(number)):
        print('it works')
    else:
        print('it doesnt works')


test_number = input("input your number: ")
tester(test_number)

# 3025 
# 30 + 25 = 55 
# 55 ** 2 = 3025 
#numbers to test -> 2025 3025 9801

