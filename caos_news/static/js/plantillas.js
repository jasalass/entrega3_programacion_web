

const navbar = `<nav class="navbar navbar-expand-lg bg-dark navbar-dark fixed-top">
                    <div class="container-fluid">
                        <a class="navbar-brand" href="/index.html">
                            <img src="/img/logo.jpg" alt="Logo de Caos News" class="img-fluid rounded-circle" style="max-height: 50px;">
                        </a>
                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                            aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                            <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarNav">
                            <ul class="navbar-nav ml-auto">
                                <li class="nav-item">
                                    <a class="nav-link" href="/views/contacto.html">Contacto</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="/views/suscripcion.html">Suscripción</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="/views/login.html">Login</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="/views/busqueda.html">Busqueda</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link" href="/views/contacto-laboral.html">Trabaja con nosotros</a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </nav>`

const footer = `<div class="container">
                    <div class="row">
                        <div class="col-md-4">
                            <h5>Caos News</h5>
                            <p>Puedes contactarnos a través de:</p>
                            <ul class="list-unstyled">
                            <li><strong>Email:</strong> contacto@caosnews.com</li>
                            <li><strong>Teléfono:</strong> +1 234 567 8900</li>
                            </ul>
                        </div>
                        <div class="col-md-4">
                            <h5>Enlaces rápidos</h5>
                            <ul class="list-unstyled">
                                <li><a href="/views/contacto.html" class="text-white">Formulario de Contacto</a></li>
                                <li><a href="/views/contacto-laboral.html" class="text-white">Trabaja con nosotros</a></li>
                            </ul>
                        </div>
                        
                    </div>
                </div>`


$(document).ready(function(){
    $("header").html(navbar)
    $("footer").html(footer)
   
})

