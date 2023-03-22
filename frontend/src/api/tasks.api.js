import api from "./config.js"
import apiHelpers from "./helpers.js"

export default {
  getTasks: () => {
    return new Promise((resolve, reject) => {
      api
        .get("/api/tasks/list")
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
  addNewTask: (description) => {
    return new Promise((resolve, reject) => {
      api
        .post("/api/tasks/add", apiHelpers.dataToForm({ description }))
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
  addNewCoupon: (coupon_name, type, price) => {
    return new Promise((resolve, reject) => {
      api
        .post("/api/coupons/create", apiHelpers.dataToForm({ coupon_name, type, price }))
        .then((response) => {
          return resolve(response.data)
        })
        .catch((error) => {
          return reject(error)
        })
    })
  },
  applyCoupon: (coupon_name) => {
    return new Promise((resolve, reject) => {
      api
        .post("api/coupons/apply", apiHelpers.dataToForm({ coupon_name }))
        .then((response) => {
          return resolve(response.data)
        })
        .catch ((error) => {
          return reject(error)
        })
    })
  },
}
