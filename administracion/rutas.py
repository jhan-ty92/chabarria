#!C:\Python34\python 
import pymysql 
import sys
sys.path.append("..")
from layout .principal import *
cabezera()

con=pymysql.connect(user="root",password="",host="",database="buses_chavarria")
cursor=con.cursor()
c=cursor.execute("select * from oficina")

oficina=con.cursor()
oficina.execute("select * from oficina")
of=""
sumr=""
sumi=""
for art in oficina:
    of=of+"<option value="+str(art[0])+">"+str(art[1])+"</option>"
    sumr=sumr+str(art[0])+"-"
    sumi=sumi+str(art[1])+"-"
sumr=sumr[0:len(sumr)-1]
sumi=sumi[0:len(sumi)-1]

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
            <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12" style="width: 40%">
                <div class="card">
                    <div class="header bg-indigo">
                        <center><h2>
                            Lista de Oficinas
                        </h2></center>
                    </div>
                    <div class="body" style="height:468px; overflow-y: scroll;">
                        <div class="row clearfix">

                        """)
if c>=1:
    print("""<div class="table-responsive">
                <center><table class="table table-bordered table-striped table-hover js-basic-example dataTable" style="width: 90% ">
                    <thead>
                        <tr>
                            <th width=30><center>N°</center></th>
                            <th width=240><center>Oficina</center></th>
                                        
                        </tr>
                    </thead>
                    <tbody>
                    """)
    c=0
    for art in cursor:
        c=c+1
        cad=cad+str(
        """case '"""+str(art[1])+"""':
                id=document.getElementsByName('id"""+str(art[1])+"""')[0].value; 
                hora=document.getElementsByName('hora"""+str(art[1])+"""')[0].value;
                datos=document.getElementsByName('datos"""+str(art[1])+"""')[0].value; 
                break;""")

        print("""
                <tr>
                    <td><center>"""+str(c)+"""</center></td>
                    <td><center>
                     <form>
                     <a class="carrera" data-carrera="4" style="text-decoration: none;cursor: pointer;" onclick="capturar(this)" id='"""+str(art[1])+"""'>
                    <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12" style="width: 100%" >
                                <div class="info-box" style="border-radius: 12px;">
                                    <i class="material-icons">business</i>
                                    <center>
                                    <div class="content">
                                       
                                        <input type="hidden" name='id"""+str(art[1])+"""' value='"""+str(art[0])+"""'>
                                        <input type="hidden" name='hora"""+str(art[1])+"""' value='"""+str(art[5])+"""'>
                                        <input type="hidden" name='datos"""+str(art[1])+"""' value='"""+str(str(art[2])+"-"+str(art[3])+"-"+str(art[4]))+"""'>
                                        <div class="text">OFICINA """+str(art[1])+"""</div>
                                        
                                        

                                    </div>
                                    </center>
                                </div>
                    </div>
                    </a>
                    </form>
                    </center></td>
                </tr>""")
    print("""</tbody>
                </table></center>
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
            <div class="col-lg-6 col-md-6 col-sm-6 col-xs-12" style="width: 60%">
                <div class="card">
                    <div class="header bg-indigo">
                        <h2>
                            Oficina
                        </h2>
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
    

<div class="modal" id="ruta" tabindex="-1" role="dialog" aria-labellebdy="myModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header header bg-indigo">
                <center><h5 class="modal-title">NUEVA RUTA</h5></center>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times</span>
                </button>
            </div>
            <div class="modal-body">
             <form action="../mysqldb/registros/RegistroRuta.py" method="POST" class="form-registro" accept-charset="UTF-8">     
                <input  id="codigo" name="origen" type="hidden" ></input>
                <div class="box-body">
                    <div class="row">
                        <div class="col-sm-12">
                        <div class="col-sm-4">
                            <label for="ruta">RUTA ORIGEN</label>
                            <input class="form-control" type="text" name="direccion" id="nombre" required disabled>    
                        </div>
                        <div class="col-sm-4">
                            <center><i class="material-icons">arrow_back</i>
                            <label for="ruta">RUTA</label>
                            <i class="material-icons">arrow_forward</i></center>
                        </div>
                        <div class="col-sm-4">
                            <label for="ruta">RUTA DESTINO</label>
                            <div id="c_output">
                                <select class="form-control">
                                    <option>  </option>
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
                        <div class="col-sm-12">
                        <div class="col-sm-12">
                            <label for="r">SUB RUTAS:</label>
                            <textarea rows="3" class="form-control no-resize" name="sub_ruta"></textarea>
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
    $('#ruta').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget)
    var recipient0 = button.data('codigo')
    var recipient1 = button.data('nombre')
    var modal = $(this)    
    modal.find('.modal-body #codigo').val(recipient0)
    modal.find('.modal-body #nombre').val(recipient1)
    });    
</script>

<script>
    function capturar(b)
    {
        var id=""; 
        var hora="";
        var datos="";
        switch(b.id){
        """+str(cad)+"""
        }
        var res=hora.split("-");
        var d=datos.split("-");

        var mysql = $.ajax({
            url:"../mysqldb/consultas/MostrarRutas.py",
            dataType:"text",
            data:{valor:id},
            async:false
        }).responseText;
        document.getElementById("resultado").innerHTML="<div class='col-lg-12 col-md-12 col-sm-12 col-xs-12'><div class='card' ><div class='header'><h2>OFICINA<small id='oficina_name'>"+b.id+"</small></h2><ul class='header-dropdown m-r--5'><li><div class='col-xs-3 col-sm-3 col-md-3 col-lg-3'><a data-toggle='modal' data-target='#ruta' id='"+id+"'  onclick='seleccion(this);'  data-codigo='"+id+"' data-nombre='"+b.id+"'><button type='button' class='btn bg-indigo waves-effect'><div class='demo-google-material-icon'> <i class='material-icons'>note_add</i> <span class='icon-name'>Nueva Ruta</span></div></button></a></div></li></ul></div><div class='body'><div class='row clearfix'><div class='col-sm-12 table-responsive'><table width='100%'' class='table table-bordered table-striped table-hover'><tbody><tr class='odd gradeX'><td>HORARAIO DE ATENCION</td><td>"+hora+"</td></tr><tr class='odd gradeX'><td>DIRECCION</td><td>"+d[0]+"</td></tr></tbody></table><table width='100%'' class='table table-bordered table-striped table-hover'><tr><td>"+mysql+"</td></tr></table></div></div></div></div></div>";
    }
</script>
<script>
    function seleccion(b)
    { 
        var valor=""+b.id;
         
        var sumr='"""+sumr+"""';
        var sumi='"""+sumi+"""';
        var ar=sumr.split("-");
        var ai=sumi.split("-");
        var string="<option></option>";
        for(var i=0;i<ar.length;i++){
            if(ar[i]!=valor){
                string=string+"<option value="+ar[i]+">"+ai[i]+"</option>";
            }
        }
        string="<select name='destino' required class='form-control'>"+string+"</select>";
        document.getElementById('c_output').innerHTML=string;

    }
</script>
""")