#!C:\Python34\python
import cgi
import sys
import pymysql
print ("Content-Type:text/html \r\n\r\n")
try:
	form = cgi.FieldStorage()
	con=pymysql.connect(user="root",password="",host="",database="buses_chavarria")
	id=form.getvalue('id')
	posi=form.getvalue('posi')
	if (posi=="si"):
		suma=""
		cont=form.getvalue('contador')
		lis=[]
		for k in range(0,int(cont)):
			fc="fc"+str(k)
			suma=suma+str(form.getvalue(fc))+"-"
		suma=suma[0:len(suma)-3]
		rcursor=con.cursor()
		rcursor.execute("update bus set mapeo='"+suma+"' where cod="+str(id))
	else:
		piso=form.getvalue('piso')
		a1=form.getvalue('a1')
		f1=form.getvalue('f1')
		a=a1.split('-')
		f=f1.split('-')
		e=""
		lis=[]
		aux=0
		for k in range(0,int(piso)):
			for i in range(0,int((int(a[k])/int(f[k]))+3)):
				for j in range(0,int(int(f[k])*2)):
					ij="ij"+str(aux)+""+str(j)
					lis.append(str(form.getvalue(ij)))
				aux=aux+1
			lis.append(str("&"))
		suma=""
		for i in range(len(lis)):
			if lis[i]!="X": 
				suma=suma+str(lis[i]).upper()+"-"
		suma=suma[0:len(suma)-3]
		cursor=con.cursor()
		cursor.execute("update bus set mapeo='"+suma+"' where cod="+str(id))
	con.commit()
	con.close()
	print("<script>location.href='../../administracion/bus.py'</script>")
except:
	print("<script>location.href='../../error/error.py'</script>")