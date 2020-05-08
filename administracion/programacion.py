#!C:\Python34\python 
import cgi
import pymysql 
import sys
sys.path.append("..")
from layout .principal import *
cabezera()

con=pymysql.connect(user="root",password="",host="",database="buses_chavarria")

form = cgi.FieldStorage()
codigo=form.getvalue('id')




############OFICINA#############
oficina=con.cursor()
oficina.execute("""select ru_fr.cod,of1.nombre,of2.nombre,fre.fecuencia,ru.accion FROM ruta_frecuencia ru_fr 
                  inner join ruta ru on ru_fr.cod_ruta=ru.cod
                  inner join frecuencia fre on ru_fr.cod_frecuencia=fre.cod
                  inner join oficina of1 on ru.oficina_origen=of1.cod
                  inner join oficina of2 on ru.oficina_destino=of2.cod
                    """)
of=""

co=""
ini=""
fin=""
fre=""

a=[]
for art in oficina:
    if str(art[4])=="1":
        a.append(str(art[1]))
        co=co+str(art[0])+"/"
        ini=ini+str(art[1])+"/"
        fin=fin+str(art[2])+"/"
        fre=fre+str(art[3])+"/"

co=co[0:len(co)-1]
ini=ini[0:len(ini)-1]
fin=fin[0:len(fin)-1]
fre=fre[0:len(fre)-1]

b=list(set(a))
for i in b:
    of=of+"<option>"+str(i)+"</option>"




##############CHOFER#########
chofer=con.cursor()
chofer.execute("""select p_b.cod,p.nombre,p.apellidos,p.accion from personal_bus p_b 
                  inner join personal p on p_b.cod_personal=p.cod""")
choferaux=con.cursor()
choferaux.execute("""select p_b.cod,p.nombre,p.apellidos,p.accion from personal_bus p_b 
                  inner join personal p on p_b.cod_personal=p.cod""")

cho="<option></option>"
cho1="<option></option>"
for l in chofer:
    if str(l[3])=="1":
        cho=cho+("""<option value="""+str(l[0])+""">"""+str(l[1])+" "+str(l[2])+"""</option>""")

for l1 in choferaux:
    if str(l1[3])=="1":
        cho1=cho1+("""<option value="""+str(l1[0])+""">"""+str(l1[1])+" "+str(l1[2])+"""</option>""")


##############################
#########################BUSS###################

codi=""
pla=""
pis=""

bu=con.cursor()
bu.execute("select cod,placa,accion,piso from bus WHERE mapeo <>'None'")
bus="<option></option>"
for l in bu:
    if str(l[2])=="1":
        bus=bus+("""<option>"""+str(l[1])+"""</option>""")
        codi=codi+str(l[0])+"/"
        pla=pla+str(l[1])+"/"
        pis=pis+str(l[3])+"/"


################################################


