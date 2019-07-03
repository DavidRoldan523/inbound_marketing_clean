<template>
  <div>
    <div class="card text-center">
      <div class="card-header">Featured</div>
      <div class="card-body">
        <div class="input-group mb-3">
          <div class="input-group-prepend">
            <span class="input-group-text" id="inputGroupFileAddon01">Upload</span>
          </div>
          <div class="custom-file">
            <input
              type="file"
              class="custom-file-input"
              id="inputGroupFile01"
              aria-describedby="inputGroupFileAddon01"
            />
            <label class="custom-file-label" for="inputGroupFile01">Choose file</label>
          </div>
        </div>
        <form>
          <div class="form-group">
            <label for="exampleFormControlInput1">Email address</label>
            <input
              type="email"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="name@example.com"
            />
          </div>
          <div class="form-group">
            <label for="exampleFormControlInput1">Email address</label>
            <input
              type="email"
              class="form-control"
              id="exampleFormControlInput1"
              placeholder="name@example.com"
            />
          </div>
          <button type="button" class="btn btn-info">Info</button>
          <button type="button" class="btn btn-success">Success</button>
        </form>
      </div>
      <div class="card-footer text-muted">2 days ago</div>
    </div>
  </div>
</template>


<script>
export default {
  name: "Content"
};
</script>