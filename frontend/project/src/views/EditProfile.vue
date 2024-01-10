<template>
  <div class="flex flex-col items-center h-screen pt-2">
    <div class="flex items-center justify-between w-full mb-12 px-4">
      <svg
        class="cursor-pointer"
        @click="router.go(-1)"
        width="24px"
        height="24px"
        viewBox="0 0 24 24"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        stroke="#ffffff"
        stroke-width="2.4"
      >
        <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
        <g
          id="SVGRepo_tracerCarrier"
          stroke-linecap="round"
          stroke-linejoin="round"
        ></g>
        <g id="SVGRepo_iconCarrier">
          <path
            fill-rule="evenodd"
            clip-rule="evenodd"
            d="M15.7071 4.29289C16.0976 4.68342 16.0976 5.31658 15.7071 5.70711L9.41421 12L15.7071 18.2929C16.0976 18.6834 16.0976 19.3166 15.7071 19.7071C15.3166 20.0976 14.6834 20.0976 14.2929 19.7071L7.29289 12.7071C7.10536 12.5196 7 12.2652 7 12C7 11.7348 7.10536 11.4804 7.29289 11.2929L14.2929 4.29289C14.6834 3.90237 15.3166 3.90237 15.7071 4.29289Z"
            fill="#ffffff"
          ></path>
        </g>
      </svg>
      <h1 class="font-black text-xl text-white">Edit Profile</h1>
      <p></p>
    </div>
    <v-avatar color="#700a08" size="140">
      <h1 class="text-4xl font-black">{{ userAvatar }}</h1>
    </v-avatar>
    <div class="flex w-full items-center justify-center gap-32 mt-8 mb-4">
      <div class="w-1/4 text-white">
        <label for="input-first-name">First Name</label>
        <v-text-field
          id="input-first-name"
          v-model="first_name"
          class="bg-white rounded-xl"
          hide-details
          variant="outlined"
        ></v-text-field>
      </div>
      <div class="w-1/4 text-white">
        <label for="input-old-password">Old Password</label>
        <v-text-field
          id="input-old-password"
          type="password"
          v-model="old_password"
          class="bg-white rounded-xl"
          hide-details
          variant="outlined"
        ></v-text-field>
      </div>
    </div>

    <div class="flex w-full items-center justify-center gap-32 my-4">
      <div class="w-1/4 text-white">
        <label for="input-last-name">Last Name</label>
        <v-text-field
          id="input-last-name"
          v-model="last_name"
          class="bg-white rounded-xl"
          hide-details
          variant="outlined"
        ></v-text-field>
      </div>
      <div class="w-1/4 text-white">
        <label for="input-new-password">New Password</label>
        <v-text-field
          type="password"
          id="input-new-password"
          v-model="new_password"
          class="bg-white rounded-xl"
          hide-details
          variant="outlined"
        ></v-text-field>
      </div>
    </div>

    <div class="flex w-full items-center justify-center gap-32 mt-4">
      <div class="w-1/4 text-white">
        <label for="input-email-address">Email Address</label>
        <v-text-field
          id="input-email-address"
          v-model="email"
          class="bg-white rounded-xl"
          hide-details
          variant="outlined"
        ></v-text-field>
      </div>
      <div class="w-1/4 text-white">
        <label for="input-again-password">New Password (Again)</label>
        <v-text-field
          type="password"
          id="input-again-password"
          v-model="new_password_again"
          class="bg-white rounded-xl"
          hide-details
          variant="outlined"
        ></v-text-field>
      </div>
    </div>

    <div class="flex w-full mt-auto mb-5">
      <div class="ml-auto mr-16 w-56">
        <v-btn color="#700a08" block rounded="lg" @click="Save()">Save</v-btn>
      </div>
    </div>
  </div>
  <v-snackbar
    :color="snackbarcolor"
    variant="outlined"
    v-model="snackbar"
    :timeout="2000"
  >
    {{ snackbarText }}
    <template v-slot:actions>
      <v-btn :color="snackbarcolor" variant="text" @click="snackbar = false">
        Close
      </v-btn>
    </template>
  </v-snackbar>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { me, updateUser, changePassword } from "/src/services/userService";

import store from "/src/store";
import { useRouter } from "vue-router";

const router = useRouter();

const { state } = store;

const snackbarText = ref("");
const snackbarcolor = ref("success");
const userId = ref();
const first_name = ref();
const last_name = ref();
const email = ref();
const old_password = ref();
const new_password = ref();
const new_password_again = ref();
const snackbar = ref(false);

const userAvatar = computed(() => {
  let data = state.user;
  if (data) {
    let userData = JSON.parse(data);
    return (
      userData?.first_name.charAt(0).toUpperCase() +
      userData?.last_name.charAt(0).toUpperCase()
    );
  }
});

const Me = async () => {
  try {
    const resp = await me();
    userId.value = resp.data.id;
    first_name.value = resp.data.first_name;
    last_name.value = resp.data.last_name;
    email.value = resp.data.username;
  } catch (error) {
    console.log("error :>> ", error);
  }
};

const Save = async () => {
  let data = {
    username: email.value,
    first_name: first_name.value,
    last_name: last_name.value,
  };

  try {
    const resp = await updateUser(userId.value, data);
    if (
      old_password.value &&
      old_password.value != "" &&
      new_password.value &&
      new_password.value != "" &&
      new_password_again.value &&
      new_password_again.value != ""
    ) {
      if (new_password.value == new_password_again.value) {
        changePasswordFunc();
      } else {
        openSnackbar("Your passwords do not match !", "red");
      }
    } else {
      openSnackbar("User Information Changed !", "success");
    }
    MeRefresh();
  } catch (error) {
    openSnackbar("User Information Could Not Be Changed !", "red");
    console.log("error :>> ", error);
  }
};

const changePasswordFunc = async () => {
  let data = {
    old_password: old_password.value,
    new_password: new_password.value,
    new_password_again: new_password_again.value,
  };
  try {
    const resp = await changePassword(userId.value, data);
    openSnackbar("Your password has been changed !", "success");
    old_password.value = null;
    new_password.value = null;
    new_password_again.value = null;
  } catch (error) {
    openSnackbar(error.data.error, "red");
    console.log("error :>> ", error);
  }
};

function openSnackbar(text, color) {
  snackbarcolor.value = color;
  snackbarText.value = text;
  snackbar.value = true;
}

const MeRefresh = async () => {
  try {
    const resp = await me();
    store.commit("setUser", JSON.stringify(resp.data));
  } catch (error) {
    console.log("error :>> ", error);
  }
};

onMounted(() => {
  Me();
});
</script>
