import axiosInstance from "/src/axios";

export const getNotes = async (params) => {
  const response = await axiosInstance.get(`note/`, { params });
  return response;
};

export const getNote = async (id) => {
  const response = await axiosInstance.get(`note/${id}/`);
  return response;
};

export const createNote = async (data) => {
  const response = await axiosInstance.post(`note/`, data);
  return response;
};

export const updateNote = async (id, data) => {
  const response = await axiosInstance.patch(`note/${id}/`, data);
  return response;
};

export const deleteNote = async (id) => {
  const response = await axiosInstance.delete(`note/${id}/`);
  return response;
};
