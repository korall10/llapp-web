<script setup lang="ts">
import { RouterView } from "vue-router";
</script>

<template>
  <v-app>
    <v-main class="h-screen bg-black">
      <router-view />
    </v-main>
  </v-app>
</template>
