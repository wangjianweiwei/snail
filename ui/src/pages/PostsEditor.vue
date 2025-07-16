<script setup>
import {onMounted, ref, watch} from "vue";
import {useRoute} from "vue-router";
import {composePostApi, imageUpload, retrievePostApi, updatePostApi} from "@/services";
import {useTheme} from 'vuetify'

const theme = useTheme()
const route = useRoute()
const snackbar = ref(false)
const snackbarText = ref("")
const postId = route.params.id
const titleRef = ref("")
let editor = null

const HeaderComponent = () => {
  const React = window.React;
  const {useState} = React;

  return React.createElement(() => {
    const [title, setTitle] = useState(titleRef.value);

    const handleSave = async () => {
      // 调用 Vue 中的保存逻辑，例如：
      await updatePostApi({pk: postId, title: title});
      snackbar.value = true;
      snackbarText.value = "标题保存成功";
    };

    const handleKeyDown = (e) => {
      if (e.key === 'Enter') {
        e.preventDefault();
        e.target.blur(); // 主动触发 blur
      }
    };

    return React.createElement(
      'div',
      {
        style: {
          // padding: '10px 0px',
          // background: '#1e1e1e',
          // color: '#fff',
          borderBottom: '1px solid #333',
        }
      },
      React.createElement('input', {
        value: title,
        onChange: (e) => setTitle(e.target.value),
        onKeyDown: handleKeyDown,
        placeholder: "请输入标题",
        className: "doc-title-input",
        style: {
          width: '100%',
          fontSize: '24px',
          fontWeight: '600',
          padding: '16px 0px 16px 0px',
          // backgroundColor: '#1e1e1e',
          border: '1px solid transparent',
          borderRadius: '8px',
          outline: 'none',
          transition: 'border-color 0.2s, box-shadow 0.2s',
        },
        onBlur: (e) => {
          handleSave();
        }
      })
    );
  });
};


async function save() {
  let content = editor.getDocument()
  let text = editor.getDocument("text/plain")
  let abstract = text.substring(0, 128)

  let res = await composePostApi(postId, content, abstract, text.length)
  snackbar.value = true
  if (res) {
    snackbarText.value = "保存成功"
  } else {
    snackbarText.value = "保存失败"
  }
}

function handleCtrlS(event) {
  if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 's') {
    event.preventDefault(); // 阻止默认保存行为
    save()
  }
}

onMounted(async () => {
  let data = await retrievePostApi(postId)
  titleRef.value = data.title
  const {createOpenEditor} = window.Doc;
  // 创建编辑器
  editor = createOpenEditor(document.getElementById('editor'), {
    header: HeaderComponent(),
    darkMode: true,
    defaultFontsize: 15,
    layout: "fixed",
    placeholder: {
      tip: '请输入文字',
      emptyParagraphTip: '输入 / 唤起更多',
    },
    toc: {
      enable: false
    },
    input: {},
    image: {
      isCaptureImageURL() {
        return false;
      },
      createUploadPromise: async (request) => {
        const {type, data} = request;

        if (type === 'url') {
          // 假设你有一个接口可以根据URL转存图片
          console.log("需要转存的图片URL:", data);
        } else if (type === 'file') {
          // 假设上传文件
          const formData = new FormData();
          formData.append("image", data);
          // 使用 axios 上传图片
          let response = await imageUpload(formData)
          return {
            url: response.url,
            size: response.size, // 文件大小
            filename: response.filename
          }
        }
        console.log(response.data.data, "////")


      },
    },
  });
  // 设置内容
  editor.setDocument('json', data.content || {type: "element", name: "#root",});
  watch(() => theme.global.name.value, (newVal, oldVal) => {
    if (newVal === "dark") {
      editor.theme.setActiveTheme("dark-mode")
    } else {
      editor.theme.setActiveTheme("default")
    }
  })
  // 监听内容变动
  document.addEventListener('keydown', handleCtrlS, true);
})

</script>

<template>
  <div style="height: 100%">
    <div id="editor" style="height: 100%" class="ne-doc-major-editor"></div>
    <v-snackbar
      v-model="snackbar"
      color="grey-darken-3"
      timeout="700"
      location="top right"
      variant="elevated"
    >
      <template v-slot:text>
        <v-progress-circular
          color="primary"
          size="20"
          indeterminate
        ></v-progress-circular>
        <span class="ml-3">{{ snackbarText }}</span>
      </template>
    </v-snackbar>
  </div>
</template>

<style>
.lakex-dark-theme-dark {
  --lakex-editor-background-primary: rgba(var(--v-theme-background)) !important;
}

.ne-layout-mode-fixed .ne-editor-wrap-content, .ne-layout-mode-adapt .ne-editor-wrap-content {
  min-width: 100% !important;
}

.ne-layout-mode-fixed .ne-editor-outer-wrap-box, .ne-layout-mode-adapt .ne-editor-outer-wrap-box {
  min-width: 100% !important;
}

.ne-layout-mode-fixed .ne-engine, .ne-layout-mode-adapt .ne-engine {
  padding: 20px 10px 90px 10px !important;
}

.ne-doc-major-editor .ne-layout-mode-fixed .ne-editor-extra-box {
  padding: 0 10px !important;
}

.ne-doc-major-editor .ne-layout-mode-fixed .ne-ui {
  padding: 0 10px !important;
}

.ne-editor ne-card[data-card-type=block] {
  margin: 14px 0 !important;
}
</style>
