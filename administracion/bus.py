#!C:\Python34\python 
import pymysql 
import sys
sys.path.append("..")
from layout .principal import *
cabezera()

con=pymysql.connect(user="root",password="",host="",database="buses_chavarria")
cursor=con.cursor()
c=cursor.execute("select * from bus")
cad=""
grafico=""
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
                <i class="material-icons">link</i> Buses
            </li>
        </ol>
        <div class="row clearfix">
            <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">
                <div class="card">
                    <div class="header">
                        <h2>
                            Lista de buses<small>Lista</small>
                        </h2>
                        <ul class="header-dropdown m-r--5">
                            <li>
                                <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3">
                                  <a data-toggle="modal" data-target="#re_bus"><button type="button" class="btn bg-indigo waves-effect"><div class="demo-google-material-icon"> <i class="material-icons">create_new_folder</i> <span class="icon-name">Nuevo bus</span></div></button></a>
                                </div>
                            </li> 
                        </ul>
                    </div>
                    <div class="body" style="height:445px; overflow-y: scroll;">
                        <div class="row clearfix">
                        """)
if c>=1:
    conta=0
    for art in cursor:
        conta=conta+1
        i="check"
        ac="ACTIVO"
        if str(art[10])=="0": 
            ac="NO ACTIVO"
            i="close"
        cad=cad+str(
        """case '"""+str(art[2])+"""':
                id=document.getElementsByName('id"""+str(art[2])+"""')[0].value;
                as=document.getElementsByName('as"""+str(art[2])+"""')[0].value;
                fi=document.getElementsByName('fi"""+str(art[2])+"""')[0].value; 
                accion=document.getElementsByName('accion"""+str(art[2])+"""')[0].value;
                c=document.getElementsByName('c"""+str(art[2])+"""')[0].value;
                n_b=document.getElementsByName('nb"""+str(art[2])+"""')[0].value;

                datos=document.getElementsByName('datos"""+str(art[2])+"""')[0].value;
                mapeo=document.getElementsByName('mapeo"""+str(art[2])+"""')[0].value; 
                ico='"""+str(i)+"""';
                break;""")
        grafico=grafico+str(
        """case '"""+str(art[2])+"""':
                id=document.getElementsByName('id"""+str(art[2])+"""')[0].value;
                tipo=document.getElementsByName('tipo"""+str(art[2])+"""')[0].value;
                piso=document.getElementsByName('piso"""+str(art[2])+"""')[0].value;
                asientos=document.getElementsByName('asientos"""+str(art[2])+"""')[0].value;
                filas=document.getElementsByName('filas"""+str(art[2])+"""')[0].value;
                mapeo=document.getElementsByName('mapeo"""+str(art[2])+"""')[0].value;  
                break;""")        

        print("""           <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">
                                <div class="info-box" style="border-radius: 12px;">
                                    <i class="material-icons">directions_bus</i>
                                <center>

                                    <div class="content">
                                        <form>
                                        <input type="hidden" name='id"""+str(art[2])+"""' value='"""+str(art[0])+"""'>
                                        <input type="hidden" name='as"""+str(art[2])+"""' value='"""+str(art[7])+"""'>
                                        <input type="hidden" name='fi"""+str(art[2])+"""' value='"""+str(art[8])+"""'>
                                        <input type="hidden" name='c"""+str(art[2])+"""' value='"""+str(art[9])+"""'>
                                        <input type="hidden" name='nb"""+str(art[2])+"""' value='"""+str(conta)+"""'>
                                        <input type="hidden" name='mapeo"""+str(art[2])+"""' value='"""+str(art[13])+"""'>
                                        <input type="hidden" name='accion"""+str(art[2])+"""' value='"""+str(ac)+"""'>
                                        <input type="hidden" name='datos"""+str(art[2])+"""' value='"""+str(str(art[1])+"-"+str(art[3])+"-"+str(art[4])+"-"+str(art[5])+"-"+str(art[6])+"-"+str(art[7])+"-"+str(art[8]))+"""'>
                                        <a class="carrera" data-carrera="4" style="text-decoration: none;cursor: pointer;" onclick="capturar(this)" id='"""+str(art[2])+"""'>
                                            <div class="text">PLACA: """+str(art[2])+"""</div>
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
    

