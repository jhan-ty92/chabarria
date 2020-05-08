#!C:\Python34\python
import cgi
import sys
import pymysql
print ("Content-Type:text/html \r\n\r\n")
try:
	form = cgi.FieldStorage()
	codigo=form.getvalue('codigo')
	sub_ruta=str(form.getvalue('sub_ruta')).upper()
	con1=pymysql.connect(user="root",password="",host="",database="buses_chavarria")
	cursor1=con1.cursor()
	cursor1.execute("update ruta set sub_ruta='"+sub_ruta+"' WHERE cod="+codigo)
	con1.commit()
	con1.close()
	print("<script>location.href='../../administracion/configurarruta.py?id="+str(codigo)+"'</script>")
except:
	print("<script>location.href='../../error/error.py'</script>")