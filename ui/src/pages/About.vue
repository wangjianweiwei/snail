<script setup lang="ts">
import {ref} from "vue";

let items = ref([
  {
    id: 1,
    color: 'info',
    icon: 'mdi-information',
  },
  {
    id: 2,
    color: 'blue-grey-darken-1',
    icon: 'mdi-alert-circle',
  },
  {
    id: 3,
    color: 'primary',
    icon: 'mdi-alert-circle',
  },
  {
    id: 4,
    color: 'waning',
    icon: 'mdi-alert-circle',
  },
    {
    id: 5,
    color: 'indigo-lighten-5',
    icon: 'mdi-alert-circle',
  },
    {
    id: 6,
    color: 'teal-darken-2',
    icon: 'mdi-alert-circle',
  },
])
</script>

<template>
  <div class="pa-6">
    <v-row>
      <v-col cols="12">
        <v-card border>
          <v-parallax
            height="200"
            src="https://cdn.vuetifyjs.com/images/parallax/material.jpg"
          ></v-parallax>
          <v-card-text class="d-flex justify-start align-start">
            <v-avatar
              class="user-profile-avatar"
              color="grey"
              rounded
              size="150"
            >
              <v-img src="/src/assets/images/touxiang.png" cover></v-img>
            </v-avatar>
            <div class="ml-5">
              <p class="text-h5">王剑威</p>
              <p class="d-flex align-center ga-1 mt-3">
                <v-btn prepend-icon="mdi-xml" text="研发" variant="text" color=""></v-btn>
                <v-btn prepend-icon="mdi-map-marker-outline" text="北京" variant="text" color=""></v-btn>
                <v-btn prepend-icon="mdi-calendar-today-outline" text="2025-05-14" variant="text" color=""></v-btn>
              </p>
            </div>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col class="v-col-md-4 v-col-12">
        <v-row>
          <v-col cols="12">
            <v-card rounded border class="text-medium-emphasis" title="基本信息">
              <v-list density="compact">
                <v-list-subheader class="text-disabled">ABOUT</v-list-subheader>
                <v-list-item class="align-center">
                  <v-icon icon="mdi-account-outline"></v-icon>
                  <span class="ml-2">Full Name: John Doe</span>
                </v-list-item>
                <v-list-item>
                  <v-icon icon="mdi-check-bold"></v-icon>
                  <span class="ml-2">Status: active</span>

                </v-list-item>
                <v-list-item title="Role: Developer"></v-list-item>
                <v-list-item title="Country: USA"></v-list-item>
                <v-list-subheader class="text-disabled">CONTACTS</v-list-subheader>
                <v-list-item title="Contact: (123) 456-7890"></v-list-item>
                <v-list-item title="Skype: john.doe"></v-list-item>
                <v-list-item title="Email: john.doe@example.com"></v-list-item>
                <v-list-subheader class="text-disabled">TEAMS</v-list-subheader>
                <v-list-item title="Backend Developer(126 Members)"></v-list-item>
                <v-list-item title="VueJS Developer(98 Members)"></v-list-item>
                <v-list-item title="Role: Developer"></v-list-item>
              </v-list>
            </v-card>
          </v-col>
          <v-col cols="12">
            <v-card rounded border class="text-medium-emphasis" title="个人技能">
              <v-list density="compact">
                <v-list-subheader class="text-disabled">ABOUT</v-list-subheader>
                <v-list-item class="align-center">
                  <v-icon icon="mdi-account-outline"></v-icon>
                  <span class="ml-2">Full Name: John Doe</span>
                </v-list-item>
                <v-list-item>
                  <v-icon icon="mdi-check-bold"></v-icon>
                  <span class="ml-2">Status: active</span>

                </v-list-item>
                <v-list-item title="Role: Developer"></v-list-item>
                <v-list-item title="Country: USA"></v-list-item>
                <v-list-subheader class="text-disabled">CONTACTS</v-list-subheader>
                <v-list-item title="Contact: (123) 456-7890"></v-list-item>
                <v-list-item title="Skype: john.doe"></v-list-item>
                <v-list-item title="Email: john.doe@example.com"></v-list-item>
                <v-list-subheader class="text-disabled">TEAMS</v-list-subheader>
                <v-list-item title="Backend Developer(126 Members)"></v-list-item>
                <v-list-item title="VueJS Developer(98 Members)"></v-list-item>
                <v-list-item title="Role: Developer"></v-list-item>
              </v-list>
            </v-card>
          </v-col>
        </v-row>
      </v-col>
      <v-col class="v-col-md-8 v-col-12">
        <v-row>
          <v-col cols="12">
            <v-card rounded border class="text-medium-emphasis" title="工作经历">
              <v-timeline side="end">
                <v-timeline-item
                  v-for="item in items"
                  :key="item.id"
                  :dot-color="item.color"
                  size="small"
                >
                  <v-alert
                    :color="item.color"
                    :icon="item.icon"
                    :value="true"
                  >
                    Lorem ipsum dolor sit amet, no nam oblique veritus. Commune scaevola imperdiet nec ut, sed euismod
                    convenire principes at. Est et nobis iisque percipit, an vim zril disputando voluptatibus, vix an
                    salutandi sententiae.
                  </v-alert>
                </v-timeline-item>
              </v-timeline>
            </v-card>
          </v-col>
          <v-col cols="12" md="6">
            <v-card rounded border class="text-medium-emphasis" title="项目经历">
              <v-timeline side="end">
                <v-timeline-item
                  v-for="item in items"
                  :key="item.id"
                  :dot-color="item.color"
                  size="small"
                >
                  <v-alert
                    :color="item.color"
                    :icon="item.icon"
                    :value="true"
                  >
                    Lorem ipsum dolor sit amet, no nam oblique veritus. Commune scaevola imperdiet nec ut, sed euismod
                    convenire principes at. Est et nobis iisque percipit, an vim zril disputando voluptatibus, vix an
                    salutandi sententiae.
                  </v-alert>
                </v-timeline-item>
              </v-timeline>
            </v-card>
          </v-col>
          <v-col cols="12" md="6">
            <v-card rounded border class="text-medium-emphasis" title="主要成就">
              <v-timeline side="end">
                <v-timeline-item
                  v-for="item in items"
                  :key="item.id"
                  :dot-color="item.color"
                  size="small"
                >
                  <v-alert
                    :color="item.color"
                    :icon="item.icon"
                    :value="true"
                  >
                    Lorem ipsum dolor sit amet, no nam oblique veritus. Commune scaevola imperdiet nec ut, sed euismod
                    convenire principes at. Est et nobis iisque percipit, an vim zril disputando voluptatibus, vix an
                    salutandi sententiae.
                  </v-alert>
                </v-timeline-item>
              </v-timeline>
            </v-card>
          </v-col>
        </v-row>
      </v-col>


    </v-row>
  </div>
</template>


<style lang="css">
.user-profile-avatar {
  border: 5px solid #141414;
  inset-block-start: -3rem;
}
</style>