<div class="modal" id="re_bus" tabindex="-1" role="dialog" aria-labellebdy="myModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header header bg-indigo">
                <center><h5 class="modal-title">NUEVO BUS</h5></center>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times</span>
                </button>
            </div>
            <div class="modal-body">
             <form action="../mysqldb/registros/RegistroBus.py" method="POST" class="form-registro" accept-charset="UTF-8">     
                <div class="box-body">
                    <div class="row">
                        <div class="col-lg-6">
                            <label for="MARCA">MARCA:</label>
                            <input class="form-control" type="text" name="marca" required> 
                        </div>
                        <div class="col-lg-6">
                            <label for="PLACA">PLACA:</label>
                            <input class="form-control" type="text" name="placa" required>
                        </div>
                    </div>
                </div>
                <br>
                <div class="box-body">
                    <div class="row">
                        <div class="col-lg-6">
                            <label for="AÑO DE FABRICA">AÑO DE FABRICA:</label>
                            <input class="form-control" type="text" name="fabrica" required> 
                        </div>
                        <div class="col-lg-6">
                            <label for="CELULAR">TIPO DE BUS:</label>
                            <input class="form-control" type="text" name="tipo" required>
                        </div>
                    </div>
                </div>
                <br>

                <div class="box-body">
                    <div class="row">
                        <div class="col-lg-6">
                            <label for="num_pisos">ESTADO:</label>
                            <textarea name="estado" rows="3" class="form-control no-resize" required></textarea>
                        </div>
                        <div class="col-lg-6">
                            <label for="num_pisos">NUMERO DE PISOS:</label>
                            <select class="form-control" name="piso" id="entrada" onchange="capa();">
                                <option></option>
                                <option>1</option>
                                <option>2</option>
                                <option>3</option>
                                <option>4</option>
                            </select>
                        </div>
                    </div>
                </div>
                <div id="salida"></div>
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

<div class="modal" id="editBus" tabindex="-1" role="dialog" aria-labellebdy="myModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header header bg-indigo">
                <center><h5 class="modal-title">EDITAR OFICINA</h5></center>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times</span>
                </button>
            </div>
            <div class="modal-body">
             <form action="../mysqldb/actualizaciones/actualizarBus.py" method="POST" class="form-registro" accept-charset="UTF-8">     
                <input  id="codigo" name="codigo" type="hidden"></input>
                <div class="box-body">
                    <div class="row">
                        <div class="col-lg-6">
                            <label for="MARCA">MARCA:</label>
                            <input class="form-control" type="text" name="marca" id="marca" disabled> 
                        </div>
                        <div class="col-lg-6">
                            <label for="PLACA">PLACA:</label>
                            <input class="form-control" type="text" name="placa" id="placa" disabled>
                        </div>
                    </div>
                </div>
                <br>
                <div class="box-body">
                    <div class="row">
                        <div class="col-lg-6">
                            <label for="AÑO DE FABRICA">AÑO DE FABRICA:</label>
                            <input class="form-control" type="text" name="fabrica" id="ano_fabrica" disabled> 
                        </div>
                        <div class="col-lg-6">
                            <label for="CELULAR">TIPO DE BUS:</label>
                            <input class="form-control" type="text" name="tipo" id="tipo" disabled>
                        </div>
                    </div>
                </div>
                <br>


                <div class="box-body">
                    <div class="row">
                        <div class="col-lg-6">
                            <label for="AÑO DE FABRICA">Nª DE PISOS:</label>
                            <input class="form-control" type="text" name="piso" id="piso" disabled> 
                        </div>
                        <div class="col-lg-6">
                            <label for="CELULAR">CAPACIDAD:</label>
                            <input class="form-control" type="text" name="capacidad" id="capacidad" disabled>
                        </div>
                    </div>
                </div>
                <br>



                <div class="box-body">
                    <div class="row">
                        <div class="col-lg-6">
                            <label for="num_pisos">ESTADO:</label>
                            <textarea name="estado" rows="3" class="form-control no-resize" id="estado" required></textarea>
                        </div>
                    </div>
                </div>
                <br>
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



