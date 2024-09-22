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