ruta=con.cursor()
ru=ruta.execute("""select pr.cod,pr.frecha_viaje,f.fecuencia,b.tipo,b.placa,of1.nombre,of2.nombre,pr.pasajes,pr.accion FROM programar_venta pr
              inner join bus b on pr.cod_bus=b.cod
              inner join ruta_frecuencia rf on pr.cod_ruta_frecuencia=rf.cod
              inner join frecuencia f on rf.cod_frecuencia=f.cod
              inner join ruta ru on rf.cod_ruta=ru.cod
              inner join oficina of1 on ru.oficina_origen=of1.cod
              inner join oficina of2 on ru.oficina_destino=of2.cod
                    """)

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
                <i class="material-icons">link</i> Rutas
            </li>
        </ol>
        <div class="row clearfix">
            <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                <div class="card">
                    <div class="header">
                    <br>
                        <ul class="header-dropdown m-r--5">
                            <li>
                                <div class="col-xs-3 col-sm-3 col-md-3 col-lg-3">
                                  <a data-toggle="modal" data-target="#re_ruta"><button type="button" class="btn bg-indigo waves-effect"><div class="demo-google-material-icon"> <i class="material-icons">note_add</i> <span class="icon-name">Programacion</span></div></button></a>
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
                                            <th><h5 align="center">N°</h5></th>
                                            <th><h5 align="center">FECHA VIAJE</h5></th>
                                            <th><h5 align="center">HORA</h5></th>
                                            <th><h5 align="center">SERVICIO</h5></th>
                                            <th><h5 align="center">PLACA</h5></th>
                                            <th><h5 align="center">ORIGEN</h5></th>
                                            <th><h5 align="center">DESTIONO</h5></th>
                                            <th><h5 align="center">PASAJE</h5></th>
                                            <th><h5 align="center">ACCION</h5></th>
                                        </tr>
                                    </thead>
                                    <tbody>""")
    i=0
    for art in ruta:
        ii="check"
        ac="ACTIVO"
        if str(art[8])=="0": 
            ac="NO ACTIVO"
            ii="close"

        i=i+1
        print("""                       <tr>
                                            <td><center>"""+str(i)+"""</center></td>
                                            <td><center>"""+str(art[1])+"""</center></td>
                                            <td><center>"""+str(art[2])+"""</center></td>
                                            <td><center>"""+str(art[3])+"""</center></td>
                                            <td><center>"""+str(art[4])+"""</center></td>
                                            <td><center>"""+str(art[5])+"""</center></td>
                                            <td><center>"""+str(art[6])+"""</center></td>
                                            <td><center>"""+str(art[7])+"""</center></td>
                                            <td><center><div class="btn-group">
                                    <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                        OPERACIONES <span class="caret"></span>
                                    </button>
                                    <ul class="dropdown-menu">
                                        <li><a style='padding-left: 15px;' data-toggle="modal" data-target="#venta" style='padding-left: 15px;' data-toggle='tooltip' data-placement='bottom' onclick="capturar1(this)" id='"""+str(art[0])+"""' title='VISUALIZAR VENTA'><i class='material-icons'>visibility</i></a></li>
                                        <li><a data-toggle="modal" data-target="#myModal" style='padding-left: 15px;' data-toggle='tooltip' data-placement='bottom' title='IMPRIMIR LISTA' onclick="capturar(this)" id='"""+str(art[0])+"""'><i class='material-icons'>print</i></a></li>
                                        <li><a data-toggle="modal" style='padding-left: 15px;' data-target="#venta_reserva" data-toggle='tooltip' data-placement='bottom' title='REPORTE VENTA' onclick="capturar2(this)" id='"""+str(art[0])+"""'><i class='material-icons'>content_paste</i></a></li>
                                        <li><a href='../mysqldb/actualizaciones/actualizarestadoPrograma.py?id="""+str(art[0])+"""' data-toggle='tooltip' data-placement='bottom' title='"""+ac+"""'><i class='material-icons'>"""+ii+"""</i></a></li>
                                    </ul>
                                </div>
                                </center></td>
                                        </tr>""")                                          
    print("""                       </tbody>
                                </table>
                        </div>""")
else:
    print("AUN NO HAY RUTAS REGISTRADAS")
print("""

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
                <center><h5 class="modal-title">PROGRAMAR VENTA PASAJE</h5></center>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times</span>
                </button>
            </div>
            <div class="modal-body">
             <form action="../mysqldb/registros/RegistrarProgramacion.py" method="POST" class="form-registro" accept-charset="UTF-8">     
                <br>
                <div class="box-body">
                    <div class="row">
                        <div class="col-sm-12">
                        <div class="col-sm-4">
                            <label>RUTA INICIO:</label>
                            <select id="c_input" name="ini" class="form-control" onchange="c_random();" required>
                                <option></option>
                                """+str(of)+"""
                            </select>       
                        </div>
                        <div class="col-sm-4">
                            <label>RUTA DESTINO:</label>
                            <div id="c_output">
                                <select class="form-control" required>
                                    <option></option>
                                </select>
                            </div>
                        </div>
                        <div class="col-sm-4">
                            <label>HORA SALIDA:</label>
                            <div id="cc_output">
                                <select class="form-control" required>
                                    <option></option>
                                </select>
                            </div>
                        </div>
                        </div>
                    </div>
                </div>
                <br>
                <div class="box-body">
                    <div class="row">
                        <div class="col-sm-12">
                        <div class="col-sm-6">
                            <label>CHOFER:</label>
                            <select name="chofer" class="form-control" required>
                                """+str(cho)+"""
                            </select>       
                        </div>
                        <div class="col-sm-6">
                            <label>CHOFER AUXILIAR:</label>
                            <select name="choferaux" class="form-control" required>
                                """+str(cho1)+"""
                            </select> 
                        </div>
                        </div>
                    </div>
                </div>
                <br>
                <div class="box-body">
                    <div class="row">
                        <div class="col-sm-12">
                        <div class="col-sm-6">
                            <label>FECHA VIAJE:</label>
                            <div class="input-group">
                                <span class="input-group-addon">
                                    <i class="material-icons">date_range</i>
                                </span>
                                <div class="form-line">
                                    <input type="date" class="form-control date" name="fecha" required>
                                </div>
                            </div>     
                        </div>
                        <div class="col-sm-6">
                            <label>BUS:</label>
                            <select name="bus" class="form-control" id="numero" onchange="pasaje();" required>
                                """+str(bus)+"""
                            </select>
                        </div>
                        </div>
                    </div>
                </div>
                <div id="mostrarpasaje"></div>
                <div class="box-body">
                    <div class="row">
                        <div class="col-sm-12">
                        <div class="col-sm-6">
                            <label>USUARIO:</label>
                            <input class="form-control" type="password" style="text-transform:uppercase; text-align:center;" name="usu" required>
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

