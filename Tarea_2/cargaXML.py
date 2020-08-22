import xml.etree.ElementTree as ET

carga = []

def cargaXml():

 
    arbol = ET.parse('archivoXML.xml')
    raiz = arbol.getroot()
    
    for element in raiz:              
        for subelement in element:
            carga.append(subelement.text)
    
    print("         *************************")
    print("         Datos del archivo cargado")     
    print("         *************************")

    print("         Tipo de Estructura: ", type(carga))
    print("")
    
    for i in carga:        
        print("         ", i)       


        

    