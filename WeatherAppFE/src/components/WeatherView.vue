<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios';

interface weatherResponse {
  name: string
  main: {
    temp: number
  }
  weather : {
    description: string
  }[]
}

const city = ref<string>('');
const weather = ref<weatherResponse | null>(null);
const error = ref<string>('')

const getWeather = async () => {
  try {
    error.value = '';
    const res = await axios.get<weatherResponse>(
      `http://127.0.0.1:8000/weather?city=${encodeURIComponent(city.value)}`
    );
    weather.value =res.data;
  } catch {
    error.value = 'City not found';
    weather.value = null
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
    <p>Temperature: {{ weather?.main?.temp }} &deg;C</p>
    <p>Condition: {{ weather?.weather[0]?.description }}</p>
  </div>
</div>
</template>
