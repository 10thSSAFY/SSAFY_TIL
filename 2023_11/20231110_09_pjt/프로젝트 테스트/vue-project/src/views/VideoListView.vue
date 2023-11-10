<template>
  <div>
    <img @click="goDetail(videoInfo)" :src="videoInfo.snippet.thumbnails.medium.url" alt="image">
    <p @click="goDetail(videoInfo)">{{ videoInfo.snippet.title }}</p>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()

defineProps({
  videoInfo: Object,
})

const goDetail = (videoInfo) => {
  console.log(videoInfo)
  router.push(`/${videoInfo.id}`)
}

</script>

<style scoped>

</style>