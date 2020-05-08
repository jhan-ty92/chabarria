#!C:\Python34\python
print ("Content-Type:text/html \r\n\r\n")
print("""
<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>Error - Pagina no encontrada</title>

        <!-- Fonts -->
        <link href="https://fonts.googleapis.com/css?family=Oswald" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.min.css">
        <!-- Styles -->
        <style>
            html, body {
               background-color: black;
                color: #fff;
                font-family: 'Oswald', sans-serif;
                font-weight: 100;
                height: 100vh;
                margin: 0;
            }

            .full-height {
                height: 100vh;
            }

            .flex-center {
                align-items: center;
                display: flex;
                justify-content: center;
            }

            .position-ref {
                position: relative;
            }

            .top-right {
                position: absolute;
                right: 10px;
                top: 18px;
            }

            .content {
                text-align: center;
            }

            .title {
                font-size: 84px;
            }
            .m-b-md {
                margin-bottom: 30px;
            }
        </style>
    </head>
    <body>
        <div class="container flex-center position-ref full-height">
            <div class="row">
                <div class="col-md-12">
                    <div class="content">
                        <img src="../public/images/tras.png" width="130" class="img img-responsive animated flip infinite">
                        <h2>Que intentas hacer !</h2>
                        <H1 style="text-transform: uppercase ;" >La pagina que intentas solicitar no esta en el servidor (Error 404!)</H1>
                        <a  href="#"> volver  al pagina de Inicio</a>
                    </div>
                </div>
            </div>
        </div>
    </body>
</html>""")