<div id="resultado"></div>

<div id="mostrar_venta"></div>
                    
                    

""")

fin_cabezera()



print("""

    <script type="text/javascript">
        function copiar()
        {
            document.getElementById("nombrenit").value=document.getElementById("no0").value;
            document.getElementById("nit").value=document.getElementById("ci0").value;

        }
    </script>

<script>

function guardar(b)
{
    var monto=document.getElementById("monto").value;
    if(monto!="" && monto!="0" && monto!="0.0"){
        var datos=$('#formulario').serialize();
        var registro = $.ajax({
            url:"../mysqldb/registros/RegistroVenta.py",
            Type:"post",
            data:datos,
            async:false
        }).responseText;
        var a=registro;
        if(a==1){
            alert("Usuario Incorrecto");
            document.getElementById("codUsuario").value='';
        }
        else{
        $("#venta_reserva").modal("hide");
        $("#venta_pasaje").modal("hide"); 
        $("#venta.close").click();
        var mysql = $.ajax({
            url:"modal/venta.py",
            dataType:"text",
            data:{valor:b.id},
            async:false
        }).responseText;
        document.getElementById("resultado").innerHTML=mysql;
        $("#venta").modal("show");
        }
    }
    else{
        alert("Ingresar Monto");
    }
}
</script>


<script>

    function cerrar(b)
    {
        $("#venta_reserva").modal("hide");
        $("#venta_pasaje").modal("hide"); 
        $("#venta.close").click();        
        var mysql = $.ajax({
            url:"modal/venta.py",
            dataType:"text",
            data:{valor:b.id},
            async:false
        }).responseText;
        document.getElementById("resultado").innerHTML=mysql;
        $("#venta").modal("show");
    }
</script>


