#!C:\Python34\python
import cgi
import sys
import pymysql

print ("Content-Type:text/html \r\n\r\n")
con=pymysql.connect(user="root",password="",host="",database="buses_chavarria")
cursor=con.cursor()
form = cgi.FieldStorage()
buscar=form.getvalue('valor')


cursor.execute("""select ru.cod,of1.nombre,of2.nombre,ru.sub_ruta,ru.accion FROM ruta ru 
                  inner join oficina of1 on ru.oficina_origen=of1.cod
                  inner join oficina of2 on ru.oficina_destino=of2.cod
                  where oficina_origen='"""+str(buscar)+"'")
cad="<table border=1 width='100%'><tr><th width=30><center>N</center></th><th><center>RUTA ORIGEN</center></th><th><center>RUTA DESTINO</center></th><th><center>ACCION</center></th></tr>"
i=0
for art in cursor:
    ico="check"
    accion="ACTIVO"
    if str(art[4])=="0": 
        ac="NO ACTIVO"
        ico="close"
    i=i+1
    cad=cad+"<tr><td><center>"+str(i)+"</center></td><td><center>"+str(art[1])+"</center></td><td><center>"+str(art[2])+"</center></td><td><center><a href='../administracion/configurarruta.py?id="+str(art[0])+"' data-toggle='tooltip' data-placement='bottom' title='AGREGAR FRECUENCIA'><i class='material-icons'>alarm</i></a><a href='../mysqldb/actualizaciones/actualizarestadoRuta.py?id="+str(art[0])+"' style='padding-left: 15px;' data-placement='bottom' title="+str(accion)+" ><i class='material-icons'>"+str(ico)+"</i></a></center></td></tr>"
cad=cad+"</table>"
print(cad)