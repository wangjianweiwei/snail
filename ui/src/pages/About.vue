<script setup>
import 'animate.css';
import {ref} from "vue";
import {useI18n} from "vue-i18n";

const {t} = useI18n()
const items = ref([
  {
    id: 1,
    color: 'info',
    icon: 'mdi-information',
    size: "small"
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
const works = ref([
  {
    id: 1,
    color: 'info',
    company: "北京海马轻帆娱乐科技有限公司",
    working_hours: "2019/04 - 2023/03",
    title: "研发工程师",
    responsibility: "<ul>\n" +
      "                          <li>主导后端平台架构设计，完成微服务模块拆分及技术选型，保障系统高并发高可用</li>\n" +
      "                          <li>统筹后端开发生命周期管理，通过敏捷开发模式精准控制项目进度、成本与交付质量</li>\n" +
      "                          <li>建立标准化开发流程与技术规范，主导Code Review提升团队代码质量30%+</li>\n" +
      "                          <li>深度参与产品需求评审，从技术可行性、扩展性及性能维度提供关键决策建议</li>\n" +
      "                          <li>攻克分布式事务处理、实时计算引擎等5+项核心技术难题，推动系统性能提升200%</li>\n" +
      "                          <li>构建千万级深度学习数据采集管道，设计自动化预处理框架提升数据清洗效率60%</li>\n" +
      "                          <li>主导CI/CD及监控体系落地，实现日均300+次自动化部署，系统可用性达99.95%</li>\n" +
      "                        </ul>"
  },
  {
    id: 2,
    color: "primary",
    company: "北京莱迈医疗信息科技有限公司",
    working_hours: "2023/04 - 至今",
    title: "项目研发部负责人",
    responsibility: "<ul>\n" +
      "                          <li>主导后端平台架构设计，完成微服务模块拆分及技术选型，保障系统高并发高可用</li>\n" +
      "                          <li>统筹后端开发生命周期管理，通过敏捷开发模式精准控制项目进度、成本与交付质量</li>\n" +
      "                          <li>建立标准化开发流程与技术规范，主导Code Review提升团队代码质量30%+</li>\n" +
      "                          <li>深度参与产品需求评审，从技术可行性、扩展性及性能维度提供关键决策建议</li>\n" +
      "                          <li>攻克分布式事务处理、实时计算引擎等5+项核心技术难题，推动系统性能提升200%</li>\n" +
      "                          <li>构建千万级深度学习数据采集管道，设计自动化预处理框架提升数据清洗效率60%</li>\n" +
      "                          <li>主导CI/CD及监控体系落地，实现日均300+次自动化部署，系统可用性达99.95%</li>\n" +
      "                        </ul>"
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
            src="/src/assets/images/material.jpg"
          ></v-parallax>
          <v-card-text class="d-flex align-bottom flex-sm-row flex-column ga-6 pa-6">
            <div class="d-flex h-0">
              <v-avatar
                class="user-profile-avatar mx-auto"
                rounded
                size="130"
              >
                <v-img src="/src/assets/images/touxiang.png" cover></v-img>
              </v-avatar>
            </div>
            <div class="mt-16 mt-sm-0 pt-6 pt-sm-0 w-100">
              <h4 class="mb-2 text-center text-h4 text-sm-start">{{ t('about.text.name') }}</h4>
              <div class="d-flex align-center justify-center justify-sm-space-between flex-wrap gap-5">
                <div class="d-flex flex-wrap justify-center justify-sm-start flex-grow-1 ga-8">
                  <span class="d-flex ga-2 align-center">
                    <v-icon icon="mdi-xml"></v-icon>
                    <span class="text-body-2 font-weight-medium">{{ t('about.text.develop') }}</span>
                  </span>

                  <span class="d-flex ga-2 align-center">
                    <v-icon icon="mdi-map-marker-outline"></v-icon>
                    <span class="text-body-2 font-weight-medium">{{ t('about.text.beijing') }}</span>
                  </span>

                  <span class="d-flex ga-2 align-center">
                    <v-icon icon="mdi-calendar-today-outline"></v-icon>
                    <span class="text-body-2 font-weight-medium">2018-03-14</span>
                  </span>
                </div>
              </div>
            </div>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col class="v-col-md-4 v-col-12">
        <v-row class="animate__animated animate__fadeInLeft">
          <v-col cols="12">
            <v-card rounded border :subtitle="t('about.text.basic')">
              <v-card-text>
                <v-list density="compact">
                  <v-list-item class="align-center">
                    <v-icon icon="mdi-account" size="small"></v-icon>
                    <span class="ml-1">{{ t("about.text.full_name") }}: {{ t("about.text.name") }}</span>
                  </v-list-item>
                  <v-list-item>
                    <v-icon icon="mdi-check-bold" size="small"></v-icon>
                    <span class="ml-1">{{ t('about.text.status') }}: {{ t("about.text.in-service") }}</span>
                  </v-list-item>
                  <v-list-item>
                    <v-icon icon="mdi-crown" size="small"></v-icon>
                    <span class="ml-1">角色: 研发</span>
                  </v-list-item>
                  <v-list-item>
                    <v-icon icon="mdi-flag-variant" size="small"></v-icon>
                    <span class="ml-1">国家: 中国</span>
                  </v-list-item>
                  <v-list-item>
                    <v-icon icon="mdi-phone-in-talk" size="small"></v-icon>
                    <span class="ml-1">电话: 17611061199</span>
                  </v-list-item>
                  <v-list-item>
                    <v-icon icon="mdi-wechat" size="small"></v-icon>
                    <span class="ml-1">微信: wang594504110</span>
                  </v-list-item>
                  <v-list-item>
                    <v-icon icon="mdi-email" size="small"></v-icon>
                    <span class="ml-1">Email: 594504110@qq.com</span>
                  </v-list-item>
                  <v-list-item>
                    <v-icon icon="mdi-github" size="small"></v-icon>
                    <span class="ml-1">Github: <a href="https://github.com/wangjianweiwei">https://github.com/wangjianweiwei</a></span>
                  </v-list-item>
                </v-list>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="12">
            <v-card rounded border :subtitle="t('about.text.skill')">
              <v-card-text>
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
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-col>
      <v-col class="v-col-md-8 v-col-12">
        <v-row class="animate__animated animate__fadeInRight">
          <v-col cols="12">
            <v-card rounded border :subtitle="t('about.text.work')">
              <v-card-text>
                <v-timeline side="end" density="comfortable" line-thickness="2px" line-inset="22" truncate-line="start"
                            align="start">
                  <v-timeline-item
                    width="100%"
                    v-for="work in works"
                    :key="work.id"
                    :dot-color="work.color"
                    size="xs-small"
                  >
                    <template v-slot:default>

                      <div class="d-flex justify-space-between align-center gap-2 flex-wrap mb-3">
                        <span class="text-body-2 font-weight-bold">{{ work.company }}</span>
                        <span class="text-disabled">{{ work.working_hours }}</span>
                      </div>
                      <div class="mb-3">
                        {{ work.title }}
                      </div>
                      <div v-html="work.responsibility">

                      </div>
                    </template>
                  </v-timeline-item>
                </v-timeline>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="12">
            <v-card rounded border :subtitle="t('about.text.projects')">
              <v-card-text>
                <v-timeline side="end" density="comfortable">
                  <v-timeline-item
                    v-for="item in items"
                    :key="item.id"
                    :dot-color="item.color"
                    size="xs-small"
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
              </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="12">
            <v-card rounded border :subtitle="t('about.text.achievement')">
              <v-card-text>
                <v-timeline side="end" density="comfortable">
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
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-col>


    </v-row>
  </div>
</template>


<style lang="css">
.user-profile-avatar {
  border: 3px solid rgb(var(--v-theme-surface));
  inset-block-start: -3rem;
}
</style>
