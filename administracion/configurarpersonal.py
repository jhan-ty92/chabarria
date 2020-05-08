#!C:\Python34\python
import cgi
import pymysql 
import sys
sys.path.append("..")
from layout .principal import *
print ("Content-Type:text/html \r\n\r\n")
try:
    form = cgi.FieldStorage()
    id=form.getvalue('id')
    cabezera()
    con=pymysql.connect(user="root",password="",host="",database="buses_chavarria")
    personal=con.cursor()

    p=personal.execute("select * from personal WHERE cod='"+str(id)+"'")
    usuario=con.cursor()
    u=usuario.execute("select * from usuario WHERE cod_personal='"+str(id)+"'")
    socio=con.cursor()
    s=socio.execute("""select s.cod,b.marca,b.placa,b.tipo from socio s
                       inner join bus b on b.cod=s.cod_bus
                       WHERE s.cod_personal='"""+str(id)+"'""")
    oficina=con.cursor()
    o=oficina.execute("""select po.cod,of.nombre,of.direccion,po.cod_oficina FROM personal_oficina po
                         inner join oficina of on of.cod=po.cod_oficina
                         WHERE po.cod_personal='"""+str(id)+"'""")
    

    oficina2=con.cursor()
    oficina2.execute("select * from oficina")



    licencia=con.cursor()
    l=licencia.execute("select * from personal_bus WHERE cod_personal='"+str(id)+"'")
    
    cadena_oficina=""


    nom=""
    ape=""
    tip=""

    per=""
    for art in personal:
        per=per+str(art[0])+"-"+str(art[1])+"-"+str(art[2])+"-"+str(art[3])+"-"+str(art[4])+"-"+str(art[5])+"-"+str(art[6])+"-"+str(art[7])+"-"+str(art[8])+"-"+str(art[9])
        nom=str(art[1])
        ape=str(art[2])
        tip=str(art[9])
        
    person=per.split('-')
    lis=["SOCIO","ADMINISTRADOR DE OFICINA","PESONAL DE BUS"]
    valid="<option>"+str(tip)+"</option>"
    for i in range(len(lis)):
        if tip!=lis[i]:
            valid=valid+"<option>"+str(lis[i])+"</option>"

    lis=["ALTO LA PAZ","BENI","CHUQUISACA","COCHABAMBA","LA PAZ","ORURO","PANDO","POTOSÍ","SANTA CRUZ","TARIJA"]
    valid1="<option>"+str(person[5])+"</option>"
    for i in range(len(lis)):
        if str(person[5])!=lis[i]:
            valid1=valid1+"<option>"+str(lis[i])+"</option>"                            

    usu=""
    pas1=""
    pas2=""
    pas3=""
    for art in usuario:
        usu=usu+str(art[0])+"-"+str(art[1])+"-"+str(art[2])
        pas1=str(art[0])
        pas2=str(art[1])    
        pas3=str(art[2])
    

    so=""
    for art in socio:
        so=so+str(art[0])+"/"+str(art[1])+"/"+str(art[2])+"&"

    

    cadena_bus="";

    bus=con.cursor()
    bus.execute("""select s.cod,b.placa,s.cod_bus, s.cod_personal from socio s
                inner join bus b on b.cod=s.cod_bus
                where s.cod_personal ='"""+str(id)+"'")
    b1=con.cursor()
    b1.execute("select * from bus")
    aux=con.cursor()
    aux.execute("""select s.cod,b.placa,s.cod_bus, s.cod_personal from socio s
                inner join bus b on b.cod=s.cod_bus""")
    
    lis=[]
    for art in bus:
        cadena_bus=cadena_bus+"<option value="+str(art[2])+" selected>"+str(art[1])+"</option>"
    
    for art in aux:
        lis.append(str(art[2]))
    
    for b in b1:    
        si=False
        for i in lis:
            if i == str(b[0]):
                si=True
        if si==False:
            cadena_bus=cadena_bus+"<option value="+str(b[0])+">"+str(b[2])+"</option>"




    of=""
    ofii=""
    idofii=""
    for art in oficina:
        of=of+str(art[0])+"-"+str(art[1])+"-"+str(art[2])
        idofii=str(art[0])
        ofii=str(art[1])
        idof=str(art[3])

    li=""
    licen1=""
    licen2=""
    for art in licencia:
        li=li+str(art[0])+"-"+str(art[1])
        licen1=str(art[0])
        licen2=str(art[1])
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
                    <a href="personal.py">
                        Personal
                    </a>
                </li>
                <li class="active">
                    <i class="material-icons">link</i> Edtar Personal
                </li>
            </ol>
            <div class="row clearfix">
                <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12">
                    <div class="card">
                        <div class="header">
                            <h2>
                                """+str(tip)+"""<small>"""+str(nom)+" "+str(ape)+"""</small>
                            </h2>
                        </div>
                        <div class="body" style="height:445px; overflow-y: scroll;">
                            <div class="row clearfix">
                                <div class='col-sm-12 table-responsive'>
                                    <center><img src='../public/images/u.png' width='150' height='150' alt='User' /></center>
                                    <table width='100%'' class='table table-bordered table-striped table-hover dataTable js-basic-example' >
                                        <tbody>
                                            <tr>
                                                <td>
                                                    <br>""")
    if p>=1: 
        print("""                                   <a class="carrera" data-carrera="4" style="text-decoration: none;cursor: pointer;" onclick="capturar(this)" id='p'>    
                                                    <div class="col-lg-6">
                                                        <div class="info-box bg-pink hover-zoom-effect">
                                                            <div class="icon">
                                                                <i class="material-icons">person</i>
                                                            </div>
                                                            <div class="content">
                                                                <div class="text">DATOS PERSONALES</div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    </a>""")
    if o>=1:
        cadena_oficina="<option value="+str(idof)+">"+str(ofii)+"</option>";
        for art in oficina2:
            if str(art[0])!=str(idof):
                cadena_oficina=cadena_oficina+"<option value="+str(art[0])+">"+str(art[1])+"</option>" 
        print("""                                   <a class="carrera" data-carrera="4" style="text-decoration: none;cursor: pointer;" onclick="capturar(this)" id='o'>
                                                    <div class="col-lg-6">
                                                        <div class="info-box bg-deep-purple hover-zoom-effect">
                                                            <div class="icon">
                                                                <i class="material-icons">business</i>
                                                            </div>
                                                            <div class="content">
                                                                <div class="text">OFICINA</div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                     </a>""")
    if s>=1: 
        print("""                                   <a class="carrera" data-carrera="4" style="text-decoration: none;cursor: pointer;" onclick="capturar(this)" id='s'>
                                                    <div class="col-lg-6">
                                                        <div class="info-box bg-deep-purple hover-zoom-effect">
                                                            <div class="icon">
                                                                <i class="material-icons">directions_bus</i>
                                                            </div>
                                                            <div class="content">
                                                                <div class="text">BUS</div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                     </a>""")
    if l>=1: 
        print("""                                   <a class="carrera" data-carrera="4" style="text-decoration: none;cursor: pointer;" onclick="capturar(this)" id='l'>
                                                    <div class="col-lg-6"> 
                                                        <div class="info-box bg-blue hover-zoom-effect">
                                                            <div class="icon">
                                                                <i class="material-icons">picture_in_picture_alt</i>
                                                            </div>
                                                            <div class="content">
                                                                <div class="text">LICENCIA</div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                     </a>""")
    if u>=1: 
        print("""                                   <a class="carrera" data-carrera="4" style="text-decoration: none;cursor: pointer;" onclick="capturar(this)" id='u'>
                                                    <div class="col-lg-6"> 
                                                        <div class="info-box bg-red hover-zoom-effect">
                                                            <div class="icon">
                                                                <i class="material-icons">lock_open</i>
                                                            </div>
                                                            <div class="content">
                                                                <div class="text">USUARIO</div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    </a>""")
    print("""
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
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
                                        <center><h3 style="padding-top: 170px;">Seleccione un opcion</h3></center>
                                    </div>
                                </div>

                            </div>
                        </div>
                    </div>
                </div>
            </div>    
        </div>
    </section>


