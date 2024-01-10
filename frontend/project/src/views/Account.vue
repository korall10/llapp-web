<template>
  <div class="w-screen h-screen flex justify-center items-start">
    <div class="w-96 mt-8 bg-black flex flex-col gap-3 px-5 py-4 p-4">
      <h1 class="font-bold text-lg text-center mb-6">
        <span class="!text-primary">LL</span>
        APP
      </h1>
      <h2 class="font-bold text-3xl text-center">Create a free account</h2>
      <p class="font-semibold text-center">
        Joın LLAPP for free. Create and share unlimited notes with your friends
      </p>
      <div class="mb-4 mt-6 flex flex-col gap-8">
        <div>
          <label for="input-name">First Name</label>
          <v-text-field
            id="input-first-name"
            v-model="first_name"
            class="bg-white rounded-xl"
            hide-details
            variant="outlined"
          ></v-text-field>
        </div>
        <div>
          <label for="input-name">Last Name</label>
          <v-text-field
            id="input-last-name"
            v-model="last_name"
            class="bg-white rounded-xl"
            hide-details
            variant="outlined"
          ></v-text-field>
        </div>

        <div>
          <label for="input-email">Email Address</label>
          <v-text-field
            id="input-email"
            v-model="username"
            class="bg-white rounded-xl"
            hide-details
            variant="outlined"
          ></v-text-field>
        </div>
        <div>
          <label for="input-password">Password</label>
          <v-text-field
            id="input-password"
            v-model="password"
            class="bg-white rounded-xl"
            hide-details
            variant="outlined"
            type="password"
          ></v-text-field>
        </div>
      </div>

      <v-btn
        class="mt-6"
        size="x-large"
        color="#700a08"
        rounded="pill"
        :loading="loading"
        @click="createUser()"
      >
        Create Account
      </v-btn>
      <v-btn
        class="mt-2"
        size="small"
        color="black"
        rounded="pill"
        @click="go()"
      >
        Already have an account?</v-btn
      >
    </div>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";
import { ref } from "vue";
import { publicCreateUser } from "/src/services/userService";

const router = useRouter();

const loading = ref(false);
const last_name = ref();
const first_name = ref();
const password = ref();
const username = ref();

const createUser = async () => {
  loading.value = true;
  let userData = {
    username: username.value,
    password: password.value,
    first_name: first_name.value,
    last_name: last_name.value,
  };
  try {
    let response = await publicCreateUser(userData);
    go();
  } catch (error) {
    console.log("error :>> ", error);
  }
  loading.value = false;
};

const go = () => {
  router.push({ name: "login" });
};
</script>
