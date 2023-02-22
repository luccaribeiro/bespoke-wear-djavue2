<template>
  <v-container>
    <h1>Carrinho de compras</h1>
    <br>
    <v-row>
      <v-col cols="12" sm="6" md="4" v-for="product in products" :key="product.id">
        <v-card>
          <v-img class="image" :src="product[0][0].image" height="250px"></v-img>
          <v-card-title class="text-center">
            {{ product[0][0].name }}
            <br />
            <span class="font-weight-bold">{{ product[0][0].price }}</span>
          </v-card-title>
          <v-card-text  class="d-flex justify-center">{{ product[0][0].description }}</v-card-text>
          <v-card-actions class="d-flex justify-center">
        <v-icon size="32" @click="deleteOfCart(product[1])" class="lixeira">mdi-delete</v-icon>
        </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
    <br>
    <h2 v-if="products.length>0">Total: {{total.toFixed(2)}}</h2>
    <v-btn @click="dialog = true" v-if="products.length>0" color="primary">Comprar</v-btn>
    <h2 v-else>Carrinho vazio</h2>
     <v-dialog
      v-model="dialog"
      width="800"
    >

      <v-card>
        <v-row align="center" class="mt-10" no-gutters>
      <v-col cols="12" sm="6" offset-sm="3">
        <v-sheet class="pa-2"><h1>Comprar</h1></v-sheet>
        <h3>O valor a ser pago é: {{total.toFixed(2)}}</h3>
        <br>
        <v-form class="form">
          <v-text-field
            label="Nome Completo"
            prepend-inner-icon="mdi-text"
            variant="outlined"
            ></v-text-field>
            <v-text-field
            label="Endereço"
            prepend-inner-icon="mdi-format-align-justify"
            variant="outlined"
            ></v-text-field>
                        <v-text-field
            v-model=price
            label="Número cartão de credito"
            prepend-inner-icon="mdi-currency-usd"
            variant="outlined"
            type="number"
            ></v-text-field>
            <v-text-field
            type=date
            label="Validade Cartão de credito"
            prepend-inner-icon="mdi-currency-usd"
            variant="outlined"
            ></v-text-field>
             <v-text-field
            type=number
            label="CVV"
            prepend-inner-icon="mdi-currency-usd"
            variant="outlined"
            ></v-text-field>



          <v-btn
            size="large"
            rounded="pill"
            color="primary"
            append-icon="mdi-chevron-right"
            @click="dialog = false"
            >
            Finalizar compra
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
  </v-container>
</template>

<script>
import { useAppStore } from "@/stores/appStore"

export default {
      setup() {
    const appStore = useAppStore()
    return { appStore}
  },
  data () {
    return {
      dicionario: {},
      products: [],
      products_id: [],
      total: 0,
      dialog: false,
    }
  },
  methods: {
     async getShoppingList(){
        this.dicionario = {};
        this.products = [];
        this.products_id =  [];
        this.total =  0;
        var requestOptions = {
        method: 'GET',
        redirect: 'follow'
      };
      
      fetch("http://localhost/api/produtos/shoppingcart", requestOptions)
        .then(response => response.text())
        .then(result => {
            let texto = result
            texto = JSON.parse(texto)
            this.dicionario = texto["shoppingCart"]
            for(let item of this.dicionario){
                this.products_id.push([item['product_id'], item['id']])
            }
            for(let id of this.products_id){
                var requestOptions = {method: 'GET',redirect: 'follow'};
                fetch(`http://localhost/api/produtos/shoppingcart/${id[0]}`, requestOptions)
                  .then(response => response.text())
                  .then(result => {
                    let texto = result
                    texto = JSON.parse(texto)
                    texto = texto['product']
                    this.products.push([texto, id[1]])
                    this.total += Number(texto[0]['price'])
                  })
                  .catch(error => console.log('error', error));
                            }
        })
        .catch(error => console.log('error', error));
          },
        async main(){
          await this.getShoppingList()
        },
        deleteOfCart(id){
            var requestOptions = {
            method: 'DELETE',
            redirect: 'follow'
          };
          
          fetch(`http://localhost/api/produtos/removecart/${id}`, requestOptions)
            .then(response => response.text())
            .then(result => {
                this.getShoppingList()
                this.appStore.showSnackbar("Item removido com sucesso! ")
            })
            .catch(error => {
              console.log('error', error)
              this.appStore.showSnackbar("ERRO!! ")
            });
        },
  },
  
  created(){
    this.main()
  }
  }
</script>

<style>
.image{
  margin: 10px 20px;
}
.text-center {
  text-align: center;
}
.font-weight-bold {
  font-weight: bold;
}
.d-flex {
  display: flex;
}
.justify-center {
  justify-content: center;
}
.lixeira{
    margin: 20px;
}
</style>

<style scoped>
.titulo{
  margin-left: 40px;
}

.form{
margin-bottom: 20px;
}

</style>