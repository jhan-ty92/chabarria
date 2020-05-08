#!C:\Python34\python

import cgi 
import pymysql 
import sys
sys.path.append("..")
from layout .principal import *
cabezera()
print ("Content-Type:text/html \r\n\r\n")
try:
    form = cgi.FieldStorage()
    cod=form.getvalue('id')
    con=pymysql.connect(user="root",password="",host="",database="buses_chavarria")
    cursor=con.cursor()
    cursor.execute("""select of1.nombre,of2.nombre,ru.sub_ruta,ru.oficina_origen,ru.cod FROM ruta ru 
                  inner join oficina of1 on ru.oficina_origen=of1.cod
                  inner join oficina of2 on ru.oficina_destino=of2.cod
                  where ru.cod='"""+str(cod)+"'")

    ini=""
    fin=""
    sub=""
    ori=""
    cod_ru=""
    for art in cursor:
        ini=ini+str(art[0])
        fin=fin+str(art[1])
        sub=sub+str(art[2])
        ori=ori+str(art[3])
        cod_ru=cod_ru+str(art[4])



    ruta=con.cursor()
    ru=ruta.execute("""select rf.cod,fre.fecuencia,rf.accion,ru.cod FROM ruta_frecuencia rf
                  inner join frecuencia fre on rf.cod_frecuencia=fre.cod
                  inner join ruta ru on rf.cod_ruta=ru.cod
                  where rf.cod_ruta='"""+cod+"'")



    frecuencia=con.cursor()
    frecuencia.execute("select * from frecuencia")
    fre=""
    for art in frecuencia:
        if str(art[2])=="1":
            fre=fre+"<option value="+str(art[0])+">"+str(art[1])+"</option>"


    print("""
<section class="content">
    <div class="container-fluid">
        <ol class="breadcrumb breadcrumb-bg-blue-grey">
            <li >
                <a href="index.py">
                    <i class="material-icons">home</i> Principal
                </a>
            </li>
            <li class="active">
                <a href="rutas.py">
                   <i class="material-icons">repeat</i> Rutas
                </a>
            </li>
            <li class="active">
                <i class="material-icons">alarm</i> Frecuencia
            </li>
        </ol>
        <div class="row clearfix">
            <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12" style="width: 50%">
                <div class="card">
                    <div class="header bg-indigo">
                     <center>   <h2>
                            EDITAR RUTA
                        </h2>   </center>
                    </div>
                    <div class="body" style="height:445px; overflow-y: scroll;">
                        <div class="row clearfix">
                            <div class="box-body">
                    <div class="row">
                        <div class="col-sm-12">
                        <div class="col-sm-4">
                            <center><label for="ruta">RUTA ORIGEN</label>
                            <br>
                            <label style="color:">"""+ini+"""</label></center>
                        </div>
                        <div class="col-sm-4">
                            <center><i class="material-icons">arrow_back</i>
                            <label style="">RUTA</label>
                            <i class="material-icons">arrow_forward</i></center>
                        </div>
                        <div class="col-sm-4">
                            <center><label for="ruta">RUTA DESTINO</label>
                            <br>
                            <label style="color:">"""+fin+"""</label></center>  
                        </div>
                        </div>
                    </div>
                </div>

                <form action="../mysqldb/actualizaciones/actualizarRuta.py" method="POST" class="form-registro" accept-charset="UTF-8">     
                    <input name="codigo" value="""+cod+""" type="hidden" ></input>
                    <div class="box-body">
                        <div class="row">
                            <div class="col-sm-12">
                            <div class="col-sm-12">
                            <div class="col-sm-12">
                                <label for="r">SUB RUTAS:</label>
                                <textarea rows="3" class="form-control no-resize" name="sub_ruta">"""+str(sub)+"""</textarea>    
                            </div>
                            </div>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <center>
                            <button type="submit" class="btn bg-indigo waves-effect"><div class="demo-google-material-icon"> <i class="material-icons">create_new_folder</i> <span class="icon-name">GRABAR DATOS</span></div></button>  
                        </center>
                    </div>
                </form>

                        </div>
                    </div>
                </div>
            </div>
            <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12" style="width: 50%">
                <div class="card">
                    <div class="header bg-indigo">
                     <center>   <h2>
                            FRECUENCIAS
                        </h2>   </center>
                    </div>
                    <div class="body">

                        <div class="row clearfix" style="height:400px;overflow-y: scroll;">
                            
                            <div class='col-lg-12 col-md-12 col-sm-12 col-xs-12'>
                            <div class="header">
                                <h2>
                                    <small>"""+ini+""" - """+fin+"""</small>
                                </h2>
                                <ul class="header-dropdown m-r--5">
                                    <li>
                                        <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3">
                                            <a data-toggle="modal" data-target="#re_ruta"><button type="button" class="btn bg-indigo waves-effect"><div class="demo-google-material-icon"> <i class="material-icons">create_new_folder</i> <span class="icon-name">Agregar</span></div></button></a>
                                        </div>
                                    </li> 
                                </ul>
                            </div>
                            <div class="body">
                                <div class="table-responsive">
                                    <table class="table table-bordered table-striped table-hover js-basic-example dataTable">
                                        <thead>
                                            <tr>
                                                <th width=30><center>N°</center></th>
                                                <th width=240><center>FRECUENCIA</center></th>
                                                <th><center>ACCION</center></th>
                                            </tr>
                                        </thead>
                                        <tbody>

""")
    if ru!=0:
        i=0
        for art in ruta:
            i=i+1
            print("""
                                            <tr>
                                                <td><center>"""+str(i)+"""</center></td>
                                                <td><center>"""+str(art[1])+"""</center></td>
                                                <td><center><center><a  href='../mysqldb/eliminar/EliminarRuta_Fre.py?id="""+str(art[0])+""";&cod="""+str(cod)+""";' data-toggle='tooltip' style='padding-left: 15px;' data-placement='bottom' title='ELIMINAR' ><i class='material-icons'>delete</i></a></center></center></td>
                                            </tr>""")

    print("""                           </tbody>
                                    </table>
                                </div>
                            </div>
                        </div> 
                    </div>
                    </div>
                </div>
            </div>
        </div>    
    </div>
</section>
    

<div class="modal" id="re_ruta" tabindex="-1" role="dialog" aria-labellebdy="myModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header header bg-indigo">
                <center><h5 class="modal-title">NUEVA RUTA</h5></center>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times</span>
                </button>
            </div>
            <div class="modal-body">
             <form action="../mysqldb/registros/RegistroRuta_Frecuencia.py" method="POST" class="form-registro" accept-charset="UTF-8">     
                <input name="cod" value="""+cod+""" type="hidden" ></input>
                <input name="ruta" value="""+cod_ru+""" type="hidden" ></input>
                <div class="box-body">
                    <div class="row">
                        <div class="col-sm-12">
                        <div class="col-sm-12">
                        <div class="col-sm-12">
                        <div class="col-sm-12">
                        <div class="col-sm-12">
                        <div class="col-sm-12">
                            <label for="r">FRECUENCIA:</label>
                            <div class="input-group">
                                <span class="input-group-addon">
                                    <i class="material-icons">access_time</i>
                                </span>
                                <select name="fre" class="form-control">
                                <option></option>
                                """+fre+"""
                            </select>
                            </div>
                        </div>
                        </div>
                        </div>
                        </div>
                        </div>
                        </div>
                    </div>
                </div>
                <br>
                <div class="row">
                <div class="col-sm-12">
                        <div class="col-sm-12">
                        <div class="col-sm-12">
                        <div class="col-sm-12">
                    <div class="col-md-5">

                        <button type="submit" class="btn bg-indigo waves-effect"><div class="demo-google-material-icon"> <i class="material-icons">create_new_folder</i> <span class="icon-name">GRABAR DATOS</span></div></button>  
                    </div>
                        </div>
                        </div>
                        </div>
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
except:
    print("<script>location.href='../error/error.py'</script>")
