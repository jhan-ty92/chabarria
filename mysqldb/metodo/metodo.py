import pymysql
def usuario(si):
    con=pymysql.connect(user="root",password="",host="",database="buses_chavarria")
    usu=con.cursor()
    usu.execute("select * from usuario WHERE pasword=MD5('"+str(si)+"')") 
    us="-1"  
    for art in usu:
        us=str(art[0])
    return us
	