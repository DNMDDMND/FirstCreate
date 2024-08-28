<template>
    <el-container class="wrapper" element-loading-text="拼命加载中">
        <el-header class="book_header">
            <el-col class="titleContainer">
                <!-- 这里放置“标题和logo” -->
                <span class="bookICON"></span>
                <span class="loginTitle">书籍管理系统</span>
            </el-col>

            <el-col class="searchBook">
                <!-- 这里放置“书籍搜索框“ -->
                <el-input placeholder="搜索书籍" v-model="searchBookContent">

                </el-input>
                <el-button type="danger" icon="el-icon-search"></el-button>
            </el-col>

            <el-col class="MyBook">
                <!-- 这里放置“我的书架” -->
                <el-button icon="el-icon-notebook-2" style="float:right">我的书架</el-button>
                <el-button icon="el-icon-document-add" @click="addBook = true"
                    style="float:right;margin-right:15px;">添加书籍</el-button>
            </el-col>
        </el-header>

        <el-main class="mainContent">
            <el-row class="navigation">
                <!-- 这里放置导航栏 -->
                <el-menu class="el-menu-style" router unique-opened mode="horizontal" background-color="#3E3D43"
                    text-color="#ffffff" active-text-color="#FFFFFF">
                    <el-menu-item class="el-menu-item-category-style">
                        <i class="el-icon-menu"></i>
                        <span slot="title">作品分类</span>
                    </el-menu-item>
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
                            <el-menu-item :index="item.index" :key="item.index" class="el-menu-item-style" @click.native="item.func">
                                <i :class="item.icon"></i>
                                <span slot="title">{{ item.title }}</span>
                            </el-menu-item>
                        </template>
                    </template>
                </el-menu>
            </el-row>

            <el-row class="bookContent">
                <!-- 这里放置页面主要内容 -->
                <el-col class="bookCategory">
                    <!-- 这里放置作品分类 -->
                    <el-row class="darkCategory">
                        <el-col class="left-icon">
                            <span class="el-icon-xuanhuan"></span>
                            <div>
                                <el-link target="_blank" :underline="false">玄幻</el-link><br>
                                <p class="categoryCount">{{bookCategoryItems['Xuanhuan']}}</p>
                            </div>
                        </el-col>
                        <el-col class="right-icon">
                            <span class="el-icon-qihuan"></span>
                            <div>
                                <el-link target="_blank" :underline="false">奇幻</el-link><br>
                                <p class="categoryCount">{{bookCategoryItems['Qihuan']}}</p>
                            </div>
                        </el-col>
                    </el-row>

                    <el-row class="lightCategory">
                        <el-col class="left-icon">
                            <span class="el-icon-wuxia"></span>
                            <div>
                                <el-link target="_blank" :underline="false">武侠</el-link><br>
                                <p class="categoryCount">{{bookCategoryItems['Wuxia']}}</p>
                            </div>
                        </el-col>
                        <el-col class="right-icon">
                            <span class="el-icon-xianxia"></span>
                            <div>
                                <el-link target="_blank" :underline="false">仙侠</el-link><br>
                                <p class="categoryCount">{{bookCategoryItems['Xianxia']}}</p>
                            </div>
                        </el-col>
                    </el-row>

                    <el-row class="darkCategory">
                        <el-col class="left-icon">
                            <span class="el-icon-dushi"></span>
                            <div>
                                <el-link target="_blank" :underline="false">都市</el-link><br>
                                <p class="categoryCount">{{bookCategoryItems['Dushi']}}</p>
                            </div>
                        </el-col>
                        <el-col class="right-icon">
                            <span class="el-icon-xianshi"></span>
                            <div>
                                <el-link target="_blank" :underline="false">现实</el-link><br>
                                <p class="categoryCount">{{ bookCategoryItems['Xianshi']}}</p>
                            </div>
                        </el-col>
                    </el-row>

                    <el-row class="lightCategory">
                        <el-col class="left-icon">
                            <span class="el-icon-junshi"></span>
                            <div>
                                <el-link target="_blank" :underline="false">军事</el-link><br>
                                <p class="categoryCount">{{ bookCategoryItems['Junshi']}}</p>
                            </div>
                        </el-col>
                        <el-col class="right-icon">
                            <span class="el-icon-lishi"></span>
                            <div>
                                <el-link target="_blank" :underline="false">历史</el-link><br>
                                <p class="categoryCount">{{ bookCategoryItems['Lishi']  }}</p>
                            </div>
                        </el-col>
                    </el-row>

                    <el-row class="darkCategory">
                        <el-col class="left-icon">
                            <span class="el-icon-youxi"></span>
                            <div>
                                <el-link target="_blank" :underline="false">游戏</el-link><br>
                                <p class="categoryCount">{{ bookCategoryItems['Youxi']  }}</p>
                            </div>
                        </el-col>
                        <el-col class="right-icon">
                            <span class="el-icon-tiyu"></span>
                            <div>
                                <el-link target="_blank" :underline="false">体育</el-link><br>
                                <p class="categoryCount">{{ bookCategoryItems['Tiyu']  }}</p>
                            </div>
                        </el-col>
                    </el-row>

                    <el-row class="lightCategory">
                        <el-col class="left-icon">
                            <span class="el-icon-kehuan"></span>
                            <div>
                                <el-link target="_blank" :underline="false">科幻</el-link><br>
                                <p class="categoryCount">{{ bookCategoryItems['Kehuan']  }}</p>
                            </div>
                        </el-col>
                        <el-col class="right-icon">
                            <span class="el-icon-wuxian"></span>
                            <div>
                                <el-link target="_blank" :underline="false">诸天无限</el-link><br>
                                <p class="categoryCount">{{ bookCategoryItems['Wuxian']  }}</p>
                            </div>
                        </el-col>
                    </el-row>

                    <el-row class="darkCategory">
                        <el-col class="left-icon">
                            <span class="el-icon-xuanyi"></span>
                            <div>
                                <el-link target="_blank" :underline="false">悬疑灵异</el-link><br>
                                <p class="categoryCount">{{ bookCategoryItems['Xuanyi']  }}</p>
                            </div>
                        </el-col>
                        <el-col class="right-icon">
                            <span class="el-icon-qing"></span>
                            <div>
                                <el-link target="_blank" :underline="false">轻小说</el-link><br>
                                <p class="categoryCount">{{ bookCategoryItems['Qing']  }}</p>
                            </div>
                        </el-col>
                    </el-row>
                </el-col>
            </el-row>
        </el-main>

        <!-- 添加书籍窗口 -->
        <el-dialog title="添加书籍" :visible.sync="addBook" class="uartDialog">
            <el-col class="uploadContent">
                <el-form :model="addBookList" @submit.native.prevent>
                    <el-form-item label="">
                        <!-- 之后还得新增一些判断 1.是否信息填写完成 2.重复名图片怎么处理(我打算获取图片的UID) 3.重复小说禁止上传 -->
                        <el-upload 
                            class="avatar-uploader" 
                            ref="upload"
                            action="http://127.0.0.1:8000/bookList/avatarupload/"
                            drag 
                            :show-file-list="false"
                            :multiple="false"
                            :limit="1"
                            :before-upload="beforeAvatarUpload"
                            :on-success="handleAvatarSuccess">
                            <i class="el-icon-picture" style="transform: scale(3);margin-top: 25px;"></i>
                            <div class="el-upload__text" style="margin-bottom: 20px;">将封面图片拖到此处<br>或者<em>点击选取图片</em>
                            </div>
                            <img v-if="imageUrl" :src="imageUrl" class="avatar">
                            <!-- <i v-else class="el-icon-plus avatar-uploader-icon"></i> -->
                        </el-upload>
                    </el-form-item>

                    <el-form-item label="">
                        <el-upload 
                            action="http://127.0.0.1:8000/bookList/contentupload/"
                            ref="txtUpload" 
                            class="txt-uploader" 
                            drag 
                            :auto-upload='true' 
                            :multiple='false'
                            :before-upload="beforeTXTUpload"
                            :on-success="handleContentSuccess"
                            accept=".txt" 
                            type="file">
                            <i class="el-icon-upload"></i>
                            <div class="el-upload__text">将txt文件拖到此处<br>或者<em>点击选取txt文件</em></div>
                        </el-upload>
                    </el-form-item>
                </el-form>
            </el-col>

            <el-col class="inputContent">
                <el-row class="inputForm">
                    <el-form :model="addBookList" @submit.native.prevent>
                        <el-form-item label="书籍标题">
                            <el-input v-model="addBookList.title"></el-input>
                        </el-form-item>
                        <el-form-item label="书籍作者">
                            <el-input v-model="addBookList.author"></el-input>
                        </el-form-item>
                        <el-form-item label="书籍类型">
                            <el-select v-model="addBookList.type" placeholder="请选择书籍类型">
                                <el-option 
                                    v-for="(type, index) in bookType" 
                                    :key="index" 
                                    :label="type[1]"
                                    :value="type[0]">
                                </el-option>
                            </el-select>
                        </el-form-item>
                        <el-form-item label="简介" class="description">
                            <el-input v-model="addBookList.description" type="textarea" resize="none"></el-input>
                        </el-form-item>
                    </el-form>
                </el-row>

                <el-row class="inputButton">
                    <el-button @click="addBook = false">取 消</el-button>
                    <el-button type="primary" @click="submitBookList" style="margin-right: 20px;">确 认</el-button>
                </el-row>

            </el-col>
        </el-dialog>
    </el-container>
