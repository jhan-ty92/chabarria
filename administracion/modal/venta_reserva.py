#!C:\Python34\python   
import cgi
import os,sys,time
import pymysql
con=pymysql.connect(user="root",password="",host="",database="buses_chavarria")
try:
  form = cgi.FieldStorage()
  cod=form.getvalue('valor')
  ide=cod.split("-")
  asi=ide[0]
  asi=asi[1:len(asi)]
  pru=con.cursor()
  pru.execute("""select * from venta_pasaje where asiento='"""+str(asi)+"""' and cod_programacion='"""+str(ide[1])+"'""")
  si=""

  cod_pa=""
  ci=""
  nombre=""
  apellidos=""
  asiento=""
  nit=""
  nombre_nit=""
  pasaje=""
  usu=""
  for art in pru:
    si=str(art[7])
  if si=="None":
    mostrarAsientoR=con.cursor()
    mostrarAsientoR.execute("""select vpa.ci, vpa.nombre, vpa.apellidos, vpa.asiento, vpa.nom_nit, vpa.num_nit,psb.pasajes,b.asientopiso,vpa.monto,vpa.cod from venta_pasaje vpa
                          inner join programar_venta psb on psb.cod=vpa.cod_programacion
                          inner join bus b on b.cod=psb.cod_bus
                          where vpa.asiento='"""+str(asi)+"""' and  vpa.cod_programacion='"""+str(ide[1])+"'""")
    for art in mostrarAsientoR:
      ci=str(art[0])
      nombre=str(art[1])
      apellidos=str(art[2])
      asiento=str(art[3])
      nit=str(art[5])
      nombre_nit=str(art[4])
      pasaje=str(art[8])
      cod_pa=str(art[9])
    print("""
<div class="modal" id="venta_reserva" tabindex="-1" role="dialog" aria-labellebdy="myModalLabel" aria-hidden="true" data-backdrop="static" data-keyboard="false">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
              <form id="formulario" class="form-registro" accept-charset="UTF-8">     
                <div class="modal-header header">
                  <button type="button" class="close" data-dismiss="modal" aria-label="Close" onclick="cerrar(this)" id="""+str(ide[1])+""">
                    <span aria-hidden="true">&times</span>
                  </button>
                </div>
                <div class="box-body">
                <div class="table-responsive">
                  <input class="form-control" style="text-align:center" type="hidden"  name="codigo" value='"""+str(ide[1])+"""'>
                  <input class="form-control" style="text-align:center" type="hidden"  name="tratamiento" value="VR"> 
                  <input class="form-control" style="text-align:center" type="hidden" name="conta" value="1">
                  <table width="100%" style="background:rgba(0,0,255,0.6);">
                         <tr>
                      <td>
                        <table id="example1" class="table table-bordered table-striped">
                          <thead style="background-color: blue;color:white; font-weight: bold;">
                            <tr>
                              <th style="width:35px"><h5 align="center">NIT</h5></th>
                              <th style="width:35px"><h5 align="center">NOMBRE NIT</h5></th>
                              <th style="width:10px"><h5 align="center">PASAJE Bs</h5></th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr>
                              <td style="width:135px"><input class="form-control" type="text" style="text-transform:uppercase; text-align:center;" value='"""+str(nit)+"""' name="nit" id="nit" required/></td>
                              <td><input class="form-control" type="text" style="text-transform:uppercase; text-align:center;" value='"""+str(nombre_nit)+"""' name="nombrenit" id="nombrenit"/></td>
                              <td><center><input class="form-control" type="text" style="text-transform:uppercase; text-align:center;"  name="monto" id="monto" value='"""+str(pasaje)+"""' required/></center></td>
                            </tr>
                          </tbody>
                        </table> 
                      </td>
                    </tr>
                    <tr>
                      <td>
                        <table id="example1" class="table table-bordered table-striped">
                          <thead style="background-color: blue;color:white; font-weight: bold;">
                            <tr>
                              <th style="width:35px"><h5 align="center">ASIENTO</h5></th>
                              <th style="width:135px"><h5 align="center">C.I</h5></th>
                              <th><h5 align="center">NOMBRE</h5></th>
                              <th><h5 align="center">APELLIDOS</h5></th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr>
                              <td><input type="hidden" name="nu0" value='"""+str(asiento)+"""'/>
                              <input class="form-control" type="text" value='"""+str(asiento)+"""' style="text-align:center" disabled/></td>
                              <td><input class="form-control" type="text" style="text-transform:uppercase; text-align:center;" name="ci0" id="ci0" value='"""+str(ci)+"""' onkeyup="copiar();"/></td>
                              <td><input class="form-control" type="text" style="text-transform:uppercase; text-align:center;" name="no0" id="no0" value='"""+str(nombre)+"""' onkeyup="copiar();"/></td>
                              <td><input class="form-control" type="text" style="text-transform:uppercase; text-align:center;" name="ap0" value='"""+str(apellidos)+"""' required/></td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                      </table>
                    <div id="datos">
                      <table width="100%" style="background:rgba(0,0,255,0.6);">
                        <tr>
                          <td>
                            <center>
                            <table id="example1" class="table table-bordered table-striped" style="width:335px; background:rgba(0,0,255,0.6);">
                              <thead>
                                <tr>
                                  <th style="width:15px"  bgcolor="blue" style="color:white; font-weight: bold;">
                                    <h5 align="center" style="color:white;">PASSWORD</h5>
                                  </th>
                                  <th style="width:135px">
                                    <input class="form-control" style="text-transform:uppercase" name="codUsuario" type="password" required/>
                                  </th>
                                </tr>
                              </thead>
                            </table>
                            </center>
                          </td>
                        </tr>
                      </table>
                    </div>
                    <div>
                      <div class="modal-footer">
                        <button type="button" onclick="guardar(this)" id='"""+str(ide[1])+"""' class="btn bg-indigo waves-effect">
                        <div class="demo-google-material-icon"> <i class="material-icons">note_add</i> <span class="icon-name">VENDER</span></div>
                        </button>
                        <button type="button" data-dismiss="modal" aria-label="Close" class="btn bg-orange waves-effect" onclick="cancelar(this)" id='"""+str(ide[1])+"-"+str(cod_pa)+"""'><div class="demo-google-material-icon"> <i class="material-icons">delete</i> <span class="icon-name">CANCELAR</span></div></button>
                        <button type="button" data-dismiss="modal" aria-label="Close" class="btn bg-red waves-effect" onclick="cerrar(this)" id='"""+str(ide[1])+"""'><div class="demo-google-material-icon"> <i class="material-icons">close</i> <span class="icon-name">SALIR</span></div></button>
                      </div>
                    </div>
                  </div>
                </div>   
              </form>     
          </div>
      </div>
    </div>

""")
  else:
    mostrarAsiento=con.cursor()
    mostrarAsiento.execute("""select vpa.ci, vpa.nombre, vpa.apellidos, vpa.asiento, vpa.nom_nit, vpa.num_nit,p.nombre,psb.pasajes,b.asientopiso,vpa.monto,vpa.cod from venta_pasaje vpa
                          inner join usuario usup on vpa.cod_usuario=usup.cod
                          inner join programar_venta psb on psb.cod=vpa.cod_programacion
                          inner join bus b on b.cod=psb.cod_bus
                          inner join personal p on p.cod=usup.cod_personal 
                          where vpa.asiento='"""+str(asi)+"""' and  vpa.cod_programacion='"""+str(ide[1])+"'""")
    for art in mostrarAsiento:
      ci=str(art[0])
      nombre=str(art[1])
      apellidos=str(art[2])
      asiento=str(art[3])
      nit=str(art[5])
      nombre_nit=str(art[4])
      pasaje=str(art[9])
      usu=str(art[6])
      cod_pa=str(art[10])
    print("""
<div class="modal" id="venta_reserva" tabindex="-1" role="dialog" aria-labellebdy="myModalLabel" aria-hidden="true" data-backdrop="static" data-keyboard="false">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
              <form action="#" method="POST" class="form-registro" accept-charset="UTF-8">     
                <div class="modal-header header">
                  <button type="button" class="close" data-dismiss="modal" aria-label="Close" onclick="cerrar(this)" id="""+str(ide[1])+""">
                    <span aria-hidden="true">&times</span>
                  </button>
                </div>
                <div class="box-body">
                 

                <div class="table-responsive">
                  <input class="form-control" style="text-align:center" type="hidden"  name="codigo" value="'+bb+'">
                  

                  <table width="100%" style="background:rgba(0,0,255,0.6);">
                         <tr>
                      <td>
                        <table id="example1" class="table table-bordered table-striped">
                          <thead style="background-color: blue;color:white; font-weight: bold;">
                            <tr>
                              <th style="width:35px"><h5 align="center">NIT</h5></th>
                              <th style="width:35px"><h5 align="center">Nombre NIT</h5></th>
                              <th style="width:10px"><h5 align="center">Pasaje Bs</h5></th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr>
                              <td style="width:135px"><input class="form-control"  type="text" value='"""+str(nit)+"""' name="nit" style="text-align:center" disabled required/></td>
                              <td><input class="form-control" type="text" style="text-align:center" value='"""+str(nombre_nit)+"""' name="nombrenit" disabled required /></td>
                              <td><center><input class="form-control" type="text" style="text-align:center"  name="monto" value='"""+str(pasaje)+"""' disabled required/></center></td>
                            </tr>
                          </tbody>
                        </table> 
                      </td>
                    </tr>
                    <tr>
                      <td>
                        <table id="example1" class="table table-bordered table-striped">
                          <thead style="background-color: blue;color:white; font-weight: bold;">
                            <tr>
                              <th style="width:35px"><h5 align="center">Asiento</h5></th>
                              <th style="width:135px"><h5 align="center">C.i</h5></th>
                              <th><h5 align="center">Nombre</h5></th>
                              <th><h5 align="center">Apellidos</h5></th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr>
                              <td><input type="hidden" name="asiento" value='"""+str(asiento)+"""'/><input class="form-control" type="text" value='"""+str(asiento)+"""' style="text-align:center" disabled/></td>
                              <td><input class="form-control" type="text" style="text-align:center" name="ci" value='"""+str(ci)+"""' disabled required/></td>
                              <td><input class="form-control" type="text" style="text-align:center" name="nombre" value='"""+str(nombre)+"""' disabled required/></td>
                              <td><input class="form-control" type="text" style="text-align:center" name="apellidos" value='"""+str(apellidos)+"""' disabled required/></td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                      </table>

                    <div id="datos">
                      <table width="100%" style="background:rgba(0,0,255,0.6);">
                        <tr>
                          <td>
                            <center>
                            <table id="example1" class="table table-bordered table-striped" style="width:335px; background:rgba(0,0,255,0.6);">
                              <thead>
                                <tr>
                                  <th style="width:15px"  bgcolor="blue" style="color:white; font-weight: bold;">
                                    <h5 align="center" style="color:white;">USUARIO</h5>
                                  </th>
                                  <th style="width:135px">
                                    <input class="form-control" style="background:white;" type="text" value='"""+str(usu)+"""' disabled/>
                                  </th>
                                </tr>
                              </thead>
                            </table>
                            </center>
                          </td>
                        </tr>
                      </table>
                    </div>
                    <div>
                      <div class="modal-footer">
                        <button type="button" data-dismiss="modal" aria-label="Close" class="btn bg-red waves-effect" onclick="cerrar(this)" id='"""+str(ide[1])+"""'><div class="demo-google-material-icon"> <i class="material-icons">close</i> <span class="icon-name">SALIR</span></div></button>
                      </div>
                    </div>
                  </div>
                </div>   
              </form>     
          </div>
      </div>
    </div>

""")
except:
  print("<script>location.href='../../error/error.py'</script>")