<script>
    function cancelar(b)
    {
        var aaa=b.id;
        var aaaa=aaa.split("-");
        var aa=aaaa[0];
        var bb=aaaa[1];

        var registro = $.ajax({
            url:"../mysqldb/actualizaciones/actualizarestadoPasaje.py",
            Type:"post",
            data:{valor:bb},
            async:false
        }).responseText;
        var a=registro;
        if(a==1){
            alert("Recerva Cancelada");
        }

        $("#venta_reserva").modal("hide");
        $("#venta_pasaje").modal("hide"); 
        $("#venta.close").click();        
        var mysql = $.ajax({
            url:"modal/venta.py",
            dataType:"text",
            data:{valor:aa},
            async:false
        }).responseText;
        document.getElementById("resultado").innerHTML=mysql;
        $("#venta").modal("show");
    }
</script>




<script>
    function metodo_venta(b)
    {

        var aaa=b.id;
        var aaaa=aaa.split("-");
        var aa=aaaa[0];
        var bb=aaaa[1];
        var monto=aaaa[2];
        
        if(aa.substring(0,1)=='Z'){
            
            var reserva = $.ajax({
            url:"modal/venta_reserva.py",
            dataType:"text",
            data:{valor:b.id},
            async:false
            }).responseText;

            document.getElementById("mostrar_venta").innerHTML=reserva;

            $("#venta_reserva").modal("show");
        
        }
        else{

        let valoresCheck = [];
        $("input[type=checkbox]:checked").each(function(){
            valoresCheck.push(this.value);
        });
        var tt=[];
        for(var k=0;k<valoresCheck.length;k++){
            if(valoresCheck[k].substring(0,1)!='X' && valoresCheck[k].substring(0,1)!='Z'){
                tt.push(valoresCheck[k]);
            }
        }

        for(var i=1;i<tt.length;i++)
        {
            for(var j=0;j<(tt.length-i);j++)
            {
                if(parseInt(tt[j],10)>parseInt(tt[j+1],10))
                {
                    k=tt[j+1];
                    tt[j+1]=tt[j];
                    tt[j]=k;
                }
            }
        }
        
        var cadena='<div class="modal" id="venta_pasaje" tabindex="-1" role="dialog" aria-labellebdy="myModalLabel" aria-hidden="true" data-backdrop="static" data-keyboard="false" style=" opacity:0.99;"><div class="modal-dialog" role="document"><div class="modal-content"><form id="formulario" class="form-registro" accept-charset="UTF-8"><div class="modal-header header"><button type="button" class="close" data-dismiss="modal" aria-label="Close" onclick="cerrar(this)" id="'+bb+'"><span aria-hidden="true">&times</span></button></div><center><input type="radio" id="radio_34" class="with-gap radio-col-indigo" checked name="tratamiento" value="V" onclick="show2();"/><label for="radio_34">VENTA</label><input type="radio" id="radio_30" class="with-gap radio-col-red" name="tratamiento" value="R" onclick="show1();"/><label for="radio_30">RECERVA</label></center><div class="table-responsive"><input class="form-control" style="text-align:center" type="hidden"  name="codigo" value="'+bb+'"><table style="background:rgba(0,0,255,0.6);"><tr><td></td></tr><tr><td><table id="example1" class="table table-bordered table-striped"><thead style="background-color: blue;color:white; font-weight: bold;"><tr><th style="width:35px"><h5 align="center">NIT</h5></th><th style="width:35px"><h5 align="center">NOMBRE NIT</h5></th><th style="width:10px"><h5 align="center">PASAJE Bs</h5></th></tr></thead><tbody><tr><td style="width:135px"><input class="form-control"  type="text"  style="text-transform:uppercase; text-align:center;" name="nit" id="nit"/></td><td><input class="form-control" type="text" style="text-transform:uppercase; text-align:center;" name="nombrenit" id="nombrenit"/></td><td> <center><input class="form-control" type="text" style="text-transform:uppercase; text-align:center;" id="monto" name="monto" value="'+monto+'" required/></center></td></tr></tbody></table>  </td></tr>    <tr><td><table id="example1" class="table table-bordered table-striped"><thead style="background-color: blue;color:white; font-weight: bold;"><tr><th style="width:35px"><h5 align="center">ASIENTO</h5></th><th style="width:135px"><h5 align="center">C.I</h5></th><th><h5 align="center">NOMBRE</h5></th><th><h5 align="center">APELLIDOS</h5></th></tr></thead><tbody>';
        
        var contador=0;
        for(var i=0;i<tt.length;i++){
            cadena=cadena+'<tr><td bgcolor="white"><input class="form-control" style="text-align:center" type="text" value="'+tt[i]+'" disabled><input class="form-control" style="text-align:center" type="hidden"  name="nu'+contador+'" value="'+tt[i]+'"></td><td style="width:135px" bgcolor="white"><input class="form-control" type="text" style="text-transform:uppercase; text-align:center;" name="ci'+contador+'" id="ci'+contador+'" onkeyup="copiar();" ></td><td bgcolor="white"><input class="form-control" type="text" style="text-transform:uppercase; text-align:center;"  name="no'+contador+'" id="no'+contador+'" onkeyup="copiar();"></td><td bgcolor="white"><input class="form-control" type="text" style="text-transform:uppercase; text-align:center;" name="ap'+contador+'"  required></td></tr>';
            contador=contador+1;
        }
        if(tt.length==0){
            cadena=cadena+'<tr><td bgcolor="white"><input class="form-control" style="text-align:center" type="text" value="'+aa+'" style="text-transform:uppercase"><input class="form-control" style="text-align:center" type="hidden"  name="nu'+contador+'" value="'+aa+'"></td><td style="width:135px" bgcolor="white"><input class="form-control" type="text" style="text-transform:uppercase; text-align:center;" name="ci'+contador+'" id="ci'+contador+'"  onkeyup="copiar();"></td><td bgcolor="white"><input class="form-control" type="text" style="text-transform:uppercase; text-align:center;" name="no'+contador+'" id="no'+contador+'" onkeyup="copiar();"></td><td bgcolor="white"><input class="form-control" type="text" style="text-transform:uppercase; text-align:center;" name="ap'+contador+'" required></td></tr>';
            contador=contador+1;
        }

        document.getElementById("mostrar_venta").innerHTML=cadena+'</tbody></table></td></tr><tr><td></table><input name="conta" value="'+contador+'" type="hidden" ></input>           <div id="datos"><table width="100%" style="background:rgba(0,0,255,0.6);"><tr><td><center>            <div id="div1" > <table id="example1" class="table table-bordered table-striped" style="width:335px; background:rgba(0,0,255,0.6);"><thead><tr><th style="width:15px"  bgcolor="blue" style="color:white; font-weight: bold;"><h5 align="center" style="color:white;">Contraseña</h5></th><th style="width:135px"><input class="form-control" type="password" style="text-transform:uppercase; text-align:center;" name="codUsuario" required/></th></tr></thead></table></div>     </center></td></tr></table></div><div><div class="modal-footer"><button type="button" onclick="guardar(this)" id="'+bb+'" class="btn bg-indigo waves-effect"><div class="demo-google-material-icon"> <i class="material-icons">note_add</i> <span class="icon-name">GUARDAR</span></div></button><button type="button" aria-label="Close" onclick="cerrar(this)" id="'+bb+'" class="btn bg-red waves-effect"><div class="demo-google-material-icon"> <i class="material-icons">close</i> <span class="icon-name">CANCELAR</span></div></button></div></form></div></div></div>';
        
        }


    }
