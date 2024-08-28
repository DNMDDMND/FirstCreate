import Vue from 'vue'
import Router from 'vue-router'

// 定义路由组件
import index from '@/components/index'
import login from '@/components/Login'
import BookDetail from '@/components/BookDetail'
import ChapterDetail from '@/components/ChapterDetail'
import dataStatistics from '@/components/DataStatistics'
// import Home from '@/components/Home'
import BookTest from '@/components/BookTest'
import commonViews from '@/components/commonViews'
import mainHeader from '@/components/mainHeader'
import mainIndex from '@/components/mainIndex'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    // 以下为父组件
    {
      path: '/commonViews',
      name: 'commonViews',
      component: commonViews
    },
    {
      path: '/mainHeader',
      name: 'mainHeader',
      component: mainHeader
    },
    // 以下为子组件
    {
      path: '/',
      name: 'index',
      component: index,
      children: [
        {
          path: '/Home',
          name: 'Home',
          component: () => import('../components/Home')
        }
      ]
    },
    {
      path: '/mainIndex',
      name: 'mainIndex',
      component: mainIndex,
      children: [
        {
          path: '/book/:id',
          name: 'BookDetail',
          component: () => import('../components/BookDetail')
        },
        {
          path: '/book/:id/:chapterID',
          name: 'ChapterDetail',
          component: () => import('../components/ChapterDetail')
        },
        {
          path: '/dataStatistics',
          name: 'DataStatistics',
          component: () => import('../components/DataStatistics')
        },
      ]
    },
    // 以下为独立组件
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/BookTest',
      name: 'BookTest',
      component: BookTest
    }
  ]
})

export default router;
