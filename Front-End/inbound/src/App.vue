<template>
  <div id="app">
    <Navbar></Navbar>
    <img alt="Vue logo" src="./assets/logo.png">    
    <Content></Content>
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <Footer></Footer>    
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'
import Content from './components/Content.vue'

export default {
  name: 'app',
  components: {
    HelloWorld,
    Navbar,
    Footer,
    Content
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
