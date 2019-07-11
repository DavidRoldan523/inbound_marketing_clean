<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand animated heartBeat ml-3" href="#">
        <i class="fas fa-campground"></i> Inbound | Email
      </a>
      <!-- <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>-->
      <div class="collapse navbar-collapse d-flex justify-content-end" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a class="nav-link" data-toggle="modal" data-target=".bd-example-modal-lg" href="#">
              <i class="far fa-question-circle fa-2x"></i>
              <span class="sr-only">(current)</span>
            </a>
          </li>
        </ul>
      </div>
    </nav>

    <!-- Large modal -->

    <div
      class="modal fade bd-example-modal-lg"
      tabindex="-1"
      role="dialog"
      aria-labelledby="myLargeModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Funcionamiento</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <div class="embed-responsive embed-responsive-16by9">              
              <iframe
                width="560"
                height="315"
                src="https://www.youtube.com/embed/OHy1yJr6EtQ"
                frameborder="0"
                allowfullscreen                
              ></iframe>
            </div>

            <p>
              <strong>1.  Sintaxis correo:</strong>              
            </p>
            <p>
               - Para la verificación de la sintaxis es necesario determinar que el correo se encuentre 
               dividido en (nombre de usuario, seguido de '@', finalizando con un dominio).         
            </p>     
            <p>
              - Nombre de usuario: El nombre de usuario no debe contener caracteres especiales ni espacios.
            </p>
            <p>
               - Debe contener un '@' después del nombre de usuario y antes del nombre del dominio sin espacios.
            </p>
              <strong>2. Dominio existente:</strong>
            <p>
               - Verificada la sintaxis del usuario se debe determinar que el dominio del correo exista y esté 
               escrito correctamente ejemplo: (gmail.com, hotmail.com, yahoo.com, outlook.com).
            </p>
          </div>
          <div class="modal-footer text-center">
            <button type="button" class="btn btn-primary" data-dismiss="modal">Entendido</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
    
<script>
export default {
  name: "Navbar"
};
$("#myModal").on("shown.bs.modal", function() {
  $("#myInput").trigger("focus");
});
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Fredoka+One&display=swap");

img {
  width: 100%;
  height: auto;
}

p {
  text-align: justify;
}

nav {
  font-family: "Fredoka One", cursive;
}

i {
  animation-duration: 2s;
  animation-delay: 0.5s;
  animation-iteration-count: inherit;
}

a:hover {
  animation-duration: 3s;
  animation-delay: 0.5;
  animation-iteration-count: infinite;
}
</style>
