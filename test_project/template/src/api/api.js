/* eslint-disable */
import axios from 'axios'
import qs from 'qs'; 

axios.defaults.timeout = 60000 // 请求超时
axios.defaults.baseURL = '/api'
axios.defaults.withCredentials = true      // axios请求携带cookie

// login
export const loginToBookView = (params)=>{
    return axios.post(`/userInfo/login/`,params)
}

export const signupToBookView = (params)=>{
    return axios.post(`/userInfo/regester/`,params)
}

// commonViews
export const getBookList = (params)=>{
    return axios.post(`/bookList/getbooklist/`,params)
}

export const getBookType = ()=>{
    return axios.post(`/bookList/getbooktype/`)
}

export const getBookCategory = ()=>{
    return axios.post(`/bookList/getbookcategory/`)
}

// Home
export const getAllBook = ()=>{
    return axios.post(`/bookList/getallbook/`)
}

export const recordInfo = (params)=>{
    return axios.post(`/bookList/recordinfo/`,params)
}

// BookDetail
export const getBookInfo = (params)=>{
    return axios.post(`/bookList/getbookinfo/`,params)
}

// ChapterDetail
export const getChapter = (params)=>{
    return axios.post(`/bookList/getchapter/`,params)
}

// DataStatistics
export const getAllRecordData = (params)=>{
    return axios.post(`/bookList/getallrecorddata/`,params)
}