<div class="modal" id="re_socio" tabindex="-1" role="dialog" aria-labellebdy="myModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header header bg-indigo">
                <center><h5 class="modal-title">BUSES</h5></center>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times</span>
                </button>
            </div>
            <div class="modal-body">
             <form action="../mysqldb/actualizaciones/actualizarSocio.py"  method="POST" class="form-registro" accept-charset="UTF-8">     
                <input name="codigo" value='"""+str(id)+"""' type="hidden" ></input>
                
                <div class="col-sm-12">
                <div class="col-sm-12">
                <div class="col-sm-12">
                <div class="col-sm-12">
                <div class="col-sm-12">
                <div class="col-sm-12">
                <br>
                <center>
                <div class="box-body">
                    <div class="row">
                    <div class="demo-masked-input">        
                            
                        
                        <select id="my-select" multiple="multiple" name="bus">
                            """+str(cadena_bus)+"""
                        </select>
                    </div>
                    </div>
                </div>
                </center>
                <br>
                <div class="row">
                    <div class="col-md-5">
                        <button type="submit" class="btn bg-indigo waves-effect"><div class="demo-google-material-icon"> <i class="material-icons">tab</i> <span class="icon-name">GRABAR DATOS</span></div></button>  
                    </div>
                </div>
                </div>
                </div>
                </div>
                </div>
                </div>
                </div>
                <br>
            </form>     
            </div>
            <div class="modal-footer"></div>
        </div>
    </div>
