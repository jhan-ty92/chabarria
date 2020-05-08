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
            <li class="active">
                <i class="material-icons">link</i> Oficinas
            </li>
        </ol>
        <div class="row clearfix">
            <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">
                <div class="card">
                    <div class="header">
                        <h2>
                            Lista de Oficinas<small>Lista</small>
                        </h2>
                        <ul class="header-dropdown m-r--5">
                            <li>
                                <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3">
                                  <a data-toggle="modal" data-target="#re_oficina"><button type="button" class="btn bg-indigo waves-effect"><div class="demo-google-material-icon"> <i class="material-icons">create_new_folder</i> <span class="icon-name">Nueva Oficina</span></div></button></a>
                                </div>
                            </li> 
                        </ul>
                    </div>
                    <div class="body" style="height:445px; overflow-y: scroll;">
                        <div class="row clearfix">
                        """)
if c>=1:
    for art in cursor:
        i="check"
        ac="ACTIVO"
        if str(art[6])=="0": 
            ac="NO ACTIVO"
            i="close"
        cad=cad+str(
        """case '"""+str(art[1])+"""':
                id=document.getElementsByName('id"""+str(art[1])+"""')[0].value; 
                hora=document.getElementsByName('hora"""+str(art[1])+"""')[0].value;
                accion=document.getElementsByName('accion"""+str(art[1])+"""')[0].value;
                datos=document.getElementsByName('datos"""+str(art[1])+"""')[0].value; 
                ico='"""+str(i)+"""';
                break;""")

        print("""           <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">
                                <div class="info-box" style="border-radius: 12px;">
                                    <i class="material-icons">account_balance</i>
                                <center>
                                    <div class="content">
                                        <form>
                                        <input type="hidden" name='id"""+str(art[1])+"""' value='"""+str(art[0])+"""'>
                                        <input type="hidden" name='hora"""+str(art[1])+"""' value='"""+str(art[5])+"""'>
                                        <input type="hidden" name='accion"""+str(art[1])+"""' value='"""+str(ac)+"""'>
                                        <input type="hidden" name='datos"""+str(art[1])+"""' value='"""+str(str(art[2])+"-"+str(art[3])+"-"+str(art[4]))+"""'>
                                        <a class="carrera" data-carrera="4" style="text-decoration: none;cursor: pointer;" onclick="capturar(this)" id='"""+str(art[1])+"""'>
                                            <div class="text">OFICINA """+str(art[1])+"""</div>
                                        </a>
                                        </form>

                                    </div>
                                </center>
                                </div>
                            </div>""")
else:
    print("""
        <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">
                AUN NO HAY OFICINAS REGISTRADAS
        </div>""")

print("""
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">
                <div class="card">
                    <div class="header bg-indigo">
                        <h2>
                            Oficina
                        </h2>
                        <ul class="header-dropdown m-r--5">
                            <li>     
                                <i class="material-icons">chrome_reader_mode</i>
                            </li>  
                        </ul>
                    </div>
                    <div class="body">
                        <div class="row clearfix" style="height:425px;overflow-y: scroll;">
                        
                            <div id="resultado">     
                                <div class="col-lg-12 ajax-content">
                                    <center><h3 style="padding-top: 170px;">Seleccione una oficina</h3></center>
                                </div>
                            </div>   

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
                <center><h5 class="modal-title">NUEVA OFICINA</h5></center>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times</span>
                </button>
            </div>
            <div class="modal-body">
             <form action="../mysqldb/registros/RegistroOficina.py" method="POST" class="form-registro" accept-charset="UTF-8">     
                <div class="box-body">
                    <div class="row">
                        <div class="col-lg-6">
                            <label for="NOMBRE">NOMBRE:</label>
                            <input class="form-control" type="text" name="nombre" required> 
                        </div>
                        <div class="col-lg-6">
                            <label for="DIRECCION">DIRECCION:</label>
                            <input class="form-control" type="text" name="direccion" required>
                        </div>
                    </div>
                </div>
                <br>
                <div class="box-body">
                    <div class="row">
                        <div class="col-lg-6">
                            <label for="TELEFONO">TELEFONO:</label>
                            <input class="form-control" type="text" name="telefono" > 
                        </div>
                        <div class="col-lg-6">
                            <label for="CELULAR">CELULAR:</label>
                            <input class="form-control" type="text" name="celular" >
                        </div>
                    </div>
                </div>
                <br>

                <div class="box-body">
                    <center><label for="HORA">HORARIO DE ATENCION:</label></center>
                    <div class="row">
                        <div class="col-lg-6">
                        <div class="demo-masked-input">        
                            <div class="input-group">
                                <span class="input-group-addon">
                                    <i class="material-icons">access_time</i>
                                </span>
                                <div class="form-line">
                                    <input type="text" class="form-control time12" name="hora_i" placeholder="hr: 06:00 am">
                                </div>
                            </div> 
                        </div>
                        </div>
                        <div class="col-lg-6">
                            <div class="demo-masked-input">        
                            <div class="input-group">
                                <span class="input-group-addon">
                                    <i class="material-icons">access_time</i>
                                </span>
                                <div class="form-line">
                                    <input type="text" class="form-control time12" name="hora_f" placeholder="hr: 11:59 pm">
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

