import os,sys,time

def cabezera():
	print("""
<!DOCTYPE html>
<html>

<head>

    <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
    <title>UNSXX</title>
    <!-- Favicon-->
    
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Roboto:400,700&subset=latin,cyrillic-ext" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" type="text/css">
    <link media="all" type="text/css" rel="stylesheet" href="../public/css/icono.css">
    <link media="all" type="text/css" rel="stylesheet" href="../public/favicon.ico">
    <link media="all" type="text/css" rel="stylesheet" href="../public/plugins/bootstrap/css/bootstrap.css">
    <link media="all" type="text/css" rel="stylesheet" href="../public/plugins/node-waves/waves.css">
    <link media="all" type="text/css" rel="stylesheet" href="../public/plugins/animate-css/animate.css">
    <link media="all" type="text/css" rel="stylesheet" href="../public/plugins/jquery-datatable/skin/bootstrap/css/dataTables.bootstrap.css">
    <link media="all" type="text/css" rel="stylesheet" href="../public/css/style.css">
    <link media="all" type="text/css" rel="stylesheet" href="../public/css/themes/all-themes.css">
    <link media="all" type="text/css" rel="stylesheet" href="../public/plugins/animate-css/animate.css">
    <link media="all" type="text/css" rel="stylesheet" href="../public/plugins/sweetalert/sweetalert.css">
    <link href="../public/plugins/multi-select/css/multi-select.css" rel="stylesheet">



    <link href="../public/plugins/bootstrap/css/bootstrap.css" rel="stylesheet">
    <link href="../public/plugins/node-waves/waves.css" rel="stylesheet" />
    <link href="../public/plugins/animate-css/animate.css" rel="stylesheet" />
    <link href="../public/plugins/bootstrap-colorpicker/css/bootstrap-colorpicker.css" rel="stylesheet" />
    <link href="../public/plugins/dropzone/dropzone.css" rel="stylesheet">
    <link href="../public/plugins/multi-select/css/multi-select.css" rel="stylesheet">
    <link href="../public/plugins/jquery-spinner/css/bootstrap-spinner.css" rel="stylesheet">
    <link href="../public/plugins/bootstrap-tagsinput/bootstrap-tagsinput.css" rel="stylesheet">
    <link href="../public/plugins/bootstrap-select/css/bootstrap-select.css" rel="stylesheet" />
    <link href="../public/plugins/nouislider/nouislider.min.css" rel="stylesheet" />
    <link href="../public/css/style.css" rel="stylesheet">
    <link href="../public/css/themes/all-themes.css" rel="stylesheet" />

    
    <link href="../public/plugins/bootstrap-material-datetimepicker/css/bootstrap-material-datetimepicker.css" rel="stylesheet" />
    <link href="../public/plugins/waitme/waitMe.css" rel="stylesheet" />
    <link href="../public/plugins/bootstrap-select/css/bootstrap-select.css" rel="stylesheet" />

   

    <style>
.fullscreen-modal .modal-dialog {
  margin: 10px;
  margin-right:5px;
  margin-left:8px;
  width: 100%;
}
@media (min-width: 768px) {
  .fullscreen-modal .modal-dialog {
    width: 750px;
  }
}
@media (min-width: 992px) {
  .fullscreen-modal .modal-dialog {
    width: 970px;
  }
}
@media (min-width: 1200px) {
  .fullscreen-modal .modal-dialog {
     width: 98.50%;
  }
}
</style>

</head>
<body class="theme-red">
    <!-- Page Loader -->
    <div class="page-loader-wrapper">
        <div class="loader">
            <div class="preloader">
                <div class="spinner-layer pl-red">
                    <div class="circle-clipper left">
                        <div class="circle"></div>
                    </div>
                    <div class="circle-clipper right">
                        <div class="circle"></div>
                    </div>
                </div>
            </div>
            <p>cargando...</p>
        </div>
    </div>
    <div class="overlay"></div>
    <div class="search-bar">
        <div class="search-icon">
            <i class="material-icons">search</i>
        </div>
        <input type="text" placeholder="START TYPING...">
        <div class="close-search">
            <i class="material-icons">close</i>
        </div>
    </div>
    <!-- #END# Search Bar -->
    <!-- Top Bar -->
    <nav class="navbar">
        <div class="container-fluid">
            
    
             <div class="navbar-header">
                <a href="javascript:void(0);" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar-collapse" aria-expanded="false"></a>
                <a href="javascript:void(0);" class="bars"></a>

                <div class="container-fluid">
                    <img src="../public/images/fondotrasparente.png" width="17" height="10" alt="User" />
                    <img src="../public/images/trans.png" width="50" height="50" alt="User" />
                    <img src="../public/images/logoSiaa.png" width="150" height="50" alt="User" />
              </div>
            </div>



            <div class="collapse navbar-collapse" id="navbar-collapse">
                <ul class="nav navbar-nav navbar-right">
                    <li class="dropdown">
                        <a href="javascript:void(0);" class="dropdown-toggle" data-toggle="dropdown" role="button">
                            <i class="material-icons">notifications</i>        
                        </a>
                        <ul class="dropdown-menu">
                            <li class="header">NOTIFICACION</li>
                            
                            <li class="footer">
                                <a href="javascript:void(0);">Ver todas las Notificaciones</a>
                            </li>
                        </ul>
                    </li>
                    <li class="pull-right"><a href="javascript:void(0);" class="js-right-sidebar" data-close="true"><i class="material-icons">more_vert</i></a></li>
                </ul>
            </div>
        </div>
    </nav>
    <!-- #Top Bar -->
    <section>
        <!-- Left Sidebar -->
        <aside id="leftsidebar" class="sidebar">
             <!-- User Info -->
            <div class="user-info">
                <div class="image">
                  <img src="../public/images/user.jpg" width="35" height="35" alt="User" />
                </div>
                <div class="info-container">
                    <div class="name" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">On-line</div>
                        <div class="btn-group user-helper-dropdown">
                            <a href="#" class="btn btn-default">Salir</a>
                        </div>
                      
                    </div>
                </div>
            <!-- #User Info -->
            <!-- Menu -->
            <div class="menu">
                <ul class="list">
                    <li class="header">MENU DE NAVEGACION</li>

                    <li class="active">
                        <a href="index.py">
                            <i class="material-icons">home</i>
                            <span id="datos_d">Administracion """+str(time.localtime()[0])+"""</span>
                        </a>
                    </li>

                    <li class="active">
                        <a href="oficinas.py">
                            <i class="material-icons">location_city</i><span id="datos_d">Oficinas</span>
                        </a>
                    </li>

                    <li class="active">
                        <a href="bus.py">
                            <i class="material-icons">directions_bus</i>
                            <span id="datos_d">Buses</span>
                        </a>
                    </li>

                    <li class="active">
                        <a href="personal.py">
                            <i class="material-icons">people</i>
                            <span id="datos_d">Personal</span>
                        </a>
                    </li>

                    

                    <li class="active">
                        <a href="frecuencia.py">
                            <i class="material-icons">timer</i>
                            <span id="datos_d">Frecuencias</span>
                        </a>
                    </li>

                    <li class="active">
                        <a href="rutas.py">
                            <i class="material-icons">call_split</i>
                            <span id="datos_d">Rutas</span>
                        </a>
                    </li>

                    
                    <li class="active">
                        <a href="programacion.py">
                            <i class="material-icons">laptop_chromebook</i>
                            <span id="datos_d">Programar Venta Pasaje</span>
                        </a>
                    </li>

                    <li>
                        <a href="javascript:void(0);" class="menu-toggle">
                            <i class="material-icons">card_giftcard</i>
                            <span id="datos_d">Encomiendas</span>
                        </a>
                        <ul class="ml-menu">
                            <li>
                                <a href="#">
                                    <span>Recepcion</span>
                                </a>
                                <a href="#">
                                    <span>Entrega</span>
                                </a>
                            </li>
                        </ul>
                    </li>

                </ul>
            </div>
        </aside>
        <aside id="rightsidebar" class="right-sidebar">
            <ul class="nav nav-tabs tab-nav-right" role="tablist">
                <li role="presentation" class="active"><a href="#settings" data-toggle="tab">CONFIGURACIONES</a></li>
            </ul>
            <div class="tab-content">
                <div role="tabpanel" class="tab-pane fade in active in active" id="settings">
                    <div class="demo-settings">
                        <p>Configuracion</p>
                        
                    </div>
                </div>
            </div>
        </aside>
    </section>

		""")
