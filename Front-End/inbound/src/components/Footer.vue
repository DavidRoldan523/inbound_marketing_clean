<template>
  <div>
    <div>
      <div class="fluid-container footer">
        <p class="text-center">Copyright &copy 2018, ABC Marketing. All Rights Reserved.</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Navbar"
};
</script>

<style scoped>
.fluid-container.footer {
  background: rgb(52, 58, 64);
}
.fluid-container.footer > *:last-child {
  margin-bottom: 0px;
  color: #fff;
}
</style>
