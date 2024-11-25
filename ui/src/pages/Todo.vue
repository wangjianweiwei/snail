<script setup>
import {ref, reactive, onMounted, watch} from "vue";
import {useDate} from "vuetify";
import {getTodos, updateTodo, createTodo, deleteTodo} from "@/services";
import 'animate.css';

const filter = [
  {name: "全部", status: '', date: () => ""},
  {name: "全部完成", status: 1, date: () => ""},
  {name: "全部待办", status: 0, date: () => ""},
  {
    name: "完成",
    status: 1,
    date: () => getDate(datePickerVal.value)
  },
  {
    name: "待办",
    status: 0,
    date: () => getDate(datePickerVal.value)
  }
]
const datePickerVal = ref(new Date())
const selectedFilter = ref({name: "全部待办", status: 0, date: () => ""})
const NewTaskName = ref("")
const NewTaskLoading = ref(false)
const planDateDialog = ref({view: false, task: null})

const tasks = reactive([])

const dataFormats = {
  date: 'YYYY-MM-DD',            // Format date as '2024-08-11'
  datetime: 'YYYY-MM-DD HH:mm:ss', // Format datetime as '2024-08-11 14:10:48'
  time: 'HH:mm:ss'               // Format time as '14:10:48'
}

async function fetchTodos() {
  tasks.splice(0, tasks.length);
  let todos = await getTodos(selectedFilter.value.status, selectedFilter.value.date())
  tasks.push(...todos.paged)
}

onMounted(async () => {
  await fetchTodos()
})

