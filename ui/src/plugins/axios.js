import axios from "axios";


const request = axios.create({
  // baseURL: "http://me-api.ifmatch.top"
  baseURL: "http://127.0.0.1:8000",
})
request.interceptors.request.use(config => {
  // 1.从缓存中获取到token,这里的Authorization时登录时你给用户设置token的键值
  let authorization = localStorage.getItem("token");
  // 2.如果token不为null，那么设置到请求头中，此处哪怕为null，我们也不进行处理，因为后台会进行拦截
  if (authorization) {
    //后台给登录用户设置的token的键时什么，headers['''']里的键也应该保持一致
    config.headers['Authorization'] = authorization;
  }
  // 3.放行
  return config;
}, error => {
//失败后抛出错误
  Promise.reject(error);
})

export default request