</div>


<div class="modal" id="re_licencia" tabindex="-1" role="dialog" aria-labellebdy="myModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header header bg-indigo">
                <center><h5 class="modal-title">EDITAR LICENCIA</h5></center>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times</span>
                </button>
            </div>
            <div class="modal-body">
             <form action="../mysqldb/actualizaciones/actualizarLicencia.py" method="POST" class="form-registro" accept-charset="UTF-8">     
                <input name="codigo" value='"""+licen1+"""' type="hidden" ></input>
                <input name="id" value='"""+str(id)+"""' type="hidden" ></input>
                <div class="box-body">
                    <div class="row">
                        <div class="col-lg-6">
                            <label for="LI">LICENCIA</label>
                            <input class="form-control" type="text" name="licencia" value='"""+licen2+"""' required> 
                        </div>
                    </div>
                </div>
                <br>
                <div class="row">
                    <div class="col-md-5">
                        <button type="submit" class="btn bg-indigo waves-effect"><div class="demo-google-material-icon"> <i class="material-icons">tab</i> <span class="icon-name">GRABAR DATOS</span></div></button>  
                    </div>
                </div>
            </form>     
            </div>
            <div class="modal-footer"></div>
        </div>
    </div>
</div>


<div class="modal" id="re_usuario" tabindex="-1" role="dialog" aria-labellebdy="myModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header header bg-indigo">
                <center><h5 class="modal-title">EDITAR USUARIO</h5></center>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times</span>
                </button>
            </div>
            <div class="modal-body">
             <form action="../mysqldb/actualizaciones/actualizarUsuario.py" method="POST" class="form-registro" accept-charset="UTF-8">
             <input name="codigo" value='"""+pas1+"""' type="hidden" ></input>
             <input name="id" value='"""+str(id)+"""' type="hidden" ></input>     
                <div class="box-body">
                    <div class="row">
                        <div class="col-lg-6">
                            <label for="LI">USUARIO</label>
                            <input class="form-control" type="text" name="uss" value='"""+pas2+"""' required> 
                        </div>
                        <div class="col-lg-6">
                            <label for="LI">CONTRASEÑA</label>
                            <input class="form-control" type="text" name="passs" value='"""+pas3+"""' required> 
                        </div>
                    </div>
                </div>
                <br>
                <div class="row">
                    <div class="col-md-5">
                        <button type="submit" class="btn bg-indigo waves-effect"><div class="demo-google-material-icon"> <i class="material-icons">tab</i> <span class="icon-name">GRABAR DATOS</span></div></button>  
                    </div>
                </div>
            </form>     
            </div>
            <div class="modal-footer"></div>
        </div>
    </div>
</div>


<div class="modal" id="re_oficina" tabindex="-1" role="dialog" aria-labellebdy="myModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header header bg-indigo">
                <center><h5 class="modal-title">CAMBIO OFICINA</h5></center>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times</span>
                </button>
            </div>
            <div class="modal-body">
             <form action="../mysqldb/actualizaciones/actualizarOfPersonal.py" method="POST" class="form-registro" accept-charset="UTF-8">
                <input name="codigo" value='"""+idofii+"""' type="hidden" ></input>
                <input name="id" value='"""+str(id)+"""' type="hidden" ></input>     
                <div class="box-body">
                    <div class="row">
                        <div class="col-lg-6">
                            <label for="NOMBRE">OFICINA</label>
                            <select name="oficina" class="form-control">
                            """+cadena_oficina+"""
                            </select>
                        </div>
                    </div>
                </div>
                <br>
                <div class="row">
                    <div class="col-md-5">
                        <button type="submit" class="btn bg-indigo waves-effect"><div class="demo-google-material-icon"> <i class="material-icons">person</i> <span class="icon-name">GRABAR DATOS</span></div></button>  
                    </div>
                </div>
            </form>     
            </div>
            <div class="modal-footer"></div>
        </div>
    </div>
