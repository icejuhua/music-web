<template>
        <!-- Modal -->
<div class="modal fade" id="passwordmodel" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog modal-xl">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="staticBackdropLabel">修改密码</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form class="row g-3 ">
                <div class="col-md-12">
                    <label for="old-password" class="form-label">旧密码*</label>
                    <input v-model="username" type="password" class="form-control" id="old-password">
                </div>
                <div class="col-md-6">
                    <label for="new-password" class="form-label">新密码*</label>
                    <input v-model="username" type="password" class="form-control" id="new-password">
                </div>
                <div class="col-md-6">
                    <label for="new-password-confirm" class="form-label">确认密码*</label>
                    <input v-model="username" type="password" class="form-control" id="new-password-confirm">
                </div>
            </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">关闭</button>
        <button type="button" class="btn btn-primary">提交</button>
      </div>
    </div>
  </div>
</div>
</template>

<script>

</script>

<style scoped>

</style>