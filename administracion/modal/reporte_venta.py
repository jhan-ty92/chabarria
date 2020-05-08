#!C:\Python34\python   
import cgi
import os,sys,time
import pymysql
con=pymysql.connect(user="root",password="",host="",database="buses_chavarria")
try:
  form = cgi.FieldStorage()
  cod=form.getvalue('valor')
 
  pru=con.cursor()
  pru.execute("""select vpa.monto,p.nombre from venta_pasaje vpa
                          inner join usuario usup on vpa.cod_usuario=usup.cod
                          inner join programar_venta psb on psb.cod=vpa.cod_programacion
                          inner join bus b on b.cod=psb.cod_bus
                          inner join personal p on p.cod=usup.cod_personal 
                          where vpa.cod_programacion='"""+str(cod)+"' and vpa.cod_usuario<>'None' """)

  suma=""
  for art in pru:
    suma=suma+"<tr><td>"+str(art[0])+"</td><td>"+str(art[1])+"</td></tr>"


  print("""
<div class="modal" id="venta_reserva" tabindex="-1" role="dialog" aria-labellebdy="myModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-body">
        <center><table border=1 width='50%'>
        <tr><td>
        <center><table border=0>
          <tr><td><center><h5>TRANS TOURS CHAVARRIA S.R.L.</h5></center></td></tr>
          <tr>
          <td>
          <table>
          
            """+str(suma)+"""
          
          </table>
          </td></tr>
          <tr><td><div class="modal-footer">
        <button type="button" class="btn bg-indigo waves-effect" onclick="javascript:imprim1(imp1);"><i class='material-icons'>print</i></button>
      </div></td></tr>
        </table></center>
        </td></tr>
        </table></center>
      </div>
      
    </div>
  </div>
</div>
""")
except:
  print("<script>location.href='../../error/error.py'</script>")