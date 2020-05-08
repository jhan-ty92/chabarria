#!C:\Python34\python   
import cgi
import os,sys,time
import pymysql
form = cgi.FieldStorage()

cod=form.getvalue('valor')

con=pymysql.connect(user="root",password="",host="",database="buses_chavarria")


mostrarAsiento=con.cursor()
buscar=mostrarAsiento.execute("select * from venta_pasaje where cod_programacion="+str(cod)+" and accion=1 and cod_usuario<>'None' order by nombre ")
mostrarLibres=""
teo=1
if buscar!=0:
  for art in mostrarAsiento:
    mostrarLibres=mostrarLibres+"""
                  <tr>
                    <th><center><font size=1>"""+str(teo)+"""</center></th>
                    <td><center><font size=1>"""+str(art[2])+"  "+str(art[3])+"""</center></td>
                    <td><center><font size=1>"""+str(art[1])+"""</center></td>
                    <td><center><font size=1>"""+str(art[8])+"""</center></td>
                  </tr>"""
    teo=teo+1
else:
  mostrarLibres=mostrarLibres+"""
                  <tr>
                    <th><font size=1><center>#</center></th>
                    <td><font size=1></td>
                    <td><font size=1></td>
                    <td><font size=1></td>
                  </tr>"""


cursor=con.cursor()
cursor.execute("""select pr.cod,pr.cod_bus,pr.frecha_viaje,f.fecuencia,b.placa,b.tipo,of1.nombre,of2.nombre,b.marca,b.capacidad,cho.licencia,cho1.licencia,choper.nombre,choper.apellidos,choper1.nombre,choper1.apellidos,cho.cod_personal,cho1.cod_personal,pr.pasajes,ru.oficina_origen,ru.oficina_destino,rf.cod_ruta,rf.cod_frecuencia FROM programar_venta pr
              inner join bus b on pr.cod_bus=b.cod
              inner join personal_bus cho on cho.cod=pr.chofer
              inner join personal_bus cho1 on cho1.cod=pr.choferaux
              inner join personal choper on choper.cod=cho.cod_personal
              inner join personal choper1 on choper1.cod=cho1.cod_personal
              inner join ruta_frecuencia rf on pr.cod_ruta_frecuencia=rf.cod
              inner join frecuencia f on rf.cod_frecuencia=f.cod
              inner join ruta ru on rf.cod_ruta=ru.cod
              inner join oficina of1 on ru.oficina_origen=of1.cod
              inner join oficina of2 on ru.oficina_destino=of2.cod
              WHERE pr.cod="""+str(cod)+"""""")


codprogramacion=""
codbus=""
fecha=""
hora=""
placa=""
tipo=""
o=""
d=""
marca=""
capacidad=""
li1=""
li2=""
cho1=""
cho2=""
n2="2:"
for art in cursor:
  codprogramacion=codprogramacion+str(art[0])
  
  codbus=codbus+str(art[1])

  fecha=fecha+str(art[2])
  hora=hora+str(art[3])
  placa=placa+str(art[4])
  tipo=tipo+str(art[5])
  o=o+str(art[6])
  d=d+str(art[7])
  marca=marca+str(art[8])
  capacidad=capacidad+str(art[9])
  li1=li1+str(art[10])
  li2=li2+str(art[11])
  cho1=cho1+str(art[12])+"  "+str(art[13])
  cho2=cho2+str(art[14])+"  "+str(art[15])
  tripu="2"
  if li1==li2:
    li2=""
    cho2=""
    n2=""
    tripu="1"

    
  


