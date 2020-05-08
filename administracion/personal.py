#!C:\Python34\python 
import pymysql 
import sys
sys.path.append("..")
from layout .principal import *
cabezera()

con=pymysql.connect(user="root",password="",host="",database="buses_chavarria")
cursor=con.cursor()
c=cursor.execute("select * from personal")

bus=con.cursor()
bus.execute("select * from bus")

oficina=con.cursor()
oficina.execute("select * from oficina")

cadena_bus="";
for art in bus:
    cadena_bus=cadena_bus+"<option value="+str(art[0])+">"+str(art[2])+"</option>"

cadena_oficina="";
for art in oficina:
    cadena_oficina=cadena_oficina+"<option value="+str(art[0])+">"+str(art[1])+"</option>"    

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
                <i class="material-icons">link</i> Personal
            </li>
        </ol>
        <div class="row clearfix">
            <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">
                <div class="card">
                    <div class="header">
                        <h2>
                            Lista de personal<small>Lista</small>
                        </h2>
                        <ul class="header-dropdown m-r--5">
                            <li>
                                <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3">
                                  <a data-toggle="modal" data-target="#re_personal"><button type="button" class="btn bg-indigo waves-effect"><div class="demo-google-material-icon"> <i class="material-icons">person_add</i> <span class="icon-name">Nuevo personal</span></div></button></a>
                                </div>
                            </li> 
                        </ul>
                    </div>
                    <div class="body" style="height:445px; overflow-y: scroll;">
                        <div class="row clearfix">
                        """)
if c>=1:
    print(""""              <div class='col-sm-12 table-responsive'>
                                <table width='100%'' class='table table-bordered table-striped table-hover dataTable js-basic-example' >
                                    <thead>
                                        <tr>
                                            <th><center>Nombre</center></th>
                                            <th><center>Apellidos</center></th>
                                            <th><center>ACCION</center></th>
                                        </tr>
                                    </thead>
                                    <tbody>""")

    for art in cursor:
        i="check"
        ac="ACTIVO"
        if str(art[10])=="0": 
            ac="NO ACTIVO"
            i="close"
        cad=cad+str(
        """case '"""+str(art[0])+"""':
                nombre=document.getElementsByName('nombre"""+str(art[0])+"""')[0].value;
                apellidos=document.getElementsByName('apellidos"""+str(art[0])+"""')[0].value;
                datos=document.getElementsByName('datos"""+str(art[0])+"""')[0].value;
                accion=document.getElementsByName('accion"""+str(art[0])+"""')[0].value;  
                ico='"""+str(i)+"""';
                break;""")

        print("""                       <tr class='odd gradeX'>
                                        <form>
                                            <input type="hidden" name='nombre"""+str(art[0])+"""' value='"""+str(art[1])+"""'>
                                            <input type="hidden" name='apellidos"""+str(art[0])+"""' value='"""+str(art[2])+"""'>
                                            <input type="hidden" name='datos"""+str(art[0])+"""' value='"""+str(art[1])+"-"+str(art[2])+"-"+str(art[3])+"-"+str(art[4])+"-"+str(art[5])+"-"+str(art[6])+"-"+str(art[7])+"-"+str(art[8])+"-"+str(art[9])+"""'>
                                            <input type="hidden" name='accion"""+str(art[0])+"""' value='"""+str(ac)+"""'>
                                            <td><center>"""+str(art[1])+"""</center></td>
                                            <td><center>"""+str(art[2])+"""</center></td>
                                            <td>
                                                <center>
                                                <a class="carrera" data-carrera="4" style="text-decoration: none;cursor: pointer;" onclick="capturar(this)" id='"""+str(art[0])+"""'>    
                                                    <i class="material-icons">visibility</i>
                                                </a>
                                                </center>
                                            </td>
                                        </form>
                                        </tr>""")
    print("""
                                    </tbody>
                                </table>
                            </div>""")
else:
    print("""
        <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">
                AUN NO HAY PESONAL REGISTRADO
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
                            Personal
                        </h2>
                        <ul class="header-dropdown m-r--5">
                            <li>     
                                <i class="material-icons">person</i>
                            </li>  
                        </ul>
                    </div>
                    <div class="body">
                        <div class="row clearfix" style="height:425px;overflow-y: scroll;">
                        
                            <div id="resultado">     
                                <div class="col-lg-12 ajax-content">
                                    <center><h3 style="padding-top: 170px;">Seleccione un personal</h3></center>
                                </div>
                            </div>   

                        </div>
                    </div>
                </div>
            </div>
        </div>    
    </div>
</section>
    