watch(datePickerVal, (n, o) => {
  console.log(n, `${n.getFullYear()}-${n.getMonth() + 1}-${n.getDate()}`)
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
  setTimeout(async () => {
    await fetchTodos()
  }, 3000)

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

const updateTask = async (task_id, task, cb) => {
  // task.loading = true

  await updateTodo(task_id, task)
  // task.loading = false

  await fetchTodos()
  if (cb) {
    cb()
  }
}

const getDate = (date) => {
  return `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`

}


const Load = ({done}) => {
  done("empty")
}
</script>

<template>
  <div style="height: 100%;overflow: scroll" class="py-lg-5">
    <v-layout style="height: 100%">
      <v-row justify="center" style="height: 100%" no-gutters>
        <v-col lg="10" xl="9" style="height: 100%">
          <v-card style="height: 100%" rounded="lg">
            <v-row no-gutters style="height: 100%">
              <v-col cols="3" class="border-e-sm" style="height: 100%">
                <v-locale-provider locale="zhHans">
                  <v-date-picker
                    :data-format-as="dataFormats"
                    header="选择一个日期"
                    show-adjacent-months
                    width="100%"
                    v-model="datePickerVal"
                    @update:modelValue="fetchTodos()"
                  >
                  </v-date-picker>
                </v-locale-provider>
                <v-divider></v-divider>
              </v-col>
              <v-col cols="9" style="height: 100%">
                <v-row no-gutters style="height: 16%">
                  <v-col cols="12" class="border-b-sm d-flex align-center justify-space-between px-5">
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
                    <v-btn-toggle
                      rounded="lg"
                      density="compact"
                      border
                      group
                      divided
                      mandatory
                      color="#696CFF"
                    >
                      <v-btn>列表</v-btn>
                      <v-btn>天</v-btn>
                      <v-btn>周</v-btn>
                      <v-btn>月</v-btn>
                    </v-btn-toggle>
                  </v-col>
                  <v-col cols="12" class="px-5 d-flex align-center">
                    <v-text-field
                      variant="outlined"
                      density="compact"
                      label="添加一个待办事项....."
                      :loading="NewTaskLoading && 'primary'"
                      @keyup.enter="addTask"
                      v-model="NewTaskName">
                    </v-text-field>
                  </v-col>
                </v-row>
                <v-row style="height: 84%" no-gutters>
                  <v-col cols="12" style="height: 100%;">
                    <v-infinite-scroll height="100%" @load="Load">
                      <v-hover v-for="(task, i) in tasks" :key="task.id" :model-value="task.hover">
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
                                @blur="updateTask(task.id, {title: task.title}, null)"
                                @keyup.enter="(e) => e.target.blur()"
                                :loading="task.loading"
                                density="compact">
                                <template #append-inner>
                                  <v-icon
                                    v-if="task.is_completed"
                                    size="xs"
                                    color="success">
                                    mdi-check
                                  </v-icon>
                                </template>
                                <template #append>
                                  <v-menu>
                                    <template v-slot:activator="{ props }">
                                      <v-btn icon="mdi-dots-vertical" variant="text" size="small"
                                             v-bind="props"></v-btn>
                                    </template>
                                    <v-list density="compact" rounded>
                                      <v-list-item
                                        value="1"
                                        rounded
                                        class="mx-2 my-1"
                                        title="计划"
                                        @click="planDateDialog = {view: true, task: {id: task.id, title: task.title, plan_at: task.plan_at ? new Date(task.plan_at): new Date()}}"
                                        prepend-icon="mdi-update">
                                      </v-list-item>
                                      <v-list-item
                                        rounded
                                        class="mx-2 my-1"
                                        value="2"
                                        title="置顶"
                                        prepend-icon="mdi-format-vertical-align-top">
                                      </v-list-item>
                                      <v-list-item
                                        base-color="error"
                                        rounded
                                        class="mx-2 my-1"
                                        value="3"
                                        title="删除"
                                        @click="deleteTask(task, i)"
                                        prepend-icon="mdi-trash-can-outline">
                                      </v-list-item>
                                    </v-list>
                                  </v-menu>
                                </template>
                              </v-text-field>
                            </template>
                          </v-list-item>
                        </template>
                      </v-hover>
                    <template #empty>
                      <p class="text-body-2 text-disabled my-8">没有更多啦</p>
                    </template>
                    </v-infinite-scroll>
                  </v-col>
                </v-row>
              </v-col>
            </v-row>
          </v-card>
        </v-col>
      </v-row>
    </v-layout>
    <v-dialog max-width="400" v-model="planDateDialog.view">
      <template v-slot:default>
        <v-card title="选择一个计划时间">
          <v-card-text>
            <v-locale-provider locale="zhHans" :dataformatas="dataFormats">
              <v-date-picker
                rounded="lg"
                hide-header
                landscape
                width="100%"
                v-model="planDateDialog.task.plan_at"
              >
              </v-date-picker>
            </v-locale-provider>
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn
              text="保存"
              @click="updateTask(planDateDialog.task.id, {plan_at: getDate(planDateDialog.task.plan_at)}, () => {planDateDialog = {view: false, task: {}}})"
            ></v-btn>
          </v-card-actions>
        </v-card>
      </template>
    </v-dialog>
  </div>


</template>

<style scoped>
/* 针对 WebKit 浏览器 (如 Chrome, Safari, Edge) */
::-webkit-scrollbar {
  width: 3px; /* 滚动条的宽度 */
  height: 3px; /* 滚动条的高度（用于水平滚动条） */
}

::-webkit-scrollbar-track {
  background: #2e2e2e; /* 滚动条轨道的背景色 */
  border-radius: 4px; /* 圆角 */
}

::-webkit-scrollbar-thumb {
  background-color: #555; /* 滚动条滑块的颜色 */
  border-radius: 4px; /* 滑块的圆角 */
  border: 2px solid #2e2e2e; /* 为滑块加上边框以显示间隙 */
}

::-webkit-scrollbar-thumb:hover {
  background-color: #777; /* 滑块在悬停时的颜色 */
}

::-webkit-scrollbar-thumb:active {
  background-color: #999; /* 滑块在点击时的颜色 */
}

/* 针对 Firefox 浏览器 */
* {
  scrollbar-width: thin; /* 滚动条的宽度 */
  scrollbar-color: #555 #2e2e2e; /* 滑块颜色 #555 和轨道颜色 #2e2e2e */
}
</style>
