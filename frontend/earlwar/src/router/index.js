import Vue from 'vue'
import VueRouter from 'vue-router'
import Edit from '../views/Edit.vue'
import Folder from "@/views/Folder";

Vue.use(VueRouter)

const routes = [
  {
    path: '/folder/:path',
    name: 'Folder',
    component: Folder
  },
  {
    path: '/edit/:path',
    name: 'Edit',
    component: Edit
  }
]

const router = new VueRouter({
  routes
})

export default router
