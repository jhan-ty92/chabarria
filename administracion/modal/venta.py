#!C:\Python34\python   
import cgi
import os,sys,time
import pymysql
form = cgi.FieldStorage()

cod=form.getvalue('valor')

con=pymysql.connect(user="root",password="",host="",database="buses_chavarria")

teo=2

cursor=con.cursor()
cursor.execute("""select pr.cod,pr.cod_bus,pr.frecha_viaje,f.fecuencia,b.placa,b.tipo,of1.nombre,of2.nombre,b.marca,b.capacidad,cho.licencia,cho1.licencia,choper.nombre,choper.apellidos,choper1.nombre,choper1.apellidos,cho.cod_personal,cho1.cod_personal,pr.pasajes,ru.oficina_origen,ru.oficina_destino,rf.cod_ruta,rf.cod_frecuencia,b.mapeo,b.piso,b.asientopiso,b.filapiso,pr.pasajes FROM programar_venta pr
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


ven=con.cursor()
total=ven.execute("select * from venta_pasaje where cod_programacion="+str(cod))
reser=con.cursor()
venta=reser.execute("select * from venta_pasaje where cod_programacion="+str(cod)+" and cod_usuario<>'None'")
reserva=total-venta;


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
n2="2"

asientos=""
filas=""

piso=""
mapeo=""

pasajes=""
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

  mapeo=mapeo+str(art[23])
  piso=piso+str(art[24])
  asientos=asientos+str(art[25])
  filas=filas+str(art[26])

  pasajes=pasajes+str(art[27])

  tripu="2"
  if li1==li2:
    li2=""
    cho2=""
    n2=""
    tripu="1"


a=asientos.split("-");
f=filas.split("-");

cad=""    
cortar=mapeo.split("&")
ccont=0
cad=cad+"<table>"

monto=pasajes.split("-")
libre=int(capacidad)-total

for k in range(0,int(piso)):
  cad=cad+"<tr><td>"
  a=cortar[k]
  if a[0:1]=="-":
    a=a[1:len(a)]
  if a[len(a)-1:len(a)]=="-":
        a=a[0:len(a)-1]

  fil=a.split("-")
  pp=0
  p=0
  for i in range(0,len(fil)): 
    if p==1*int(f[k])+1:
      break;
    if(fil[i]=="1"  or fil[i]=="2"  or fil[i]=="3"  or fil[i]=="4"  or fil[i]=="5"  or fil[i]=="6"  or fil[i]=="7"  or fil[i]=="8"  or fil[i]=="9"  or fil[i]=="10"or
       fil[i]=="11" or fil[i]=="12" or fil[i]=="13" or fil[i]=="14" or fil[i]=="15" or fil[i]=="16" or fil[i]=="17" or fil[i]=="18" or fil[i]=="19" or fil[i]=="20"or
       fil[i]=="21" or fil[i]=="22" or fil[i]=="23" or fil[i]=="24" or fil[i]=="25" or fil[i]=="26" or fil[i]=="27" or fil[i]=="28" or fil[i]=="29" or fil[i]=="30"or
       fil[i]=="31" or fil[i]=="32" or fil[i]=="33" or fil[i]=="34" or fil[i]=="35" or fil[i]=="36" or fil[i]=="37" or fil[i]=="38" or fil[i]=="39" or fil[i]=="40"or
       fil[i]=="41" or fil[i]=="42" or fil[i]=="43" or fil[i]=="44" or fil[i]=="45" or fil[i]=="46" or fil[i]=="47" or fil[i]=="48" or fil[i]=="49" or fil[i]=="50"or
       fil[i]=="51" or fil[i]=="52" or fil[i]=="53" or fil[i]=="54" or fil[i]=="55" or fil[i]=="56" or fil[i]=="57" or fil[i]=="58" or fil[i]=="59" or fil[i]=="60"or
       fil[i]=="61" or fil[i]=="62" or fil[i]=="63" or fil[i]=="64" or fil[i]=="65" or fil[i]=="66" or fil[i]=="67" or fil[i]=="68" or fil[i]=="69" or fil[i]=="70"or
       fil[i]=="71" or fil[i]=="72" or fil[i]=="73" or fil[i]=="74" or fil[i]=="75" or fil[i]=="76" or fil[i]=="77" or fil[i]=="78" or fil[i]=="79" or fil[i]=="80"or
       fil[i]=="81" or fil[i]=="82" or fil[i]=="83" or fil[i]=="84" or fil[i]=="85" or fil[i]=="86" or fil[i]=="87" or fil[i]=="88" or fil[i]=="89" or fil[i]=="90"or
       fil[i]=="91" or fil[i]=="92" or fil[i]=="93" or fil[i]=="94" or fil[i]=="95" or fil[i]=="96" or fil[i]=="97" or fil[i]=="98" or fil[i]=="99" or fil[i]=="100" or

       fil[i]=="1Z"  or fil[i]=="2Z"  or fil[i]=="3Z"  or fil[i]=="4Z"  or fil[i]=="5Z"  or fil[i]=="6Z"  or fil[i]=="7Z"  or fil[i]=="8Z"  or fil[i]=="9Z"  or fil[i]=="10Z"or
       fil[i]=="11Z" or fil[i]=="12Z" or fil[i]=="13Z" or fil[i]=="14Z" or fil[i]=="15Z" or fil[i]=="16Z" or fil[i]=="17Z" or fil[i]=="18Z" or fil[i]=="19Z" or fil[i]=="20Z"or
       fil[i]=="21Z" or fil[i]=="22Z" or fil[i]=="23Z" or fil[i]=="24Z" or fil[i]=="25Z" or fil[i]=="26Z" or fil[i]=="27Z" or fil[i]=="28Z" or fil[i]=="29Z" or fil[i]=="30Z"or
       fil[i]=="31Z" or fil[i]=="32Z" or fil[i]=="33Z" or fil[i]=="34Z" or fil[i]=="35Z" or fil[i]=="36Z" or fil[i]=="37Z" or fil[i]=="38Z" or fil[i]=="39Z" or fil[i]=="40Z"or
       fil[i]=="41Z" or fil[i]=="42Z" or fil[i]=="43Z" or fil[i]=="44Z" or fil[i]=="45Z" or fil[i]=="46Z" or fil[i]=="47Z" or fil[i]=="48Z" or fil[i]=="49Z" or fil[i]=="50Z"or
       fil[i]=="51Z" or fil[i]=="52Z" or fil[i]=="53Z" or fil[i]=="54Z" or fil[i]=="55Z" or fil[i]=="56Z" or fil[i]=="57Z" or fil[i]=="58Z" or fil[i]=="59Z" or fil[i]=="60Z"or
       fil[i]=="61Z" or fil[i]=="62Z" or fil[i]=="63Z" or fil[i]=="64Z" or fil[i]=="65Z" or fil[i]=="66Z" or fil[i]=="67Z" or fil[i]=="68Z" or fil[i]=="69Z" or fil[i]=="70Z"or
       fil[i]=="71Z" or fil[i]=="72Z" or fil[i]=="73Z" or fil[i]=="74Z" or fil[i]=="75Z" or fil[i]=="76Z" or fil[i]=="77Z" or fil[i]=="78Z" or fil[i]=="79Z" or fil[i]=="80Z"or
       fil[i]=="81Z" or fil[i]=="82Z" or fil[i]=="83Z" or fil[i]=="84Z" or fil[i]=="85Z" or fil[i]=="86Z" or fil[i]=="87Z" or fil[i]=="88Z" or fil[i]=="89Z" or fil[i]=="90Z"or
       fil[i]=="91Z" or fil[i]=="92Z" or fil[i]=="93Z" or fil[i]=="94Z" or fil[i]=="95Z" or fil[i]=="96Z" or fil[i]=="97Z" or fil[i]=="98Z" or fil[i]=="99Z" or fil[i]=="100Z"):
      p=p+1
    pp=pp+1
  pp=pp-1
  ff=len(fil)/pp
  if((len(fil)/pp)!=round(len(fil)/pp)):
    ff=round(len(fil)/pp+1)
  if(k==0):
    if(piso=="1"):
      cad=cad+"<br>"
    else:
      cad=cad+"<br> PRIMER PISO"
    cad=cad+"<table style='margin: 5px;' width='80%'><tr><td rowspan='2' width='10' style='background: url(../public/images/c1.png) no-repeat center center;background-size:100% 100%;' ><img src='../public/images/v.png' width='165'></td></tr><tr><td style='background: url(../public/images/t1.png) no-repeat center center;background-size:100% 100%;'><table style='margin-right: 18px;margin-left: 18px;'>"                
  else:
    cad=cad+"<br>SEGUNDO PISO<table style='margin: 5px;' width='100%'><tr><td width='100%' style='background: url(../public/images/todo1.png) no-repeat center center;background-size:100% 100%;'><center><table style='margin-right: 18px;margin-left: 18px;'>"
             
  cont=0;
  
  matriz=[] 
  for i in range(int(ff)):
    matriz.append([]) 
    for j in range(pp): 
      if(cont<len(fil)):
          if fil[cont]=='TV':
            matriz[i].append("<td><img src='../public/images/tv1.png' width='45' height='45'></td>")
          elif fil[cont]=='V':
            matriz[i].append("<td><img src='../public/images/v.png' width='45' height='45'></td>")
          elif fil[cont]=='ES' or fil[cont]=='E':
            matriz[i].append("<td><center><img src='../public/images/es1.png' width='45' height='55'></center></td>")
          elif fil[cont]=='BA' or fil[cont]=='B':
            matriz[i].append("<td><input type='hidden' name='fc"+str(ccont)+"' value='BA'><img src='../public/images/ba1.png' width='45' height='45'></td>")
          else:
            pru=fil[cont]
            if pru[len(pru)-1:len(pru)]=="Z":
              matriz[i].append("<td><table style='margin-right: 8px;' height=10><tr><td><h5>"+str(pru[0:len(pru)-1])+"</h5><p><input id='"+str(pru[0:len(pru)-1])+"' class='filled-in chk-col-indigo' type='checkbox' value='X"+str(pru[0:len(pru)-1])+"' disabled checked><label for='"+str(pru[0:len(pru)-1])+"'><strong></strong><em></em></label></td><td><img src='../public/images/a2.png' width='45' height='50'></td></tr></table></td>")
              libre=libre-1
            else:

              busAs=con.cursor()
              bus=busAs.execute("select * from venta_pasaje WHERE cod_programacion= '"+str(cod)+"' AND asiento='"+str(pru).strip()+"' AND accion=1")
              if bus!=0:
                op=""
                for art in busAs:
                  op=str(art[7])
                if op=="None":
                  matriz[i].append("<td><table style='margin-right: 8px;' height=10><tr><td><h5>"+str(pru)+"</h5><p><input id='0"+str(pru)+"' class='filled-in chk-col-orange' type='checkbox' value='Z"+str(pru)+"' disabled checked><label for='0"+str(pru)+"'><strong></strong><em></em></label></td><td><a data-toggle='modal' data-target='#venta_pasaje' onclick='metodo_venta(this)' id='Z"+str(pru)+"-"+str(cod)+"-"+str(monto[k])+"'><img src='../public/images/a1.png' width='45' height='50'></a></td></tr></table></td>")
                else:
                  matriz[i].append("<td><table style='margin-right: 8px;' height=10><tr><td><h5>"+str(pru)+"</h5><p><input id='0"+str(pru)+"' class='filled-in chk-col-red' type='checkbox' value='Z"+str(pru)+"' disabled checked><label for='0"+str(pru)+"'><strong></strong><em></em></label></td><td><a data-toggle='modal' data-target='#venta_pasaje' onclick='metodo_venta(this)' id='Z"+str(pru)+"-"+str(cod)+"-"+str(monto[k])+"'><img src='../public/images/a3.png' width='45' height='50'></a></td></tr></table></td>")
              else:
                matriz[i].append("<td><table style='margin-right: 8px;' height=10><tr><td><h5>"+str(pru)+"</h5><p><input id='0"+str(pru)+"' class='filled-in chk-col-green' type='checkbox' value='"+str(pru)+"'><label for='0"+str(pru)+"'><strong></strong><em></em></label></td><td><a data-toggle='modal' data-target='#venta_pasaje' onclick='metodo_venta(this)' id='"+str(pru)+"-"+str(cod)+"-"+str(monto[k])+"'><img src='../public/images/a4.png' width='45' height='50'></a></td></tr></table></td>")
          ccont=ccont+1
      else:
        matriz[i].append("<td><img src='../public/images/v.png' width='45' height='45'></td>")
      cont=cont+1
  ccont=ccont+1;
  j=int(pp)-1
  while j>=0: 
    cad=cad+"<tr>"
    for i in range(int(ff)): 
      cad=cad+matriz[i][j]
    cad=cad+"</tr>"
    j=j-1
  if(k==0):
    cad=cad+"</table></td></tr></table>"
  else:
    cad=cad+"</table></table>"

  cad=cad+"</td></tr>"
cad=cad+"</table>"
print("""
<div class="modal fullscreen-modal fade" id="venta" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" data-backdrop="static" data-keyboard="false" style=" opacity:0.99;">  
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close"  onclick="setTimeout(function(){location.reload();}, 1);">
            <span aria-hidden="true">&times</span>
          </button>
        </div>
        <div class="modal-body">  
          <main style="margin: 25px">
            <div class="">
              <div class="row">
                <center><font size=6>TRANS TOURS CHAVARRIA S.R.L.</font></center>
                                <center>
                <div class="table-responsive">
                <table style="border-collapse: collapse;" border="1" width="100%"> 
                  <tr>
                    <th colspan=4 width="50%"><center><font size=2>DATOS DE VIAJE</center></th>
                    <th colspan=4 width="50%"><center><font size=2>DATOS DE VEHICULOS</center></th>
                  </tr>
                  <tr>
                    <th><center><font size=2>CIUDAD ORIGEN:</center></th>
                    <th><center><font size=2>CIUDAD DESTINO:</center></th>
                    <th><center><font size=2 style="margin: 8px;">FECHA:</center></th>
                    <th><center><font size=2 style="margin: 8px;">HORA:</th></center>
                    <th><center><font size=2>MARCA:</center></th>
                    <th><center><font size=2>PLACA</center></th>
                    <th><center><font size=2>TIPO DE BUS</center></th>
                    <th width="15%"><center><font size=2>CAPACIDAD</center></th>
                  </tr>
                  <tr>     
                    <td><center><h5>"""+str(o)+"""</h5></center></td>
                    <td width="13%"><center><h5>"""+str(d)+"""</h5></center></td>
                    <td><center><h5>"""+str(fecha)+"""</h5></center></td>
                    <td><center><h5>"""+str(hora)+"""</h5></center></td>
                
                    <td><center><h5>"""+str(marca)+"""</h5></center></td>
                    <td><center><h5>"""+str(placa)+"""</h5></center></td>
                    <td><center><h5>"""+str(tipo)+"""</h5></center></td>
                    <td><center><h5>"""+str(capacidad)+"""</h5></center></td>
                  </tr>
                </table>
                </div>
                </center>
                <div class="box-body">
                    <div class="row">
                        <div class="col-sm-3">
                <br>
                         <center>
                <div class="table-responsive">
                <table style="border-collapse: collapse;" border="1" width="100%"> 
                  <tr>
                    <th width="20%"><center><font size=1>LIBRES</center></th>
                    <th width="20%"><center><font size=1>VENDIDOS</center></th>
                    <th width="20%"><center><font size=1>RESERVADOS</center></th>
                  </tr>
                  <tr>
                    <td><center><h5 style="color:green;">"""+str(libre)+"""</h5></center></td>
                    <td><center><h5 style="color:red;">"""+str(venta)+"""</h5></center></td>
                    <td><center><h5 style="color:orange;">"""+str(reserva)+"""</h5></center></td>
                  </tr>
                </table>
                </div>
                </center>
                <br>
                 <br>
                <center>
                <div class="table-responsive">
                <table style="border-collapse: collapse;" width="80%"> 
                  <tr>
                    <td width="15%"><center><h5 style="color:green;">LIBRE</h5></center></td>
                    <td ><center><img src='../public/images/s4.png' width='65' height='65'></center></td>
                  </tr>
                  <tr>
                    <td width="15%"><center><h5 style="color:red;">VENDIDO</h5></center></td>
                    <td><center><img src='../public/images/s3.png' width='65' height='65'></center></td>
                  </tr>
                  <tr>
                    <td width="15%"><center><h5 style="color:orange;">RESERVADO</h5></center></td>
                    <td><center><img src='../public/images/s1.png' width='65' height='65'></center></td>
                  </tr>
                  <tr>
                    <td width="15%"><center><h5 style="color:blue;">INHABIL</h5></center></td>
                    <td><center><img src='../public/images/s2.png' width='65' height='65'></center></td>
                  </tr>
                </table>
                </div>
                </center>
              
                </div>
                    
                <div class="col-sm-9">
                  <div class="table-responsive"><center>
                  """+str(cad)+"""
                  </center></div>
                </div>
                </div>
                </div>

              </div>
            </div>
          </main>
        </div>
        <div class="modal-footer">
           <button type="button" class="btn bg-red waves-effect" onclick="setTimeout(function(){location.reload();}, 1);">
           <i class='material-icons'>clear</i>Salir
           </button>
        </div>
      </div>
    </div>
  </div>
""")