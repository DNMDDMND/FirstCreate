<template>
    <el-container class="wrapper" element-loading-text="拼命加载中">
        <el-row style="width:100%">
            <el-row class="book_detail">
                <el-row class="book_detail_header">
                    <span class="header_text">
                        <el-link target="_blank" :underline="false">书籍管理系统</el-link> > {{ bookInfo.bookType }}小说 > {{
                        bookInfo.bookTitle }}
                    </span>
                </el-row>

                <el-row class="book_detail_content">
                    <el-row style="width: 100%;height:90%;">
                        <el-col class="bookCover">
                            <div class="bookCoverContent">
                                <!-- <img :src="bookInfo.bookCover" alt="Book Cover" class="bookCoverPic"> -->
                            </div>
                        </el-col>

                        <el-col class="bookContent">
                            <el-row class="bookInfo">
                                <el-row class="title">
                                    <h1 style="margin: 0px;">{{ bookInfo.bookTitle }}</h1>
                                </el-row>

                                <el-row class="bookInfoContent">
                                    <el-col class="author">
                                        <div>
                                            作者：<el-link target="_blank" :underline="false">{{ bookInfo.bookAuthor
                                                }}</el-link>
                                        </div>

                                        <div style="margin-top: 8px;">
                                            更新时间：{{ bookInfo.bookUpdateTime }}
                                        </div>
                                    </el-col>
                                    <el-col class="action">
                                        <div>
                                            操作：<el-link target="_blank" :underline="false">投票操作，</el-link>
                                            <el-link target="_blank" :underline="false">加入书架，</el-link>
                                            <el-link target="_blank" :underline="false">直达底部</el-link>
                                        </div>
                                        <div style="margin-top: 8px;overflow: hidden;white-space: nowrap;">
                                            最新章节：<el-link target="_blank" :underline="false">{{ bookInfo.bookNewChapter
                                                }}</el-link>
                                        </div>
                                    </el-col>
                                </el-row>
                            </el-row>
                            <el-divider></el-divider>
                            <el-row class="bookIntro">
                                <div>
                                    &nbsp;&nbsp;{{ bookInfo.bookSummary }}
                                </div>
                            </el-row>
                        </el-col>
                    </el-row>

                    <el-row style="width: 100%;height:14%;margin-top: 15px;">
                        <span class="recommend">推荐阅读: <el-link v-for="(book, index) in recommendBooks" :key="index"
                                target="_blank" :underline="false">{{ book }}<span
                                    v-if="index < recommendBooks.length - 1">、</span></el-link></span>
                    </el-row>
                </el-row>
            </el-row>

            <el-row class="book_chapters">
                <el-row class="chapters_header">
                    <span>《{{ bookInfo.bookTitle }}》 正文</span>
                </el-row>
                <el-row class="chapters_content">
                    <el-row v-for="(group, index) in groupedChapters" :key="index" class="oneLineChapters">
                        <el-col v-for="chapter in group" :key="chapter.id" class="oneChapters" :span="6">
                            <el-link target="_blank" :underline="false" @click="goToChapterDetail(chapter.id)">{{ chapter.chapter_title }}</el-link>
                        </el-col>
                        <el-divider></el-divider>
                    </el-row>
                </el-row>
            </el-row>
        </el-row>
    </el-container>
</template>

<script>
import {
    getBookInfo
}from "../api/api";
import { Loading } from 'element-ui';

export default {
    name: 'BookDetail',
    data() {
        return {
            bookInfo: {
                bookID: '',
                bookTitle: '',
                bookType: '',
                bookCover: '',
                bookAuthor: '',
                bookSummary: '',
                bookNewChapter: '',
                bookUpdateTime: '',
                bookChapters: {}
            },
            groupedChapters:[],
            recommendBooks:[
                '混沌剑神','牧神记','莽荒纪','逆天邪神','武炼巅峰','剑道独尊'
            ],
        }
    },
    created() {
        console.log('bookID: ',this.$route.params.id)
        this.fetchBook(this.$route.params.id);
    },
    methods: {
        fetchBook(bookID) {

            const loadingInstance = Loading.service({
                lock: true, // 锁定屏幕
                text: '处理中...'
            })
            const params = {'bookID':bookID}
            getBookInfo(params)
                .then(response =>{
                    if (response.data.code===0){
                        this.$message({ type: 'success', message: response.data.msg });
                        const cover_image = `../../static/bookCover/${response.data.data['bookCover']}`
                        this.bookInfo = response.data.data
                        this.bookInfo.bookCover = cover_image
                        this.bookInfo.bookNewChapter = this.bookInfo.bookChapters[this.bookInfo.bookChapters.length-1]['chapter_title']
                        console.log('bookInfo: ',this.bookInfo)

                        // 每4章节分一组
                        this.chapterGroups(this.bookInfo.bookChapters);
                    }else{
                        this.$message({ type: 'error', message: response.data.msg });
                    }
                })
                .catch(error => {
                    console.error('Error fetching book info:', error);
                })
            loadingInstance.close()
        },
        chapterGroups(bookChapters) {
            let groupedChapters = []
            // 数据结构设计为[[{'id':1,'title':''},{},{},{}],[{},{},{},{}]]
            let count = 0
            let oneGroupedChapters = []
            for (let i=0;i<bookChapters.length;i++){
                oneGroupedChapters.push(bookChapters[i])
                count += 1
                if (count===4){
                    groupedChapters.push(oneGroupedChapters)
                    count = 0
                    oneGroupedChapters = []
                    continue
                }
                if (i === bookChapters.length-1){
                    groupedChapters.push(oneGroupedChapters)
                }
            }
            this.groupedChapters = groupedChapters
        },
        goToChapterDetail(chapterID){
            this.$router.push(`/book/${this.bookInfo.bookID}/${chapterID}`)
            console.log('chapterID: ',chapterID)
        }
    }
}

