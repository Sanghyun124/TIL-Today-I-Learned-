<template>
  <div id="app">
    <h1>SSAFY TUBE</h1>
    <iframe :src="watch" width="720" height="405" frameborder="0" allowfullscreen></iframe>
    <div>
      {{ videoTitle }}
    </div>
  </div>
</template>


<script>
import axios from 'axios'

export default {
  name: 'App',
  components: {
  },
  data(){
    return{
      watch:"",
      videoTitle:""
    }
  },
  created(){
    const API_URI = 'https://www.googleapis.com/youtube/v3/search' 
      const param = {
        key:process.env.VUE_APP_YOUTUBE_API_KEY,
        part:'snippet',
        q: '코딩노래',
        maxResults: 5,
        type: 'video',
      }
      axios({
        methods : 'get',
        url : API_URI,
        params : param,
      })
      .then((response) => {
        console.log(response.data.items[0].snippet.title)
        this.watch = 'https://www.youtube.com/embed/' + response.data.items[0].id.videoId
        this.videoTitle = response.data.items[0].snippet.title
      })
      .catch(error =>{
        console.log(error.response);
      })
  }
}
</script>

<style>
#app {
  font-family: 'Noto Sans KR',Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
