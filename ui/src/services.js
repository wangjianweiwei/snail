import request from "@/plugins/axios";
import {it} from "vuetify/locale";

export async function getTodos(status, time_filter) {
  console.log(time_filter)
  let response = await request.get(`/api/todo/?status=${status}&date=${time_filter}`)
  return response.data.data
}

export async function updateTodo(item_id, data) {
  let response = await request.put(`/api/todo/update`, {pk: item_id, updated: data})

  return response.data
}

export async function createTodo(title) {
  let response = await request.post('/api/todo/create', {title: title})
  return response.data.data
}

export async function deleteTodo(item_id) {
  let response = await request.delete("/api/todo/delete", {params: {pk: item_id}})
  return response.data.data
}

export async function getPostsApi(page, size) {
  let response = await request.get("/api/posts/", {params: {page: page, size: size}})
  return response.data.data
}

export async function createPostApi(title) {
  let response = await request.post("/api/posts/create", {title: title, content: "12312312"})
  return response.data.data
}

export async function retrievePostApi(pk) {
  let response = await request.get("/api/posts/retrieve", {params: {pk: pk}})
  return response.data.data
}

export async function updatePostApi(data) {
  let response = await request.put("/api/posts/update", data)
}

export async function composePostApi(pk, content) {
  let response = await request.put("/api/posts/compose", {pk: pk, content: content})
  return response.data.data
}


export async function loginApi(email, otp_code) {
  let response = await request.post("/api/auth/login", {email: email, otp_code: otp_code})
  return response.data.data
}

export async function createOtpQrcodeApi(email) {
  let response = await request.get("/api/auth/otp_qrcode", {params: {email: email}})
  return response.data.data
}

export async function registerApi(email, secret) {
  let response = await request.post("/api/auth/register", {email: email, secret: secret})
  return response.data.data
}

export async function checkInitializationApi() {
  let response = await request.get("/api/auth/check_initialization")
  return response.data.data
}


export async function getPhotosApi() {
  let response = await request.get("/api/photos/")
  return response.data.data
}

export async function uploadPhotosApi(event, files) {
  const formData = new FormData();
  formData.append("name", event);
  for (const file of files) {
    formData.append("images", file); // 多文件时用相同的键名
  }

  let response = await request.post("/api/photos/", formData, {
    headers: {
      "Content-Type": "multipart/form-data"
    }
  })
  return response.data.data
}

export async function getEventsApi() {
  let response = await request.get("/api/photos/events")
  return response.data.data
}
