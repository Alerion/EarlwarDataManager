import Vue from 'vue'
import VueRouter from 'vue-router'
import Units from '../views/Units.vue'
import Abilities from '../views/Abilities.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Units',
    component: Units
  },
  {
    path: '/abilities',
    name: 'Abilities',
    component: Abilities
  }
]

const router = new VueRouter({
  routes
})

export default router
