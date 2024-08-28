import Vue from 'vue';
import Vuex from 'vuex';

// 引入插件  持久化
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

const store = new Vuex.Store({
    state: {
        booksList: [] // 定义一个booksList，以供全局使用
    },
    mutations: {
        setBooksList(state, booksList) {
            state.booksList = booksList
        }
    },
    /* vuex数据持久化配置 */
    plugins: [createPersistedState({
        storage: window.sessionStorage,
        paths: ['booksList'] // 暂时只持久化 booksList 状态
    })],
});

export default store;