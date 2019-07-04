<template>
  <div class="container">
    <div class="card">
      <div class="card-header">
        <img src="@/assets/martechlogo.png" alt />
      </div>
      <div class="card-body">
        <div class="direct_content">
          <div class="container">
            <div class="form-group">
              <input type="file" name="img[]" class="file" />
              <div class="input-group mb-3">
                <div class="input-group-prepend">
                  <span class="input-group-text" id="basic-addon1">
                    <i class="fas fa-paperclip"></i>
                  </span>
                </div>
                <input
                  type="text"
                  class="form-control"
                  disabled
                  placeholder="Seleccione el archivo"
                  aria-label="Upload File"
                  aria-describedby="basic-addon1"
                />
                <div class="input-group-append">
                  <button class="browse input-group-text btn btn-primary" id="basic-addon2">
                    <i class="fas fa-search mr-2"></i> Buscar
                  </button>
                </div>
              </div>
            </div>
          </div>

          <form>
            <div class="form-group mt-3">
              <label for="exampleInputEmail1">Nombre Columna Email</label>
              <input id="name" type="text" class="form-control ancho" />
            </div>
            <div class="form-group">
              <label for="exampleInputPassword1">Delimitador</label>
              <select class="form-control" id="exampleFormControlSelect1">
                <option>,</option>
                <option>;</option>
                <option>|</option>
                <option>"</option>
                <option>'</option>
              </select>
            </div>
            <div class="form-group">
              <label for="exampleInputPassword1">Resultado</label>
              <input id="result" type="text" class="form-control" />
            </div>
          </form>
        </div>
        <div class="d-flex justify-content-around">
          <button type="button" class="btn btn-outline-info btn-lg">
            <i class="fas fa-broom"></i> Limpiar
          </button>
          <button type="button" class="btn btn-outline-success btn-lg">
            <i class="fas fa-caret-right"></i> Ejecutar
          </button>
        </div>
      </div>
      <div class="card-footer text-muted"></div>
    </div>
  </div>
</template>


<script>
export default {
  name: "Content"
};

$(function() {
  $('[data-toggle="tooltip"]').tooltip();
});

$(document).on("click", ".browse", function() {
  var file = $(this)
    .parent()
    .parent()
    .parent()
    .find(".file");
  file.trigger("click");
});
$(document).on("change", ".file", function() {
  $(this)
    .parent()
    .find(".form-control")
    .val(
      $(this)
        .val()
        .replace(/C:\\fakepath\\/i, "")
    );
});
</script> 

<script>
/* import Vue from "vue";
import Vuelidate from "vuelidate";
Vue.use(Vuelidate);
src = "vuelidate/dist/vuelidate.min.js";

import { required, minLength, between } from "vuelidate/lib/validators";

export default {
  data() {
    return {
      name: "",
      delimitid: 0
    };
  },
  validations: {
    name: {
      required,
      minLength: minLength(4)
    },
    age: {
      between: between(20, 30)
    }
  }
}; */
</script>


<style scoped>
img {
  width: 25%;
  height: auto;
}

.direct_content {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}

.file {
  visibility: hidden;
  position: absolute;
}

/* 
 * Styles for demo only 
 */

body {
  background-color: #fff;
  margin: 50px;
}

.container {
  background-color: #fff;
  padding: 15px;
  border-radius: 8px;
  box-shadow: 0px 0px 24.08px 3.92px rgba(0, 0, 0, 0.25);
}

h1 {
  color: #fff;
  font-size: 3rem;
  font-weight: 900;
  margin: 0 0 5rem 0;
  background: -webkit-linear-gradient(#fff, #999);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-align: center;
}

.btn.btn-primary {
  background-color: #007bff;
  border-color: #007bff;
  outline: none;
  color: #fff;
}

.ancho {
  width: 30px;
}
</style>

