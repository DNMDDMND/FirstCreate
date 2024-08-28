<template>
    <div class="wrapper">
        <mainHeader />
        <div class="childrenContent">
            <router-view></router-view>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import mainHeader from './mainHeader.vue'
import {
    
}from "../api/api";

export default {
    name: 'mainIndex',
    data() {
        return {}
    },
    components: { mainHeader },
    methods: {

    },
}
</script>

<style lang="less" scoped>
.wrapper {
    overflow: auto; /* 添加滚动条 */
}

.childrenContent {
    margin-top: 30px;
    position: absolute;
    left: 125px;
    top: 140.11px;
    width: 80%;

    /* 设置滚动条的样式 */
    &::-webkit-scrollbar {
        width: 8px;
    }
    &::-webkit-scrollbar-thumb {
        background-color: rgba(0, 0, 0, 0.2);
    }
}

</style>