#!C:\Python34\python 
import pymysql 
import sys
sys.path.append("..")
from layout .principal import *
cabezera()

con=pymysql.connect(user="root",password="",host="",database="buses_chavarria")
cursor=con.cursor()
c=cursor.execute("select * from oficina")
cad=""
print ("Content-Type:text/html \r\n\r\n")

print("""
<section class="content">
    <div class="container-fluid">
        <ol class="breadcrumb breadcrumb-bg-blue-grey">
            <li >
                <a href="index.py">
                    <i class="material-icons">home</i> Principal
                </a>
            </li>
        </ol>
        <div class="row clearfix">
            <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">
                <div class="card">
                    <div class="header">
                        <h2>
                            VACIO<small>VACIO</small>
                        </h2>
                        <ul class="header-dropdown m-r--5">
                            <li>
                                <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3">
                                  <a data-toggle="modal" data-target="#re_oficina"><button type="button" class="btn bg-indigo waves-effect"><div class="demo-google-material-icon"> <i class="material-icons">create_new_folder</i> <span class="icon-name">Nueva</span></div></button></a>
                                </div>
                            </li> 
                        </ul>
                    </div>
                    <div class="body" style="height:445px; overflow-y: scroll;">
                        
                                        

                    </div>
                </div>
            </div>
            <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">
                <div class="card">
                    <div class="header bg-indigo">
                        <h2>VACIO</h2>
                        <ul class="header-dropdown m-r--5">
                            <li>     
                                <i class="material-icons">chrome_reader_mode</i>
                            </li>  
                        </ul>
                    </div>
                    <div class="body">
                        <div class="row clearfix" style="height:400px;overflow-y: scroll;">
                            <center><h3 style="padding-top: 170px;">VACIO</h3>  
                        </div>
                    </div>
                </div>
            </div>
        </div>    
    </div>
</section>
""")
fin_cabezera()
