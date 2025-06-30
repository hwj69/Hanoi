<script setup>
const props = defineProps({
  size: Number,
  color: String
})
</script>

<template>
  <div class="disk" :style="{ width: size * 20 + 'px', backgroundColor: color }"></div>
</template>

<style scoped>
.disk {
  height: 20px;
  margin: 2px 0;
  border-radius: 4px;
}
</style>