def fin_cabezera():
	print("""

<script src="../public/plugins/jquery/jquery.min.js"></script>
<script src="../public/plugins/bootstrap/js/bootstrap.js"></script>
<script src="../public/plugins/jquery-slimscroll/jquery.slimscroll.js"></script>
<script src="../public/plugins/node-waves/waves.js"></script>
<script src="../public/js/pages/ui/tooltips-popovers.js"></script>
<script src="../public/plugins/jquery-datatable/jquery.dataTables.js"></script>
<script src="../public/plugins/jquery-datatable/skin/bootstrap/js/dataTables.bootstrap.js"></script>
<script src="../public/plugins/jquery-datatable/extensions/export/dataTables.buttons.min.js"></script>
<script src="../public/plugins/jquery-datatable/extensions/export/buttons.flash.min.js"></script>
<script src="../public/plugins/jquery-datatable/extensions/export/jszip.min.js"></script>
<script src="../public/plugins/jquery-datatable/extensions/export/pdfmake.min.js"></script>
<script src="../public/plugins/jquery-datatable/extensions/export/vfs_fonts.js"></script>
<script src="../public/plugins/jquery-datatable/extensions/export/buttons.html5.min.js"></script>
<script src="../public/plugins/jquery-datatable/extensions/export/buttons.print.min.js"></script>
<script src="../public/js/admin.js"></script>
<script src="../public/js/pages/tables/jquery-datatable.js"></script>
<script src="../public/js/demo.js"></script>

<script src="../public/plugins/sweetalert/sweetalert.min.js"></script>
<script src="../public/plugins/multi-select/js/jquery.multi-select.js"></script>
<script src="../public/plugins/bootstrap-notify/bootstrap-notify.js"></script>
<script src="../public/js/validacion.js"></script>
<script src="../public/plugins/jquery-validation/jquery.validate.js"></script>
<script src="../public/plugins/jquery-validation/localization/messages_es.js"></script>
<script src="../public/js/jquery.printPage.js"></script>
<script src="../public/plugins/bootstrap-select/js/bootstrap-select.js"></script>
<script src="../public/plugins/bootstrap-colorpicker/js/bootstrap-colorpicker.js"></script>
<script src="../public/plugins/dropzone/dropzone.js"></script>
<script src="../public/plugins/jquery-inputmask/jquery.inputmask.bundle.js"></script>
<script src="../public/plugins/multi-select/js/jquery.multi-select.js"></script>
<script src="../public/plugins/jquery-spinner/js/jquery.spinner.js"></script>
<script src="../public/plugins/bootstrap-tagsinput/bootstrap-tagsinput.js"></script>
<script src="../public/plugins/nouislider/nouislider.js"></script>
<script src="../public/js/pages/forms/advanced-form-elements.js"></script>


    <script src="../public/plugins/bootstrap-select/js/bootstrap-select.js"></script>
    <script src="../public/plugins/jquery-slimscroll/jquery.slimscroll.js"></script>
    <script src="../public/plugins/node-waves/waves.js"></script>
    <script src="../public/plugins/autosize/autosize.js"></script>
    <script src="../public/plugins/momentjs/moment.js"></script>
    <script src="../public/plugins/bootstrap-material-datetimepicker/js/bootstrap-material-datetimepicker.js"></script>
    <script src="../public/js/pages/forms/basic-form-elements.js"></script>

</body>
</html>
<script>
    function capa(){
    var a=document.getElementById('entrada').value;
    var string="";
    if(a==="4"){
        string=string+'<br><div class="box-body"><label>NUMERO DE ASIENTOS:</label><div class="row"><div class="col-sm-3"><input class="form-control" type="text" name="a1" placeholder="Primer piso" required></div><div class="col-sm-3"><input class="form-control" type="text" name="a2" placeholder="Segundo piso" required></div><div class="col-sm-3"><input class="form-control" type="text" name="a3" placeholder="Tercer piso" required></div><div class="col-sm-3"><input class="form-control" type="text" name="a4" placeholder="Cuarto piso" required></div></div></div><br><div class="box-body"><label>NUMERO DE FILAS:</label><div class="row"><div class="col-sm-3"><input class="form-control" type="text" name="f1" placeholder="Primer piso" required></div><div class="col-sm-3"><input class="form-control" type="text" name="f2" placeholder="Segundo piso" required></div><div class="col-sm-3"><input class="form-control" type="text" name="f3" placeholder="Tercer piso" required></div><div class="col-sm-3"><input class="form-control" type="text" name="f4"  placeholder="Cuarto piso" required></div></div></div>';
    }
    else if(a==="3"){
        string=string+'<br><div class="box-body"><label>NUMERO DE ASIENTOS:</label><div class="row"><div class="col-sm-3"><input class="form-control" type="text" name="a1" placeholder="Primer piso" required></div><div class="col-sm-3"><input class="form-control" type="text" name="a2" placeholder="Segundo piso" required></div><div class="col-sm-3"><input class="form-control" type="text" name="a3" placeholder="Tercer piso" required></div></div></div><br><div class="box-body"><label>NUMERO DE FILAS:</label><div class="row"><div class="col-sm-3"><input class="form-control" type="text" name="f1" placeholder="Primer piso" required></div><div class="col-sm-3"><input class="form-control" type="text" name="f2" placeholder="Segundo piso" required></div><div class="col-sm-3"><input class="form-control" type="text" name="f3" placeholder="Tercer piso" required></div></div></div>';
    }
    else if(a==="2"){
        string=string+'<br><div class="box-body"><label>NUMERO DE ASIENTOS:</label><div class="row"><div class="col-sm-3"><input class="form-control" type="text" name="a1" placeholder="Primer piso" required></div><div class="col-sm-3"><input class="form-control" type="text" name="a2" placeholder="Segundo piso" required></div></div></div><br><div class="box-body"><label>NUMERO DE FILAS:</label><div class="row"><div class="col-sm-3"><input class="form-control" type="text" name="f1" placeholder="Primer piso" required></div><div class="col-sm-3"><input class="form-control" type="text" name="f2" placeholder="Segundo piso" required></div></div></div>';
    }
    else if(a==="1"){
        string=string+'<br><div class="box-body"><label>NUMERO DE ASIENTOS:</label><div class="row"><div class="col-sm-3"><input class="form-control" type="text" name="a1" placeholder="Primer piso" required></div></div></div><br><div class="box-body"><label>NUMERO DE FILAS:</label><div class="row"><div class="col-sm-3"><input class="form-control" type="text" name="f1" placeholder="Primer piso" required></div></div></div>';
    }
    document.getElementById('salida').innerHTML=string;
    }
</script>
		""")