</script>






    <script type="text/javascript">
        function show1(){
            document.getElementById('div1').style.display ='none';
        }
        function show2(){
            document.getElementById('div1').style.display = 'block';
        }
    </script>





<script>
    function c_random(){
        var a=document.getElementById('c_input').value;
        var c='"""+co+"""';
        var i='"""+ini+"""';
        var fi='"""+fin+"""';
        var fr='"""+fre+"""';

        var cod=c.split("/");
        var ini=i.split("/");
        var fin=fi.split("/");
        var fre=fr.split("/");
        
        var uni=[]
        for(var i=0;i<ini.length;i++){
            if(a==ini[i]){
                uni.push(fin[i]);
            }
        }

        var h;
        var out=[];
        var obj={};
        for(h=0;h<uni.length;h++){
            obj[uni[h]]=0;
        }
        for(h in obj){
            out.push(h);
        }


        var string="<option></option>";
        for(var i=0;i<out.length;i++){
            string=string+"<option>"+out[i]+"</option>";
        }

        string="<select id='cc_input' name='fin' class='form-control' onchange='cc_random();' required>"+string+"</select>";
        document.getElementById('c_output').innerHTML=string;
    }
</script>

<script>
    function cc_random(){
        var a=document.getElementById('c_input').value;
        var b=document.getElementById('cc_input').value;
        var c='"""+co+"""';
        var i='"""+ini+"""';
        var fi='"""+fin+"""';
        var fr='"""+fre+"""';

        var cod=c.split("/");
        var ini=i.split("/");
        var fin=fi.split("/");
        var fre=fr.split("/");
        
        var uni=[]
        for(var i=0;i<ini.length;i++){
            if(a==ini[i] && b==fin[i]){
                uni.push(fre[i]);
            }
        }

        var string="<option></option>";
        for(var i=0;i<uni.length;i++){
            string=string+"<option>"+uni[i]+"</option>";
        }

        string="<select name='hora' class='form-control' required>"+string+"</select>";
        document.getElementById('cc_output').innerHTML=string;
    }
