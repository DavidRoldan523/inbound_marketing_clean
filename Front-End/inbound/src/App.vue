<template>
  <div id="app">
    <div class="main">
      <Navbar></Navbar>
      <Content></Content>
      <Footer></Footer>
    </div>
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue";
import Footer from "./components/Footer.vue";
import Content from "./components/Content.vue";
import FileUpload from "./components/FileUpload.vue";

export default {
  name: "app",
  components: {
    Navbar,
    Footer,
    Content,
    FileUpload
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

</style>
