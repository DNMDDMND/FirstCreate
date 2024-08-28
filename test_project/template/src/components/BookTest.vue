<template>
    <div>
        <el-row>
            <el-col :span="24">
                <h1>书籍管理</h1>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="12">
                <el-input v-model="newBookName" placeholder="请输入书籍名称"></el-input>
            </el-col>
            <el-col :span="12">
                <el-button type="primary" @click="addBook">添加书籍</el-button>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="24">
                <el-table :data="books" style="width: 100%">
                    <el-table-column prop="book_name" label="书名"></el-table-column>
                    <el-table-column prop="add_time" label="添加时间"></el-table-column>
                    <!-- 这里可以根据需要添加更多的列 -->
                </el-table>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import axios from 'axios'
axios.defaults.timeout = 60000 // 请求超时
axios.defaults.baseURL = '/api'
axios.defaults.withCredentials = true      // axios请求携带cookie
export default {
    name: 'BookTest',
    data() {
        return {
            newBookName: '',
            books: []
        };
    },
    methods: {
        addBook() {
            if (this.newBookName.trim() === '') {
                this.$message.error('书籍名称不能为空');
                return;
            }
            axios.get('/add_book/', { params: { book_name: this.newBookName } })
                .then(response => {
                    if (response.data.error_num === 0) {
                        this.$message.success('书籍添加成功');
                        this.newBookName = '';
                        this.getBooks();
                    } else {
                        this.$message.error('书籍添加失败: ' + response.data.msg);
                    }
                })
                .catch(error => {
                    this.$message.error('请求失败: ' + error);
                });
        },
        getBooks() {
            axios.get('/show_books/')
                .then(response => {
                    if (response.data.error_num === 0) {
                        // 更新books数据属性，以便在模板中显示书籍列表
                        // 格式化添加时间
                        response.data.list = response.data.list.map(book => {
                            const addTime = new Date(book.fields.add_time);
                            book.fields.add_time = addTime.toLocaleString();
                            return book.fields;
                        });
                        this.books = response.data.list;
                    } else {
                        this.$message.error('获取书籍信息失败: ' + response.data.msg);
                    }
                })
                .catch(error => {
                    this.$message.error('请求失败: ' + error);
                });
        }
    },
    mounted() {
        this.getBooks();
    }
};
</script>

<style scoped>
/* 这里可以添加一些CSS样式 */
</style>