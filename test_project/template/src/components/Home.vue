<template>
    <el-container class="wrapper" element-loading-text="拼命加载中">

        <el-main class="mainContent">
            <el-row class="bookContent">
                <!-- 这里放置页面主要内容 -->
                <el-col class="books">
                    <!-- 这里放置书架和作品推荐 -->
                    <el-row class="bookShelf">
                        <!-- 这里放置书架，展示书籍 -->
                        <!-- <el-col v-for="(book, index) in showBooksList" :key="index" class="bookShelfContent" v-if="index<4">
                            <div class="book">
                                <img :src="book.bookCover" alt="Book Cover" class="bookCover">
                                <span class="bookList">
                                    <span class="TitleAndAuthor">
                                        <el-link target="_blank" :underline="false" class="Title">{{ book.bookTitle
                                            }}</el-link>
                                        <span class="Author">作者: {{ book.bookAuthor }}</span>
                                    </span>
                                    <hr>
                                    <span class="Summary">{{ book.bookSummary }}</span>
                                </span>
                            </div>
                        </el-col> -->

                        <el-col v-for="index in booksIndexs" :key="index" class="bookShelfContent">
                            <div class="book">
                                <img :src="showBooksList[index].bookCover" alt="Book Cover" class="bookCover">
                                <span class="bookList">
                                    <span class="TitleAndAuthor">
                                        <el-link target="_blank" :underline="false" class="Title" @click="goToDetail(showBooksList[index])">{{ showBooksList[index].bookTitle}}</el-link>
                                        <span class="Author">作者: {{ showBooksList[index].bookAuthor }}</span>
                                    </span>
                                    <hr>
                                    <span class="Summary">{{ showBooksList[index].bookSummary }}</span>
                                </span>
                            </div>
                        </el-col>

                        <el-col class="page">
                            <el-button @click="backPage" :disabled="booksIndexs[0]===0" type="text" class="el-icon-caret-left" style="font-size: 20px;"></el-button>
                            <el-button @click="nextPage" :disabled="lastPage" type="text" class="el-icon-caret-right" style="font-size: 20px;"></el-button>
                            <el-button type="text" class="el-icon-refresh" style="position: absolute;right: 0;"
                                @click="changeBooks">换一换</el-button>
                        </el-col>
                    </el-row>

                    <el-row class="bookRecommend">
                        <!-- 这里放置作品推荐栏 -->
                        <el-col class="recommendTitle">
                            <!-- 这里放置作品推荐栏标题 -->
                            <span style="float:left;margin-left: 10px;margin-top: 7px;">热门小说</span>
                        </el-col>

                        <el-col class="recommendContent">
                            <!-- 这里放置作品推荐内容 -->
                            <el-col v-for="(book, index) in recommendList" :key="index" class="recommendOne" v-if="index < 14">
                                <span class="recommendType">[{{ book.type }}]</span>
                                <span class="recommendTitle">
                                    <el-link target="_blank" :underline="false" style="float:left;">{{ book.title }}</el-link>
                                </span>
                                <span class="recommendAuthor">{{ book.author }}</span>
                            </el-col>
                        </el-col>
                    </el-row>
                </el-col>
            </el-row>
        </el-main>

    </el-container>

</template>

<script>
import {
    getAllBook,
    recordInfo
} from "../api/api";

