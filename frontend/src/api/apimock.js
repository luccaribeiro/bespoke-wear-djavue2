import axios from 'axios'

export default {
    addNewCoupon: (coupon_nameS, type, price) => {
        return new Promise((resolve, reject) => {
        axios.post("http://localhost:3003/cupons", {
          name: coupon_nameS,
          kind_of_discount: type,
          discount_value: price
        })
            .then((response) => {
            return resolve(response.data)
            })
            .catch((error) => {
            return reject(error)
            })
        })
      },
      applyCoupon: (name) => {
        return new Promise((resolve, reject) => {
          axios.get(`http://localhost:3003/cupons?name=${name}`)
            .then((response) => {
              if (response.data.length > 0) {
                return resolve(response.data[0])
              } else {
                return resolve({"kind_of_discount": "null"})
              }
            })
            .catch ((error) => {
              return reject(error)
            })
        })
      },
}