</script>

<style lang="less" scoped>
.wrapper {
    width:100%;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    // height: 100vh; // 设置高度为视口的100% 
    overflow-y: auto;
    // background-color: red;
    display: flex;
    justify-content: center;
}

// *************书籍详细信息框************* //
// 以下定义书籍详细信息框的样式
.book_detail{
    height:400px;
    width:100%;
    // background-color: red;
    border: 3px solid;
    border-color: #DDDDDD;
}

// 以下定义信息框的头部的样式
.book_detail .book_detail_header{
    height:10%;
    width:100%;
    border-bottom: 3px solid;
    border-color: #DDDDDD;
    display: flex;
    align-items: center;
}

.book_detail_header .header_text{
    float:left;
    margin-left: 5px;
    font-size: 14px;
}

.header_text /deep/.el-link--inner {
    color: rgb(22, 139, 217);
    margin-bottom: 2px;
}

.header_text /deep/.el-link--inner:hover {
    color: #004cff;
}

// 书籍信息内容框样式
.book_detail_content{
    height: 86%;
    width:100%;
    padding-left: 30px;
    padding-right: 30px;
    padding-top: 20px;
}

.book_detail_content .recommend{
    float:left;
    font-size: 14px;
}

// 书籍封面区块样式
.book_detail_content .bookCover{
    height:100%;
    width:20%;
}

.bookCover .bookCoverContent{
    height:100%;
    width:100%;
    border: 12px solid;
    border-color: #DDDDDD;
    box-sizing: border-box; /* 边框和内边距包含在元素的宽度和高度内 */
    background-clip: padding-box; /* 背景被裁剪到内边距框 */
}

.bookCoverContent .bookCoverPic{
    width: 100%;
    height: 100%;
    // object-fit: cover; /* 使用 cover 来填充元素 */
}

// 书籍信息内容样式
.book_detail_content .bookContent{
    text-align: left;
    margin-left: 15px;
    padding-left: 15px;
    padding-right: 15px;
    height:100%;
    width:75%;
}

// 书籍简单信息
.bookContent .bookInfo{
    width:100%;
    height:40%;
    // background-color: red;
}

.bookInfo .title{
    width:100%;
    height:20%;
}

.bookInfo .bookInfoContent{
    width:100%;
    height:80%;
}

.author{
    width:50%;
    height: 100%;
    padding-top: 15px;
}

.action{
    width:50%;
    height: 100%;
    padding-top: 15px;
}

/deep/.el-divider--horizontal{
    margin: 0px;
    background: 0 0;
    border-top: 2px dashed #e8eaec;
}

// 书籍简介
.bookContent .bookIntro{
    width:100%;
    height:60%;
    padding-top: 15px;    
    font-size: 12px;
}


.bookInfoContent a {
        margin-bottom: 2px;
        font-size: 16px;
		font-weight: 600;
		color: rgba(0, 0, 0, 0.85);
	}

.book_detail_content /deep/.el-link--inner {
    color: rgb(22, 139, 217);
    margin-bottom: 2px;
}

.book_detail_content /deep/.el-link--inner:hover {
    color: #004cff;
}

// *************书籍章节框************* //
.book_chapters{
    min-height: 50px; // 设置最小高度，防止内容超出容器
    height: auto; // 内容自适应高度
    width:100%;
    margin-top: 25px;
    border: 3px solid;
    border-color: #DDDDDD;
}

.book_chapters .chapters_header{
    width: 100%;
    height: 50px;
    border-bottom: 3px solid;
    border-color: #DDDDDD;
    display: flex;
    justify-content: center;
    align-items: center;
    
}

.book_chapters .chapters_content{
    width:100%;
}
.chapters_content .oneLineChapters {
    height:40px;
}

.chapters_content .oneLineChapters .oneChapters {
    height: 25px;
    text-align: left;
    font-size: 8px;
    margin-top: 12px;
    padding-left: 15px;
    padding-right: 15px;
    overflow: hidden; //隐藏超出容器的内容 
    white-space: nowrap; // 防止文本换行 
    text-overflow: ellipsis; // 显示省略号
}

.oneChapters /deep/.el-link--inner{
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    font-size: 12px;
}
</style>