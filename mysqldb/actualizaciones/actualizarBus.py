#!C:\Python34\python
import cgi
import sys
import pymysql
print ("Content-Type:text/html \r\n\r\n")
try:
	form = cgi.FieldStorage()
	id=form.getvalue('codigo')
	estado=str(form.getvalue('estado')).upper()

	con1=pymysql.connect(user="root",password="",host="",database="buses_chavarria")
	cursor1=con1.cursor()
	cursor1.execute("update bus set estado='"+str(estado)+"' where cod="+str(id))
	con1.commit()
	con1.close()
	print("<script>location.href='../../administracion/bus.py'</script>")
except:
	print("<script>location.href='../../error/error.py'</script>")