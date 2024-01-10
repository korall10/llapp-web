<template>
  <div class="w-screen h-screen flex justify-center items-start">
    <div class="w-96 mt-32 bg-black flex flex-col gap-3 px-5 py-4 p-4">
      <h1 class="font-exrabold text-3xl text-center mb-6">
        <span class="!text-primary font-black">LL</span>
        APP
      </h1>
      <div>
        <label for="input-email">Email Address</label>
        <v-text-field
          v-model="email"
          id="input-email"
          class="bg-white rounded-xl"
          hide-details
          variant="outlined"
          @keyup.enter="login()"
        ></v-text-field>
      </div>
      <div class="mb-4">
        <label for="input-password">Password</label>
        <v-text-field
          v-model="password"
          id="input-password"
          class="bg-white rounded-xl"
          hide-details
          variant="outlined"
          type="password"
          @keyup.enter="login()"
        ></v-text-field>
      </div>

      <v-btn
        class="mt-6"
        size="x-large"
        color="#700a08"
        rounded="pill"
        @click="login()"
      >
        Login
      </v-btn>
      <v-btn class="mt-2" color="black" rounded="pill" @click="go()">
        Sign up
      </v-btn>
    </div>
  </div>
  <v-snackbar color="red" variant="outlined" v-model="snackbar" :timeout="2000">
    Your email or password is incorrect !
  </v-snackbar>
</template>

<script setup>
import { token, me } from "/src/services/userService";
import { useRouter } from "vue-router";
import { ref } from "vue";
import store from "/src/store";

// const { state } = store;
const router = useRouter();
const snackbar = ref(false);
const email = ref();
const password = ref();

const go = () => {
  router.push({ name: "account" });
};

const login = async () => {
  let data = {
    username: email.value,
    password: password.value,
  };
  try {
    const resp = await token(data);
    store.commit("setTokens", {
      access: resp.data.access,
      refresh: resp.data.refresh,
    });
    store.commit("setIsAuthenticated", true);
    Me();
    router.push("/");
  } catch (error) {
    snackbar.value = true;
    console.log("error :>> ", error);
  }
};

const Me = async () => {
  try {
    const resp = await me();
    store.commit("setUser", JSON.stringify(resp.data));
  } catch (error) {
    console.log("error :>> ", error);
  }
};
</script>
