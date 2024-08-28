<template>
    <el-container class="wrapper" element-loading-text="拼命加载中">
        <el-backtop :bottom="60" :width="500">
            <div class="backToTop">
                返回顶部
            </div>
        </el-backtop>

        <el-row style="padding-left: 125px;padding-right: 125px;height:150px;width:100%">
            <el-row class="book_header" style="width:100%">
                <el-col class="titleContainer">
                    <!-- 这里放置“标题和logo” -->
                    <span class="bookICON"></span>
                    <span class="loginTitle">书籍管理系统</span>
                </el-col>

                <el-col class="searchBook">
                    <!-- 这里放置“书籍搜索框“ -->
                    <el-autocomplete 
                        popper-class="my-autocomplete" 
                        placeholder="搜索书籍" 
                        v-model="state2"
                        :fetch-suggestions="querySearch" 
                        :trigger-on-focus="false" 
                        @select="handleSelect">
                        <template slot-scope="{ item }">
                            <div class="searchContent">
                                <div class="bookCover"><img :src="item.bookCover" alt="Book Cover" class="bookCoverPic"></div>
                                <div class="bookTitle">{{ item.bookTitle }}</div>
                                <span class="bookType">{{ item.bookType }}</span>
                            </div>
                        </template>
                        <el-button type="danger" icon="el-icon-search" slot="suffix"></el-button>
                    </el-autocomplete>
                </el-col>

                <el-col class="MyBook">
                    <!-- 这里放置“我的书架” -->
                    <el-button icon="el-icon-notebook-2" style="float:right">我的书架</el-button>
                    <el-button icon="el-icon-document-add" @click="addBook = true"
                        style="float:right;margin-right:15px;">添加书籍</el-button>
                </el-col>
            </el-row>

            <el-row style="width:100%">
                <el-row class="navigation">
                    <!-- 这里放置导航栏 -->
                    <el-menu class="el-menu-style" router unique-opened mode="horizontal" background-color="#3E3D43"
                        text-color="#ffffff" active-text-color="#FFFFFF">
                        <template v-for="item in navigationItems">
                            <template v-if="item.subs">
                                <el-submenu :index="item.index" :key="item.index" class="el-menu-item-sub-style">
                                    <template slot="title">
                                        <i :class="item.icon"></i>
                                        <span slot="title">{{ item.title }}</span>
                                    </template>
                                    <template v-for="subItem in item.subs">
                                        <el-menu-item @click.native="subItem.func">
                                            {{ subItem.title }}
                                        </el-menu-item>
                                    </template>
                                </el-submenu>
                            </template>
                            <template v-else>
                                <el-menu-item :index="item.index" :key="item.index" class="el-menu-item-style"
                                    @click.native="item.func">
                                    <i :class="item.icon"></i>
                                    <span slot="title">{{ item.title }}</span>
                                </el-menu-item>
                            </template>
                        </template>
                    </el-menu>
                </el-row>
            </el-row>

        </el-row>

    </el-container>
</template>

<script>
import {
    getChapter
}from "../api/api";

export default {
    name:'mainHeader',
    data() {
        let self = this
        return{
            navigationItems: [
                {
                    icon: 'el-icon-s-home',
                    title: '首页'
                },
                {
                    icon: 'el-icon-my-request',
                    title: '全部作品',
                }, {
                    icon: 'el-icon-my-issue',
                    title: '排行',
                }, {
                    icon: 'el-icon-my-audit',
                    title: '完本'
                }, {
                    icon: 'el-icon-my-tc',
                    title: '免费'
                },
                {
                    icon: 'el-icon-mobile-phone',
                    title: '客户端'
                },
                {
                    icon: 'el-icon-user-solid',
                    title: '显示当前用户名',
                    subs: [
                    {
                        title: '个人中心',
                    }, {
                        title: '数据统计',
                        func: self.goToSta
                    }, {
                        title: '退出登录',
                        func: self.signout
                    }]
                }
            ],
            state2:''
        }
    },

    created() {
    },
    methods: {
        signout() {
            this.$message({ type: 'warning', message: '即将退出登录' });
            setTimeout(() => {
                localStorage.removeItem('isLoggedIn');
                localStorage.removeItem('userID');
                localStorage.removeItem('bookCategoryItems');
                this.$router.push('/login');
                
            }, 2000)
        },
        goToSta(){
            this.$router.push('/dataStatistics')
        },
        querySearch(queryString, cb) {
            var booksList = this.booksList;
            var results = queryString ? booksList.filter(this.createFilter(queryString)) : booksList;
            // 调用 callback 返回建议列表的数据
            cb(results);
        },
        createFilter(queryString) {
            return (book) => {
                return (book.bookTitle.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
            };
        },
        handleSelect(item) {
            this.$router.push(`/book/${item.bookID}`)
            next();
        }
    },
    watch:{
        $route(to,from) {this.$router.go(0)}
    },
    mounted(){
        this.booksList = this.$store.state.booksList
        // console.log('booksList: ',this.booksList)
    }
}

</script>

<style lang="less" scoped>
// 返回顶部
.backToTop{
    height: 45px;
    width: 100%;
    background-color: #f2f5f6;
    box-shadow: 0 0 6px rgba(0,0,0, .12);
    text-align: center;
    line-height: 20px;
    color: #1989fa;
    font-size:15px;
}

.wrapper {
    width:100%;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    overflow-y: auto;
    display: flex;
    justify-content: center;
}

.book_header {
    display: flex;
    margin-bottom: 15px;
}

// 以下定义标题的样式
.book_header .titleContainer {
    display: flex;
    margin-top: 15px;
}

.book_header .titleContainer .bookICON {
    width: 50px;
    height: 50px;
    background: url('~@/assets/book.jpeg') no-repeat center center;
    background-size: contain;
    display: inline-block;
    margin-right: 10px;
}

.book_header .titleContainer .loginTitle {
    font-size: 24px;
    font-weight: bold;
    font-family: 'Kaiti', sans-serif;
    margin-top: 10px;
}

// 以下定义搜索框的样式
.book_header .searchBook {
    display: flex;
    margin-top: 18px;
}

.my-autocomplete li {
    .searchContent {
        display: flex;
        align-items: center;
        width: 100%;
    }

    .searchContent .bookCover {
        height: 100%;
        width: 20%;
        padding-top: 5px;
    }

    .bookCoverPic{
        width: 50px;
        height: 80%;
    }

    .searchContent .bookTitle {
        height: 100%;
        width: 70%;
        text-overflow: ellipsis;
        overflow: hidden;
        padding-left: 10px;
    }

    .searchContent .bookType {
        height: 100%;
        width: 10%;
        font-size: 12px;
        color: #b4b4b4;
    }
}
.el-autocomplete /deep/.el-input--suffix{
    width: 350px;
    padding-right: 0;
}

.el-autocomplete /deep/.el-button--danger{
    margin-right: -10px;
}

.book_header .MyBook {
    margin-top: 18px;
}

// 以下定义el-menu的基本样式
.el-menu-style {
    display: flex;
    justify-content: center;
    font-size: 15px;
    font-weight: bold;
}

</style>