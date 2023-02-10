<template>
   <v-container>
    <v-row align="center" class="mt-10" no-gutters>
      <v-col cols="12" sm="6" offset-sm="3">
        <v-sheet class="pa-2"> <h1>Registrar-se</h1> </v-sheet>
        <v-form>
          <v-text-field
            v-model="username"
            label="Username"
            prepend-inner-icon="mdi-email-fast-outline"
            variant="outlined"
            required
            @keyup.enter="login"></v-text-field>
          <v-text-field
            v-model="email"
            label="E-Mail"
            prepend-inner-icon="mdi-email-fast-outline"
            variant="outlined"
            required
            @keyup.enter="login"></v-text-field>

          <v-text-field
            v-model="password"
            type="password"
            label="Password"
            prepend-inner-icon="mdi-key-outline"
            variant="outlined"
            required
            @keyup.enter="login"></v-text-field>

          <v-btn
            block
            size="large"
            rounded="pill"
            color="primary"
            append-icon="mdi-chevron-right"
            @click="register()">
            Criar sua conta
          </v-btn>
          <v-btn
            class="my-2"
            block
            size="large"
            rounded="pill"
            color="primary"
            variant="outlined"
            :to="{ name: 'base-home' }">
            Início
          </v-btn>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

import axios from 'axios'

export default {
  data() {
    return {
      username: '',
      email: '',
      password: '',
    }
  },
    methods: {
    async register(){
      var formdata = new FormData();
      formdata.append("email", this.email);
      formdata.append("password", this.password);
      formdata.append("username", this.username);

      var requestOptions = {
        method: 'POST',
        body: formdata,
        redirect: 'follow'
      };

      fetch("http://localhost/api/accounts/register", requestOptions)
        .then(response => response.text())
        .then(result => {console.log(result)
        this.$router.push({ name: 'accounts-login' })
        })
        .catch(error => console.log('error', error));
    }
  },
}
</script>
