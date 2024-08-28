<template>
  <div class="wrapper">
    <div class="content">
      <!-- 展示登陆标题和图片 -->
      <div class="loginShow">
        <div class="titleContainer">
          <span class="bookICON"></span>
          <span class="loginTitle">书籍管理系统</span>
        </div>
        <div class="BookPic">
          <img src="~@/assets/Books.png" alt="Logo" />
        </div>
      </div>
      <!-- 登陆账号/密码的实现 -->
      <div class="loginContent">
        <h1>用户登陆</h1>
        <el-form :model="loginfo" status-icon :rules="loginRules" @submit.native.prevent class="form">
          <el-row>
            <el-form-item prop="username">
              <el-input placeholder="请输入账号" v-model="loginfo.username" prefix-icon="el-icon-user" clearable
                class="input">
              </el-input>
            </el-form-item>
            <el-form-item prop="password">
              <el-input placeholder="请输入密码" v-model="loginfo.password" prefix-icon="el-icon-view" clearable
                show-password @keyup.enter.native="login()" class="input">
              </el-input>
            </el-form-item>
          </el-row>
          <el-row class="login-button">
            <el-col>
              <el-form-item class="item1">
                <el-button type="primary" @click="login" native-type="submit" class="btn">登&nbsp;&nbsp;录</el-button>
              </el-form-item>
            </el-col>
          </el-row>
        </el-form>
        <p class="tips">
          没有账号？
          <span class="signup-link" @click="isSignupShow = true">注册</span>
        </p>
      </div>
    </div>

    <!-- 注册窗口 -->
    <el-dialog :title="'用户注册'" :visible.sync="isSignupShow" customClass="dialogWidth">
      <el-form :model="signupinfo" status-icon :rules="signRules" @submit.native.prevent class="form">
        <el-row>
          <el-form-item prop="username">
            <el-input placeholder="请输入账号" v-model="signupinfo.username" prefix-icon="el-icon-user" clearable
              class="input">
            </el-input>
          </el-form-item>

          <el-form-item prop="password">
            <el-input placeholder="请输入密码" v-model="signupinfo.password" prefix-icon="el-icon-view" clearable
              show-password class="input">
            </el-input>
          </el-form-item>

          <el-form-item prop="confirmPassword">
            <el-input placeholder="请再次输入密码" v-model="signupinfo.confirmPassword" prefix-icon="el-icon-view" clearable
              show-password class="input">
            </el-input>
          </el-form-item>

          <el-form-item prop="email">
            <el-input placeholder="请输入邮箱账号" v-model="signupinfo.email" prefix-icon="el-icon-message" clearable
              class="input">
            </el-input>
          </el-form-item>

          <el-form-item prop="gender">
            <el-select placeholder="请选择性别" v-model="signupinfo.gender" clearable class="input">
              <template slot="prefix">
                <span style="padding-left: 5px;">
                  <i class="el-icon-male"></i>
                </span>
              </template>
              <el-option label="男" value="male"/>
              <el-option label="女" value="female"/>
            </el-select>
          </el-form-item>
        </el-row>
        <el-row class="sign-button">
          <el-col>
            <el-form-item class="item1">
              <el-button type="primary" @click="signup" native-type="submit" class="btn">注&nbsp;&nbsp;册</el-button>
              <el-button @click="isSignupShow = false; signupinfo = []" native-type="submit"
                class="btn">取&nbsp;&nbsp;消</el-button>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
    </el-dialog>
  </div>

</template>


