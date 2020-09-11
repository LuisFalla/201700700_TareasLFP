import webbrowser

cadena = """(
    <
        [precio] = 45.09,
        [descripcion] = "hola mundo",
        [disponible] = true
    >,
    <
        [precio] = 4,
        [descripcion] = "adios mundo",
        [disponible] = false
    >,
    <
        [precio] = -56.4,
        [descripcion] = "este es otro ejemplo, las cadenas pueden ser muy largas",
        [disponible] = false
    >
)"""

#lista de tokens
listaToken = []

class Valor():    
    def __init__(self):
        self.entrada = ""
        self.cadena = ""
        self.cadenaAux = ""
        self.estado = 0
        self.listaToken = []

class Token():    

    tipo = ""
    lexema = ""

    def __init__(self, t, l):
        self.tipo = t
        self.lexema = l
    
    def mostrar(self):
        print(self.tipo,self.lexema)
    
    def retornarTipo(self):
        if self.tipo == "PARENTESIS_ABIERTO":
            return "Parentesis Abierto", self.lexema
        elif self.tipo == "PARENTESIS_CERRADO":
            return "Parentesis Cerrado", self.lexema
        elif self.tipo == "MENOR_QUE":
            return "Simbolo Menor Que", self.lexema
        elif self.tipo == "MAYOR_QUE":
            return "Simbolo Mayor Que", self.lexema
        elif self.tipo == "CORCHETE_ABIERTO":
            return "Corchete Abierto", self.lexema
        elif self.tipo == "CORCHETE_CERRADO":
            return "Corchete Cerrado", self.lexema
        elif self.tipo == "COMILLA_DOBLE":
            return "Comilla Doble", self.lexema        
        elif self.tipo == "SIGNO_IGUAL":
            return "Signo igual", self.lexema
        elif self.tipo == "SIMBOLO_COMA":
            return "Simbolo coma", self.lexema
        elif self.tipo == "SIGNO_PUNTO":
            return "Simbolo punto", self.lexema
        elif self.tipo == "SIGNO_MENOS":
            return "Signo menos", self.lexema        
        elif self.tipo == "NUMERO_ENTERO":
            return "Numero Entero", self.lexema
        elif self.tipo == "NUMERO_RACIONAL":
            return "Numero Racional", self.lexema
        elif self.tipo == "ID":
            return "Identificador", self.lexema
        elif self.tipo == "CADENA":
            return "Cadena-String", self.lexema
        elif self.tipo == "BOOLEAN":
            return "Booleano", self.lexema
        else:
            return "SIMBOLO DESCONOCIDO", self.lexema

v = Valor()

def afd(entrada):

    v.entrada = entrada + "#"
    v.cadena = ""
    v.estado = 0        
    
    for i in v.entrada:               
        if v.estado == 0: 
            if i == '\n':
                v.estado = 0
            elif i == "\t":
                v.estado = 0
            elif i == " ":
                v.estado = 0
            elif i == "(":    
                v.cadena += i
                agregarToken("PARENTESIS_ABIERTO")  
            elif i == ")":
                v.cadena += i
                agregarToken("PARENTESIS_CERRADO")
            elif i == "<":
                v.cadena += i
                agregarToken("MENOR_QUE")
            elif i == ">":
                v.cadena += i
                agregarToken("MAYOR_QUE")
            elif i == "[":
                v.cadena += i
                agregarToken("CORCHETE_ABIERTO")
            elif i == "]":
                v.cadena += i
                agregarToken("CORCHETE_CERRADO")                
            elif i == '"':
                v.estado = 3                
            elif i == "=":
                v.cadena += i
                agregarToken("SIGNO_IGUAL")
            elif i == ",":
                v.cadena += i
                agregarToken("SIMBOLO_COMA")            
            elif i == "-":
                v.cadena += i
                v.estado = 1                
            elif i.isdigit():
                v.cadena += i
                v.estado = 1
            elif i.isalpha():
                v.cadena += i
                v.estado = 3                                 
            else:
                if i == "#":
                    print("Cadena correcta")
                    break
                else:
                    v.cadena += i
                    agregarToken("")            
        elif v.estado == 1:
            if i.isdigit():
                v.cadena += i
                v.estado = 1
            elif i == ".":
                v.cadena += i
                v.estado = 2            
            else:
                agregarToken("NUMERO_ENTERO")
                #i = i[-1]
        elif v.estado == 2:
            if i.isdigit():
                v.cadena += i
                v.estado = 2            
            else:
                agregarToken("NUMERO_RACIONAL")
                #i = i[-1]                
        elif v.estado == 3:
            if i.isalpha():
                v.cadena += i
                v.estado = 3
            elif i == " ":
                v.cadena += i
                v.estado = 3
            elif i == ",":                
                v.cadena += i
                v.estado = 3
            elif i == '"':
                agregarToken("CADENA")
            elif i == '\n':
                agregarToken("BOOLEAN")
            else:                
                agregarToken("ID")       
                #i = i[-1]                           
        else:
            print("Error")     
            v.estado = 0

def agregarToken(tipo):
    x = Token(tipo,v.cadena)
    v.listaToken.append(x.retornarTipo())
    v.cadena = ""
    v.estado = 0


def reporte():

    filew = open("reporte.html", "w")

    filew.write("<html>")
    filew.write("<head>")
    filew.write("<title>Lista Token</title>")
    filew.write('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">')
    filew.write("</head>")
    filew.write("<body>")        
    filew.write('<div class="container" style="text-align:center">')
    filew.write("<br>")
    filew.write("<br>")
    filew.write('<div class="jumbotron jumbotron-fluid">')
    filew.write('<div class="container">')
    filew.write('<h1 class="display-4">Reporte Token</h1>')
    filew.write("</div>")
    filew.write("</div>")
    filew.write('<table class="table">')
    filew.write('<thead>')
    filew.write("</tr>")
    filew.write('<th class="bg-light">TOKEN</th>')
    filew.write('<th class="bg-info">LEXEMA</th>')        
    filew.write("</tr>")
    filew.write("</thead>")
    filew.write("<tbody>")
                            
    for i in v.listaToken:

        filew.write("<tr>")          
        filew.write("<td>")
        filew.write(str(i[0]))
        filew.write("</td>")
        filew.write("<td>")
        filew.write(str(i[1]))
        filew.write("</td>")    
        filew.write("</tr>")                        
                            
    filew.write("</tbody>")
    filew.write("</table>")
    filew.write("<br>")
    filew.write("<br>")
    filew.write("</div>")
    filew.write("</body>")        
    filew.write("</html>")        

    filew.close()

    webbrowser.open_new_tab("reporte.html") 

afd(cadena)

print("----------------------------------------")
for i in v.listaToken:
    print("Token:",i[0],"| Lexema:",i[1])

#reporte()