<div class="modal" id="re_personal" tabindex="-1" role="dialog" aria-labellebdy="myModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header header bg-indigo">
                <center><h5 class="modal-title">NUEVO PERSONAL</h5></center>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times</span>
                </button>
            </div>
            <div class="modal-body">
             <form action="../mysqldb/registros/RegistroPersonal.py" method="POST" class="form-registro" accept-charset="UTF-8">     
                <div class="box-body">
                    <div class="row">
                        <div class="col-lg-6">
                            <label for="NOMBRE">NOMBRE:</label>
                            <input class="form-control" type="text" name="nombre" required> 
                        </div>
                        <div class="col-lg-6">
                            <label for="APELLIDOS">APELLIDOS:</label>
                            <input class="form-control" type="text" name="apellidos" required>
                        </div>
                    </div>
                </div>
                <br>
                <div class="box-body">
                    <div class="row">
                        <div class="col-lg-6">
                            <label for="CI">CI:</label>
                            <input class="form-control" type="text" name="ci" required> 
                        </div>
                        <div class="col-lg-6">
                            <label for="TELEFONO">TELEFONO:</label>
                            <input class="form-control" type="text" name="telefono" required>
                        </div>
                    </div>
                </div>
                <br>
                <div class="box-body">
                    <div class="row">
                        <div class="col-lg-6">
                            <label for="CIUDAD">CIUDAD:</label>
                            <select id="c_input" name="ciudad" class="form-control" onchange="c_random();">
                                <option></option>
                                <option>ALTO LA PAZ</option>
                                <option>BENI</option>
                                <option>CHUQUISACA</option>
                                <option>COCHABAMBA</option>
                                <option>LA PAZ</option>
                                <option>ORURO</option>
                                <option>PANDO</option>
                                <option>POTOSÍ</option>
                                <option>SANTA CRUZ</option>
                                <option>TARIJA</option>
                            </select>
                        </div>
                        <div class="col-lg-6">
                            <label for="PROVINCIA">PROVINCIA:</label>
                            <div id="provincia_m">
                                <div id="c_output">
                                    <select class="form-control">
                                        <option>  </option>
                                        <option>SELECCIONE CIUDAD</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <br>
                <div class="box-body">
                    <div class="row">
                        <div class="col-lg-6">
                            <label for="LOCALIDAD">LOCALIDAD:</label>
                            <input class="form-control" type="text" name="localidad" required> 
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
                            <label for="Tipo">TIPO PERSONAL:</label>
                            <select class="form-control" name="tipo" id="input" onchange="random();">
                                <option></option>
                                <option>SOCIO</option>
                                <option>ADMINISTRADOR DE OFICINA</option>
                                <option>PESONAL DE BUS</option>
                            </select> 
                        </div>
                    </div>
                </div>
                <br>
                <div id="output"></div>
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
    function random(){
        var a=document.getElementById('input').value;
        var string="";
        if(a==="PESONAL DE BUS"){
          string=string+'<div class="box-body"><div class="row"><div class="col-lg-6"><label for="usuario">LICENCIA:</label><input class="form-control" name="n1" type="text" required></input></div></div></div>';
        }
        else if(a==="SOCIO"){
          string=string+'<div class="box-body"><div class="row"><div class="col-lg-6"><label for="bus">BUS:</label><select class="form-control" multiple="multiple" name="n2" required>"""+str(cadena_bus)+"""</select></div><div class="col-lg-6"><label for="usuario">LICENCIA:</label><input class="form-control" name="n1" type="text"></input></div></div></div>';
                                        
        }
        else if(a==="ADMINISTRADOR DE OFICINA"){
          string=string+'<div class="box-body"><div class="row"><div class="col-lg-6"><label for="usuario">OFICINA :</label><select class="form-control" name="n1" required><option></option>"""+cadena_oficina+"""</select></input></div></div></div>';
        }
        document.getElementById('output').innerHTML=string;
    }
</script>

