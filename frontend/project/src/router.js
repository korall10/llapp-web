import { createRouter, createWebHistory } from "vue-router";
import store from "../src/store";

const { state } = store;
const routes = [
  {
    name: "login",
    path: "/login",
    component: () => import("/src/views/Login.vue"),
  },
  {
    name: "account",
    path: "/account",
    component: () => import("/src/views/Account.vue"),
  },
  {
    name: "dashboard",
    path: "/",
    component: () => import("/src/views/Common.vue"),
    redirect: { name: "home" },
    children: [
      {
        name: "home",
        path: "home",
        component: () => import("/src/views/Home.vue"),
      },
      {
        name: "settings",
        path: "settings",
        component: () => import("/src/views/Settings.vue"),
      },
      {
        name: "edit-profile",
        path: "profile",
        component: () => import("/src/views/EditProfile.vue"),
      },
      {
        name: "edit-note",
        path: "note/:id?",
        component: () => import("/src/views/EditNote.vue"),
      },
      {
        name: "trash",
        path: "trash",
        component: () => import("/src/views/Trash.vue"),
      },
      {
        name: "trash-details",
        path: "trash/:id",
        component: () => import("/src/views/TrashDetails.vue"),
      },
    ],
  },
];

const router = createRouter({
  routes,
  history: createWebHistory(),
});

router.beforeEach((to, from, next) => {
  let isAuthenticate = state.isAuthenticate;
  if (to.name === undefined) {
    next({ name: "notFound" });
  } else if (to.name === "login" && !isAuthenticate) {
    next();
  } else if (to.name === "login" && isAuthenticate) {
    next({ name: "dashboard" });
  } else if (to.name === "account" && isAuthenticate) {
    next({ name: "dashboard" });
  } else if (to.name === "account" && !isAuthenticate) {
    next();
  } else if (to.name !== "login" && !isAuthenticate) {
    next({ name: "login" });
  } else if (to.name === "unauthorized") {
    next();
  } else {
    next();
  }
});

export default router;
