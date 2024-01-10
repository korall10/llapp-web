import { createStore } from "vuex";

const store = createStore({
  state: {
    isAuthenticate: false,
    accessToken: null,
    refreshToken: null,
    user: {},
  },
  mutations: {
    setIsAuthenticated(state, isAuthenticated) {
      state.isAuthenticate = isAuthenticated;
      localStorage.setItem("isAuthenticate", isAuthenticated);
    },
    setTokens(state, tokens) {
      state.accessToken = tokens.access;
      state.refreshToken = tokens.refresh;
      localStorage.setItem("refreshToken", tokens.refresh);
      localStorage.setItem("accessToken", tokens.access);
    },
    setUser(state, user) {
      state.user = user;
      localStorage.setItem("user", JSON.stringify(user));
    },
  },
});

if (localStorage.getItem("isAuthenticate")) {
  store.commit("setIsAuthenticated", localStorage.getItem("isAuthenticate"));
}
if (
  localStorage.getItem("accessToken") &&
  localStorage.getItem("refreshToken")
) {
  store.commit("setTokens", {
    access: localStorage.getItem("accessToken"),
    refresh: localStorage.getItem("refreshToken"),
  });
}

if (localStorage.getItem("user")) {
  store.commit("setUser", JSON.parse(localStorage.getItem("user")));
}

export default store;
