// Composables
import DefaultLayout from "@/layouts/default/DefaultLayout.vue"
import TaskListView from "@/views/tasks/TaskListView.vue"
import ShoppingCartlist from "@/views/tasks/ShoppingCartlist.vue"

export default [
  {
    path: "/tasks",
    component: DefaultLayout,
    children: [
      {
        path: "list",
        name: "tasks-list",
        component: TaskListView,
      },
      {
        path: "shopping",
        name: "tasks-shopping-list",
        component: ShoppingCartlist,
      }
    ],
  },
]
