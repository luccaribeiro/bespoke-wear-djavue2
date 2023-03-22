<template>
  <v-app-bar>
    <v-app-bar-title ><p class="titulo">{{ title }}</p></v-app-bar-title>
    <template #append>
      <v-btn icon="mdi-ticket-percent" v-if="admin" @click="couponDialog = true"></v-btn>
      <v-btn icon="mdi-plus" v-if="admin" @click="dialog = true"></v-btn>
      <v-btn icon="mdi-home" :to="{ name: 'tasks-list' }"></v-btn>
      <v-btn @click="goShopping()" icon v-bind:title="' items in cart'" class="cart-button">
      <v-badge :content=store.itemsQuantity color="error">
        <v-btn @click="goShopping()" icon v-bind:title="' items in cart'" class="cart-button">
          <v-icon>mdi-cart</v-icon>
        </v-btn>
      </v-badge>
  </v-btn>
      <v-btn
        :prepend-icon="theme === 'light' ? 'mdi-weather-sunny' : 'mdi-weather-night'"
        @click.stop="themeClick"></v-btn>

      <v-btn icon="mdi-dots-vertical">
        <v-icon icon="mdi-dots-vertical" />
        <v-menu activator="parent">
          <v-list>
            <v-list-item :to="{ name: 'accounts-logout' }"> Sair </v-list-item>
          </v-list>
        </v-menu>
      </v-btn>
    </template>
    <div class="text-center">
    <v-dialog
      v-model="dialog"
      width="800"
    >
      <v-card>
        <v-row align="center" class="mt-10" no-gutters>
      <v-col cols="12" sm="6" offset-sm="3">
        <v-sheet class="pa-2"> <h1>Novo produto</h1> </v-sheet>
        <v-form class="form">
          <v-text-field
            v-model=name
            label="Nome do produto"
            prepend-inner-icon="mdi-text"
            variant="outlined"
            ></v-text-field>
            <v-text-field
            v-model=description
            label="Descrição do produto"
            prepend-inner-icon="mdi-format-align-justify"
            variant="outlined"
            ></v-text-field>
                        <v-text-field
            v-model=price
            label="Preço do produto"
            prepend-inner-icon="mdi-currency-usd"
            variant="outlined"
            type="number"
            ></v-text-field>
            <v-text-field
            v-model=image
            label="Link da Imagem"
            prepend-inner-icon="mdi-image"
            variant="outlined"
            ></v-text-field>



          <v-btn
            size="large"
            rounded="pill"
            color="primary"
            append-icon="mdi-chevron-right"
            @click="adicionaProduto()">
            Adicionar Produto
          </v-btn>
          <v-btn
            class="my-2 botao"
            size="large"
            rounded="pill"
            color="primary"
            variant="outlined"
            @click="dialog=false">
            Cancelar
          </v-btn>
        </v-form>
      </v-col>
    </v-row>
      </v-card>
    </v-dialog>
    <v-dialog
      v-model="couponDialog"
      width="800"
    >

      <v-card>
        <v-row align="center" class="mt-10" no-gutters>
      <v-col cols="12" sm="6" offset-sm="3">
        <v-sheet class="pa-2"> <h1>Novo Cupom</h1> </v-sheet>
        <v-form class="form">
          <v-text-field
            v-model=couponName
            label="Nome do Cupom"
            prepend-inner-icon="mdi-text"
            variant="outlined"
            ></v-text-field>
            <v-select
              v-model="couponType"
              prepend-inner-icon="mdi-ticket-percent"
              label="Tipo de cupom"
              :items="items"
            ></v-select>
            <v-text-field
            v-model=couponPrice
            label="Preço do cupom"
            prepend-inner-icon="mdi-currency-usd"
            variant="outlined"
            type="number"
            ></v-text-field>
          <v-btn
            size="large"
            rounded="pill"
            color="primary"
            append-icon="mdi-chevron-right"
            @click="adicionaCupom()">
            Adicionar Cupom
          </v-btn>
          <v-btn
            class="my-2 botao"
            size="large"
            rounded="pill"
            color="primary"
            variant="outlined"
            @click="couponDialog=false">
            Cancelar
          </v-btn>
        </v-form>
      </v-col>
    </v-row>
      </v-card>
    </v-dialog>
  </div>
  </v-app-bar>
</template>

<script>
import { shoppingCartStore } from '../stores/cartStore'
import api from '~api'
export default {
  setup() {
    const store = shoppingCartStore()
    return {store}
  },
  props: {
    title: {
      type: String,
      required: false,
      default: "Bespoke Wear",
    },
    theme: {
      type: String,
      required: true,
      default: "dark",
    },
  },
  emits: ["themeClick"],
  data: () => {
    return {
      count: 0,
      admin: null,
      usuario: null,
      dialog: false,
      name: '',
      description: '',
      image: '',
      price: '',
      couponDialog: false,
      couponName: '',
      couponType: '',
      couponPrice: '',
      items: [
        { title: 'Absoluto', value: 'AB' },
        { title: 'Porcentagem', value: 'PC' }
      ]
      // atualizaContador: false,
    }
  },
  methods: {
    themeClick() {
      this.$emit("themeClick")
    },
    async infosUsuarios(){
      var requestOptions = {method: 'GET', redirect: 'follow'};

      await fetch("http://localhost/api/accounts/whoami", requestOptions)
        .then(response => response.text())
        .then(result => {
          this.usuario = result
          this.admin = this.usuario.indexOf('\"ADMIN\": true')
          if(this.admin == -1){
            this.admin = false
          } else{
            this.admin = true
          }
        })
        .catch(error => console.log('error', error));
    },
    adicionaProduto(){
      var formdata = new FormData();
      formdata.append("name", this.name);
      formdata.append("description", this.description);
      formdata.append("price", this.price);
      formdata.append("image", this.image);
      
      var requestOptions = {
        method: 'POST',
        body: formdata,
        redirect: 'follow'
      };
      
      fetch("http://localhost/api/produtos/add", requestOptions)
        .then(response => response.text())
        .then(result => this.dialog = false)
        .catch(error => console.log('error', error));
    },
    // contador(){
    //     var requestOptions = {
    //     method: 'GET',
    //     redirect: 'follow'
    //   };

    //   fetch("http://localhost/api/produtos/shoppingcart", requestOptions)
    //     .then(response => response.text())
    //     .then(result => {
    //       let texto = result
    //       texto = JSON.parse(texto)
    //       this.count = texto['shoppingCart'].length
    //       this.atualizaContador = !this.atualizaContador
    //     })
    //     .catch(error => console.log('error', error));
    //       },
    goShopping(){
      // this.atualizaContador = !this.atualizaContador
      this.$router.push({ name: "tasks-shopping-list" })
    },
    async adicionaCupom() {
      console.log("alo")
      console.log(this.couponName, this.couponType, this.couponPrice, typeof(this.couponPrice))
      api.addNewCoupon(
        this.couponName,
        this.couponType,
        parseInt(this.couponPrice),
      )
      this.couponName=''
      this.couponType=''
      this.couponPrice=''
      this.couponDialog = false
    }
  },
  created(){
    this.infosUsuarios()
  },
  watch: {

  }
}
</script>

<style>
.count {
  position: absolute;
  top: 5px;
  right: 5px;
  background-color: #8E69B9;
  color: white;
  border-radius: 50%;
  width: 18px;
  height: 18px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 12px;
}

.titulo{
font-family: Chalkduster;
font-size: 35px;
}
</style>

<style scoped>
.titulo{
  margin-left: 40px;
}

.form{
margin-bottom: 20px;
}
.botao{

}

</style>


