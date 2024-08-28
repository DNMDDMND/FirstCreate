<template>
    <el-container class="wrapper" element-loading-text="拼命加载中">
        <el-tabs v-model="currShowData" style="width:100%;height:100%;" id="print">
            <el-tab-pane label="书籍数据" name="bookData">
                <el-row class="echart-box">
                    <div class="ertable" ref="box1"></div>
                </el-row>
            </el-tab-pane>
            <el-tab-pane label="用户数据" name="userData">
                <el-row class="echart-box">
                    <div class="ertable" ref="box2"></div>
                </el-row>
            </el-tab-pane>
        </el-tabs>

        <el-row class="tableButton">
            <el-col :span="6">
                <el-select v-model="needShowData" v-if="currShowData === 'bookData'">
                    <el-option label="点击量" value="clickCountSta"></el-option>
                    <el-option label="作品类型统计" value="bookTypeCountSta"></el-option>
                </el-select>
                <el-select v-model="needShowData" v-else-if="currShowData === 'userData'">
                    <el-option label="用户性别统计" value="genderCountSta"></el-option>
                    <el-option label="阅读时间段" value="dataCountSta"></el-option>
                </el-select>
            </el-col>

            <div class="iconSelect">
                <el-dropdown style="margin-right: 15px;" @command="ChartTypeSelect">
                    <span style="cursor: pointer;font-size: 30px;">
                        <i class="el-icon-s-data"></i>
                    </span>
                    <el-dropdown-menu slot="dropdown">
                        <el-dropdown-item command="bar">柱形图</el-dropdown-item>
                        <el-dropdown-item command="line">折线图</el-dropdown-item>
                        <el-dropdown-item command="pie">饼状图</el-dropdown-item>
                    </el-dropdown-menu>
                </el-dropdown>

                <el-dropdown @command="ChartButtonSelect">
                    <span style="cursor: pointer;font-size: 30px;">
                        <i class="el-icon-menu"></i>
                    </span>
                    <el-dropdown-menu slot="dropdown">
                        <el-dropdown-item command="fullScreen">全屏显示</el-dropdown-item>
                        <el-dropdown-item command="printEcharts">打印表格</el-dropdown-item>
                        <el-dropdown-item command="downEchartsPic">下载表格图片</el-dropdown-item>
                    </el-dropdown-menu>
                </el-dropdown>
            </div>
        </el-row>
    </el-container>
</template>

<script>
import {
    getAllRecordData
} from "../api/api";
import { EleResize } from '../assets/esresize.js'

