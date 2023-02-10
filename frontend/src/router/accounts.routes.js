// Composables
import EmptyLayout from "@/layouts/default/EmptyLayout.vue"
import LoginView from "@/views/accounts/LoginView.vue"
import LogoutView from "@/views/accounts/LogoutView.vue"
import RegisterView from "@/views/accounts/RegisterView.vue"

export default [
  {
    path: "/accounts",
    component: EmptyLayout,
    children: [
      {
        path: "login",
        name: "accounts-login",
        component: LoginView,
      },
      {
        path: "logout",
        name: "accounts-logout",
        component: LogoutView,
      },
      {
        path: "register",
        name: "accounts-register",
        component: RegisterView,
      },
    ],
  },
]
