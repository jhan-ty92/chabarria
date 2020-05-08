#!C:\Python34\python
import cgi
import sys
import pymysql
print ("Content-Type:text/html \r\n\r\n")
try:
	form = cgi.FieldStorage()
	id=form.getvalue('codigo')
	con1=pymysql.connect(user="root",password="",host="",database="buses_chavarria")
	cursor1=con1.cursor()
	cursor1.execute("update oficina set nombre='"+str(form.getvalue('nombre'))+"',direccion='"+str(form.getvalue('direccion'))+"',telefono='"+str(form.getvalue('telefono'))+"',celular='"+str(form.getvalue('celular'))+"',horario_atencion='"+str(str(form.getvalue('hora_i'))+" - "+str(form.getvalue('hora_f')))+"' where cod="+str(id))
	con1.commit()
	con1.close()
	print("<script>location.href='../../administracion/oficinas.py'</script>")
except:
	print("<script>location.href='../../error/error.py'</script>")