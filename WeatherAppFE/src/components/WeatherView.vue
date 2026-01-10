<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios';

const city = ref('');
const weather = ref (null);
const error = ref('')

const getWeather = async () => {
  try {
    error.value = '';
    const res = await axios.get(
      `http://127.0.0.1:8000/weather?city=${city.value}`
    );
    weather.value =res.data;
  } catch {
    error.value = 'City not found';
  }
};
</script>

<template>
<div>
  <h1>Weather App</h1>
  <input v-model="city" placeholder="Enter city name" />
  <button @click="getWeather">Search</button>

  <p v-if="error">{{ error }}</p>

  <div v-if="weather">
    <h2>{{ weather.name }}</h2>
    <p>Temperature: {{ weather.main.temp }} &deg;C</p>
    <p>Condition: {{ weather.weather[0].description }}</p>
  </div>
</div>
</template>
