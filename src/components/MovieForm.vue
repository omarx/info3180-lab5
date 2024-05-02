<script setup>
import { ref, onMounted } from 'vue';

const csrf_token = ref("");

onMounted(() => {
  fetch('/api/v1/csrf-token')
      .then((response) => response.json())
      .then((data) => {
        csrf_token.value = data.csrf_token;
      });
});

const movie = ref({
  title: '',
  description: '',
  poster: null
});

const onFileChange = (event) => {
  movie.value.poster = event.target.files[0];
};

console.log(csrf_token.value);

const submitForm = async () => {
  const formData = new FormData();
  formData.append('title', movie.value.title);
  formData.append('description', movie.value.description);
  if (movie.value.poster) {
    formData.append('poster', movie.value.poster);
  }
  formData.append('csrf_token', csrf_token.value);

  try {
    const response = await fetch("/api/v1/movies", {
      method: "POST",
      body: formData,
      headers: {
        'X-CSRFToken': csrf_token.value
      }
    });
    const data = await response.json();
    console.log(data);
    if (response.ok) {
      alert('Movie added successfully!');
    } else {
      alert('Failed to add movie. ' + data.errors.join('; '));
    }
  } catch (error) {
    console.error('Error:', error);
    alert('Error submitting form.');
  }
};
</script>


<template>
  <div class="container">
    <form @submit.prevent="submitForm">
      <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title</label>
        <input type="text" class="form-control" v-model="movie.title" id="title" placeholder="Enter Title" required>
      </div>
      <div class="form-group mb-3">
        <label for="description" class="form-label">Movie Description</label>
        <textarea class="form-control" v-model="movie.description" id="description" placeholder="Enter Description" required></textarea>
      </div>
      <div class="form-group mb-3">
        <label for="poster" class="form-label">Movie Poster</label>
        <input type="file" class="form-control" @change="onFileChange" id="poster" required>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>

</template>

<style scoped>
.form-group label {
  font-weight: bold;
}
</style>
