<template>
  <footer class="bespoke-wear-footer">
    <div class="container">
      <p class="text-center">
        &copy; {{ year }} Bespoke Wear | Todos os direitos reservados
      </p>
    </div>
  </footer>
</template>

<script>
export default {
  data() {
    return {
      year: new Date().getFullYear()
    };
  }
};
</script>

<style>
.bespoke-wear-footer {
  background-color: #212121;
  color: #fff;
  padding: 1rem 0;
}

.bespoke-wear-footer p {
  font-family: 'Chalkduster', sans-serif;
  font-size: 12px;
  margin: 0;
}
</style>