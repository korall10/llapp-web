import axios from "axios";
import store from "../src/store";
import router from "../src/router";
import { refresh } from "/src/services/userService";

const { state } = store;

const axiosInstance = axios.create({
  baseURL: "http://localhost:8000/api/", // API adresinizi buraya ekleyin
});

// Axios isteklerine interceptor eklemek
axiosInstance.interceptors.request.use(
  (config) => {
    // Her istek gönderilmeden önce yapılacak işlemler

    // Token eklemek için
    const token = state.accessToken; // Token'i buraya ekleyin veya uygun bir yerden alın
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }

    return config;
  },
  (error) => {
    // İstek gönderilmeden önce hata durumunda yapılacak işlemler
    return Promise.reject(error);
  }
);

axiosInstance.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    const originalConfig = error.config;
    if (error.response && error.response.status === 401) {
      console.log(state.refreshToken);
      let resp = refresh(state.refreshToken)
        .then((resp) => {
          store.commit("setTokens", {
            access: resp.data.access,
            refresh: state.refreshToken,
          });
          return axiosInstance(originalConfig);
        })
        .catch((err) => {
          console.log("err", err);
          state.refreshToken = null;
          state.accessToken = null;
          state.user = {};
          state.isAuthenticate = false;

          router.replace({ name: "login" });
        });
    }
    return Promise.reject(error.response);
  }
);

export default axiosInstance;
