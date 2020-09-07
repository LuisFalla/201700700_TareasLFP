import os

def menu():
    os.system('cls')
    #entrada = input("Ingrese cadena de caracteres: ")
    #afd(entrada)
    
    entrada1 = "__servidor1"
    print("Entrada 1: ", entrada1)
    afd(entrada1)
    
    entrada2 = "3servidor"
    print("Entrada 2: ", entrada2)
    afd(entrada2)

def afd(entrada):
    entrada = entrada + "#"
    estado = 0        

    for i in entrada:               
        if estado == 0: 
            if i == "_":                
                estado = 1
            elif i.isalpha():                
                estado = 2                
            else:                 
                print("Cadena no valida")  
                break              
        elif estado == 1:
            if i == "_":                
                estado = 1
            elif i.isalpha():                
                estado = 3                
            else:                
                print("Cadena no valida")     
                break                
        elif estado == 2:
            if i.isalpha():                
                estado = 2               
            elif i.isdigit():                
                estado = 4                               
            else:                
                print("Cadena no valida") 
                break
        elif estado == 3:
            if i.isdigit():                
                estado = 4                             
            else:                
                print("Cadena no valida")       
                break          
        elif estado == 4:            
            if i == "#":                           
                print("Cadena valida")           
            else:
                print("Cadena no valida")          
                break

menu()