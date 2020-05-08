#!C:\Python34\python
import cgi
import sys
import pymysql
print ("Content-Type:text/html \r\n\r\n")
try:
	form = cgi.FieldStorage()
	codigo=form.getvalue('codigo')
	licencia=str(form.getvalue('licencia')).upper()
	id=form.getvalue('id')
	con1=pymysql.connect(user="root",password="",host="",database="buses_chavarria")
	cursor1=con1.cursor()
	cursor1.execute("update personal_bus set licencia='"+licencia+"',cod_personal='"+id+"' WHERE cod="+codigo)
	con1.commit()
	con1.close()
	print("<script>location.href='../../administracion/configurarpersonal.py?id="+str(id)+"'</script>")
except:
	print("<script>location.href='../../error/error.py'</script>")