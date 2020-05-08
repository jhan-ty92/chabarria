#!C:\Python34\python
import cgi
import sys
import pymysql
print ("Content-Type:text/html \r\n\r\n")
try:
	form = cgi.FieldStorage()
	id=form.getvalue('id')
	codigo=form.getvalue('codigo')
	nombre=str(form.getvalue('nombre')).upper()
	apellidos=str(form.getvalue('apellidos')).upper()
	ci=str(form.getvalue('ci')).upper()
	telefono=str(form.getvalue('telefono')).upper()
	ciudad=str(form.getvalue('ciudad')).upper()
	provincia=str(form.getvalue('provincia')).upper()
	localidad=str(form.getvalue('localidad')).upper()
	direccion=str(form.getvalue('direccion')).upper()
	tipo=str(form.getvalue('tipo')).upper()
	con1=pymysql.connect(user="root",password="",host="",database="buses_chavarria")
	cursor1=con1.cursor()
	cursor1.execute("update personal set nombre='"+nombre+"',apellidos='"+apellidos+"',ci='"+ci+"',telefono='"+telefono+"',ciudad='"+ciudad+"',provincia='"+provincia+"',localidad='"+localidad+"',direccion='"+direccion+"',tipo_personal='"+tipo+"' WHERE cod="+str(codigo))
	con1.commit()
	con1.close()
	print("<script>location.href='../../administracion/configurarpersonal.py?id="+str(id)+"'</script>")
except:
	print("<script>location.href='../../error/error.py'</script>")