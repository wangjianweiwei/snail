import request from "@/plugins/axios";

export async function getTodos(status, time_filter) {
  console.log(time_filter)
  let response = await request.get(`/api/todo/?status=${status}&date=${time_filter}`)
  return response.data
}

export async function updateTodo(item_id, data) {
  let response = await request.put(`/api/todo/${item_id}/`, data)

  return response.data
}

export async function createTodo(title) {
  let response = await request.post('/api/todo/', {title: title})
  return response.data
}

export async function deleteTodo(item_id) {
  let response = await request.delete(`/api/todo/${item_id}`)
  return response.data
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

export async function composePostApi(pk, content) {
  let response = await request.put("/api/posts/compose", {pk: pk, content: content})
  return response.data.data
}
