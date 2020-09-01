import json
import webbrowser

carga = []
 
def cargar():
    with open('archivo.json') as file:
        carga.append(json.load(file))          

        valor = 0
        for i in carga:
            valor += 1

            filew = open("reporte.html", "w")

            filew.write("<html>")
            filew.write("<head>")
            filew.write("<title>Reporte</title>")
            filew.write('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">')
            filew.write("</head>")
            filew.write("<body>")        
            filew.write('<div class="container">')
            filew.write('<table class="table">')
            filew.write('<thead class="thead-dark">')
            filew.write("<tr>")
            filew.write('<th scope="col">Nombre</th>')
            filew.write('<th scope="col">Edad</th>')        
            filew.write('<th scope="col">Activo</th>')
            filew.write('<th scope="col">Saldo</th>')
            filew.write("</tr>")
            filew.write("</thead>")
            filew.write("<tbody>")            
            v = 0
            while v < valor:  
                for j in i:
                    filew.write("<tr>")          
                    filew.write("<td>")
                    filew.write(str(j['nombre']))
                    filew.write("</td>")
                    filew.write("<td>")
                    filew.write(str(j['edad']))
                    filew.write("</td>")
                    filew.write("<td>")
                    filew.write(str(j['activo']))
                    filew.write("</td>")
                    filew.write("<td>")
                    filew.write(str(j['saldo']))
                    filew.write("</td>")                    
                    filew.write("</tr>")
                v += 1        
            
            filew.write("</tbody>")
            filew.write("</table>")
            filew.write("</div>")
            filew.write("</body>")        
            filew.write("</html>")

    filew.close()

    webbrowser.open_new_tab("reporte.html")                                

cargar()
            