<div class='modal' id='mapeo1' tabindex='-1' role='dialog' aria-labellebdy='myModalLabel' aria-hidden='true'>
    <div class='modal-dialog' role='document'>
        <div class='modal-content'>
            
             <form action='../mysqldb/actualizaciones/mapeo.py' method='POST' class='form-registro' accept-charset='UTF-8'>     
            <div class='modal-header header bg-indigo'>
                <button type='button' class='close' data-dismiss='modal' aria-label='Close'>
                    <span aria-hidden="true">&times</span>
                </button>
            </div>
                <div id="panel_grafico"></div>
                     
            <div class='modal-footer'><button type="submit" class="btn bg-indigo waves-effect"><div class="demo-google-material-icon"> <i class="material-icons">edit</i> <span class="icon-name">GUARDAR</span></div></button></div>
            </form>
        </div>
    </div>
</div>
""")
fin_cabezera()

print("""


<script>       
    $('#editBus').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget)
    var recipient0 = button.data('codigo')
    var recipient1 = button.data('marca')
    var recipient2 = button.data('placa')
    var recipient3 = button.data('ano_fabrica')
    var recipient4 = button.data('tipo')
    var recipient5 = button.data('estado')
    var recipient6 = button.data('piso')
    var recipient7 = button.data('asientopiso')
    var recipient8 = button.data('filapiso')
    var recipient9 = button.data('capacidad')
    var modal = $(this)    
    modal.find('.modal-body #codigo').val(recipient0)
    modal.find('.modal-body #marca').val(recipient1)
    modal.find('.modal-body #placa').val(recipient2)
    modal.find('.modal-body #ano_fabrica').val(recipient3)
    modal.find('.modal-body #tipo').val(recipient4)
    modal.find('.modal-body #estado').val(recipient5)
    modal.find('.modal-body #piso').val(recipient6)
    modal.find('.modal-body #asientopiso').val(recipient7)
    modal.find('.modal-body #filapiso').val(recipient8)
    modal.find('.modal-body #capacidad').val(recipient9)
    });    
</script>

<script>
    function capturar(b)
    {           
        var id=""; 

        var n_b=""; 
        
        var as=""; 
        var fi=""; 
        var accion="";
        var ico="";
        var c="";

        var datos="";
        var mapeo="";
        switch(b.id){
        """+str(cad)+"""
        }
        
        var d=datos.split("-");
        var ss="";
        var divas=as.split("-");
        for(var i=0;i<divas.length;i++){
            ss=ss+"(Piso Nª"+(i+1)+"= "+divas[i]+") ";
        }

        document.getElementById("resultado").innerHTML="<div class='col-lg-12 col-md-12 col-sm-12 col-xs-12'><div class='card' ><div class='header'><h2>BUS<small id='oficina_name'>"+b.id+"</small></h2></div><div class='body'><div class='row clearfix'><div class='col-sm-12 table-responsive'>                                            <table width='100%' class='table table-bordered table-striped table-hover'><tbody><tr class='odd gradeX'><td><br>OPERACIONES</td><td  colspan='2'>                     <table width='100%' class='table table-striped table-hover'><tbody><tr class='odd gradeX'><td><center> <a href='../mysqldb/actualizaciones/actualizarestadoBus.py?id="+id+"' data-toggle='tooltip' data-placement='bottom' title='"+accion+"'><i class='material-icons'>"+ico+"</i></a></center></td><td><center><a style='padding-left: 15px;' data-placement='bottom' title='Editar bus' data-toggle='modal' data-target='#editBus' data-codigo='"+id+"' data-marca='"+d[0]+"' data-placa='"+b.id+"' data-ano_fabrica='"+d[1]+"' data-tipo='"+d[2]+"' data-estado='"+d[3]+"' data-piso='"+d[4]+"' data-capacidad='"+c+"' data-asientopiso='"+as+"' data-filapiso='"+fi+"'><i class='material-icons'>border_color</i></a></center></td><td><center><form><input type='hidden' name='id"+b.id+"' value='"+id+"'><input type='hidden' name='tipo"+b.id+"' value='"+d[2]+"'><input type='hidden' name='piso"+b.id+"' value='"+d[4]+"'><input type='hidden' name='asientos"+b.id+"' value='"+as+"'><input type='hidden' name='filas"+b.id+"' value='"+fi+"'><input type='hidden' name='mapeo"+b.id+"' value='"+mapeo+"'><a style='padding-left: 15px;' data-placement='bottom' title='configurar bus' onclick='graficar(this)' id='"+b.id+"' data-toggle='modal' data-target='#mapeo1'><i class='material-icons'>build</i></a></form></center></td></tr></tbody></table>                              </td><tr><tr class='odd gradeX'><td>N° DE BUS</td><td  colspan='2'><center>"+n_b+"</center></td></tr><tr class='odd gradeX'><td>MARCA</td><td colspan='2'><center>"+d[0]+"</center></td></tr><tr class='odd gradeX'><td>PLACA</td><td colspan='2'><center>"+b.id+"</center></td></tr><tr class='odd gradeX'><td>AÑO DE  FABRICA</td><td colspan='2'><center>"+d[1]+"</center></td></tr><tr class='odd gradeX'><td>TIPO DE BUS</td><td colspan='2'><center>"+d[2]+"</center></td></tr><tr class='odd gradeX'><td>Nª DE SISENTOS</td><td colspan='2'><center>"+ss+"</center></td></tr><tr class='odd gradeX'><td>CAPACIDAD</td><td colspan='2'><center>"+c+"</center></td></tr><tr class='odd gradeX'><td>ESTADO DEL BUS</td><td colspan='2'><center>"+d[3]+"</center></td></tr><tr class='odd gradeX'><td>ACCION</td><td colspan='2'><center>"+accion+"</center></td></tr></tbody></table></div></div></div></div></div>";
    }
