<template>
  <div class="flex flex-col items-center h-screen pt-2 relative">
    <div class="flex items-center justify-between w-full mb-12 px-8">
      <p></p>
      <h1 class="font-black text-xl text-white">Trash</h1>
      <p></p>
    </div>
    <v-container>
      <v-row justify="center">
        <v-col :cols="2"
          ><template v-for="note in notes0">
            <div
              class="flex flex-col rounded-lg p-3 border-white border-2 min-h-32 text-white cursor-pointer hover:!text-black hover:bg-white mb-4"
              :style="{ height: `${note.body.length / 5}px` }"
              @click="goEditNote(note.id)"
            >
              <h1 class="font-bold break-words">{{ note.title }}</h1>
              <p class="break-words font-extralight text-pretty truncate">
                {{ note.body }}
              </p>
            </div>
          </template></v-col
        >
        <v-col :cols="2">
          <template v-for="note in notes1">
            <div
              class="flex flex-col rounded-lg p-3 border-white border-2 min-h-32 text-white cursor-pointer hover:!text-black hover:bg-white mb-4"
              :style="{ height: `${note.body.length / 5}px` }"
              @click="goEditNote(note.id)"
            >
              <h1 class="font-bold break-words">{{ note.title }}</h1>
              <p class="break-words font-extralight text-pretty truncate">
                {{ note.body }}
              </p>
            </div>
          </template>
        </v-col>
        <v-col :cols="2">
          <template v-for="note in notes2">
            <div
              class="flex flex-col rounded-lg p-3 border-white border-2 min-h-32 text-white cursor-pointer hover:!text-black hover:bg-white mb-4"
              :style="{ height: `${note.body.length / 5}px` }"
              @click="goEditNote(note.id)"
            >
              <h1 class="font-bold break-words">{{ note.title }}</h1>
              <p class="break-words font-extralight text-pretty truncate">
                {{ note.body }}
              </p>
            </div>
          </template>
        </v-col>
        <v-col :cols="2"
          ><template v-for="note in notes3">
            <div
              class="flex flex-col rounded-lg p-3 border-white border-2 min-h-32 text-white cursor-pointer hover:!text-black hover:bg-white mb-4"
              :style="{ height: `${note.body.length / 5}px` }"
              @click="goEditNote(note.id)"
            >
              <h1 class="font-bold break-words">{{ note.title }}</h1>
              <p class="break-words font-extralight text-pretty truncate">
                {{ note.body }}
              </p>
            </div>
          </template></v-col
        >
        <v-col :cols="2"
          ><template v-for="note in notes4">
            <div
              class="flex flex-col rounded-lg p-3 border-white border-2 min-h-32 text-white cursor-pointer hover:!text-black hover:bg-white mb-4"
              :style="{ height: `${note.body.length / 5}px` }"
              @click="goEditNote(note.id)"
            >
              <h1 class="font-bold break-words">{{ note.title }}</h1>
              <p class="break-words font-extralight text-pretty truncate">
                {{ note.body }}
              </p>
            </div>
          </template></v-col
        >
      </v-row>
    </v-container>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import store from "/src/store";
import { useRouter } from "vue-router";
import { getNotes } from "/src/services/noteService";

const router = useRouter();
const { state } = store;
const notes = ref([]);
const notes1 = ref([]);
const notes2 = ref([]);
const notes3 = ref([]);
const notes4 = ref([]);
const notes0 = ref([]);

function goEditNote(id) {
  router.push({ name: "trash-details", params: { id: id } });
}

const getNotesFunc = async () => {
  let filters = {
    is_trash: true,
  };
  try {
    const resp = await getNotes(filters);
    notes.value = resp.data;
    resp.data.forEach((note, index) => {
      if (index % 5 === 0) {
        notes0.value.push(note);
      } else if (index % 5 === 4) {
        notes4.value.push(note);
      } else if (index % 5 === 3) {
        notes3.value.push(note);
      } else if (index % 5 === 2) {
        notes2.value.push(note);
      } else {
        notes1.value.push(note);
      }
    });
  } catch (error) {
    console.log("error :>> ", error);
  }
};

onMounted(() => {
  getNotesFunc();
});
</script>
