def hexa_to_octal(number):
    result1 = 0
    pwr = 0
    hex_dict = "0123456789ABCDEF"
    for x in number[::-1]:
        digit = hex_dict.index(x)
        result1 +=  digit * (16 ** pwr)
        pwr +=1
    oct=int(result1)
    result2 =""
    while oct >= 1:
        remain = oct % 8
        result2 = str(int(remain))+result2
        oct //= 8
    print(result2)
   

def octal_to_hexa(number):
    octal=int(number)
    result1 = 0
    pwr = 0
    while octal > 0:
        digit = octal % 10
        result1 = result1 + digit * (8**pwr)
        pwr = pwr + 1
        octal = octal//10
    hex_dict = "0123456789ABCDEF"
    hex=int(result1)
    result2 =""
    while hex > 0:
        remain = hex % 16
        result2 = hex_dict[remain]+result2
        hex //= 16
    print(result2)

def binary_to_hexa(number):
    binary = int(number)
    result1 = 0
    pwr = 0
    while binary > 0:
        digit = binary % 10
        result1 = result1 + digit * (2**pwr)
        pwr = pwr + 1
        binary = binary//10
    hex_dict = "0123456789ABCDEF"
    hex=int(result1)
    result =""
    while hex > 0:
        remain = hex % 16
        result = hex_dict[remain]+result
        hex //= 16
    print(result)

def binary_to_octal(number):
    binary = int(number)
    result1 = 0
    pwr = 0
    while binary > 0:
        digit = binary % 10
        result1 = result1 + digit * (2**pwr)
        pwr = pwr + 1
        binary = binary//10
    oct=int(result1)
    result2 =""
    while oct >= 1:
        remain = oct % 8
        result2 = str(int(remain))+result2
        oct //= 8
    print(result2)

def decimal_to_hexa(number):
    hex_dict = "0123456789ABCDEF"
    hex=int(number)
    result =""
    while hex > 0:
        remain = hex % 16
        result += hex_dict[remain]
        hex //= 16
    print(result)

def decimal_to_octal(number):
    oct=int(number)
    result =""
    while oct >= 1:
        remain = oct % 8
        result += str(int(remain))
        oct //= 8
    print(result)

def octal_to_binary(number):
    oct= int(number)
    result1 = 0
    pwr = 0
    while oct > 0:
        digit = oct % 10
        result1 += digit * (8**pwr)
        pwr += 1
        oct = oct//10
    dec = result1
    result2 = ""
    remain = 0
    while dec >= 1:
        remain = dec % 2
        dec //= 2
        result2 = str(int(remain)) + result2
    print(result2)

def hexa_to_binary(number):
    result1 = 0
    pwr = 0
    hex_dict = "0123456789ABCDEF"
    for x in number [::-1]:
        digit = hex_dict.index(x)
        result1 +=  digit * (16 ** pwr)
        pwr +=1
    dec = result1
    result2 = ""
    remain = 0
    while dec >= 1:
        remain = dec % 2
        dec //= 2
        result2 += str(int(remain)) 
    print(result2)

def octal_to_decimal(number):
    octal = int(number)
    result = 0
    pwr = 0
    while octal > 0:
        digit = octal % 10
        result += digit * (8**pwr)
        pwr += 1
        octal = octal//10
    print(result)

def hexa_to_decimal(number):
    result = 0
    pwr = 0
    hex_dict = "0123456789ABCDEF"
    for x in number[::-1]:
        digit = hex_dict.index(x)
        result +=  digit * (16 ** pwr)
        pwr += 1
    print(result)

def binary_to_decimal(number):
    binary = int(number)
    result = 0
    pwr = 0
    while binary > 0:
        digit = binary % 10
        result += digit * (2**pwr)
        pwr += 1
        binary = binary//10
    print(result)

def decimal_to_binary(number):
    dec = int(number)
    result = ""
    remain = 0
    while dec >= 1:
        remain = dec % 2
        dec //= 2
        result += str(int(remain)) 
    print(result)



# Conclusion Function
def conc(number, menu2_choice, menu3_choice):
    if menu2_choice == "A" and menu3_choice == "A":
        print(number)
    elif menu2_choice == "A" and menu3_choice == "B":
        decimal_to_binary(number)
    elif menu2_choice == "A" and menu3_choice == "C":
        decimal_to_octal(number)
    elif menu2_choice == "A" and menu3_choice == "D":
        decimal_to_hexa(number)
    elif menu2_choice == "B" and menu3_choice == "B":
        print(number)
    elif menu2_choice == "B" and menu3_choice == "A":
        binary_to_decimal(number)
    elif menu2_choice == "B" and menu3_choice == "C":
        binary_to_octal(number)
    elif menu2_choice == "B" and menu3_choice == "D":
        binary_to_hexa(number)
    elif menu2_choice == "C" and menu3_choice == "C":
        print(number)
    elif menu2_choice == "C" and menu3_choice == "A":
        octal_to_decimal(number)
    elif menu2_choice == "C" and menu3_choice == "B":
        octal_to_binary(number)
    elif menu2_choice == "C" and menu3_choice == "D":
        octal_to_hexa(number)
    elif menu2_choice == "D" and menu3_choice == "D":
        print(number)
    elif menu2_choice == "D" and menu3_choice == "A":
        hexa_to_decimal(number)
    elif menu2_choice == "D" and menu3_choice == "B":
        hexa_to_binary(number)
    else :                                  #menu2_choice == "D" and menu3_choice == "C"
        hexa_to_octal(number)
# Menu3 function

def menu3(number,menu2_choice):
    while True:
        menu3_choice = input("** Please select the base you want to convert a number to **\nA) Decimal\nB) Binary\nC) octal\nD) hexadecimal\nChoose {A,B,C,D}: ")
        if menu3_choice == "A":
            conc(number, menu2_choice, menu3_choice)
            menu1()
            break
        elif menu3_choice == "B":
            conc(number, menu2_choice, menu3_choice)
            menu1()
            break
        elif menu3_choice == "C":
            conc(number, menu2_choice, menu3_choice)
            menu1()
            break
        elif menu3_choice == "D":
            conc(number, menu2_choice, menu3_choice)
            menu1()
            break
        else:
            print(str(menu3_choice), "is not valid, please select a valid choice")

# Menu2 function
def menu2(number):
    while True:
        menu2_choice = input("** Please select the base you want to convert a number from**\nA) Decimal\nB) Binary\nC) octal\nD) hexadecimal\nChoose {A,B,C,D}: ")
        if menu2_choice == "A":
            menu3(number,menu2_choice)
            break
        elif menu2_choice =="B":
            menu3(number,menu2_choice)
            break
        elif menu2_choice =="C":
            menu3(number,menu2_choice)
            break
        elif menu2_choice=="D":
            menu3(number,menu2_choice)
            break
        else :
            print(str(menu2_choice), "is not valid, please select a valid choice")

# Menu1 function
def menu1():
    while True:
        menu1_choice =input ("** Numbering System Converter **\nA) insert a new number\nB) Exit program\nChoose {A,B}: ")

        if menu1_choice=="a" or menu1_choice=="A":
            number = input("Please insert a number:")
            menu2(number)
            break
        elif menu1_choice=="b" or menu1_choice=="B":
            print ("Exiting Program")
            break
        else :
            print(str(menu1_choice),"is not valid, please select a valid choice")


menu1()