</template>

<script>
import {
    getBookList,
    getBookType,
    getBookCategory
} from "../api/api";

export default {
    name: 'Home',
    data() {
        let self = this
        return {
            searchBookContent: '',
            navigationItems: [
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
                    subs: [{
                        title: '个人中心',
                    }, {
                        title: '退出登录',
                        func: self.signout
                    }]
                }
                // {   当前仅供参考
                //     icon: 'el-icon-my-note',
                //     index: '/notes',
                //     title: 'Link Bird',
                // }
            ],
            isSuperUser: false,
            addBook: false,
            addBookList: {
                title: '',
                author: '',
                type:'',
                description:'',
                cover_image_url:'', //封面路径
                content_url:'' // 小说内容路径
            },
            imageUrl: '', // 存储上传后的图片URL
            bookType: [],
            bookCategoryItems: [],
        }
    },
    components: {},
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
        changeBooks() {
            // 在这里添加您的代码来处理书籍更换逻辑
            console.log('书籍更换逻辑');
        },
        handleSummaryChange(file, fileList) {
            // 当多余一个的时候替换文件
            if (fileList.length > 1) {
                fileList.splice(0, 1);
            }
        },
        chooseCoverImage(file){
            console.log(file)
        },
        handleAvatarSuccess(res, file) {
            // 上传文件成功时，调用该函数
            if (res.code == 0) {
                this.$message.success(res.msg);
                this.imageUrl = "http://127.0.0.1:8000/media/bookCover/" + res.file; 
                this.addBookList.cover_image_url = this.imageUrl
            } else {
                this.$message.error(res.msg);
            }
            this.$refs.upload.clearFiles()
        },
        changeAvatarUpload(file){
            // 文件改变时，调用该函数
            console.log('文件改变时，调用该函数')
            console.log('file',file)
        },
        beforeAvatarUpload(file) {
            // 在上传文件前对文件类型和大小进行检查
            const isJPG = (file.type === 'image/jpeg' || file.type === 'image/png');
            const isLt2M = file.size / 1024 / 1024 < 2;

            if (!isJPG) {
                this.$message.error('上传头像图片只能是 JPG和PNG 格式!');
            }
            if (!isLt2M) {
                this.$message.error('上传头像图片大小不能超过 2MB!');
            }
            return isJPG && isLt2M;
        },

        //以下定义小说内容上传
        beforeTXTUpload(file) {
            // 检查是否为.txt文件
            const isTXT = file.type === 'text/plain';

            if (!isTXT) {
                this.$message.error('上传的文件必须是 .txt 格式!');
            }

            return isTXT;
        },
        handleContentSuccess(res, file) {
            // 上传文件成功时，调用该函数
            if (res.code == 0) {
                this.$message.success(res.msg);
                this.addBookList.content_url = res.filePath;
            } else {
                this.$message.error(res.msg);
            }
            this.$refs.upload.clearFiles()
        },

        submitBookList() {
            // 首先判断是否所有内容已填写

            // 之后将字段上传至后端
            getBookList({'bookList':JSON.stringify(this.addBookList)})
                .then(response => {
                    if (response.data.code===0){
                        this.$message({ type: 'success', message: `书籍提交成功` });
                    }else {
                        this.$message({ type: 'error', message: `${response.data.msg}` });
                    }
                })
                .catch(error => {
                    this.$message({ type: 'error', message: `书籍提交失败，原因为${error}` })
                });
            this.addBook = false
        },
        // 获取书籍类型
        fetchBookType() {
            getBookType()
                .then(response => {
                    this.bookType = response.data.bookType;
                    console.log('this.bookType: ',this.bookType)
                })
                .catch(error => {
                    console.error('Error fetching book type:', error);
                });
        },

        // 获取书籍类型数量
        fetchBookCategory() {
            getBookCategory()
            .then(response => {
                if (response.data.code === 0){
                    this.bookCategoryItems = response.data.data
                    localStorage.setItem('bookCategoryItems', JSON.stringify(this.bookCategoryItems));
                }
            })
            .catch(error => {
                console.log('Error fetching book category: ',error)
            });
        }
    },
    computed: {
    },
    created() {
        this.fetchBookType(); // 组件创建时自动获取数据
        this.fetchBookCategory();
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

.book_header {
    display: flex;
}

// 以下定义标题的样式
.book_header .titleContainer {
    display: flex;
    margin-top: 15px;
}

.book_header .titleContainer .bookICON {
    width: 50px;
    /* 图标宽度 */
    height: 50px;
    /* 图标高度 */
    background: url('~@/assets/book.jpeg') no-repeat center center;
    /* 图标背景，使用在线链接或相对路径 */
    background-size: contain;
    /* 保持图标比例 */
    display: inline-block;
    /* 使图标可以与其他内容在同一行显示 */
    margin-right: 10px;
    /* 添加一些间距 */
}

.book_header .titleContainer .loginTitle {
    font-size: 24px;
    /* 标题字体大小 */
    font-weight: bold;
    /* 标题字体加粗 */
    font-family: 'Kaiti', sans-serif;
    /* 设置字体族为楷体 */
    margin-top: 10px;
}

// 以下定义搜索框的样式
.book_header .searchBook {
    display: flex;
    margin-top: 18px;
}

.book_header .MyBook {
    margin-top: 18px;
}

// 以下定义主页主要内容的样式
.mainContent {
    width: 100%;
    padding: 0;
    padding-top: 20px;
}

// 以下定义导航栏的样式
.mainContent .navigation {
    width: 100%;
    height: 12%;
}


// 以下定义el-menu的基本样式
.el-menu-style {
    display: flex;
    justify-content: center;
    font-size: 15px;
    font-weight: bold;
}

.el-menu-item-style {
    width:10%;
    font-size: 18px;
    font-weight: bold;
    font-family: Georgia;
    display: flex;
    align-items: center;
}

.el-menu-item-category-style {
    width: 20%;
    background-color: #313035 !important;
    position: absolute;
    left: 0;
    font-size: 18px;
    font-weight: bold;
    font-family: "PingFang SC";
}

.el-menu-item-sub-style {
    position: absolute;
    right: 0;
    width:15%;
    font-size: 18px;
    font-weight: bold;
    font-family: Georgia;
}

//以下定义页面主要内容的样式

//以下定义书籍分类的样式
.bookContent {
    width: 100%;
    height: 88%;
}

.bookCategory {
    width: 20%;
    height: 100%;
}

.bookCategory .darkCategory {
    // 深色主题
    background-color: #FAF6F5 !important;
    display: flex;
    width: 100%;
    height: 14%;
}

.bookCategory .lightCategory {
    // 浅色主题
    background-color: #FDFDFB !important;
    width: 100%;
    display: flex;
    height: 14%;
}

// 书籍类型数量样式
.categoryCount{
    font-size: 8px;
    float: left;
    margin-left: 5px;
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

// 以下定义各个图标来源及其样式
.el-icon-xuanhuan {
    width: 30px;
    /* 图标宽度 */
    height: 40px;
    /* 图标高度 */
    background: url(~@/assets/Category/xuanhuan.png) no-repeat center center;
    /* 图标背景，使用在线链接或相对路径 */
    background-size: contain;
    /* 保持图标比例 */
    display: inline-block;
    /* 使图标可以与其他内容在同一行显示 */
    // margin-right: 8px;
    margin-left: 25px;
    
}

.el-icon-qihuan {
    width: 35px;
    height: 50px;
    background: url(~@/assets/Category/qihuan.png) no-repeat center center;
    background-size: contain;
    display: inline-block;
    // margin-right: 8px;
    margin-left: 25px;

}

.el-icon-wuxia {
    width: 35px;
    height: 50px;
    background: url(~@/assets/Category/wuxia.png) no-repeat center center;
    background-size: contain;
    display: inline-block;
    // margin-right: 8px;
    margin-left: 25px;

}

.el-icon-xianxia {
    width: 35px;
    height: 50px;
    background: url(~@/assets/Category/xianxia.png) no-repeat center center;
    background-size: contain;
    display: inline-block;
    // margin-right: 8px;
    margin-left: 25px;

}

.el-icon-dushi {
    width: 35px;
    height: 50px;
    background: url(~@/assets/Category/dushi.png) no-repeat center center;
    background-size: contain;
    display: inline-block;
    // margin-right: 8px;
    margin-left: 25px;

}

.el-icon-xianshi {
    width: 35px;
    height: 50px;
    background: url(~@/assets/Category/xianshi.png) no-repeat center center;
    background-size: contain;
    display: inline-block;
    // margin-right: 8px;
    margin-left: 25px;

}

.el-icon-junshi {
    width: 35px;
    height: 50px;
    background: url(~@/assets/Category/junshi.png) no-repeat center center;
    background-size: contain;
    display: inline-block;
    // margin-right: 8px;
    margin-left: 25px;

}

.el-icon-lishi {
    width: 35px;
    height: 50px;
    background: url(~@/assets/Category/lishi.png) no-repeat center center;
    background-size: contain;
    display: inline-block;
    // margin-right: 8px;
    margin-left: 25px;

}

.el-icon-youxi {
    width: 35px;
    height: 50px;
    background: url(~@/assets/Category/youxi.png) no-repeat center center;
    background-size: contain;
    display: inline-block;
    // margin-right: 8px;
    margin-left: 25px;

}

.el-icon-tiyu {
    width: 35px;
    height: 50px;
    background: url(~@/assets/Category/tiyu.png) no-repeat center center;
    background-size: contain;
    display: inline-block;
    // margin-right: 8px;
    margin-left: 25px;

}

.el-icon-kehuan {
    width: 35px;
    height: 50px;
    background: url(~@/assets/Category/kehuan.png) no-repeat center center;
    background-size: contain;
    display: inline-block;
    // margin-right: 8px;
    margin-left: 25px;

}

.el-icon-wuxian {
    width: 35px;
    height: 50px;
    background: url(~@/assets/Category/wuxian.png) no-repeat center center;
    background-size: contain;
    display: inline-block;
    // margin-right: 8px;
    margin-left: 25px;

}

.el-icon-xuanyi {
    width: 35px;
    height: 50px;
    background: url(~@/assets/Category/xuanyi.png) no-repeat center center;
    background-size: contain;
    display: inline-block;
    // margin-right: 8px;
    margin-left: 25px;

}

.el-icon-qing {
    width: 35px;
    height: 50px;
    background: url(~@/assets/Category/qing.png) no-repeat center center;
    background-size: contain;
    display: inline-block;
    // margin-right: 8px;
    margin-left: 25px;

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

// 以下定义作品推荐标题的样式
.bookRecommend .recommendTitle{
    height: 8%;
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

//以下给添加书籍弹窗设置样式
.uartDialog {
    margin-top: -11.5vh;
    display:flex;
    /deep/ .el-dialog {
        width: 60% !important;
        height: 80%;
    }
}

.uartDialog /deep/ .el-dialog__body{
    width:100%;
    height: 100%;
    padding: 0;
    display:flex;
}

//以下定义inputContent的样式
.inputContent{
    width: 65%;
    height: 90%;
    // background-color: #ffffff;
}

.inputContent .inputForm{
    width: 100%;
    height: 85%;
}

.inputForm /deep/ .el-form-item__label{
    width:68px;
}

// 以下定义input框
.inputForm /deep/ .el-input{
    width:300px;
    margin-right: 100px;
}

.inputForm /deep/ .el-input__inner{
    width:300px;
}

.description {
    height:100px;
    /deep/ .el-textarea{
        width:300px;
        height:100px;
        margin-right: 100px;
    }
    /deep/ .el-textarea__inner{
        height:150px;
        }
}

// 以下定义select框
.inputForm /deep/ .el-select{
    width:200px;
    margin-right: 200px;
}

.inputForm /deep/ .el-input--suffix{
    width:200px;
    margin-right: 0;
}

.inputForm /deep/ .el-input--suffix .el-input__inner {
    width:200px;
    margin-right: 0;
}


.inputContent .inputButton{
    width: 100%;
    height: 15%;
    display: flex;
    justify-content: flex-end;
    align-items: center;
}

//以下定义uploadContent的样式
.uploadContent{
    width: 35%;
    height: 90%;
    // background-color: #ffffff;

}

// 以下定义uoloadContent的文字区块样式
.el-upload__text {
    line-height: 1.3;/* 行间距 */
    font-size: 12px;/* 文字大小 */
}
//以下定义书籍弹窗中的封面上传
.avatar-uploader /deep/.el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    overflow: hidden;
    position: relative; /* 设置为相对定位 */
}

.avatar-uploader /deep/.el-upload-dragger{
    width: 120px;
    height: 150px;
    display:flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap; /* 允许子项换行 */
}

.avatar-uploader /deep/.el-upload:hover {
    border-color: #409EFF;
}

.avatar {
    width: 120px;
    height: 150px;
    display: block;
    position: absolute; /* 设置为绝对定位 */
    top: 0;
    left: 0;
    z-index: 2; /* 设置一个较大的z-index值 */
}

// .avatar-uploader-icon {
//     font-size: 28px;
//     color: #8c939d;
//     width: 178px;
//     height: 178px;
//     line-height: 178px;
//     text-align: center;
// }

//以下定义书籍内容的上传
.txt-uploader /deep/.el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    overflow: hidden;
}

.txt-uploader /deep/.el-upload-dragger{
    width: 178px;
    height: 178px;
}

.txt-uploader /deep/.el-upload:hover {
    border-color: #409EFF;
}

//以下定义inputContent的样式


</style>