<div class="modal" id="editOf" tabindex="-1" role="dialog" aria-labellebdy="myModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header header bg-indigo">
                <center><h5 class="modal-title">EDITAR OFICINA</h5></center>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times</span>
                </button>
            </div>
            <div class="modal-body">
             <form action="../mysqldb/actualizaciones/actualizarOficina.py" method="POST" class="form-registro" accept-charset="UTF-8">     
                <input  id="codigo" name="codigo" type="hidden" ></input>
                <div class="box-body">
                    <div class="row">
                        <div class="col-lg-6">
                            <label for="NOMBRE">NOMBRE:</label>
                            <input class="form-control" type="text" name="nombre" id="nombre" required> 
                        </div>
                        <div class="col-lg-6">
                            <label for="DIRECCION">DIRECCION:</label>
                            <input class="form-control" type="text" name="direccion" id="direccion" required>
                        </div>
                    </div>
                </div>
                <br>
                <div class="box-body">
                    <div class="row">
                        <div class="col-lg-6">
                            <label for="TELEFONO">TELEFONO:</label>
                            <input class="form-control" type="text" name="telefono" id="telefono" > 
                        </div>
                        <div class="col-lg-6">
                            <label for="CELULAR">CELULAR:</label>
                            <input class="form-control" type="text" name="celular" id="celular">
                        </div>
                    </div>
                </div>
                <br>

                <div class="box-body">
                    <center><label for="HORA">HORARIO DE ATENCION:</label></center>
                    <div class="row">
                        <div class="col-lg-6">
                        <div class="demo-masked-input">        
                            <div class="input-group">
                                <span class="input-group-addon">
                                    <i class="material-icons">access_time</i>
                                </span>
                                <div class="form-line">
                                    <input type="text" class="form-control time24" name="hora_i" id="hora_i" placeholder="hr: 06:00" required>
                                </div>
                            </div> 
                        </div>
                        </div>
                        <div class="col-lg-6">
                            <div class="demo-masked-input">        
                            <div class="input-group">
                                <span class="input-group-addon">
                                    <i class="material-icons">access_time</i>
                                </span>
                                <div class="form-line">
                                    <input type="text" class="form-control time24" name="hora_f" id="hora_f" placeholder="hr: 24:00" required>
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

print("""
  
<script>       
    $('#editOf').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget)
    var recipient0 = button.data('codigo')
    var recipient1 = button.data('nombre')
    var recipient2 = button.data('direccion')
    var recipient3 = button.data('telefono')
    var recipient4 = button.data('celular')
    var recipient5 = button.data('hora_i')
    var recipient6 = button.data('hora_f')
    var modal = $(this)    
    modal.find('.modal-body #codigo').val(recipient0)
    modal.find('.modal-body #nombre').val(recipient1)
    modal.find('.modal-body #direccion').val(recipient2)
    modal.find('.modal-body #telefono').val(recipient3)
    modal.find('.modal-body #celular').val(recipient4)
    modal.find('.modal-body #hora_i').val(recipient5)
    modal.find('.modal-body #hora_f').val(recipient6)
    });    
</script>

<script>
    function capturar(b)
    {
        var id=""; 
        var hora="";
        var accion="";
        var ico="";
        var datos="";
        switch(b.id){
        """+str(cad)+"""
        }
        var res=hora.split("-");
        var d=datos.split("-");
        var c="";
        if (d[2]!="NONE"){
            c=d[2];
        }
        var t="";
        if (d[1]!="NONE"){
            t=d[1];
        }
        document.getElementById("resultado").innerHTML="<div class='col-lg-12 col-md-12 col-sm-12 col-xs-12'><div class='card' ><div class='header'><h2>OFICINA<small id='oficina_name'>"+b.id+"</small></h2></div><div class='body'><div class='row clearfix'><div class='col-sm-12 table-responsive'><table width='100%'' class='table table-bordered table-striped table-hover'><tbody><tr class='odd gradeX'><td>HORARAIO DE ATENCION</td><td><center>"+hora+"</center></td></tr><tr class='odd gradeX'><td>DIRECCION</td><td><center>"+d[0]+"</center></td></tr><tr class='odd gradeX'><td>TELEFONO</td><td><center>"+t+"</center></td></tr><tr class='odd gradeX'><td>CELULAR</td><td><CENTER>"+c+"</CENTER></td></tr><tr class='odd gradeX'><td>ESTADO</td><td><center>"+accion+"</center></td></tr><tr class='odd gradeX'><td>ACCION</td><td><CENTER><a href='../mysqldb/actualizaciones/actualizarestadoOficina.py?id="+id+"' data-toggle='tooltip' data-placement='bottom' title='"+accion+"'><i class='material-icons'>"+ico+"</i></a><a style='padding-left: 15px;' data-placement='bottom' title='Editar oficina' data-toggle='modal' data-target='#editOf' data-codigo='"+id+"' data-nombre='"+b.id+"' data-direccion='"+d[0]+"' data-telefono='"+t+"' data-celular='"+c+"' data-hora_i='"+res[0].trim()+"' data-hora_f='"+res[1].trim()+"'><i class='material-icons'>border_color</i></a></CENTER></td></tr></tbody></table></div></div></div></div></div>";
    }
</script>
""")