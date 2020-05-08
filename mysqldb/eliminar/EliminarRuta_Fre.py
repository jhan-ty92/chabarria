#!C:\Python34\python
import cgi
import sys
import pymysql
print ("Content-Type:text/html \r\n\r\n")
try:
	form = cgi.FieldStorage()
	id=form.getvalue('id')
	cod=form.getvalue('cod')
	con=pymysql.connect(user="root",password="",host="",database="buses_chavarria")
	cursor=con.cursor()
	cursor.execute("delete from ruta_frecuencia where cod="+str(id))
	con.commit()
	con.close()
	print("<script>location.href='../../administracion/configurarruta.py?id="+str(cod)+"'</script>")
except:
	print("<script>location.href='../../error/error.py'</script>")