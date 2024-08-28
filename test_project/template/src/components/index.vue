<template>
    <div class="wrapper">
        <commonViews />
        <div class="childrenContent">
            <router-view></router-view>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import commonViews from './commonViews.vue'
axios.defaults.timeout = 60000 // 请求超时
axios.defaults.baseURL = '/api'
axios.defaults.withCredentials = true      // axios请求携带cookie

export default {
    name: 'index',
    data() {
        return {}
    },
    components: { commonViews },
    methods: {

    },
}
</script>

<style lang="less" scoped>
.wrapper {
    overflow: hidden; /* 防止内容溢出影响整体布局 */
}

.childrenContent {
    position: absolute;
    left: 20%;
    top: 140.11px;
    bottom: 0; /* 从顶部到底部的距离 */
    width: 80%;
    overflow: auto; /* 添加滚动条 */

    /* 如果需要，可以设置滚动条的样式 */
    &::-webkit-scrollbar {
        width: 8px;
    }
    &::-webkit-scrollbar-thumb {
        background-color: rgba(0, 0, 0, 0.2);
    }
}

</style>