print("""
<div class="modal fullscreen-modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" style=" opacity:0.99;">  
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times</span>
          </button>
        </div>
        <div class="modal-body">  
          <main style="margin: 25px">
            <div class="">
              <div class="row">
              <div class="table-responsive">  
              <div id="imp1">
              <center>
                <table style="border-collapse: collapse;" border="1" width="80%"> 
                  <tr>
                    <th colspan=8 width="100%"><center><font size=2>TRANS TOURS CHAVARRIA S.R.L.</center></th>
                  </tr>
                  <tr>
                    <th colspan=8 width="100%"><center><font size=2>NOMINA DE PASAJEROS CON DESTINO A LA CIUDAD DE """+str(d).upper()+"""</center></th>
                  </tr>
                  <tr>
                    <th colspan=4 width="50%"><center><font size=1>DATOS DE VIAJE</center></th>
                    <th colspan=4 width="50%"><center><font size=1>DATOS DE VEHICULOS</center></th>
                  </tr>
                  <tr>
                    <th width="13%" ><font size=1 style="margin: 8px;">CIUDAD ORIGEN:</th>
                    <td><center><font size=1>"""+str(o)+"""</center></td>
                    <th><font size=1 style="margin: 8px;">PASAJEROS:</th>
                    <td width="3%"><center><font size=1>"""+str(int(teo)-1)+"""</center></td>
                    <th><center><font size=1>MARCA:</center></th>
                    <th><center><font size=1>PLACA</center></th>
                    <th><center><font size=1>TIPO DE BUS</center></th>
                    <th width="15%"><center><font size=1>No DE ASIENTOS</center></th>
                  </tr>
                  <tr>
                    <th width="13%"><font size=1 style="margin: 8px;">CIUDAD DESTINO:</th>
                    <td width="13%"><center><font size=1>"""+str(d)+"""</center></td>
                    <th width="10%"><font size=1 style="margin: 8px;">TRIPULACION:</th>
                    <td><center><font size=1>"""+str(tripu)+"""</center></td>
                    <td><center><font size=1>"""+str(marca)+"""</center></td>
                    <td><center><font size=1>"""+str(placa)+"""</center></td>
                    <td><center><font size=1>"""+str(tipo)+"""</center></td>
                    <td><center><font size=1>"""+str(capacidad)+"""</center></td>
                  </tr>
                  <tr>
                    <th><font size=1 style="margin: 8px;">FECHA DE SALIDA:</th>
                    <td><center><font size=1>"""+str(fecha)+"""</center></td>
                    <th><font size=1 style="margin: 8px;">TOTAL:</th>
                    <td><center><font size=1>"""+str(int(teo)-1+int(tripu))+"""</center></td>
                    <th colspan="3"><center><font size=1>CONDUCTORES: NOMBRES Y APELLIDOS</center></th>
                    <th><center><font size=1>No LICENCIA DE CONDUCIR</center></th>
                  </tr>
                  <tr>
                    <th><font size=1 style="margin: 8px;">HORA DE SALIDA:</th>
                    <td><center><font size=1>"""+str(hora)+"""</center></td>
                    <td><font size=1></td>
                    <td><font size=1></td>
                    <td colspan="3"><font size=1 style="margin: 8px;">   1:  """+str(cho1)+"""</td>
                    <td><center><font size=1 >"""+str(li1)+"""</center></td>
                  </tr>
                  <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td colspan="3"><font size=1 style="margin: 8px;">   """+str(n2)+"""  """+str(cho2)+"""</td>
                    <td><center><font size=1>"""+str(li2)+"""</center></td>
                  </tr>
                </table>
                <br>
                <table style="border-collapse: collapse;" border="1"; width="80%"> 
                  <tr>
                    <th width="1%"><center><font size=1>No</center></th>
                    <th width="5%"><center><font size=1>NOMBRE Y APELLIDOS</center></th>
                    <th width="5%"><center><font size=1><font size=1>CI<center></th>
                    <th width="1%"><center><font size=1>No ASIENTOS</center></th>
                  </tr>"""+str(mostrarLibres)+"""             
                </table>
              </center>
              </div>
              </div>

              </div>
            </div>
          </main>
        </div>
        <div class="modal-footer">
           <button type="button" class="btn bg-indigo waves-effect" onclick="javascript:imprim1(imp1);"><i class='material-icons'>print</i>Imprimir</button>
        </div>
      </div>
    </div>
  </div>
""")