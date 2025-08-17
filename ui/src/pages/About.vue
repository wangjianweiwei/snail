<script setup>
import 'animate.css';
import {ref} from "vue";
import {useI18n} from "vue-i18n";
import {getRandomColor} from "@/plugins/vuetify/theme";


const {t} = useI18n()
// 个人评价
const evaluation = [
  "具有很强的环境适应能力，学习能力以及工作中发现问题，解决问题的能力",
  "具有较好的理解能力和沟通能力，能够很好的协调员工及部门间的工作",
  "具备高度责任感与主人翁意识，始终以整体目标为导向，主动推动问题解决",
  "热爱创业型团队氛围，以结果为导向，在资源有限的环境下快速响应、持续输出价值",
  "始终保持高标准的职业素养与稳定输出，在任职期间持续获得领导与同事的高度好评"
]
// 工作经历
const works = ref([
  {
    id: 1,
    color: "primary",
    company: "北京莱迈医疗信息科技有限公司",
    working_hours: "2023/03 - 2025/07",
    title: "研发经理",
    responsibility: [
      "主导ESDR系统产品线的持续迭代与优化，在保持业务连续性的同时，对核心模块进行架构重构，提升系统稳定性与扩展性",
      "推进敏捷开发流程落地，建立以Sprint为单位的迭代机制，引入Jira实现任务拆解、优先级规划，配合Jenkins打通自动化构建与部署流程",
      "优化私有化部署方式，提高部署及更新效率",
      "系统性解决版本质量问题：过去每个版本开发周期约2个月、bug修复周期长达1个月，平均版本bug数超200；通过优化研发流程、补齐产品职能空白、提升代码质量，显著降低 bug 数量并压缩交付周期",
      "后期主导多个医院项目的定制开发与实施落地，负责公司所有医院项目的技术交付对接，梳理并规范项目问题响应与交付流程，提升多项目并行执行效率",
      "参与项目研发部门 绩效管理体系 搭建与执行，制定评估指标与激励机制，强化团队目标对齐与人才发展"
    ]
  },
  {
    id: 2,
    color: 'info',
    company: "北京海马轻帆娱乐科技有限公司",
    working_hours: "2019/04 - 2022/12",
    title: "后端研发负责人",
    responsibility: [
      "主导后端平台整体架构设计与技术选型，拆解系统模块，规划服务边界，推动系统演进与技术升级",
      "负责后端团队开发任务的全流程管理，包括需求拆解、进度跟踪、代码评审与质量控制，保障项目按时、高质量交付",
      "梳理并规范后端研发流程，制定代码规范、CI/CD流程与上线策略，提升团队协作效率与交付稳定性",
      "深度参与产品需求评审与设计讨论，站在技术可实现性、可扩展性角度提出建设性建议，推动产品功能合理落地",
      "攻克关键技术难点，承担核心模块研发任务，解决高并发、性能瓶颈、架构演进等核心问题",
      "负责后端系统的部署与运维工作，包括容器化部署、日志监控、故障响应与系统稳定性保障",
    ]
  },
])
// 项目经历
const projects = ref([
  {
    id: 1,
    color: "",
    role: "技术经理",
    name: "ESDR临床研究数据一体化平台",
    introduction: [
      {
        name: "责任描述",
        text: [
          "负责平台架构优化，技术选型，提升系统稳定性、可维护性和数据一致性",
          "跟踪并监督开发任务生命周期，把握进度，成本和质量",
          "及时解决重大的技术问题",
          "快速协调内部资源响应客户问题"]
      },
      {
        name: "项目简介",
        text: ["以自有的数字纸张及医学NLP专利技术为基础、利用人工智能和大数据技术构建的全方位临床研究数智一体化平台。本平台集数据采集/录入、数据治理分析、数据溯源等数据管理到项目精细化全流程管理和患者多端（PC端、移动端）管理于一体，支持包括了临床试验（BE和Ⅰ-Ⅳ期），RWS、IIT等在内的各种类型的临床研究，多角度及多维度实现临床研究的数字化和智能化管理"]
      },
      {
        name: "技术方案",
        text: [
          "采用前后端分离架构，后端基于Flask+SQLAlchemy构建restful服务，前端采用React+Ant Design",
          "使用MySQL存储结构化数据，Redis提供缓存与消息通信，Celery实现任务异步处理与定时调度",
          "基于智谱GLM-4大模型对化验单、病历文本等进行智能识别与结构化解析",
          "结合MinIO实现文件的私有化存储、访问控制与签名记录",
          "集成Kettle实现与多家医院的数据对接与标准化ETL流程",
          "对Medidata、里恩、Clinflash、CIMS等EDC平台进行可靠的数据对接",
          "系统整体通过docker-compose私有化部署，适配医院内网环境，支持快速上线与灵活扩容",
          "使用Apipost进行API设计，API调试，生成API文档"]
      }
    ]
  },
  {
    id: 2,
    color: "",
    name: "灵犀-剧本评估",
    role: "后端研发",
    introduction: [
      {
        name: "责任描述",
        text: [
          "主导技术方向，参与架构设计",
          "需求评审，任务拆解，任务排期，功能开发，进度跟进，质量把控，测试用例评审",
          "部署，线上运维"
        ]
      },
      {
        name: "项目简介",
        text: [
          "该系统是公司核心战略和核心产品，提供多类型作品评估，包括电影，电视剧，网络大电影，小说，针对剧情，场次，人设，互动，命运走势等多种维度对剧本分析，大部分采用和业务紧密结合的逻辑算法进行实现，除此之外还有部分算法使用深度学习实现",
          "系统提供剧本评估，拆解，会员，积分，素材，版权存证，小说转剧本，剧本大纲等一系列功能",
          "该项目自2019年12月对外提供服务，共迭代167个版本，提供300+接口",
          "系统提供包括PC网页，H5，安卓APP，微信公众号H5，微信小程序"
        ]
      },
      {
        name: "技术方案",
        text: [
          "该系统大部分采用阿里云环境，部分自建",
          "采用Django框架，按照领域和公共特性进行模块或者服务划分",
          "采用MySQL，MongoDB作为主要存储",
          "集成RabbitMQ，用于站内事件分发(event bus)，Celery broker等",
          "采用ELK+Filebeat进行日志收集，主要收集埋点数据",
          "接入微信公众号体系，例如通过微信Oauth2丰富系统的登录，注册方式等",
          "集成Sentry监控平台，通过Sentry报警以及收集的错误堆栈信息快速定位问题",
          "通过Nginx实现负载均衡，限流等需求",
          "使用阿里云oss进行文件存储或者中转",
          "接入ELK APM对进系统进行性能监控，包括但不限于接口异常，接口耗时情况，TPM等",
          "算法调度平台使用Flask作为api接口，Celery进行算法任务流调度",
          "使用Django-admin搭建管理后台",
          "自建pypi源托管二方包",
          "前端采用React框架，前后端分离",
          "使用Apipost进行API设计，API调试，生成API文档"
        ]
      }
    ]
  },
  {
    id: 3,
    color: "",
    role: "后端研发+前端研发",
    name: "灵犀-协作剧本创作",
    introduction: [
      {
        name: "责任描述",
        text: [
          "技术调研，架构设计，协同主要功能测试",
          "功能实现以及前端协同部分主要逻辑实现"
        ]
      },
      {
        name: "项目简介",
        text: [
          "实现类似石墨文档垂直于编剧行业的低延迟协同编辑器，主要功能包括多人实时协同编辑，版本保存，版本恢复，章节管理，场次管理，离线写作及网络恢复后的数据同步等主要功能",
          "自2021年3月开始技术调研，2021年6月底上线"
        ]
      },
      {
        name: "技术方案",
        text: [
          "技术栈采用Sanic+SocketIO+Redis+MongoDB+RabbitMQ+Celery+Express+Nginx",
          "利用Sanic+Socketio实现高性能的websocket服务",
          "使用RabbitMQ实现消息广播，在多用户之间进行消息传递",
          "使用阿里云oss进行文件存储或者中转",
          "利用Redis的原子性保证协同时op的顺序一致性",
          "采用Operational Transformation作为多人同时编辑时的冲突解决方案",
          "协同编辑器具体细节可以面谈"
        ]
      }
    ]
  },
  {
    id: 4,
    color: "",
    name: "灵犀-剧本格式化",
    role: "后端研发",
    introduction: [
      {
        name: "责任描述",
        text: [
          "剧本数据整理，预处理",
          "特征工程开发",
          "Web服务开发及部署"
        ]
      },
      {
        name: "项目简介",
        text: [
          "为解决国内市面上复杂多样的剧本格式（主要针对场次标题写作格式五花八门的问题）可以顺利的在评估平台进行评估，降低剧本评估在剧本格式要求的门槛，提高用户剧本评估的成功率",
          "文本格式转换，例如 word转txt，pdf转txt",
          "txt文本的预处理，包括繁体转简体，标点符号统一，全半角转换",
          "特征提取",
          "模型预测",
          "对场次标题进行标准格式化",
        ]
      },
      {
        name: "技术方案",
        text: [
          "采用LightGBM实现多分类的机器学习任务",
          "特征工程中共采用37个特征",
          "通过windows office进行文档格式转换",
          "使用Flask对外提供HTTP服务",
        ]
      }
    ]
  },
  {
    id: 5,
    color: "",
    role: "后端研发",
    name: "灵犀-数据大盘",
    introduction: [
      {
        name: "责任描述",
        text: [
          "根据运营和产品对数据的需求在系统中埋点",
          "根据Elasticsearch现有数据以及需求中要体现的数据维度在Kibana中绘制图表",
          "服务部署，线上运维"
        ]
      },
      {
        name: "项目简介",
        text: [
          "随着运营部门对产品在百度，抖音，B站，小红书以及线下等多渠道的推广，为保证精准推广和了解用户，该项目应运而生，该系统采用ELK+Filebeat"
        ]
      },
      {
        name: "技术方案",
        text: [
          "通过在代码中（不仅限于后端）进行埋点，将埋点数据写入日志文件，经Filebeat将日志发送到Logstash，在由Logstash将数据存储在Elasticsearch中，最后通过Kibana强大的自定义图表功能进行数据展示"
        ]
      }
    ]
  },
])
// 个人技能
const skills = ref(["Linux", "Python", "Git", "JavaScript", "Vue", "Element-UI", "Vuetifyjs", "多进程", "多线程", "协程", "MySQL", "MongoDB", "Redis", "Elasticsearch", "RabbitMQ", "Kafka", "Minio", "Docker", "Docker-compose", "Kubernetes", "Django", "Flask", "sqlalchemy", "asyncio", "Sanic", "FastAPI", "GitLab", "Jenkins", "Scrum", "http", "websocket", "sse", "TCP/IP", "Celery", "ELK", 'LangChain', "RAG", "Scrapy"])
// 爱好
const hobby = ref(["摄影", "篮球", "毽子", "自驾", "美剧"])
</script>

