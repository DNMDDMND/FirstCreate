// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store';

import less from 'less'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import axios from 'axios'
import VueAxios from 'vue-axios'
import * as echarts from 'echarts';
Vue.prototype.$echarts = echarts

import Print from './assets/print'

Vue.use(ElementUI)
Vue.use(VueAxios, axios)
Vue.use(less)
Vue.use(Print)


axios.defaults.withCredentials = true // 请求携带cookie
axios.defaults.headers.post['X-CSRFToken'] = ''; //设置请求头的跨域密匙
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'
axios.defaults.transformRequest = [function (data) {  //将发送的post参数封装成FROM-DATA，使后端接收
  let ret = ''
  for (let it in data) {
    ret += encodeURIComponent(it) + '=' + encodeURIComponent(data[it]) + '&'
  }
  return ret
}];

Vue.config.productionTip = false

// 路由守卫
// to：即将要进入的目标 路由对象
// from：当前导航正要离开的路由
//next：放行
router.beforeEach((to, from, next) => {
  console.log('isLoggedIn: ',Boolean(localStorage.getItem("isLoggedIn")))
  if (to.matched.length != 0) {
    if (Boolean(localStorage.getItem("isLoggedIn"))) { // 判断是否登录
      if (to.path != "/" && to.path != "/login") { //判断是否要跳到登录界面
        next();
      } else {
        /**
         * 防刷新，如果登录，修改路由跳转到登录页面，修改路由为登录后的首页
         */
        next({
          path: '/Home'
        })
      }
    } else {
      if (to.path === "/login"){
        next()
      }else {
      next({
        path: '/login',
        query: { redirect: to.fullPath }
      })};
    }
  } else {
    next({
      path: '/login',
      query: { redirect: to.fullPath } // 将跳转的路由path作为参数，登录成功后跳转到该路由
    })
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
