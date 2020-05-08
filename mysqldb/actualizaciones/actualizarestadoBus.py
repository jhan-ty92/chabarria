#!C:\Python34\python
import cgi
import sys
import pymysql
print ("Content-Type:text/html \r\n\r\n")
try:
	form = cgi.FieldStorage()
	id=form.getvalue('id')
	con=pymysql.connect(user="root",password="",host="",database="buses_chavarria")
	cursor=con.cursor()
	cursor.execute("select * from bus WHERE cod='"+str(id)+"'")
	con.commit()
	con.close()
	a=""
	for art in cursor:
   		a=a+(str(art[10]))
	c="false"
	if a=="0":
		c="true"
	con1=pymysql.connect(user="root",password="",host="",database="buses_chavarria")
	cursor1=con1.cursor()
	cursor1.execute("update bus set accion="+str(c)+" where cod="+str(id))
	con1.commit()
	con1.close()
	print("<script>location.href='../../administracion/bus.py'</script>")
except:
	print("<script>location.href='../../error/error.py'</script>")