export default {
    name: 'Home',
    data() {
        return {
            searchBookContent: '',
            recommendList: [
                {
                    type: '玄幻',
                    title: '万相之王',
                    author: '天蚕土豆'
                },
                {
                    type: '科幻',
                    title: '这个道士有点凶',
                    author: '困的睡不着'
                },
                {
                    type: '都市',
                    title: '女总裁的上门女婿',
                    author: '一起成功'
                },
                {
                    type: '科幻',
                    title: '这个道士有点凶',
                    author: '困的睡不着'
                },
                {
                    type: '科幻',
                    title: '夜以继日',
                    author: '京城男宠'
                },
                {
                    type: '玄幻',
                    title: '混沌天帝诀',
                    author: '随风漫步'
                },
                {
                    type: '都市',
                    title: '陆门 七年顾初如北',
                    author: '殷寻'
                },
                {
                    type: '都市',
                    title: '一胎双宝：总裁大人，请温柔',
                    author: '堆堆'
                },
                {
                    type: '都市',
                    title: '叶凡唐若雪',
                    author: '一起成功'
                },
                {
                    type: '科幻',
                    title: '为夫之道',
                    author: '尤四姐'
                },
                {
                    type: '都市',
                    title: '涩涩小娇妻',
                    author: '橙子殿'
                },
                {
                    type: '科幻',
                    title: '左右为难',
                    author: '木吾桐'
                },
                {
                    type: '科幻',
                    title: '深度按摩',
                    author: '裸着奔'
                },
                {
                    type: '玄幻',
                    title: '深空彼岸',
                    author: '辰东'
                }
            ],
            booksList: [
                // {
                //     bookTitle: '风起龙城',
                //     bookCover: '../../static/coverage1.png',
                //     bookAuthor: '伪戒',
                //     bookSummary: '全球灾变后六十年，小冰冻期结束，各生活大区政府开始大规模收拢待规划无政府区的土地，重整资源，全面进入了复苏阶段，而这二十年也被称为“黄金二十年”',
                // }
            ],
            booksListLength: 0,
            lastPage: false,
            booksIndexs: [],
            showBooksList: [],
        }
    },
    components: {},
    methods: {
        // 换一换书籍
        changeBooks() {
            this.booksIndexs = [0,1,2,3]
            this.lastPage = false
            this.showBooksList.sort(() => Math.random() - 0.5);
        },
        // 跳转上一页书籍
        backPage() {
            this.booksIndexs = this.booksIndexs.map(index => index - 4);
            let leftCounts = 4 - this.booksIndexs.length
            if (leftCounts>0){
                let Indexs = JSON.parse(JSON.stringify(this.booksIndexs));
                for (let i=1;i<leftCounts+1;i++){
                    Indexs.push(this.booksIndexs[this.booksIndexs.length - 1]+i)
                }
                this.booksIndexs = Indexs
            }
            this.lastPage = false
        },
        // 跳转下一页书籍
        nextPage() {
            // 边缘处理，判断是否会超出索引值
            let leftCounts = this.booksListLength - this.booksIndexs[this.booksIndexs.length - 1] - 1
            if (leftCounts<4){
                let Indexs = []
                for (let i = 0;i<leftCounts;i++){
                    Indexs.push(this.booksIndexs[i] + 4)
                }
                this.booksIndexs = Indexs
                this.lastPage = true
            }else{
                this.booksIndexs = this.booksIndexs.map(index => index + 4);
                leftCounts = this.booksListLength - this.booksIndexs[-1] - 1
                if (leftCounts===0){
                    this.lastPage = true
                }
            }

        },
        // 获取所有书籍
        fetchAllBook(){
            getAllBook()
            .then(response => {
                if (response.data.code === 0){
                    const bookData = response.data.data
                    const bookDataLength = bookData.length
                    for (let bookCount = 0;bookCount < bookDataLength;bookCount++){
                        const cover_image = `../../static/bookCover/${bookData[bookCount]['cover_image']}`
                        const bookInfo = {
                            bookID: bookData[bookCount]['id'],
                            bookTitle: bookData[bookCount]['title'],
                            bookType: bookData[bookCount]['type'],
                            bookCover: cover_image,
                            bookAuthor: bookData[bookCount]['author'],
                            bookSummary: bookData[bookCount]['description'],
                        }
                        this.booksList.push(bookInfo)
                    }
                    this.booksListLength = this.booksList.length
                    this.showBooksList = this.booksList
                    this.$store.commit('setBooksList',this.booksList)
                }
            })
            .catch(error =>{
                console.log('Error fetching all book: ',error)
            })
        },
        // 跳转书籍详细页面
        goToDetail(book){
            console.log(book)
            // 增加该书的点击量，并记录用户信息
            this.recordUserInfo(book)
            this.$router.push(`/book/${book.bookID}`)
        },
        // 记录用户信息
        recordUserInfo(book){
            const params = {'userID':localStorage.getItem('userID'),'bookID':book.bookID}

            recordInfo(params)
            .then(response =>{
                if (response.data.code !== 0) {
                    console.log('record user info error: ',response.data.msg)
                }
            })
            .catch(error =>{
                console.log('record user info error: ',error)
            })
        }
    },
    created() {
        this.fetchAllBook()
        this.booksIndexs = [0,1,2,3]
    },
    computed: {
    },
    mounted() {
    }
}
</script>

<style lang="less" scoped>
.wrapper {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    height: 100vh;
    width: 100%;
    overflow: hidden;
}

// 以下定义主页主要内容的样式
.mainContent {
    width: 100%;
    padding: 0;
}

//以下定义页面主要内容的样式

//以下定义书籍分类的样式
.bookContent {
    width: 100%;
    height: 100%;
}

.left-icon {
    display: flex;
    align-items: center;
}

.left-icon span,
.left-icon p {
    margin-top: 0;
    /* 移除默认的顶部外边距 */
}

.right-icon {
    display: flex;
    align-items: center;
}

.right-icon span,
.right-icon p {
    margin-top: 0;
    /* 移除默认的顶部外边距 */
}

// 以下定义书架和作品推荐
.books {
    width: 100%;
    height: 97%;
    display: flex;
}