</script>
<script>
    function graficar(b)
    {   
        var id=""; 
        var tipo="";  
        var piso=""; 
        var asientos="";
        var filas="";
        var mapeo="";
        switch(b.id){
        """+str(grafico)+"""
        }
        var a=asientos.split("-");
        var f=filas.split("-");
        var cad="";
        cad=cad+"<input type='hidden' name='id' value='"+id+"'><input type='hidden' name='piso' value='"+piso+"'><input type='hidden' name='a1' value='"+asientos+"'><input type='hidden' name='f1' value='"+filas+"'>";
        var dedo=0;
        if(mapeo=="None"){
            cad=cad+"<div class='box-body bg-indigo'><div class='row'><div class='form-group'><div class='form-group'><center><h4>PLACA: "+b.id+" <br>TIPO DE BUS: "+tipo+"</h4></center></div></div></div></div><br><br>";
            cad=cad+"<center><div class='box-body'><div class='row'>";           
            for(var k=0;k<piso;k++){       
                switch(piso){
                    case '1':cad=cad+"<div class='form-group'>";
                    break;
                    case '2':cad=cad+"<div class='col-sm-6'><div class='form-group'>";
                    break;
                    case '3':cad=cad+"<div class='col-sm-4'><div class='form-group'>";
                    break;
                    case '4':cad=cad+"<div class='col-sm-3'><div class='form-group'>";
                    break;
                }
                if(k==0){
                    if(piso!=1){
                        cad=cad+"<center style='color:blue'><p>PRIMER PISO</p></center>";
                    }
                    cad=cad+"<table id='inner' style='margin: 5px;' ><tr><td height='150' style='background: url(../public/images/c.png) no-repeat center center; background-size:100% 100%;'></td></tr><tr><td width='100%' style='background: url(../public/images/t.png) no-repeat center center;background-size:100% 100%;'><center><table style='margin: 15px;'>";
                }
                else{
                if(piso==2){
                        cad=cad+"<center style='color:blue'><p>SEGUNDO PISO</p></center>";
                    }
                    else{
                        if(piso==3){
                            cad=cad+"<center style='color:blue'><p>TERCER PISO</p></center>";
                        }
                    }
                    cad=cad+"<td width='50%'><table style='margin: 5px;'><tr><td width='100%' style='background: url(../public/images/todo.png) no-repeat center center;background-size:100% 100%;'><center><table style='margin: 15px;'>";
                }
                
                for(var i=0;i<((a[k]/f[k])+3);i++){
                    cad=cad+"<tr>";
                    for(var j=0;j<f[k]*2;j++){
                        cad=cad+"<td><input type='text' value='X' name='ij"+dedo+""+j+"' style='background-color:transparent;border:1;border-bottom: 1px solid #9e9e9e;outline: none;width:30px;text-align:center;color: red;'><br></td>";
                    }
                    dedo++;
                    cad=cad+"</tr>";
                }
                cad=cad+"</table></td></tr></table>";
                switch(piso){
                    case '1':cad=cad+"</div>";
                    break;
                    case '2':cad=cad+"</div></div>";
                    break;
                    case '3':cad=cad+"</div></div>";
                    break;
                    case '4':cad=cad+"</div></div>";
                    break;
                }
            }
            cad=cad+"</div></div></center>";
        }
        else{
            
            cad=cad+"<input type='hidden' name='posi' value='si'><div class='box-body bg-indigo'><div class='row'><div class='form-group'><div class='form-group'><center><h4>PLACA: "+b.id+" <br>TIPO DE BUS: "+tipo+"</h4></center></div></div></div></div><br><div class='modal-footer'><a href='../mysqldb/actualizaciones/e_mapeo.py?id="+id+"'><button type='button' class='btn btn-danger'><div class='demo-google-material-icon'> <i class='material-icons'>delete</i> <span class='icon-name'></span></div></button></a></div><br>";
            var cortar=mapeo.split("&");            
            
            cad=cad+"<center><div class='box-body'><div class='row' style='margin: 3px;'>";
            var ccont=0;
            for(var k=0;k<piso;k++){
                switch(piso){
                    case '1':cad=cad+"<div class='form-group'>";
                    break;
                    case '2':cad=cad+"<div class='col-sm-6'><div class='form-group'>";
                    break;
                    case '3':cad=cad+"<div class='col-sm-4'><div class='form-group'>";
                    break;
                    case '4':cad=cad+"<div class='col-sm-3'><div class='form-group'>";
                    break;
                }

                var a=cortar[k];
                if (a.substring(0,1)=="-"){
                    a=a.substring(1,a.length);
                }
                if (a.substring(a.length-1,a.length)=="-"){
                    a=a.substring(0,a.length-1);
                }
                var fil=a.split("-");
                var pp=0;
                var p=0;
                for(var i=0;i<fil.length;i++){
                    if(p==1*f[k]+1){
                        break;
                    }
                    if(fil[i]=="1" || fil[i]=="2"|| fil[i]=="3"  || fil[i]=="4"  || fil[i]=="5"  || fil[i]=="6"  || fil[i]=="7"  || fil[i]=="8"  || fil[i]=="9"  || fil[i]=="10"||
                    fil[i]=="11" || fil[i]=="12" || fil[i]=="13" || fil[i]=="14" || fil[i]=="15" || fil[i]=="16" || fil[i]=="17" || fil[i]=="18" || fil[i]=="19" || fil[i]=="20"||
                    fil[i]=="21" || fil[i]=="22" || fil[i]=="23" || fil[i]=="24" || fil[i]=="25" || fil[i]=="26" || fil[i]=="27" || fil[i]=="28" || fil[i]=="29" || fil[i]=="30"||
                    fil[i]=="31" || fil[i]=="32" || fil[i]=="33" || fil[i]=="34" || fil[i]=="35" || fil[i]=="36" || fil[i]=="37" || fil[i]=="38" || fil[i]=="39" || fil[i]=="40"||
                    fil[i]=="41" || fil[i]=="42" || fil[i]=="43" || fil[i]=="44" || fil[i]=="45" || fil[i]=="46" || fil[i]=="47" || fil[i]=="48" || fil[i]=="49" || fil[i]=="50"||
                    fil[i]=="51" || fil[i]=="52" || fil[i]=="53" || fil[i]=="54" || fil[i]=="55" || fil[i]=="56" || fil[i]=="57" || fil[i]=="58" || fil[i]=="59" || fil[i]=="60"||
                    fil[i]=="61" || fil[i]=="62" || fil[i]=="63" || fil[i]=="64" || fil[i]=="65" || fil[i]=="66" || fil[i]=="67" || fil[i]=="68" || fil[i]=="69" || fil[i]=="70"||
                    fil[i]=="71" || fil[i]=="72" || fil[i]=="73" || fil[i]=="74" || fil[i]=="75" || fil[i]=="76" || fil[i]=="77" || fil[i]=="78" || fil[i]=="79" || fil[i]=="80"||
                    fil[i]=="81" || fil[i]=="82" || fil[i]=="83" || fil[i]=="84" || fil[i]=="85" || fil[i]=="86" || fil[i]=="87" || fil[i]=="88" || fil[i]=="89" || fil[i]=="90"||
                    fil[i]=="91" || fil[i]=="92" || fil[i]=="93" || fil[i]=="94" || fil[i]=="95" || fil[i]=="96" || fil[i]=="97" || fil[i]=="98" || fil[i]=="99" || fil[i]=="100" ||

                    fil[i]=="1Z"  || fil[i]=="2Z"  || fil[i]=="3Z"  || fil[i]=="4Z"  || fil[i]=="5Z"  || fil[i]=="6Z"  || fil[i]=="7Z"  || fil[i]=="8Z"  || fil[i]=="9Z"  || fil[i]=="10Z"||
                    fil[i]=="11Z" || fil[i]=="12Z" || fil[i]=="13Z" || fil[i]=="14Z" || fil[i]=="15Z" || fil[i]=="16Z" || fil[i]=="17Z" || fil[i]=="18Z" || fil[i]=="19Z" || fil[i]=="20Z"||
                    fil[i]=="21Z" || fil[i]=="22Z" || fil[i]=="23Z" || fil[i]=="24Z" || fil[i]=="25Z" || fil[i]=="26Z" || fil[i]=="27Z" || fil[i]=="28Z" || fil[i]=="29Z" || fil[i]=="30Z"||
                    fil[i]=="31Z" || fil[i]=="32Z" || fil[i]=="33Z" || fil[i]=="34Z" || fil[i]=="35Z" || fil[i]=="36Z" || fil[i]=="37Z" || fil[i]=="38Z" || fil[i]=="39Z" || fil[i]=="40Z"||
                    fil[i]=="41Z" || fil[i]=="42Z" || fil[i]=="43Z" || fil[i]=="44Z" || fil[i]=="45Z" || fil[i]=="46Z" || fil[i]=="47Z" || fil[i]=="48Z" || fil[i]=="49Z" || fil[i]=="50Z"||
                    fil[i]=="51Z" || fil[i]=="52Z" || fil[i]=="53Z" || fil[i]=="54Z" || fil[i]=="55Z" || fil[i]=="56Z" || fil[i]=="57Z" || fil[i]=="58Z" || fil[i]=="59Z" || fil[i]=="60Z"||
                    fil[i]=="61Z" || fil[i]=="62Z" || fil[i]=="63Z" || fil[i]=="64Z" || fil[i]=="65Z" || fil[i]=="66Z" || fil[i]=="67Z" || fil[i]=="68Z" || fil[i]=="69Z" || fil[i]=="70Z"||
                    fil[i]=="71Z" || fil[i]=="72Z" || fil[i]=="73Z" || fil[i]=="74Z" || fil[i]=="75Z" || fil[i]=="76Z" || fil[i]=="77Z" || fil[i]=="78Z" || fil[i]=="79Z" || fil[i]=="80Z"||
                    fil[i]=="81Z" || fil[i]=="82Z" || fil[i]=="83Z" || fil[i]=="84Z" || fil[i]=="85Z" || fil[i]=="86Z" || fil[i]=="87Z" || fil[i]=="88Z" || fil[i]=="89Z" || fil[i]=="90Z"||
                    fil[i]=="91Z" || fil[i]=="92Z" || fil[i]=="93Z" || fil[i]=="94Z" || fil[i]=="95Z" || fil[i]=="96Z" || fil[i]=="97Z" || fil[i]=="98Z" || fil[i]=="99Z" || fil[i]=="100Z")
                    {
                        p=p+1;
                    }
                pp=pp+1;
                }
                pp=pp-1;
                var ff=fil.length/pp;
                if((fil.length/pp)!=parseInt(fil.length/pp,10)){
                    ff=parseInt(fil.length/pp,10)+1;
                }
                if(k==0){
                    if(piso!=1){
                        cad=cad+"<center style='color:blue'><p>PRIMER PISO</p></center>";
                    }
                    cad=cad+"<table id='inner' style='margin: 5px;' ><tr><td height='150' style='background: url(../public/images/c.png) no-repeat center center; background-size:100% 100%;'></td></tr><tr><td width='100%' style='background: url(../public/images/t.png) no-repeat center center;background-size:100% 100%;'><center><table style='margin: 15px;'>";
                }
                else{
                    if(piso==2){
                        cad=cad+"<center style='color:blue'><p>SEGUNDO PISO</p></center>";
                    }
                    else{
                        if(piso==3){
                            cad=cad+"<center style='color:blue'><p>TERCER PISO</p></center>";
                        }
                    }
                    cad=cad+"<td width='50%'><table style='margin: 5px;'><tr><td width='100%' style='background: url(../public/images/todo.png) no-repeat center center;background-size:100% 100%;'><center><table style='margin: 15px;'>";
                }
                var cont=0;
                for(var i=0;i<ff;i++){
                    cad=cad+"<tr>";
                    for(var j=0;j<pp;j++){
                        if(cont<fil.length){
                            switch(fil[cont]){
                                case 'TV':cad=cad+"<td><table style='margin: 3px;'><tr><td><input type='hidden' name='fc"+ccont+"' value='TV'> <img src='../public/images/tv.png' width='45' height='45'></td></tr></table></td>";
                                break;
                                case 'V':cad=cad+"<td><table style='margin: 3px;'><tr><td><input type='hidden' name='fc"+ccont+"' value='V'><img src='../public/images/v.png' width='45' height='45'></td></tr></table></td>";
                                break;
                                case 'ES':
                                case 'E':
                                    if (fil[cont+1]=="ES" || fil[cont+1]=="E"){
                                        cad=cad+"<td colspan='2'><table style='margin: 3px;'><tr><td><input type='hidden' name='fc"+ccont+"' value='ES'><input type='hidden' name='fc"+(ccont+1)+"' value='ES'><img src='../public/images/es.png' width='93' height='45'></td></td></tr></table>";
                                        ccont=ccont+1;
                                        cont=cont+1;
                                        j=j+1;
                                    }
                                    else{
                                        cad=cad+"<td><table style='margin: 3px;'><tr><td><input type='hidden' name='fc"+ccont+"' value='ES'><img src='../public/images/es.png' width='45' height='45'></td></td></tr></table>";
                                    }
                                    
                                break;
                                case 'BA':
                                case 'B':
                                    if(fil[cont+1]=="BA" || fil[cont+1]=="B"){
                                        cad=cad+"<td colspan='2'><table style='margin: 3px;'><tr><td><input type='hidden' name='fc"+ccont+"' value='BA'><input type='hidden' name='fc"+(ccont+1)+"' value='BA'><center style='color:blue'><p>Baño</p></center><img src='../public/images/ba.png' width='90' height='65'></td></tr></table></td>";
                                        cont=cont+1;
                                        ccont=ccont+1;
                                        j=j+1;
                                    }
                                    else{
                                        cad=cad+"<td><table style='margin: 3px;'><tr><td><input type='hidden' name='fc"+ccont+"' value='BA'><center style='color:blue'><p>Baño</p></center><img src='../public/images/ba.png' width='45' height='45'></td></tr></table></td>";
                                    }                                
                                break;
                                default:
                                    var pru=fil[cont];
                                    if(pru.substring(pru.length-1,pru.length)=="Z"){
                                        cad=cad+"<td><table style='margin: 3px;'><tr><td><center><select name='fc"+ccont+"' style='color:blue;'><option value='"+pru.substring(0,pru.length-1)+"Z'>X</option><option value='"+pru.substring(0,pru.length-1)+"'>"+pru.substring(0,pru.length-1)+"</option></center></select><br><img src='../public/images/s2.png' width='45' height='45'></td></tr></table></td>";
                                    }
                                    else{
                                        cad=cad+"<td><table style='margin: 3px;'><tr><td><center><select name='fc"+ccont+"' style='color:blue;'><option value='"+fil[cont]+"'>"+fil[cont]+"</option><option value='"+fil[cont]+"Z'>X</option></center></select><br><img src='../public/images/s4.png' width='45' height='45'></td></tr></table></td>";
                                    }                                
                                break;
                            }                            
                        ccont=ccont+1;
                        }
                        else{
                            cad=cad+"<td><table style='margin: 3px;'><tr><td><img src='../public/images/v.png' width='45' height='45'></td></tr></table></td>";
                        }
                        cont=cont+1;
                        
                    }
                    cad=cad+"</tr>";
                }


                cad=cad+"<input type='hidden' name='fc"+ccont+"' value='&'></table></td></tr></table>";

                ccont=ccont+1;


                switch(piso){
                    case '1':cad=cad+"</div>";
                    break;
                    case '2':cad=cad+"</div></div>";
                    break;
                    case '3':cad=cad+"</div></div>";
                    break;
                    case '4':cad=cad+"</div></div>";
                    break;
                }
            }
            cad=cad+"<input type='hidden' name='contador' value='"+ccont+"'></div></div></center>";          
        }  
        document.getElementById("panel_grafico").innerHTML=cad+"<br>";
    }
</script>
""")