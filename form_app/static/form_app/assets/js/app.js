let vm = Vue.createApp({
    delimiters: ["[[", "]]"],
    data(){
        return {
            firstName: 'abbas',
            testList: ['baba', 'ila', 'jaki']
        }
    }
}).mount('#app') 


