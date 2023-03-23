<template>
  <v-container>
    <h1>Catálogo</h1>
    <br>
    <v-row>
      <v-col cols="12" sm="6" md="4" v-for="product in products['products']" :key="product.id">

        <v-card>
          <v-img class="image" :src="product.image" height="250px"></v-img>
          <v-card-title class="text-center">
            {{ product.name }}
            <br />
            <span class="font-weight-bold">R$ {{ product.price }}</span>
          </v-card-title>
          <v-card-text class="d-flex justify-center">{{ product.description }}</v-card-text>
          <v-card-actions class="d-flex justify-center">
            <v-icon size="28" v-if="admin" @click="openEditProduct(product.name,product.price,product.image,product.description, product.id)" class="lixeira">mdi-pencil</v-icon>
            <v-icon size="28" v-if="admin" @click="deleteOfProduct(product.id)" class="lixeira">mdi-delete</v-icon>
            <v-btn color="primary" @click="addItemOnCart(product.id)">
              Adicionar ao carrinho
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
     <v-dialog
      v-model="dialog"
      width="800"
    >

      <v-card>
        <v-row align="center" class="mt-10" no-gutters>
      <v-col cols="12" sm="6" offset-sm="3">
        <v-sheet class="pa-2"> <h1>Editar produto</h1> </v-sheet>
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
            @click="editProduct()"
            append-icon="mdi-chevron-right">
            Atualizar Produto
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
import axios from 'axios';
import { useAppStore } from "@/stores/appStore"
import { shoppingCartStore } from '@/stores/cartStore'
export default {
    setup() {
    const appStore = useAppStore()
    const cartStore = shoppingCartStore()
    return { appStore, cartStore}
  },
  data () {
    return {
      products: [],
      admin: false,
      usuario: null,
      dialog: false,
      name: '',
      price: '',
      image: '',
      description: '',
      id: '',
    }
  },
  methods: {
    async fetchProducts() {
      try {
        const response = await axios.get('http://localhost/api/produtos/list');
        this.products = response.data;
      } catch (error) {
      }
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
    addItemOnCart(id){ 
      var formdata = new FormData();
      formdata.append("product_id", id);

      var requestOptions = {
        method: 'POST',
        body: formdata,
        redirect: 'follow'
      };

      fetch("http://localhost/api/produtos/addcart", requestOptions)
        .then(response => response.text())
        .then(result => {
          console.log(result)
          this.appStore.showSnackbar("Item adicionado ao carrinho")
        })
        .catch(error => {
          this.appStore.showSnackbar("ERRO")
          console.log('error', error)
        });
        this.cartStore.itemsQuantity++
          },
      deleteOfProduct(product_id){
        var requestOptions = {
        method: 'DELETE',
        redirect: 'follow'
      };

      fetch(`http://localhost/api/produtos/removeproduct/${product_id}`, requestOptions)
        .then(response => response.text())
        .then(result => {
          this.fetchProducts();
        })
        .catch(error => console.log('error', error));
            },
        openEditProduct(name,price,image,description, id){
            this.dialog = true
            this.name =  name
            this.price = price
            this.image = image
            this.id = id
            this.description = description
        },
        editProduct(){
          var formdata = new FormData();
          formdata.append("name", this.name);
          formdata.append("price", this.price);
          formdata.append("image", this.image);
          formdata.append("description", this.description);

          var requestOptions = {
            method: 'POST',
            body: formdata,
            redirect: 'follow'
          };

          fetch(`http://localhost/api/produtos/editproduct/${this.id}`, requestOptions)
            .then(response => response.text())
            .then(result => {
              this.fetchProducts()
                    this.dialog = false
                    this.name= ''
                    this.price= ''
                    this.image= ''
                    this.description= ''
                    this.id= ''
            })
            .catch(error => console.log('error', error));
                  }
        },
  created() {
    this.fetchProducts();
    this.infosUsuarios();
    this.cartStore.getItemsQuantity()
  },
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