export default {
    // el-icon-s-operation
    // el-icon-menu
    name: 'DataStatistics',
    data() {
        return {
            needShowData: 'clickCountSta',
            currChartsType: 'bar',
            currShowData: 'bookData',
            allRecordData: {
                'clickCount': {},
                'typeCount': {},
                'genderCount': { 'male': 0, 'female': 0 },
                'dateCount': {}
            },
        }
    },
    components: {},
    methods: {
        // 画折线图和柱形图
        drawLineOrBarChart(currShowData, needShowData, currChartsType) {
            let mycart = this.initEcharts(currShowData)

            // 设置标题
            const [title, data] = this.echartsTitleAndData(needShowData) // 这里用函数处理图标标题(或者写个字典)
            // 设置x轴和y轴的数据
            const [data_x, data_y] = this.unpackData(data)
            // 设置统计图类型
            // option.series.type = currChartsType

            const option = {
                backgroundColor: 'white', //设置无背景色
                title: {
                    text: title,
                    subtext: `截止到${this.getCurrentTime()}`,
                    left: 'center'
                },
                xAxis: {
                    type: 'category',
                    data: data_x,
                    show: true
                },
                yAxis: {
                    type: 'value'
                },
                series: [
                    {
                        data: data_y,
                        type: currChartsType,
                        showBackground: true,
                        backgroundStyle: {
                            color: 'rgba(180, 180, 180, 0.2)'
                        }
                    }
                ]
            }
            mycart.setOption(option)
        },
        // 画饼状图
        drawPieChart(currShowData, needShowData) {
            const mycart = this.initEcharts(currShowData)
            console.log('mycart: ', mycart)
            // 设置标题
            let [title, data] = this.echartsTitleAndData(needShowData)
            // 设置x轴和y轴的数据
            data = this.unpackDataForPie(data)

            const option = {
                title: {
                    text: title,
                    subtext: `截止到${this.getCurrentTime()}`,
                    left: 'center'
                },
                xAxis: {
                    show: false
                },
                series: [
                    {
                        type: 'pie',
                        data: data
                    }
                ]
            };
            mycart.setOption(option)
        },
        // 初始化表格实例
        initEcharts(currShowData) {
            let userdom = null;
            if (currShowData === 'bookData') {
                userdom = this.$refs.box1
            } else {
                userdom = this.$refs.box2
            }

            userdom.classList.remove('fullscreen-chart');
            // // 移除现有的 EleResize 监听器
            // EleResize.off(userdom);

            // let existInstance = this.$echarts.getInstanceByDom(userdom);
            // if (existInstance) {
            //     // 如果存在，销毁实例
            //     existInstance.dispose();
            //     userdom.classList.add('ertable');
            // }

            const mycart = this.$echarts.init(userdom)

            // 自适应
            var listener = function () {
                mycart.resize()
            }

            EleResize.on(userdom, listener)

            return mycart
        },
        // 处理图标标题和获取需要展示的数据
        echartsTitleAndData(needShowData) {
            let title = ''
            let data = {}
            if (needShowData === 'clickCountSta') {
                title = '用户点击量统计'
                data = this.allRecordData.clickCount
            } else if (needShowData === 'bookTypeCountSta') {
                title = '作品类型统计'
                data = this.allRecordData.typeCount
            } else if (needShowData === 'genderCountSta') {
                title = '用户性别统计'
                data = this.allRecordData.genderCount
            } else if (needShowData === 'dataCountSta') {
                title = '用户阅读时间段统计'
                data = this.allRecordData.dateCount
            }
            return [title, data]
        },
        // 获取所有需要的数据，包括点击量、作品类型数量、用户群体特征
        async fetchAllRecordData() {
            await getAllRecordData()
                .then(response => {
                    if (response.data.code === 0) {
                        const responseData = response.data.data
                        this.allRecordData.clickCount = responseData['click_count']
                        this.allRecordData.typeCount = JSON.parse(localStorage.getItem('bookCategoryItems'))
                        this.allRecordData.genderCount = responseData['gender_count']
                        this.allRecordData.dateCount = responseData['date_count']

                        console.log('allRecordData: ', this.allRecordData)
                    } else {
                        this.$message({ type: 'error', message: '获取记录的数据失败，请刷新页面再次尝试一下' });
                    }
                })
                .catch(error => {
                    console.error('Error fetching all record data:', error);
                })
            this.drawLineOrBarChart(this.currShowData, this.needShowData, this.currChartsType)
        },
        // 获取图表类型
        ChartTypeSelect(command) {
            this.currChartsType = command
        },
        // 操作图表
        ChartButtonSelect(command) {
            this.ChartsButton(command)
        },
        ChartsButton(command) {
            let element = NaN
            if (this.currShowData === 'bookData') {
                element = this.$refs.box1
            } else {
                element = this.$refs.box2
            }
            if (command === 'fullScreen') {
                this.fullScreen(element)
            } else if (command === 'printEcharts') {
                this.printEcharts(element)
            } else if (command === 'downEchartsPic') {
                this.downEchartsPic(element)
            }
        },
        // 全屏显示
        fullScreen(element) {
            if (element.requestFullScreen) {
                // HTML W3C 提议
                element.requestFullScreen()
            } else if (element.msRequestFullscreen) {
                // IE11
                element.msRequestFullScreen()
            } else if (element.webkitRequestFullScreen) {
                // Webkit
                element.webkitRequestFullScreen()
            } else if (element.mozRequestFullScreen) {
                // Firefox
                element.mozRequestFullScreen()
            }
            // 退出全屏
            if (element.requestFullScreen) {
                document.exitFullscreen()
            } else if (element.msRequestFullScreen) {
                document.msExitFullscreen()
            } else if (element.webkitRequestFullScreen) {
                document.webkitCancelFullScreen()
            } else if (element.mozRequestFullScreen) {
                document.mozCancelFullScreen()
            }

            // 添加全屏样式类
            element.classList.add('fullscreen-chart');

            // 退出全屏时，移除样式类
            const exitFullscreen = () => {
                document.removeEventListener('fullscreenchange', exitFullscreen);
                element.classList.remove('fullscreen-chart');
            };

            document.addEventListener('fullscreenchange', exitFullscreen);
        },
        // 打印图表
        printEcharts(element) {
            let { newImg, printContainer } = this.echartsConvertToiImages(element);
            // 等待图像加载完成，防止打印空白页
            newImg.onload = function () {
                printContainer.appendChild(newImg); // 将图片添加到打印容器中
                var newWindow = window.open('', '_blank'); // 打开一个新的窗口或标签页
                newWindow.document.write(printContainer.outerHTML); // 将打印容器的HTML内容写入新窗口或标签页
                newWindow.print(); // 触发新窗口或标签页的打印
                newWindow.close(); // 关闭新窗口或标签页
            };
        },
        // 下载表格图片
        downEchartsPic(element) {
            let { newImg, printContainer,imgData } = this.echartsConvertToiImages(element);
            // 等待图像加载完成，防止打印空白页
            newImg.onload = function () {
                // 将图片添加到临时的打印容器中
                printContainer.appendChild(newImg);
                // 创建一个a元素，并设置下载属性
                var a = document.createElement('a');
                a.href = imgData;
                a.download = 'chart.png';  // 设置下载的文件名
                document.body.appendChild(a);
                a.click();  // 模拟点击触发下载
                document.body.removeChild(a); // 清理DOM
            };
        },
        echartsConvertToiImages(element) {
            // 创建一个临时的打印容器
            let printContainer = document.createElement('div');
            printContainer.id = 'print-container';
            // 获取当前激活的 ECharts 实例的 canvas
            let activeChartCanvas = element.querySelector('canvas');
            if (activeChartCanvas) {
                let imgData = activeChartCanvas.toDataURL("image/png");
                let newImg = document.createElement('img');
                newImg.src = imgData;
                newImg.style.width = '100%';
                return { newImg, printContainer, imgData }; // 返回一个包含两个属性的对象
            }
            return null; // 如果没有找到canvas，返回null
        },
        // 获取当前时间
        getCurrentTime() {
            const now = new Date();
            const year = now.getFullYear();
            const month = this.padZero(now.getMonth() + 1);
            const day = this.padZero(now.getDate());
            const hours = this.padZero(now.getHours());
            const minutes = this.padZero(now.getMinutes());
            const seconds = this.padZero(now.getSeconds());

            return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
        },
        padZero(number) {
            return number < 10 ? `0${number}` : number;
        },
        // 解包数据，存储为只保有key和value的两个列表
        unpackData(data) {
            const keys = Object.keys(data);
            const values = Object.values(data);
            return [keys, values]
        },
        // 解包数据，存储为给饼状图用的数据
        unpackDataForPie(data) {
            let dataForPie = Object.entries(data).map(([name, value]) => ({
                value: value,
                name: name
            }));
            return dataForPie
        }
    },
    created() {

    },
    mounted() {
        this.fetchAllRecordData() //获取所有数据并且初始化一张表
    },
    watch: {
        currChartsType: {
            handler(newValue) {
                console.log('newValue: ', newValue)
                if (newValue === 'bar' || newValue === 'line') {
                    this.drawLineOrBarChart(this.currShowData, this.needShowData, newValue)
                }
                else if (newValue === 'pie') {
                    this.drawPieChart(this.currShowData, this.needShowData)
                }
            },
            deep: true
        },
        needShowData: {
            handler(newValue) {
                if (this.currChartsType) {
                    if (this.currChartsType === 'pie') {
                        this.drawPieChart(this.currShowData, newValue)
                    } else {
                        this.drawLineOrBarChart(this.currShowData, newValue, this.currChartsType)
                    }
                }
            },
            deep: true
        },
        currShowData: {
            handler(newValue) {
                if (newValue === 'bookData') {
                    this.needShowData = "clickCountSta"
                } else if (newValue === 'userData') {
                    this.needShowData = "genderCountSta"
                }
            },
            deep: true
        }
    }
}

</script>

<style lang="less" scoped>
.wrapper {
    width: 100%;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    overflow-x: hidden;
    overflow-y: auto;
    display: flex;
    justify-content: center;
}

.echart-box {
    width: 100%;
    height: 450px;
    margin: 20px auto;
    display: flex;
    justify-content: center;
}

.ertable {
    width: 1000px;
    height: 450px;
}

// .echart-container {
//     width: 100%;
//     height: 450px;
// }

.tableButton {
    width: 100%;
    position: absolute;
    z-index: 3;
    top: 70px;
    left: 120px;
}

.tableButton /deep/.el-input__inner {
    width: 140px;
}

.tableButton .iconSelect {
    position: absolute;
    right: 300px;
    top: 5px;
}

// 全屏后的样式
.fullscreen-chart {
    background-color: white;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>