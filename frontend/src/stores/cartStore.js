import { defineStore } from "pinia"
import axios from 'axios';
export const shoppingCartStore = defineStore('shoppingCart', {
    state: () => {
        return {
            itemsQuantity: 0
        }
    },
    actions: {
        async getItemsQuantity() {
            const items = await axios.get('http://localhost/api/produtos/shoppingcart');
            this.itemsQuantity = items.data.shoppingCart.length
        }
    }
})
