import axiosInstance from "/src/axios";

export const getAllUser = async () => {
  const response = await axiosInstance.get(`user/`);
  return response;
};

export const me = async () => {
  const response = await axiosInstance.get(`user/me/`);
  return response;
};

export const publicCreateUser = async (data) => {
  const response = await axiosInstance.post(`public/user/`, data);
  return response;
};

export const updateUser = async (id, data) => {
  const response = await axiosInstance.patch(`user/${id}/`, data);
  return response;
};

export const changePassword = async (id, data) => {
  const response = await axiosInstance.post(
    `user/${id}/change_password/`,
    data
  );
  return response;
};

export const token = async (data) => {
  const response = await axiosInstance.post(`token/`, data);
  return response;
};

export const refresh = async (refresh) => {
  const response = await axiosInstance.post(`token/refresh/`, { refresh });
  return response;
};
