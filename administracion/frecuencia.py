#!C:\Python34\python 
import pymysql 
import sys
sys.path.append("..")
from layout .principal import *
cabezera()

con=pymysql.connect(user="root",password="",host="",database="buses_chavarria")
cursor=con.cursor()
ru=cursor.execute("select * from frecuencia")
cad=""
print ("Content-Type:text/html \r\n\r\n")

print("""

<section class="content" >
    <div class="container-fluid">
        <div class="row clearfix">
            <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">
                <ol class="breadcrumb breadcrumb-bg-blue-grey" >
                    <li >
                        <a href="index.py">
                            <i class="material-icons">home</i> Principal
                        </a>
                    </li>
                    <li class="active">
                        <i class="material-icons">link</i> Frecuencias
                    </li>
                </ol>
                <div class="card">
                    <div class="header">
                        <h2>
                            Lista de Frecuencias<small>Lista</small>
                        </h2>
                        <ul class="header-dropdown m-r--5">
                            <li>
                                <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3">
                                  <a data-toggle="modal" data-target="#re_oficina"><button type="button" class="btn bg-indigo waves-effect"><div class="demo-google-material-icon"> <i class="material-icons">create_new_folder</i> <span class="icon-name">Nueva Frecuencia</span></div></button></a>
                                </div>
                            </li> 
                        </ul>
                    </div>
                    <div class="body" style="height:445px; overflow-y: scroll;">
                        <div class="row clearfix">
                            <div class="body">""")
if ru!=0:
    print("""
                            <div class="table-responsive">
                                <table class="table table-bordered table-striped table-hover js-basic-example dataTable">
                                    <thead>
                                        <tr>
                                            <th width=30><center>N°</center></th>
                                            <th width=240><center>FRECUENCIA</center></th>
                                            <th><center width=30>ESTADO</center></th>
                                            <th><center>ACCION</center></th>
                                        </tr>
                                    </thead>
                                    </tfoot>
                                    <tbody>
    """)
    i=0
    for art in cursor:
        ii="check"
        ac="ACTIVO"
        if str(art[2])=="0": 
            ac="NO ACTIVO"
            ii="close"

        i=i+1
        print("""                       <tr>
                                            <td><center>"""+str(i)+"""</center></td>
                                            <td width="15%"><center>"""+str(art[1])+"""</center></td>
                                            <td><center>"""+str(ac)+"""</center></td>
                                            <td><center><a href='../mysqldb/actualizaciones/actualizarestadoFrecuencia.py?id="""+str(art[0])+"""' data-toggle='tooltip' data-placement='bottom' title='"""+ac+"""'><i class='material-icons'>"""+ii+"""</i></a><a href='../mysqldb/eliminar/EliminarFrecuencia.py?id="""+str(art[0])+"""' style='padding-left: 15px;' data-placement='bottom' title='ELIMINAR FRECUENCIA' ><i class='material-icons'>delete</i></a></center></td>
                                        </tr>""")
    print("""         
                                    </tbody>
                                </table>
                            </div>""")
else:
    print("AUN NO HAY RUTAS REGISTRADAS")
print("""                   </div>
                        </div>
                    </div>
                </div>
            </div>

        </div>    
    </div>
</section>

<div class="modal" id="re_oficina" tabindex="-1" role="dialog" aria-labellebdy="myModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header header bg-indigo">
                <center><h5 class="modal-title">NUEVA FRECUENCIA</h5></center>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times</span>
                </button>
            </div>
            <div class="modal-body">
             <form action="../mysqldb/registros/RegistroFrecuencia.py" method="POST" class="form-registro" accept-charset="UTF-8">     
                <br>
                <div class="box-body">
                    <div class="row">
                        <div class="col-lg-6">
                        <div class="demo-masked-input">        
                            <div class="input-group">
                                <span class="input-group-addon">
                                    <i class="material-icons">access_time</i>
                                </span>
                                <div class="form-line">
                                    <input type="text" class="form-control time12" name="hora" placeholder="hr: 06:00" required>
                                </div>
                            </div> 
                        </div>
                        </div>
                    </div>
                </div>
                <br>
                <div class="row">
                    <div class="col-md-5">
                        <button type="submit" class="btn bg-indigo waves-effect"><div class="demo-google-material-icon"> <i class="material-icons">create_new_folder</i> <span class="icon-name">GRABAR DATOS</span></div></button>  
                    </div>
                </div>
            </form>     
            </div>
            <div class="modal-footer"></div>
        </div>
    </div>
</div>
""")
fin_cabezera()