// 以下定义书架的样式
.books .bookShelf{
    display: flex;
    flex-wrap: wrap; /* 允许子项换行 */
    width: 70%;
    height: 100%;
    background-color: #fff;
    border: 3px solid; /* 这里设置边框宽度为2px，边框样式为实线 */
    border-color: #DDDDDD; /* 设置边框颜色为黑色 */
}

.books .bookShelf .bookShelfContent{
    width:50%;
    height:45%;
    display: flex;
    flex-wrap: wrap; /* 允许子项换行 */
    justify-content: space-between; /* 水平方向上两端对齐 */
    align-content: space-between; /* 垂直方向上两端对齐 */
    border: 1px solid; /* 这里设置边框宽度为2px，边框样式为实线 */
    border-color: #DDDDDD; /* 设置边框颜色为黑色 */
}

// 以下定义每本书的区块样式
.bookShelfContent .book{
    width:100%;
    height:100%;
    background-color: #ffffff;
    display: flex;
    align-items: center;
    margin-left: 10px;
    margin-right: 10px;
}

// 以下为定义封面的样式
.book .bookCover{
    width: 115px;
    height: 170px;
    object-fit: cover; /* 使用 cover 来填充元素 */
    margin-right: 5px;
    margin-left: 5px;
}

.book .bookList{
    width: calc(100% - 100px);
    height: 100%;
    display: flex;
    flex-wrap: wrap; /* 允许子项换行 */
}

// 以下仅创建一个虚线
.bookList hr {
    margin: 3px;
    margin-bottom: 8px;
    border: 0.5px dashed rgb(32, 27, 27);
    width: 100%;
    height: 0;

}

.bookList /deep/.el-link--inner {
    color: rgb(22, 139, 217);

}

.bookList /deep/.el-link--inner:hover {
    color: #004cff;
}

.book .bookList .TitleAndAuthor{
    height:20%;
    width:100%;
    display: flex;
    flex-wrap: wrap; /* 允许子项换行 */
}
.TitleAndAuthor .Title{
    height:50%;
    width:100%;
    font-size: 15px;
}

.TitleAndAuthor .Author{
    height:50%;
    width:100%;
    font-size: 13px;
}

.book .bookList .Summary{
    width: 100%;
    height: 68%;
    font-size: 13px;
    color: rgb(83, 95, 81);
    text-indent: 1em; /* 文字默认空两格 */
    overflow: hidden; /* 隐藏超出部分 */
    text-overflow: ellipsis; /* 超出部分以省略号显示 */
    display: -webkit-box;
    -webkit-line-clamp: 7; /* 限制在7行 */
    -webkit-box-orient: vertical;
}

// 以下定义书架底部的页数
.books .bookShelf .page{
    width:100%;
    height:7%;
    display: flex;
    justify-content: center;
    align-items: center;
}

// 以下定义作品推荐的样式
.books .bookRecommend{
    width: 28%;
    height: 98%;
    margin-left: 2%;
    background-color: #fff;
    border: 3px solid; /* 这里设置边框宽度为2px，边框样式为实线 */
    border-color: #DDDDDD; /* 设置边框颜色为黑色 */
}

// 以下定义作品推荐标题的样式
.bookRecommend .recommendTitle{
    height: 7%;
    width: 100%;
    font-weight: bold;
}

// 以下定义作品推荐内容的样式
.bookRecommend .recommendContent{
    height: 92%;
    width: 100%;
    // background-color: #1900ff;
}

.bookRecommend .recommendOne{
    height: 7%;
    width: 100%;
    display: flex;
    font-size: 11px;
    border: 1px solid; /* 这里设置边框宽度为2px，边框样式为实线 */
    border-color: #DDDDDD; /* 设置边框颜色为黑色 */
    // background-color: #ff0000;
}

.recommendOne .recommendType{
    height:7%;
    width: 15%;
    margin-top: 5px;
    position: absolute;
    left: 0;
}

.recommendOne .recommendTitle{
    height:7%;
    width: 55%;
    position: absolute;
    left: 15%; /* 将左侧定位到父元素的中间 */
    // transform: translateX(-50%); /* 使用transform属性将元素向左移动自身宽度的一半 */
    padding-top: 5px;
    white-space: nowrap; /* 防止文本换行 */
    overflow: hidden; /* 隐藏超出部分的文本 */
    text-overflow: ellipsis; /* 显示省略号 */
}

.recommendOne .recommendTitle /deep/.el-link--inner{
    font-size: 12px;
    color: rgb(22, 139, 217);
}

.recommendOne .recommendTitle /deep/.el-link--inner:hover{
    color: #004cff;
}

.recommendOne .recommendAuthor{
    height:7%;
    width: 30%;
    position: absolute;
    right: 0;
    padding-top: 5px;
    padding-right: 5px;
    text-align: right;
    white-space: nowrap; /* 防止文本换行 */
    overflow: hidden; /* 隐藏超出部分的文本 */
    text-overflow: ellipsis; /* 显示省略号 */
}

</style>