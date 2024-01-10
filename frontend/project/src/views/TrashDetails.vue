<template>
  <div class="flex flex-col items-center h-screen pt-2 relative">
    <div class="flex items-center justify-between w-full mb-12 px-8">
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
      <h1 class="font-black text-xl text-white">Trash Note</h1>
      <p></p>
    </div>
    <div class="flex flex-col w-full p-6">
      <div class="flex items-center justify-between">
        <div class="flex flex-col w-1/3 mb-3">
          <label class="text-white" for="input-title">Title</label>
          <v-text-field
            id="input-title"
            :disabled="true"
            v-model="title"
            variant="outlined"
            hide-details
          ></v-text-field>
        </div>
        <p>{{ date }}</p>
      </div>
      <div class="flex flex-col w-2/3">
        <label class="text-white" for="input-body">Body</label>
        <v-textarea
          id="input-body"
          v-model="body"
          :disabled="true"
          hide-details
          variant="outlined"
          auto-grow
          rows="15"
          row-height="30"
        ></v-textarea>
      </div>
    </div>

    <div class="fixed bottom-0 right-0 z-50 mr-8 mb-4">
      <v-btn color="gray" rounded="lg" @click="Reload()" class="mr-2">
        Reload
      </v-btn>
      <v-btn color="#700a08" rounded="lg" @click="HardDelete()"> Delete </v-btn>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import store from "/src/store";
import { useRouter } from "vue-router";
import { useRoute } from "vue-router";
import { getNote, updateNote, deleteNote } from "/src/services/noteService";
import { format } from "date-fns";

const router = useRouter();
const route = useRoute();
const { state } = store;

const title = ref();
const body = ref();
const note = ref();
const date = ref();

const getNoteFunc = async () => {
  try {
    const resp = await getNote(route.params.id);
    note.value = resp.data;
    title.value = resp.data.title;
    body.value = resp.data.body;
    date.value = format(resp.data.created_at, "yyyy-MM-dd HH:mm:ss");
  } catch (error) {
    console.log("error :>> ", error);
  }
};

const Reload = async () => {
  let data = {
    is_trash: false,
  };
  try {
    const resp = await updateNote(route.params.id, data);
    router.push("/");
  } catch (error) {
    console.log("error :>> ", error);
  }
};

const HardDelete = async () => {
  try {
    const resp = await deleteNote(route.params.id);
    router.push({ name: "trash" });
  } catch (error) {
    console.log("error :>> ", error);
  }
};

onMounted(() => {
  getNoteFunc();
});
</script>
