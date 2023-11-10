<template>
  <form @submit.prevent="searchVideo">
    <label for="search">비디오 검색</label>
    <input type="text" id="search" v-model="inputText">
    <button type="submit">찾기</button>
  </form>
  <VideoList
    v-for="video in videos" :key="video.pk"
    :video-info="video"
  />
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import VideoList from '@/views/VideoListView.vue'

const key = import.meta.env.VITE_TMDB_API_KEY
const inputText = ref('')
const videos = ref([])
const searchVideo = function () {
  const q = inputText
  const url = 'https://www.googleapis.com/youtube/v3/search'
  console.log(url)
  axios({
    url: url,
    method: 'get',
    params: {
      key,
      type: 'video',
      part: 'snippet',
      maxResults: 30,
      q: q.value
    }
  })
    .then((response) => {
      videos.value = response.data.items
    })
    .catch((error) => {
      console.log(error)
    })
}
</script>

<style scoped>

</style>