import axios from "axios";

import {router} from "@/plugins/router";
import {baseURL} from "@/config";


const request = axios.create({
  baseURL: baseURL
})
request.interceptors.request.use(config => {
  // 1.从缓存中获取到token,这里的Authorization时登录时你给用户设置token的键值
  let token = localStorage.getItem("token");
  // 2.如果token不为null，那么设置到请求头中，此处哪怕为null，我们也不进行处理，因为后台会进行拦截
  if (token) {
    //后台给登录用户设置的token的键时什么，headers['''']里的键也应该保持一致
    config.headers['token'] = token;
  }
  // 3.放行
  return config;
}, error => {
//失败后抛出错误
  Promise.reject(error);
})


request.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response && error.response.status === 401) {
      // 未授权时跳转到登录页面
      localStorage.removeItem('token');
      router.push('/login');
    }
    return Promise.reject(error);
  }
);


export default request
