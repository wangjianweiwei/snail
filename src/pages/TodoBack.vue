<script setup>
import {ref, reactive, onMounted} from "vue";
import {getTodos, updateTodo, createTodo, deleteTodo} from "@/services";
import 'animate.css';
import {tr} from "vuetify/locale";

const filter = [
  {name: "全部", status: '', date: ''},
  {name: "已完成", status: 1, date: ''},
  {name: "未完成", status: 0, date: ''},
  {name: "最近一周完成", status: "1", date: "week"},
  {name: "最近一个月完成", status: 1, date: "month"}
]
const selectedFilter = ref({name: "未完成", status: 0, date: ''})
const dateValue = ref("week")
const datePickerVal = ref(new Date())
const NewTaskName = ref("")
const NewTaskLoading = ref(false)

const tasks = reactive([])

async function fetchTodos() {
  tasks.splice(0, tasks.length);
  let todos = await getTodos(selectedFilter.value.status, selectedFilter.value.date)
  tasks.push(...todos)
}

onMounted(async () => {
  await fetchTodos()
})


const taskCheckboxUpdate = async (task) => {
  task.loading = true
  let ele = document.getElementById(task.id)
  if (task.is_completed) {
    ele.classList.add("animate__animated")
    ele.classList.add("animate__shakeX")
  } else {
    ele.classList.remove("animate__animated")
    ele.classList.remove("animate__shakeX")
  }
  await updateTodo(task.id, {is_completed: task.is_completed, title: task.title})

  task.loading = false
}

const addTask = async () => {
  if (NewTaskName.value.length > 0) {
    NewTaskLoading.value = true
    let item = await createTodo(NewTaskName.value)
    tasks.push(item)
    NewTaskLoading.value = false
    NewTaskName.value = ""
  }
}

const deleteTask = async (task, index) => {
  task.loading = true
  await deleteTodo(task.id)
  console.log(tasks[index])
  tasks.splice(index, 1)
}

const updateTask = async (task) => {
  task.loading = true

  await updateTodo(task.id, {title: task.title})
  task.loading = false
}

function doEnter(e) {
  e.target.blur()
}

</script>

<template>
  <v-row justify="center" no-gutters>
    <v-col lg="12" xl="9">
      <v-sheet class="mx-12 my-8" rounded="lg">
        <v-row no-gutters>
          <v-col cols="1" lg="3" xl="3">
            <v-sheet rounded="lg" height="100%">
              <v-locale-provider locale="zhHans">
                <v-date-picker
                  rounded="lg"
                  title="select date"
                  header="选择一个日期"
                  show-adjacent-months
                  width="100%"
                  :model-value="datePickerVal"
                ></v-date-picker>
              </v-locale-provider>
              <v-divider></v-divider>
              <div class="pa-5">
                <h4>Event Filters</h4>
              </div>
            </v-sheet>
          </v-col>
          <v-divider vertical></v-divider>
          <v-col cols="11" lg="9" xl="9">
            <v-sheet rounded="lg">
              <div class="pa-5 d-flex justify-start">
                <v-btn-toggle
                  v-model="selectedFilter"
                  rounded="lg"
                  density="compact"
                  border
                  group
                  divided
                  mandatory
                  color="#696CFF"
                  variant="flat"
                  @update:modelValue="fetchTodos()"
                >
                  <v-btn :key="i" :value="o" v-for="(o, i) in filter">
                    {{ o.name }}
                  </v-btn>
                </v-btn-toggle>
              </div>
              <v-divider></v-divider>
              <div class="py-4">
                <div class="mx-5 mb-4">
                  <v-text-field
                    color=""
                    variant="outlined"
                    density="comfortable"
                    label="添加一个待办事项....."
                    :loading="NewTaskLoading && 'primary'"
                    @keyup.enter="addTask"
                    v-model="NewTaskName">
                  </v-text-field>
                </div>
                <v-hover v-for="(task, i) in tasks" :key="task.id">
                  <template v-slot:default="{ isHovering, props }">
                    <v-list-item
                      :id="task.id"
                      v-bind="props">
                      <template v-slot:prepend>
                        <v-checkbox-btn
                          v-model="task.is_completed"
                          @update:modelValue="taskCheckboxUpdate(task)">
                        </v-checkbox-btn>
                      </template>
                      <template #title>
                        <v-text-field
                          :key="i"
                          variant="solo-filled"
                          v-model="task.title"
                          :disabled="task.is_completed"
                          @blur="updateTask(task)"
                          @keyup.enter="doEnter"
                          :loading="task.loading"
                          density="compact">
                          <template #append-inner>
                            <v-icon
                              v-if="task.is_completed"
                              color="success">
                              mdi-check
                            </v-icon>
                            <v-btn-group
                              density="compact"
                              variant="text"
                              v-if="!task.is_completed && isHovering">
                              <v-btn icon="mdi-format-vertical-align-top"
                                     color="primary"
                                     class="mx-1"
                                     size="small"
                                     @click="deleteTask(task, i)">

                              </v-btn>
                              <v-btn icon="mdi-trash-can-outline"
                                     color="error"
                                     class="mx-1"
                                     size="small"
                                     @click="deleteTask(task, i)">
                              </v-btn>
                            </v-btn-group>
                          </template>
                        </v-text-field>
                      </template>
                    </v-list-item>
                  </template>
                </v-hover>
              </div>
            </v-sheet>
          </v-col>
        </v-row>
      </v-sheet>
    </v-col>
  </v-row>


</template>

<style scoped>
.t {
  -webkit-font-smoothing: antialiased;
  font-family: Public Sans, sans-serif, -apple-system, blinkmacsystemfont, Segoe UI, roboto, Helvetica Neue, arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", Segoe UI Symbol;
}
</style>
