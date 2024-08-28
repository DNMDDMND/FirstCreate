<template>
    <el-container class="wrapper" element-loading-text="拼命加载中">
        <el-backtop :bottom="60" :width="500">
            <div class="backToTop">
                返回顶部
            </div>
        </el-backtop>

        <el-row style="width:100%">
            <el-row class="breadCrumbs">
                <span class="header_text">
                    <el-link target="_blank" :underline="false">书籍管理系统</el-link> > {{ chapterInfo.bookType }}小说 > {{chapterInfo.bookTitle }} > {{ chapterInfo.chapterTitle }}
                </span>
            </el-row>

            <el-row class="mainContent">
                <el-row class="funcContent">
                    <div class="normalStyle">
                        阅读背景:&nbsp;<el-button v-for="(rb,index) in readBackground" :key="index" :style="rb" @click="changeReadBG(rb)"/>
                    </div>
                    <div class="normalStyle">
                        字体颜色:&nbsp;<el-button v-for="(fc,index) in fontColor" :key="index" :style="fc" @click="changeFontCol(fc)"/>
                    </div>
                    <div class="normalStyle">
                        字体大小: [<el-link v-for="(fs,index) in fontSize" :key="index" target="_blank" :underline="false" @click="changeFontSZ(fs.size)">{{ fs.name }}{{ index < fontSize.length - 1 ? '&nbsp;&nbsp;' : '' }}</el-link>]
                    </div>
                </el-row>
                <el-row class="textContent" :style="currReadBG">
                    <el-row class="title">
                        <h1>{{ chapterInfo.bookTitle }}&nbsp;{{ chapterInfo.chapterTitle }}</h1>
                    </el-row>

                    <el-row class="changeChapter">
                        <el-link target="_blank" :underline="false" @click="backToPreChap">上一章</el-link>&nbsp;&nbsp;&nbsp;&nbsp;<el-link
                            target="_blank" :underline="false" @click="backToChapList">章节列表</el-link>&nbsp;&nbsp;&nbsp;&nbsp;<el-link
                            target="_blank" :underline="false" @click="goToNextChap">下一章</el-link>
                    </el-row>

                    <el-row class="text" :style="currTextStyle">
                        <!-- <p v-html=chapterInfo.chapterContent></p> -->
                    </el-row>
                </el-row>
                <el-row class="bottomButton">
                    <el-link target="_blank" :underline="false">加入书签</el-link>&nbsp;&nbsp;&nbsp;&nbsp;
                    <el-link target="_blank" :underline="false" @click="backToPreChap">上一章</el-link>&nbsp;&nbsp;&nbsp;&nbsp;
                    <el-link target="_blank" :underline="false" @click="backToChapList">章节列表</el-link>&nbsp;&nbsp;&nbsp;&nbsp;
                    <el-link target="_blank" :underline="false" @click="goToNextChap">下一章</el-link>&nbsp;&nbsp;&nbsp;&nbsp;
                    <el-link target="_blank" :underline="false">投推荐票</el-link>
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
    name:'ChapterDetail',
    data() {
        return{
            chapterInfo: {
                'bookTitle':'',
                'bookType':'',
                'bookAuthor':'',
                'chapterTitle':'',
                'chapterContent':''
            },
            currReadBG:{},
            readBackground: [
            {"background-color":"#e9faff"},
            {"background-color":"#ffffed"},
            {"background-color":"#efefef"},
            {"background-color":"#fcefff"},
            {"background-color":"#ffffff"},
            {"background-color":"#eefaee"}],
            currFontCol:{},
            fontColor: [
            {"background-color":"#000000"},
            {"background-color":"#333333"},
            {"background-color":"#1b8001"},
            {"background-color":"#fcc0cb"},
            {"background-color":"#fa394f"},
            {"background-color":"#0000ff"}],
            currFontSZ:{},
            fontSize:[
                {'name':'很小','size':12},
                {'name':'较小','size':14},
                {'name':'中等','size':16},
                {'name':'较大','size':18},
                {'name':'很大','size':20}],
            currTextStyle:{}
        }
    },
    //         this.$message({ type: 'info', message:  this.$route.params.id + this.$route.params.chapterID});

    created() {
        console.log(this.$route.params.id,this.$route.params.chapterID)
        this.fetchChapter(this.$route.params.id,this.$route.params.chapterID)
        
        let that = this
        // 按下键盘，即刻了解键盘对应的KeyCode
        document.addEventListener("keydown", function (e) {
            that.$message({ type: 'info', message:  `您按下的按钮的KeyCode为${e.keyCode}`});
        })
        // 绑定左右键，跳转至下一章节/上一章节
        document.addEventListener("keydown", function (e) {
            if (e.keyCode===39) {
                that.goToNextChap()
            }else if (e.keyCode==37) {
                that.backToPreChap()
            }
        })
    },
    methods: {
        fetchChapter(bookID,chapterID){
            const params = {'bookID':bookID,'chapterID':chapterID}

            getChapter(params)
                .then(response => {
                    if (response.data.code===0){
                        this.$message({ type: 'success', message: response.data.msg });
                        this.chapterInfo = response.data.data
                        this.chapterInfo.chapterContent = this.handTextFormat(this.chapterInfo.chapterContent)
                        console.log('chapterInfo: ',this.chapterInfo)
                    }else {
                        this.$message({ type: 'error', message: response.data.msg });
                    }
                })
                .catch(error => {
                    console.error('Error fetching chapter content:', error);
                })
            
        },
        // 处理文本格式，包括解析换行符、首行空格
        handTextFormat(textContent){
            textContent = '&nbsp;&nbsp;&nbsp;' + textContent
            textContent = textContent.replace(/\n/g, '<br>&nbsp;&nbsp;');
            return textContent
        },
        // 更改正文背景颜色
        changeReadBG(rb){
            this.currReadBG = rb
        },
        // 更改正文字体颜色
        changeFontCol(fc){
            this.currFontCol = fc
        },
        // 更改正文字体大小
        changeFontSZ(size){
            this.currFontSZ = {"font-size":`${size}px`}
        },
        // 整合字体颜色和字体大小
        updateTextStyle(){
            this.currTextStyle = {
                'color':this.currFontCol['background-color'],
                'font-size':this.currFontSZ['font-size']
            }
        },
        // 返回章节列表
        backToChapList(){
            this.$router.push(`/book/${this.$route.params.id}`)
        },
        // 跳转至下一章
        goToNextChap(){
            const params = {'bookID':this.$route.params.id,'chapterID':Number(this.$route.params.chapterID)+1}
            getChapter(params)
                .then(response => {
                    if (response.data.code===0){
                        this.$router.push(`/book/${params.bookID}/${params.chapterID}`)
                        next();
                    }else if(response.data.code===2) {
                        this.$message({ type: 'error', message: '无法跳转至下一章，已经是最后一章了' });
                    }
                    else {
                        this.$message({ type: 'error', message: response.data.msg });
                    }
                })
                .catch(error => {
                    console.error('跳转下一章失败，原因为:', error);
                })
        },
        // 跳转至上一章
        backToPreChap(){
            const params = {'bookID':this.$route.params.id,'chapterID':Number(this.$route.params.chapterID)-1}
            getChapter(params)
                .then(response => {
                    if (response.data.code===0){
                        this.$router.push(`/book/${params.bookID}/${params.chapterID}`)
                    }else if(response.data.code===2) {
                        this.$message({ type: 'error', message: '无法返回上一章，已经是第一章了' });
                    }
                    else {
                        this.$message({ type: 'error', message: response.data.msg });
                    }
                })
                .catch(error => {
                    console.error('返回上一章失败，原因为:', error);
                })
        }
    },
    watch:{
        currFontCol: {
            handler(newValue) {
                this.updateTextStyle();
            },
            deep: true
        },
        currFontSZ: {
            handler(newValue) {
                this.updateTextStyle();
            },
            deep: true
        },
        $route(to,from) {this.$router.go(0)}
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

// *************章节内容************* //
// 导航路径
.breadCrumbs{
    height:30px;
    width:100%;
    display: flex;
    align-items: center;
}

.breadCrumbs .header_text{
    float:left;
    margin-left: 5px;
    font-size: 14px;
}

// 主要内容框(分为功能框、正文框、底部按钮框)
.mainContent{
    width:100%;
    min-height: 80px;
    height: auto;
    border: 3px solid;
    border-color: #DDDDDD;
}

// 功能框
.mainContent .funcContent{
    width:100%;
    height:40px;
    display:flex;
    justify-content: center;
    align-items: center;
    
    border-bottom: 3px solid;
    border-color: #DDDDDD;
}

.funcContent /deep/.el-button--default{
    width: 0;
    height: 0;
    padding: 9px;
    border: 1px solid;
    border-color: #DDDDDD;
}

.funcContent .normalStyle{
    display: flex;
    justify-content: center;
    align-items: center;
    margin-left: 20px;
}

// 正文框
.mainContent .textContent{
    width:100%;
    border-bottom: 3px solid;
    border-color: #DDDDDD;
    text-align: center;
    padding-left: 50px;
    padding-right: 50px;
}

.textContent .title{
    width:100%;
    height:60px;
}

.textContent .changeChapter{
    width:100%;
    height:20px;
}

.textContent .text{
    width:100%;
    text-align: left;
    line-height: 2; /* 行高，可以根据需要调整 */
}
// 底部按钮框
.mainContent .bottomButton{
    width:100%;
    height:40px;
    display: flex;
    justify-content: center;
    align-items: center;
}


/deep/.el-link--inner {
    color: rgb(22, 139, 217);
    margin-bottom: 2px;
}

/deep/.el-link--inner:hover {
    color: #004cff;
}

</style>