import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AddMovie from "../views/AddMovie.vue";
import Movies from "../views/Movies.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path:'/movies',
      name:'movie',
      component: Movies
    },
    {
      path:'/movies/create',
      name:'add_movies',
      component: AddMovie
    }
  ]
})

export default router
