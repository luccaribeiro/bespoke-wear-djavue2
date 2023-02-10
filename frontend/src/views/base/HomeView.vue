<template>
  <v-container class="fill-height">
    <v-responsive class="d-flex align-center text-center fill-height">
      <div class="py-6" />
      <h1 class="titulo">Bespoke Wear</h1>
      <v-row class="d-flex align-center justify-center">
        <v-col cols="auto">
          <v-btn v-if="!loggedUser"
            color="primary"
            :to="{ name: 'accounts-register' }"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            class="my-4">
            <v-icon icon="mdi-speedometer" size="large" start />
            Registrar-se
          </v-btn>
          <v-btn
            v-if="!loggedUser"
            color="primary"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            :to="{ name: 'accounts-login' }"
            class="my-4">
            <v-icon icon="mdi-account-arrow-right-outline" size="large" start />
            Login
          </v-btn>
          <v-btn
            v-else
            color="primary"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            :to="{ name: 'accounts-logout' }">
            <v-icon icon="mdi-account-arrow-right-outline" size="large" start />
            Logout
          </v-btn>
          <v-btn
            v-if="loggedUser"
            color="primary"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            :to="{ name: 'tasks-list' }"
            class="my-4">
            <v-icon icon="mdi-folder-star-multiple" size="large" start />
            Produtos
          </v-btn>
        </v-col>
      </v-row>
    </v-responsive>
  </v-container>
</template>

<script>
import { mapState } from "pinia"
import { useAccountsStore } from "@/stores/accountsStore"

export default {
  computed: {
    ...mapState(useAccountsStore, ["loggedUser"]),
  },
}
</script>

<style scoped>
.titulo{
font-size: 120px;
}
.my-4{
  margin: 20px;
}
</style>

