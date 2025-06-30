<script setup>
const props = defineProps({
  towers: Array,
  selectedTowerIndex: Number,
  palette: Array
})
const emit = defineEmits(['tower-click'])
</script>

<template>
  <div class="board">
    <div
      class="tower-wrapper"
      v-for="(disks, idx) in towers"
      :key="idx"
      @click="emit('tower-click', idx)"
    >
      <HanoiTower
        :disks="disks"
        :index="idx"
        :isSelected="idx === selectedTowerIndex"
        :palette="palette"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import HanoiTower from './HanoiTower.vue'
</script>

<style scoped>
.board {
  display: flex;
  justify-content: center;
  gap: 1rem;
}
.tower-wrapper {
  cursor: pointer;
}
</style>
