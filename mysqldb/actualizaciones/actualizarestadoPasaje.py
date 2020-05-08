#!C:\Python34\python
import cgi
import sys
import pymysql
print ("Content-Type:text/html \r\n\r\n")
try:
	form = cgi.FieldStorage()
	id=form.getvalue('valor')
	con=pymysql.connect(user="root",password="",host="",database="buses_chavarria")
	cursor=con.cursor()
	cursor.execute("select * from venta_pasaje WHERE cod='"+str(id)+"'")
	con.commit()
	con.close()
	a=""
	for art in cursor:
   		a=a+(str(art[9]))
	c="false"
	if a=="0":
		c="true"
	con1=pymysql.connect(user="root",password="",host="",database="buses_chavarria")
	cursor1=con1.cursor()
	cursor1.execute("update venta_pasaje set accion="+str(c)+" where cod="+str(id))
	con1.commit()
	con1.close()
	print("1")
except:
	print("<script>location.href='../../error/error.py'</script>")