<script>
import {
  loginToBookView,
  signupToBookView
} from "../api/api";
export default {
  name: 'login',
  data() {
    return {
      loginfo: {            //登陆账号&密码
        username: '',
        password: ''
      },
      signupinfo: {         //注册账号&密码
        username: '',
        password: '',
        confirmPassword: '',
        email:'',
        gender:''
      },
      loginRules: {          //登陆表单验证
        username: [
          { required: true, message: '用户名不能为空', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '密码不能为空', trigger: 'change' }
        ],
      },
      signRules: {           //注册表单验证
        username: [
          { required: true, message: '用户名不能为空', trigger: 'blur' },
          { validator: this.validateUsername, trigger: 'blur' }
        ],
        password: [
          { required: true, message: '密码不能为空', trigger: 'change' }
        ],
        confirmPassword: [
          { required: true, message: '密码不能为空', trigger: 'change' }
        ],
      },
      isSignupShow: false,         //注册窗口是否显示
    }
  },
  components: {
  },
  methods: {
    validateUsername(rule, value, callback) {
      if (value.length > 15) {
        return callback(new Error('用户名长度不能超过15个字符'));
      }
      if (!/^[a-zA-Z]/.test(value)) {
        return callback(new Error('用户名必须以字母开头'));
      }
      callback();
    },

    login() {
      const params = { user: this.loginfo.username, password: this.loginfo.password }

      loginToBookView(params)
        .then(response => {
          if (response.data.loginstatus === 1) {
            // 登录成功，存储登录状态
            localStorage.setItem('isLoggedIn', 'true');
            localStorage.setItem('userID', response.data.userID);
            this.$router.push('/Home');
          } else {
            this.$message({ type: 'error', message: response.data.message });
          }
        })
        .catch(error => {
          this.$message({ type: 'error', message: `登陆失败，原因为${error}` });
        });
    },

    signup() {
      if (this.signupinfo.password.length != 0) {
        if (this.signupinfo.username.length > 15) {
          this.$message({ type: 'warning', message: `注册失败，用户名长度不能超过15个字符` })
        } else if (!/^[a-zA-Z]/.test(this.signupinfo.username)) {
          this.$message({ type: 'warning', message: `注册失败，用户名必须以字母开头` })
        } else {
          const params = { user: this.signupinfo.username, password: this.signupinfo.password, confirmPassword: this.signupinfo.confirmPassword, email: this.signupinfo.email, gender: this.signupinfo.gender }
          signupToBookView(params)
            .then(response => {
              if (response.data.codestatus === 1) {
                this.$message({ type: 'success', message: `注册成功，即将返回登陆页面` })
                // 添加延时逻辑
                setTimeout(() => {
                  this.isSignupShow = false;
                }, 1000); // 延时1000毫秒（1秒）
              } else {
                this.$message({ type: 'error', message: response.data.message })
              }
            })
            .catch(error => {
              this.$message({ type: 'error', message: `注册失败，原因为${error}` })
            });
        }
      } else (
        this.$message({ type: 'warning', message: `注册失败，密码不能为空` })
      )

    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="less" scoped>
.wrapper {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url("~@/assets/loginBackground.png");
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  height: 100vh;
  width: 100%;
  overflow: hidden;
}


.content {
  display: flex;
  position: relative;
  top: 50%;
  /* 居中 */
  left: 50%;
  transform: translate(-50%, -50%);
  /* 水平和垂直居中 */
  height: 80%;
  /* 高度为80% */
  width: 90%;
  /* 宽度为80% */
  background: #F6F6F6
}

.content .loginShow {
  display: flex;
  flex-direction: column;
  align-items: center;
  /* 使子元素水平居中 */
  justify-content: center;
  /* 使子元素垂直居中 */
  flex: 1;
  padding: 20px;
}

.content .loginShow .titleContainer {
  display: flex;
}

.content .loginShow .bookICON {
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

.content .loginShow .loginTitle {
  font-size: 24px;
  /* 标题字体大小 */
  font-weight: bold;
  /* 标题字体加粗 */
  font-family: 'Kaiti', sans-serif;
  /* 设置字体族为楷体 */
  margin-top: 10px;
}

.content .loginShow .BookPic {
  display: flex;
  height: 80%;
  /* 保持图片的原始宽高比 */
  width: 100%;
  justify-content: center;
  /* 水平居中 */
  align-items: center;
  /* 垂直居中 */
  flex-grow: 1;
  /* 占据剩余空间 */
}

.content .loginShow .BookPic img {
  max-width: 100%;
  /* 确保图片不会超过容器宽度 */
  height: 90%;
  /* 保持图片的原始宽高比 */
  width: 85%;
  margin-left: 40px;
}

.content .loginContent {
  flex: 1;
  padding: 20px;
}

.content .loginContent .login-button {
  padding: 5px;

  .item1 {
    font-size: 10px;
    float: right;
    margin-right: 70px;
    width: 68%;
  }

  .btn {
    font-family: 'Helvetica';
    width: 100%;
    height: 40px
  }
}

.sign-button {
  width:100%;

  .item1 {
    display: flex;
    justify-content: center;
    width: 100%;
    margin-left: -15px;
  }

  .btn {
    font-family: 'Helvetica';
    width: 100px;
    height: 40px
  }
}

.form {
  padding: 15px 0 !important;
  position: relative;
  padding-right: 30px;
  z-index: 2;

  .input {
    display: block;
    appearance: none;
    outline: 0;
    border: 1px solid fade(white, 40%);
    background: #F6F6F6;
    width: 300px;

    border-radius: 3px;
    padding: 8px;
    margin-top: 0;
    margin-right: 0;
    margin-left: 125px;
    margin-bottom: 0;
    display: block;
    text-align: center;
    font-size: 14px;

    color: white;

    transition-duration: 0.25s;
    font-weight: 200;

    &:hover {
      background-color: fade(white, 40%);
    }

    &:focus {
      background-color: white;
      width: 200px;

      color: #53e3d4;
    }
  }

  button {
    font-family: 'Helvetica';
    appearance: none;
    outline: 0;
    background-color: #53b5e3;
    color: white;
    border: 0;
    padding: 10px 15px;
    border-radius: 3px;
    width: 100px;
    cursor: pointer;
    font-size: 14px;
    transition-duration: 0.25s;

    &:hover {
      background-color: rgb(245, 247, 249);
      color: #53b5e3;
    }
  }
}

.tips {
  font-size: 12px;
  padding-top: 10px;
  color: rgb(102, 102, 96);
  display: inline;
  /* 或者使用 inline-block，根据需要调整 */
}

.tips .signup-link {
  color: rgb(0, 123, 255);
  text-decoration: none;
  /* 移除下划线 */
}

.tips .signup-link:hover {
  cursor: pointer;
  /* 鼠标悬停时的光标样式 */
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.5);
  /* 鼠标悬停时的深阴影效果 */
  text-decoration: underline;
  /* 鼠标悬停时添加下划线 */
}

/* 以下设置注册窗口的样式 */
.dialogWidth {
  width: 80%;
}

/deep/.el-dialog {
  background: #F6F6F6;
}

/deep/.el-form-item__content {
  display: flex;
  align-items: center;
  /*实现垂直居中*/
  // justify-content: center;
  /* 水平居中对齐 */
}

/deep/.el-form-item__error {
  position: relative;
  top: -5px;
  left: 0;
}
</style>