<template>
  <v-row justify="center" class="py-4" no-gutters>
    <v-col cols="11" xs="11" sm="11" md="11" lg="8" xl="7" xxl="6">
      <v-row>
        <v-col cols="12" class="animate__animated animate__bounceInDown">
          <v-card>
            <v-parallax
              height="300"
              src="/src/assets/images/material.jpg"
            ></v-parallax>
            <v-card-text class="d-flex align-bottom flex-sm-row flex-column ga-6 pa-6">
              <div class="d-flex h-0">
                <v-avatar
                  class="user-profile-avatar mx-auto"
                  rounded
                  size="130"
                >
                  <v-img src="/src/assets/images/me.jpeg" cover></v-img>
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
          <v-row class="animate__animated animate__bounceInLeft animate__slow">
            <v-col cols="12">
              <v-card :subtitle="t('about.text.basic')">
                <v-card-text>
                  <v-list border="0" density="compact">
                    <v-list-item class="align-baseline">
                      <v-icon icon="mdi-account-outline" size="small"></v-icon>
                      <span class="ml-1">{{ t("about.text.full_name") }}: {{ t("about.text.name") }}</span>
                    </v-list-item>
                    <v-list-item class="align-center">
                      <v-icon icon="mdi-update" size="small"></v-icon>
                      <span class="ml-1">{{ t("about.text.age") }}: 28</span>
                    </v-list-item>
                    <v-list-item class="align-center">
                      <v-icon icon="mdi-timelapse" size="small"></v-icon>
                      <span class="ml-1">{{ t("about.text.experience") }}: 6 {{ t('about.text.year') }}</span>
                    </v-list-item>
                    <v-list-item>
                      <v-icon icon="mdi-crown-outline" size="small"></v-icon>
                      <span class="ml-1">{{ t("about.text.role") }}: {{ t("about.text.develop") }}</span>
                    </v-list-item>
                    <v-list-item>
                      <v-icon icon="mdi-flag-outline" size="small"></v-icon>
                      <span class="ml-1">{{ t("about.text.country") }}: {{ t("about.text.china") }}</span>
                    </v-list-item>
                    <v-list-item>
                      <v-icon icon="mdi-phone-outline" size="small"></v-icon>
                      <span class="ml-1">{{ t("about.text.phone") }}: 17611061199</span>
                    </v-list-item>
                    <v-list-item>
                      <v-icon icon="mdi-wechat" size="small"></v-icon>
                      <span class="ml-1">{{ t("about.text.wechat") }}: wang594504110</span>
                    </v-list-item>
                    <v-list-item>
                      <v-icon icon="mdi-email-outline" size="small"></v-icon>
                      <span class="ml-1">{{ t("about.text.email") }}: 594504110@qq.com</span>
                    </v-list-item>
                    <v-list-item>
                      <v-icon icon="mdi-github" size="small"></v-icon>
                      <span class="ml-1">Github: <a href="https://github.com/wangjianweiwei"><v-icon
                        icon="mdi-cursor-default-click-outline"></v-icon></a></span>
                    </v-list-item>
                  </v-list>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="12">
              <v-card :subtitle="t('about.text.skill')">
                <v-card-text>
                  <v-chip variant="tonal" label class="ma-1" v-for="n in skills" :text="n" color="primary">
                  </v-chip>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="12">
              <v-card :subtitle="t('about.text.hobby')">
                <v-card-text>
                  <v-chip variant="tonal" label class="ma-1" v-for="n in hobby" :text="n" color="primary">
                  </v-chip>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-col>
        <v-col class="v-col-md-8 v-col-12">
          <v-row class="animate__animated animate__bounceInRight animate__slow">
            <v-col cols="12">
              <v-card :subtitle="t('about.text.selfEvaluation')">
                <v-card-text>
                  <v-list border="0" density="compact" lines="false">
                    <v-list-item v-for="n in evaluation">
                      <p class="dot-paragraph">{{ n }}</p>
                    </v-list-item>
                  </v-list>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="12">
              <v-card :subtitle="t('about.text.work')">
                <v-card-text>
                  <v-timeline side="end" align="start">
                    <v-timeline-item
                      width="100%"
                      v-for="(work, i) in works"
                      :key="work.id"
                      :dot-color="getRandomColor()"
                      size="xs-small"
                    >
                      <template v-slot:default>
                        <v-card class="pa-3">
                          <div class="d-flex justify-space-between align-center gap-2 flex-wrap mb-3">
                            <div class="d-flex align-center">
                              <p class="text-body-1 font-weight-bold mr-1">{{ work.company }}</p>
                              <v-chip color="primary" variant="elevated" size="x-small">
                                {{ work.title }}
                              </v-chip>
                            </div>
                            <div class="text-disabled">{{ work.working_hours }}</div>
                          </div>
                          <v-list border="0" density="compact" lines="false">
                            <v-list-item v-for="i in work.responsibility">
                              <p class="dot-paragraph">{{ i }}</p>
                            </v-list-item>
                          </v-list>
                        </v-card>
                      </template>
                    </v-timeline-item>
                  </v-timeline>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="12">
              <v-card :subtitle="t('about.text.projects')">
                <v-card-text>
                  <v-timeline side="end" align="start">
                    <v-timeline-item
                      width="100%"
                      fill-dot
                      v-for="project in projects"
                      :key="project.id"
                      :dot-color="getRandomColor()"
                      size="xs-small"
                    >
                      <template v-slot:default>
                        <v-card class="pa-3">
                          <div class="d-flex justify-space-between align-center gap-2 flex-wrap">
                            <span class="text-body-1 font-weight-bold">{{ project.name }}</span>
                            <v-chip color="primary" variant="elevated" size="x-small">
                              {{ project.role }}
                            </v-chip>
                          </div>
                          <div v-for="n in project.introduction">
                            <v-chip class="mt-2" size="small" label :text="n.name" color="primary"></v-chip>
                            <v-list border="0" density="compact" lines="false">
                              <v-list-item v-for="i in n.text">
                                <p class="dot-paragraph">{{ i }}</p>
                              </v-list-item>
                            </v-list>
                          </div>
                        </v-card>
                      </template>
                    </v-timeline-item>
                  </v-timeline>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-col>
  </v-row>

</template>


<style lang="css">
.user-profile-avatar {
  border: 3px solid rgb(var(--v-theme-surface));
  inset-block-start: -3rem;
}

.dot-paragraph {
  display: list-item;
  list-style-type: disc;
  margin-left: 20px; /* 控制缩进 */
}
</style>
