<template>
  <div>
    <div class="card">
      <div class="card-header text-center py-md-3">
        <img class="animated heartBeat" src="@/assets/martechlogo.png" alt />
      </div>
      <div class="card-body pt-1">
        <form id="formTest" novalidate method="POST" action="#" enctype="multipart/form-data">
          <!-- COMPONENT START -->
          <div class="archivo">
            <div class="form-group col-md-8">
              <div class="custom-file mt-2">
                <input
                  type="file"
                  class="custom-file-input form-control-file"
                  id="customFileLang"
                  name="file"
                  lang="es"
                  accept=".csv"
                  required
                />
                <label class="custom-file-label" for="customFileLang">Seleccionar Archivo</label>
              </div>              
            </div>
          </div>
          <div class="row justify-content-center mt-3">
            <div class="col-md-3">
              <label for="validationCustom02">
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
              <!-- <b-row>
                <b-form-input type="text" id="names" v-model="texto" :state="comprobarTexto"></b-form-input>
                <p>Texto: {{texto}}</p>
              </b-row>-->
              <input
                type="text"
                name="email_column_name"
                class="form-control"
                id="validationCustom02"
                required
              />
              <div class="invalid-feedback">Ingrese datos</div>
            </div>
          </div>
          <div class="form-group row justify-content-center mt-3">
            <div class="col-md-3">
              <label for="validationCustom02">
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
              <!--            <b-row>
                <b-form-select id="select" v-model="select" :options="delimitador"></b-form-select>
                <p>Seleccion: {{select}}</p>
              </b-row>-->
              <select
                class="form-control"
                id="validationCustom02"
                name="delimiter"
                placeholder="CP"
                required
              >
                <option value disabled selected hidden>Seleccione</option>
                <option value=",">, (Coma)</option>
                <option value=";">; (Punto y coma)</option>
                <option value="|">| (Pipe)</option>
              </select>
              <div class="invalid-feedback">Ingrese datos</div>
            </div>
          </div>
          <div class="row justify-content-center mt-3">
            <div class="col-md-3">
              <label for="validationCustom03">
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
              <!--  <b-row>
                <b-form-input
                  type="text"
                  id="result"
                  v-model="resultado"
                  :state="comprobarResultado"
                ></b-form-input>
                <p>Result: {{resultado}}</p>
              </b-row>-->
              <input
                type="text"
                class="form-control"
                id="validationCustom03"
                name="column_status_email"
                required
              />
              <div class="invalid-feedback">Ingrese datos</div>
            </div>
          </div>
        </form>
        <div class="d-flex justify-content-around mt-4">
          <button
            type="button"
            @click="resetform()"
            value="Reset"
            class="btn btn-outline-info btn-lg"
          >
            <i class="fas fa-broom"></i> Limpiar
          </button>
          <button
            type="submit"
            id="registrarForm"
            @click="mostrarFormulario"
            class="btn btn-outline-success btn-lg"
          >
            <i class="fas fa-caret-right"></i> Ejecutar
          </button>
        </div>
        <!-- <hr>
        <div class="progress">
          <div
            class="progress-bar progress-bar-striped progress-bar-animated"
            role="progressbar"
            aria-valuenow="50"
            aria-valuemin="0"
            aria-valuemax="50"
            style="width: 100%"
          >50%</div>
        </div> -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Content",
  name: "Form",

  /*Validación Campos */
  data() {
    return {
      texto: "",
      resultado: "",
      select: "",
      archivo: null,
      submitstatus: null,
      delimitador: [
        { value: null, text: "Seleccione un Delimitador" },
        { value: ",", text: ", (Coma)" },
        { value: ";", text: "; (Punto y coma)" },
        { value: "|", text: "| (Pipe)" }
      ]
    };
  },

  methods: {
    resetform() {
      var archivo = document.getElementById("customFileLang");
      var placeholder = archivo.parentElement.querySelector(
        "label.custom-file-label"
      );
      if (placeholder.innerText != "Seleccionar archivo... ")
        placeholder.innerText = "Seleccionar archivo ...";
      document.getElementById("formTest").reset();

    },

    mostrarFormulario() {
      let form = document.getElementById("formTest");
      let formD = new FormData(form);

      axios({
        method: "post",
        url: "http://104.131.169.113:8003/api/v1/transform/",
        data: formD,
        config: { headers: { "Content-Type": "multipart/form-data", 
          "Authorization" : "Token f94fd116a36341bb9fdc72a92fee199cdf78f11c"} }
      })
        .then(function(response) {
          //handle success
          console.log(response.data);
          download("test.csv",response.data);
        })
        .catch(function(response) {
          //handle error
          console.log(response);
        });
    }
  }
};
//
function download(filename, text) {
  var element = document.createElement('a');
  element.setAttribute('href', 'data:text/csv;charset=utf-8,' + encodeURIComponent(text));
  element.setAttribute('download', filename);

  element.style.display = 'none';
  document.body.appendChild(element);

  element.click();

  document.body.removeChild(element);

}
//
(function() {
  "use strict";

  window.addEventListener(
    "load",
    function() {
      var form = document.getElementById("formTest");
      var btn = document.getElementById("registrarForm");
      btn.addEventListener(
        "click",
        function(event) {
          if (form.checkValidity() === false) {
            event.preventDefault();
            event.stopPropagation();
          }
          form.classList.add("was-validated");
        },
        false
      );
    },
    false
  );
})();

//

window.addEventListener("load", function() {
  var archivo = document.getElementById("customFileLang");
  archivo.addEventListener("change", function() {
    var nombreArchivoSubido = this.files[0].name;
    var placeholder = this.parentElement.querySelector(
      "label.custom-file-label"
    );
    console.log(placeholder.innerText);
    placeholder.innerText = nombreArchivoSubido;
  });
});

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