<script>
    function c_random(){
        var a=document.getElementById('c_input').value;
        if(a==="ALTO LA PAZ"){
            var array=['ALTO LA PAZ'];
        }
        else if(a==="BENI"){
            var array=['CERCADO','ITÉNEZ','GENERAL JOSÉ BALLIVIÁN','SEGUROLA','MAMORÉ','MARBÁN','MOXOS','VACA DÍEZ','YACUMA'];
        }
        else if(a==="CHUQUISACA"){
            var array=["BELISARIO BOETO","HERNANDO SILES","JAIME ZUDÁÑEZ","JUANA AZURDUY DE PADILLA","LUIS CALVO","NOR CINTI","OROPEZA","SUD CINTI","TOMINA","YAMPARÁEZ"];
        }
        else if(a==="COCHABAMBA"){
            var array=["ARANI","ARQUE","AYOPAYA","BOLÍVAR","CAPINOTA","JOSÉ CARRASCO","CERCADO","CHAPARE","ESTEBAN ARZE","GERMÁN JORDÁN","MIZQUE","CAMPERO","PUNATA","QUILLACOLLO","TAPACARÍ","TIRAQUE"];
        }
        else if(a==="LA PAZ"){
            var array=["ABEL ITURRALDE","AROMA","BAUTISTA SAAVEDRA","CARANAVI","ELIODORO CAMACHO","FRANZ TAMAYO","GUALBERTO VILLARROEL","INGAVÍ","INQUISIVI","GENERAL JOSÉ MANUEL PANDO","JOSÉ RAMÓN LOAYZA","LARECAJA","LOS ANDES","MANCO KAPAC","MUÑECAS","NOR YUNGAS","OMASUYOS","PACAJES","PEDRO DOMINGO MURILLO","SUD YUNGAS"];
        }
        else if(a==="ORURO"){
            var array=["SABAYA","CARANGAS","CERCADO","EDUARDO AVAROA","LADISLAO CABRERA","LITORAL DE ATACAMA","NOR CARANGAS","PANTALEÓN DALENCE","POOPÓ","MEJILLONES","SAJAMA","SAN PEDRO DE TOTORA","SAUCARÍ","SEBASTIÁN PAGADOR","SUD CARANGAS","TOMÁS BARRÓN"];
        }
        else if(a==="PANDO"){
            var array=["ABUNÁ","GENERAL FEDERICO ROMÁN","MADRE DE DIOS","MANURIPI","NICOLÁS SUÁREZ"];
        }
        else if(a==="POTOSÍ"){
            var array=["ALONSO DE IBÁÑEZ","ANTONIO QUIJARRO","BERNARDINO BILBAO","CHARCAS","CHAYANTA","CORNELIO SAAVEDRA","DANIEL CAMPOS","ENRIQUE BALDIVIESO","JOSÉ MARÍA LINARES","MODESTO OMISTE","NOR CHICHAS","NOR LÍPEZ","RAFAEL BUSTILLO","SUD CHICHAS","SUD LÍPEZ","TOMÁS FRÍAS"];
        }
        else if(a==="SANTA CRUZ"){
            var array=["ANDRÉS IBÁÑEZ","ÁNGEL SANDÓVAL","CHIQUITOS","CORDILLERA","FLORIDA","GERMÁN BUSCH","GUARAYOS","ICHILO","WARNES","VELASCO","CABALLERO","ÑUFLO DE CHAVES","OBISPO SANTISTEVAN","SARA","VALLEGRANDE"];
        }
        else if(a==="TARIJA"){
            var array=["ANICETO ARCE","BURDET O'CONNOR","CERCADO (TARIJA)","EUSTAQUIO MÉNDEZ","GRAN CHACO"];
        }
        else{
            var array=['SELECCIONE CIUDAD'];
        }
        var string="<option></option>";

        for(var i=0;i<array.length;i++){
            string=string+"<option>"+array[i]+"</option>";
        }
        string="<select name='provincia' class='form-control'>"+string+"</select>";
        document.getElementById('c_output').innerHTML=string;
    }
</script> 

<script>
    function capturar(b)
    {
        var nombre=""; 
        var apellidos="";
        var datos="";
        var accion="";
        var ico="";
        switch(b.id){
        """+str(cad)+"""
        }
        var d=datos.split("-");
        document.getElementById("resultado").innerHTML="<div class='col-lg-12 col-md-12 col-sm-12 col-xs-12'><div class='card' ><div class='header'><h2>"+nombre+"<small id='oficina_name'>"+apellidos+"</small></h2></div><div class='body'><div class='row clearfix'><div class='col-sm-12 table-responsive'><center><img src='../public/images/u.png' width='100' height='100' alt='User' /></center><table width='100%' class='table table-bordered table-striped table-hover'><thead><tr><th WIDTH='30'><center>TIPO DE PERSONAL</center></th><th><center>ESTADO</center></th><th><center>ACCION</center></th></tr></thead><tbody><tr class='odd gradeX'><td><center>"+d[8]+"</center></td><td><center>"+accion+"</center></td><td><center><a href='../mysqldb/actualizaciones/actualizarestadoPersonal.py?id="+b.id+"' data-toggle='tooltip' data-placement='bottom' title='PERSONAL "+accion+"'><i class='material-icons'>"+ico+"</i></a><a href='configurarpersonal.py?id="+b.id+"' data-toggle='tooltip' data-placement='bottom' style='padding-left: 15px;' title='CONFIGURAR PERSONAL'><i class='material-icons'>settings</i></a></center></td></tr></tbody></table></div></div></div></div></div>";
    }
</script>
""")