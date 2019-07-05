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
            <p>
              <strong>1. Seleccionar Archivo:</strong> Dar click en el botón
              <span class>
                <button class="btn btn-primary btn-choose" type="button">
                  <i class="fas fa-upload"></i>
                </button>
              </span> con el cual se abrirá el explorador de archivos permitiendo seleccionar el archivo CSV que se desea agregar.
            </p>
            <p>
              <strong>2. Nombre columna email:</strong> Es necesario especificar el nombre exacto de la columna en la cual se encuentra almacenado el email que se desea analizar y modificar.
            </p>
            <p>
              <strong>3. Delimitador:</strong> Es necesario seleccionar el delimitador que posee el archivo puede ser ("," ";" "|").
            </p>
            <p>
              <strong>4. Ejecutar:</strong> Al presionar el botón <button type="button" class="btn btn-outline-success">
            <i class="fas fa-caret-right"></i> Ejecutar</button> se iniciará el procesamiento del archivo seleccionado detallando el porcentaje del progreso en la ejecución.
            </p>
            <p>
              <strong>5. Descarga:</strong> Procesado el archivo permitirá descargar el archivo modificado.
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
