<script setup>
import {ref, reactive} from "vue";

let tmp_card = ref("")

let stages = reactive([
  {name: "Todo", color: ""},
  {name: "In Progress", color: ""},
  {name: "Pending", color: ""},
  {name: "Done1", color: ""},
])
let is_add = ref(false)
let add = ref("")

let cards = reactive({})
stages.forEach((stage) => {
  let count = Math.ceil(Math.random() * 10)
  Math.random()
  console.log(count, stage.name)
  let data = []
  for (let i = 0; i < count; i++) {
    data.push({title: `Task${i}`, check_ok: 3, check_no: 10})
  }
  cards[stage.name] = data
})
console.log(cards)

function add_stage() {
  console.log(add.value, ">>>>")
  stages.push({name: add.value, color: ""})
  console.log(stages)
  add.value = ""
  is_add.value = false
}


function add_card(stage) {
  stage.loading = true
  setTimeout(() => {
    stage.loading = false
    cards[stage.name].unshift({title: stage.append_card, check_ok: 0, check_no: 0})
    stage.append_card = ""

  }, 1200)
}
</script>

<template>
  <div>
    <v-row style="flex-wrap: nowrap;overflow-x: scroll;min-height: 100%">
      <v-col xl="2" sm="3" v-for="i in stages" style="height: 100%;overflow-y: scroll">
        <v-card
          elevation="24"
          :color="i.color"
        >
          <div class="pa-1">
            <div class="d-flex align-center justify-space-between px-2 py-1">

              <!--              <v-text-field variant="underlined" v-model="i.name"></v-text-field>-->
              <h4>{{ i.name }}</h4>
              <v-menu transition="scale-transition">
                <template v-slot:activator="{ props }">
                  <v-btn v-bind="props" icon="mdi-dots-vertical" size="small" variant="plain"></v-btn>
                </template>

                <v-list density="compact" elevation="24" border>
                  <v-list-item key="1" value="1">
                    <v-list-item-title>删除列表</v-list-item-title>
                  </v-list-item>
                  <v-list-item key="2" value="2">
                    <v-list-item-title>添加卡片</v-list-item-title>
                  </v-list-item>
                  <v-list-item key="3" value="3">
                    <v-list-item-title>复制列表</v-list-item-title>
                  </v-list-item>
                  <v-list-item key="4" value="4">
                    <v-list-item-title>创建引用</v-list-item-title>
                  </v-list-item>
                </v-list>
              </v-menu>
            </div>
            <div class="d-flex align-center justify-space-between px-2 py-1">
              <v-btn block variant="flat" prepend-icon="mdi-plus">添加</v-btn>
            </div>
            <v-virtual-scroll :items="cards[i.name]">
              <template #default="{item}">
                <v-hover open-delay="100">
                  <template #default="{isHovering, props}">
                    <v-card
                      class="mx-2 my-4 cursor-pointer"
                      v-bind="props"
                      :color="isHovering ? 'primary' : undefined"
                      elevation="24"
                    >
                      <div class="d-flex align-center justify-space-between px-2 py-1 pb-0">
                        <h5 class="text-subtitle-2 pr-4 py-2 pr-3">{{ item.title }}</h5>
                      </div>
                      <div class="d-flex align-center justify-space-between px-2 py-2">
                        <p>
                          <v-icon icon="mdi-calendar-month-outline" size="13"></v-icon>
                          <span class="body-text-1 pl-1">10分钟前</span>
                        </p>
                        <p><span class="body-text-1 pl-1">{{ item.check_ok }}/{{ item.check_no }}</span></p>
                      </div>
                      <v-dialog activator="parent" max-width="900">
                        <template v-slot:default="{ isActive }">
                          <v-card height="800">
                            <v-card-text>
                              <v-row justify="space-between">
                                <v-col cols="10">
                                  <v-text-field
                                    label="标题"
                                    placeholder="Placeholder"
                                    variant="plain"
                                  ></v-text-field>

                                  <v-sheet
                                    class="mx-auto px-4 py-4"
                                    border
                                    rounded>
                                    <div class="mb-2">检查项清单</div>
                                    <div class="d-flex align-center justify-space-between">
                                      <v-progress-linear color="green-darken-4" model-value="20"
                                                         :height="5"></v-progress-linear>
                                      <p>20%</p>
                                    </div>
                                    <v-checkbox-btn label="1"></v-checkbox-btn>
                                    <v-checkbox-btn label="2"></v-checkbox-btn>
                                    <v-checkbox-btn label="3"></v-checkbox-btn>
                                    <v-checkbox-btn label="4"></v-checkbox-btn>
                                    <v-checkbox-btn label="5"></v-checkbox-btn>
                                  </v-sheet>

                                </v-col>
                                <v-col cols="2">
                                  <div class="justify-lg-start">
                                    <v-btn variant="text" block class="mt-2 justify-lg-start"
                                           prepend-icon="mdi-account-group">
                                      成员
                                    </v-btn>
                                    <v-btn variant="text" block class="mt-2 justify-lg-start"
                                           prepend-icon="mdi-label">
                                      标签
                                    </v-btn>
                                    <v-btn variant="text" block class="mt-2 justify-lg-start"
                                           prepend-icon="mdi-format-list-bulleted">检查项
                                    </v-btn>
                                    <v-btn variant="text" block class="mt-2 justify-lg-start"
                                           prepend-icon="mdi-timer-sand">
                                      工时
                                    </v-btn>
                                    <v-btn variant="text" block class="mt-2 justify-lg-start"
                                           prepend-icon="mdi-attachment-plus">附件
                                    </v-btn>
                                    <v-btn variant="text" block class="mt-2 justify-lg-start"
                                           prepend-icon="mdi-vector-link">
                                      关联
                                    </v-btn>
                                    <v-btn variant="text" block class="mt-2 justify-lg-start"
                                           prepend-icon="mdi-clock-time-eight-outline">开始时间
                                    </v-btn>
                                    <v-btn variant="text" block class="mt-2 justify-lg-start"
                                           prepend-icon="mdi-clock-time-four-outline">结束时间
                                    </v-btn>
                                    <v-btn variant="text" block class="mt-2 justify-lg-start"
                                           prepend-icon="mdi-share">
                                      引用
                                    </v-btn>
                                  </div>
                                </v-col>
                              </v-row>


                            </v-card-text>
                          </v-card>
                        </template>
                      </v-dialog>
                    </v-card>
                  </template>
                </v-hover>
              </template>
            </v-virtual-scroll>
          </div>
        </v-card>
      </v-col>
      <v-col xl="2" sm="2">
        <h4 @click="is_add = true"><span class="mdi mdi-plus"></span> 添加新的</h4>
        <div v-if="is_add">
          <v-text-field class="my-3" density="compact" autofocus v-model="add"></v-text-field>
          <v-btn class="me-4" @click="add_stage">添加</v-btn>
          <v-btn variant="tonal" @click="is_add = false">取消</v-btn>
        </div>

      </v-col>
    </v-row>
  </div>
</template>

<style scoped>
.text-subtitle-2 {
  font-size: .85rem !important;
}

.body-text-1 {
  font-size: 11px;
}
</style>
