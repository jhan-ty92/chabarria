#!C:\Python34\python
import cgi
import sys
import pymysql
print ("Content-Type:text/html \r\n\r\n")
try:
	con=pymysql.connect(user="root",password="",host="",database="buses_chavarria")
	form = cgi.FieldStorage()
	cod_socio=form.getvalue('codigo').upper()
	pla=str(form.getvalue('bus')).upper()
	pla=pla.strip("]")
	pla=pla.strip("[")
	aa=pla.split(",")
	pp=""
	i=0
	pp=""
	while (i<len(aa)):
		n=aa[i]
		n=n.replace(' ','')
		n=n.strip("'")
		so="'"+str(n)+"','"+str(cod_socio)+"'"
		print(so)
		i=i+1
except:
	print("<script>location.href='../../error/error.py'</script>")