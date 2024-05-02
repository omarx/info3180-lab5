<script setup>
import { ref, onMounted } from 'vue';

const movies = ref([]);

onMounted(() => {
  fetch('/api/v1/movies')
      .then((response) => response.json())
      .then((data) => {
        movies.value = data;
      });
});
</script>

<template>
  <div class="container">
    <h1>Movies</h1>
    <div class="row">
      <div class="col-md-4" v-for="movie in movies" :key="movie.id">
        <div class="card mb-3">
          <img :src="`/api/v1/posters/${movie.poster}`" class="card-img-top" :alt="movie.title">
          <div class="card-body">
            <h4 class="card-title">{{ movie.title }}</h4>
            <p class="card-text">{{ movie.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  margin-top: 20px;
}
.card-img-top {
  width: 100%; /* Responsive image */
  height: 50vh; /* You might want to adjust this */
  object-fit: cover; /* This will cover the area without stretching the image */
}
</style>
