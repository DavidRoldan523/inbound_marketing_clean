<template>
  <div>
    <div class="card">
      <div class="card-header text-center py-md-3">
        <img class="animated heartBeat" src="@/assets/martechlogo.png" alt />
      </div>
      <div class="card-body pt-1">
        <form id="formTest" method="POST" action="#" enctype="multipart/form-data">
          <!-- COMPONENT START -->
          <div class="archivo">
            <div class="form-group col-md-8">
              <div class="custom-file mt-2">
                <input type="file" class="custom-file-input" id="customFileLang" name="file" lang="es" />
                <label class="custom-file-label" for="customFileLang">Seleccionar Archivo</label>
              </div>
              <!-- <div class="input-group input-file" name="Fichier1">
                <span class="input-group-btn">
                  <button class="btn btn-primary btn-choose" type="button">
                    <i class="fas fa-upload"></i>
                  </button>
                </span>
                <input type="file" id="archivo" name="csv" class="form-control" placeholder="Selecciona Archivo CSV   " />
                <span class="input-group-btn">
                  <button class="btn btn-outline-warning btn-reset" type="button">Resetear</button>
                </span>
              </div>-->
            </div>
          </div>
          <div class="row justify-content-center mt-3">
            <div class="col-md-3">
              <label for>
                Nombre Columna Email
                <i
                  class="fas fa-question-circle fa-xs"
                  data-toggle="tooltip"
                  data-placement="top"
                  title="Tooltip on top"
                ></i>
              </label>
            </div>
            <div class="col-md-4">
              <input type="text" name="email_column_name" class="form-control" id placeholder />
            </div>
          </div>
          <div class="form-group row justify-content-center mt-3">
            <div class="col-md-3">
              <label for="exampleFormControlSelect1">
                Delimitador
                <i
                  class="fas fa-question-circle fa-xs"
                  data-toggle="tooltip"
                  data-placement="top"
                  title="Tooltip on top"
                ></i>
              </label>
            </div>
            <div class="col-md-4">
              <select class="form-control" id="exampleFormControlSelect1" name="delimiter">
                <option>,</option>
                <option>;</option>
              </select>
            </div>
          </div>
          <div class="row justify-content-center mt-3">
            <div class="col-md-3">
              <label for>
                Nombre Nueva Columna
                <i
                  class="fas fa-question-circle fa-xs"
                  data-toggle="tooltip"
                  data-placement="top"
                  title="Tooltip on top"
                ></i>
              </label>
            </div>
            <div class="col-md-4">
              <input type="text" class="form-control" name="column_status_email" placeholder />
            </div>
          </div>
        </form>
        <div class="d-flex justify-content-around mt-4">
          <button type="button" class="btn btn-outline-info btn-lg">
            <i class="fas fa-broom"></i> Limpiar
          </button>
          <button type="button" @click="mostrarFormulario" class="btn btn-outline-success btn-lg">
            <i class="fas fa-caret-right"></i> Ejecutar
          </button>
        </div>
        <hr />
        <div class="progress">
          <div
            class="progress-bar progress-bar-striped progress-bar-animated"
            role="progressbar"
            aria-valuenow="50"
            aria-valuemin="0"
            aria-valuemax="50"
            style="width: 100%"
          >50%</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Content",
  methods: {
    mostrarFormulario() {
      let form = document.getElementById('formTest');
      let formD = new FormData(form);

      axios({
        method: 'post',
        url: 'http://104.131.169.113:8003/api/v1/transform/',
        data: formD,
        config: { headers: {'Content-Type': 'multipart/form-data' }}
        })
        .then(function (response) {
            //handle success
            console.log(response);
        })
        .catch(function (response) {
            //handle error
            console.log(response);
        });
    }
  }
};


// Funcion para activar los tooltip
$(function() {
  $('[data-toggle="tooltip"]').tooltip();
});

// Funcion para el funcionamiento del file input
function bs_input_file() {
  $(".input-file").before(function() {
    if (
      !$(this)
        .prev()
        .hasClass("input-ghost")
    ) {
      var element = $(
        "<input type='file' class='input-ghost' style='visibility:hidden; height:0'>"
      );
      element.attr("name", $(this).attr("name"));
      element.change(function() {
        element
          .next(element)
          .find("input")
          .val(
            element
              .val()
              .split("\\")
              .pop()
          );
      });
      $(this)
        .find("button.btn-choose")
        .click(function() {
          element.click();
        });
      $(this)
        .find("button.btn-reset")
        .click(function() {
          element.val(null);
          $(this)
            .parents(".input-file")
            .find("input")
            .val("");
        });
      $(this)
        .find("input")
        .css("cursor", "pointer");
      $(this)
        .find("input")
        .mousedown(function() {
          $(this)
            .parents(".input-file")
            .prev()
            .click();
          return false;
        });
      return element;
    }
  });
}
$(function() {
  bs_input_file();
});

/* Swal.fire({
  title: "¿Estas seguro?",
  text: "Una vez hecho el proceso no podras revertirlo!",
  type: "warning",
  showCancelButton: true,
  confirmButtonColor: "#3085d6",
  cancelButtonColor: "#d33",
  cancelButtonText: "Cancelar",
  confirmButtonText: "Si, Proceder"
}).then(result => {
  if (result.value) {
    Swal.fire("Enhorabuena!", "Tu archivo ha sido cargado.", "success");
  }
}); */
</script>


<style>

img {
  width: 18%;
  height: auto;
}

.card {
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.card:hover {
  box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25), 0 10px 10px rgba(0, 0, 0, 0.1);
}

img:hover {
  animation-iteration-count: infinite;
  animation-delay: 2s;
  animation-duration: 5s;
}

.archivo {
  display: flex;
  justify-content: center;
}

input[type="file"] {
  position: absolute;
  top: -500px;
}
</style>