</div>








<div class="modal" id="re_personal" tabindex="-1" role="dialog" aria-labellebdy="myModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header header bg-indigo">
                <center><h5 class="modal-title">EDITAR PERSONAL</h5></center>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times</span>
                </button>
            </div>
            <div class="modal-body">
             <form action="../mysqldb/actualizaciones/actualizarPersona.py" method="POST" class="form-registro" accept-charset="UTF-8">     
                <input name="id" value='"""+str(id)+"""' type="hidden" ></input>
                <input name="codigo" value='"""+person[0].strip()+"""' type="hidden" ></input>
                <div class="box-body">
                    <div class="row">
                        <div class="col-lg-6">
                            <label for="NOMBRE">NOMBRE:</label>
                            <input class="form-control" type="text" name="nombre" value='"""+person[1].strip()+"""' required> 
                        </div>
                        <div class="col-lg-6">
                            <label for="APELLIDOS">APELLIDOS:</label>
                            <input class="form-control" type="text" name="apellidos" value='"""+person[2].strip()+"""' required>
                        </div>
                    </div>
                </div>
                <br>
                <div class="box-body">
                    <div class="row">
                        <div class="col-lg-6">
                            <label for="CI">CI:</label>
                            <input class="form-control" type="text" name="ci" value='"""+person[3].strip()+"""' required> 
                        </div>
                        <div class="col-lg-6">
                            <label for="TELEFONO">TELEFONO:</label>
                            <input class="form-control" type="text" name="telefono" value='"""+person[4].strip()+"""' required>
                        </div>
                    </div>
                </div>
                <br>
                <div class="box-body">
                    <div class="row">
                        <div class="col-lg-6">
                            <label for="CIUDAD">CIUDAD:</label>
                            <select id="c_input" name="ciudad" class="form-control" onchange="c_random();">
                                """+valid1+"""
                            </select>
                        </div>
                        <div class="col-lg-6">
                            <label for="PROVINCIA">PROVINCIA:</label>
                            <div id="provincia_m">
                                <div id="c_output">
                                    <select select name='provincia' class="form-control">
                                        <option>"""+str(person[6])+"""</option>
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
                            <input class="form-control" type="text" name="localidad" value='"""+person[7].strip()+"""' required> 
                        </div>
                        <div class="col-lg-6">
                            <label for="DIRECCION">DIRECCION:</label>
                            <input class="form-control" type="text" name="direccion" value='"""+person[8].strip()+"""' required>
                        </div>
                    </div>
                </div>
                <br>
                <div class="box-body">
                    <div class="row">
                        <div class="col-lg-6">
                            <label for="Tipo">TIPO PERSONAL:</label>
                            <select class="form-control" name="tipo" id="input" onchange="random();">
                                """+valid+"""
                            </select> 
                        </div>
                    </div>
                </div>
                <br>
                <div id="output"></div>
                <br>
                <div class="row">
                    <div class="col-md-5">
                        <button type="submit" class="btn bg-indigo waves-effect"><div class="demo-google-material-icon"> <i class="material-icons">person</i> <span class="icon-name">GRABAR DATOS</span></div></button>  
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
        function capturar(b)
        {
        switch(b.id){
            case 'p':
            var per='"""+str(per)+"""';
            var pp=per.split("-");
            document.getElementById("resultado").innerHTML="<div class='col-lg-12 col-md-12 col-sm-12 col-xs-12'><div class='card' ><div class='header'><h2>DATOS PERSONALES</h2><a data-toggle='modal' data-target='#re_personal'><ul class='header-dropdown m-r--5'><li><i class='material-icons'>edit</i></li></ul></a></div><div class='body'><div class='row clearfix'><div class='col-sm-12 table-responsive'><table width='100%' class='table table-bordered table-striped table-hover'><tr class='odd gradeX'><td>NOMBRE</td><td>"+pp[1]+"</td></tr><tr class='odd gradeX'><td>APELLIDOS</td><td>"+pp[2]+"</td></tr><tr class='odd gradeX'><td>CI</td><td>"+pp[3]+"</td></tr><tr class='odd gradeX'><td>TELEFONO</td><td>"+pp[4]+"</td></tr><tr class='odd gradeX'><td>CIUDAD</td><td>"+pp[5]+"</td></tr><tr class='odd gradeX'><td>PROVINCIA</td><td>"+pp[6]+"</td></tr><tr class='odd gradeX'><td>LOCALIDAD</td><td>"+pp[7]+"</td></tr><tr class='odd gradeX'><td>DIRECCION</td><td>"+pp[8]+"</td></tr></table></div></div></div></div></div>";
            break;
            case 'o':
            var of='"""+str(of)+"""';
            var oo=of.split("-");
            document.getElementById("resultado").innerHTML="<div class='col-lg-12 col-md-12 col-sm-12 col-xs-12'><div class='card' ><div class='header'><h2>OFICINA</h2><a data-toggle='modal' data-target='#re_oficina'><ul class='header-dropdown m-r--5'><li><i class='material-icons'>edit</i></li></ul></a></div><div class='body'><div class='row clearfix'><div class='col-sm-12 table-responsive'><table width='100%' class='table table-bordered table-striped table-hover'><tr class='odd gradeX'><td>NOMBRE</td><td>"+oo[1]+"</td></tr><tr class='odd gradeX'><td>DIRECCION</td><td>"+oo[2]+"</td></tr></table></div></div></div></div></div>";
            break;
            case 's':
            var so='"""+str(so)+"""';
            var sss=so.split("&");
            var suma="";
            for(var i=0;i<(sss.length)-1;i++){
            var a=sss[i];
            var aa=a.split("/");
            suma=suma+"<tr class='odd gradeX'><td><center>"+(i+1)+"</center></td><td><center>"+aa[1]+"</center></td><td><center>"+aa[2]+"</center></td></tr>";
            }

            document.getElementById("resultado").innerHTML="<div class='col-lg-12 col-md-12 col-sm-12 col-xs-12'><div class='card' ><div class='header'><h2>SOCIO</h2><a data-toggle='modal' data-target='#re_socio'><ul class='header-dropdown m-r--5'><li><i class='material-icons'>edit</i></li></ul></a></div><div class='body'><div class='row clearfix'><div class='col-sm-12 table-responsive'><table width='100%' class='table table-bordered table-striped table-hover'><th><center>N°</center></th><th><center>MARCAR</center></th><th><center>PLACA</center></th>"+suma+"</table></div></div></div></div></div>";
            break;
            case 'l':
            var li='"""+str(li)+"""';
            var ll=li.split("-");
            document.getElementById("resultado").innerHTML="<div class='col-lg-12 col-md-12 col-sm-12 col-xs-12'><div class='card' ><div class='header'><h2>LICENCIA</h2><a data-toggle='modal' data-target='#re_licencia'><ul class='header-dropdown m-r--5'><li><i class='material-icons'>edit</i></li></ul></a></div><div class='body'><div class='row clearfix'><div class='col-sm-12 table-responsive'><table width='100%' class='table table-bordered table-striped table-hover'><tr class='odd gradeX'><td>LICENCIA:</td><td>"+ll[1]+"</td></tr></table></div></div></div></div></div>";
            break;   
            case 'u':
            var usu='"""+str(usu)+"""';
            var uu=usu.split("-");
            document.getElementById("resultado").innerHTML="<div class='col-lg-12 col-md-12 col-sm-12 col-xs-12'><div class='card' ><div class='header'><h2>USUARIO</h2><a data-toggle='modal' data-target='#re_usuario'><ul class='header-dropdown m-r--5'><li><i class='material-icons'>edit</i></li></ul></a></div><div class='body'><div class='row clearfix'><div class='col-sm-12 table-responsive'><table width='100%' class='table table-bordered table-striped table-hover'><tr class='odd gradeX'><td>USUARIO</td><td>"+uu[1]+"</td></tr><tr class='odd gradeX'><td>CONTRASEÑA</td><td>************</td></tr></table></div></div></div></div></div>";
            break;
            }
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


          """)
except:
    print("<script>location.href='../error/error.py'</script>")