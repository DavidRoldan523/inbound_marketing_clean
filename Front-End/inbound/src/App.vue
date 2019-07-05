<template>
  <div id="app">
    <Navbar></Navbar>
    <div class="container animated fadeIn">
      <Fileupload></Fileupload>
      <Content></Content>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue";
import Footer from "./components/Footer.vue";
import Content from "./components/Content.vue";
import Fileupload from "./components/Fileupload.vue";

export default {
  name: "app",
  components: {
    Navbar,
    Footer,
    Content,
    Fileupload
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Signika&display=swap");

#app {
  font-family: "Signika", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

html,
body {
  font-family: "Signika", sans-serif;
}
</style>