</script>


<script>
    function pasaje(){     
        var a=document.getElementById('numero').value;
        var pla='"""+pla+"""';
        var pis='"""+pis+"""';
        var placa=pla.split("/");
        var pisoo=pis.split("/");
        var piso="";
        for(var i=0;i<placa.length;i++){
          if (placa[i]===a){
            piso=pisoo[i];
          }
        }
        var string="";
        if(piso==="1"){
          string=string+'<div class="col-xs-6"><label>PASAJE:</label><input type="text" class="form-control" name="pas1" style="text-transform:uppercase"  required><br></div>';
        }
        else if(piso==="2"){
          string=string+'<div class="col-xs-6"><label>PASAJE PISO 1:</label><input type="text" class="form-control" name="pas1"  style="text-transform:uppercase"  required></div><div class="col-xs-6"><label>PASAJE PISO 2:</label><input type="text" class="form-control" name="pas2" style="text-transform:uppercase"  required><br></div>';
        }
        document.getElementById('mostrarpasaje').innerHTML=string;

    }
      
    </script>


<script>
    function capturar(b)
    {
        var mysql = $.ajax({
            url:"modal/modal.py",
            dataType:"text",
            data:{valor:b.id},
            async:false
        }).responseText;
        document.getElementById("resultado").innerHTML=mysql;
    }
</script>

<script>
    function capturar1(b)
    {
        var mysql = $.ajax({
            url:"modal/venta.py",
            dataType:"text",
            data:{valor:b.id},
            async:false
        }).responseText;
        document.getElementById("resultado").innerHTML=mysql;

    }
</script>



<script>
    function capturar2(b)
    {
        var mysql = $.ajax({
            url:"modal/reporte_venta.py",
            dataType:"text",
            data:{valor:b.id},
            async:false
        }).responseText;
        document.getElementById("resultado").innerHTML=mysql;
    }
</script>



<script>
function imprim1(imp1){
var printContents = document.getElementById('imp1').innerHTML;
        w = window.open();
        w.document.write(printContents);
        w.document.close(); // necessary for IE >= 10
        w.focus(); // necessary for IE >= 10
    w.print();
    w.close();
        return true;}
</script>

""")