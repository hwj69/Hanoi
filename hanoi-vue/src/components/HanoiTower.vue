<script setup>
import HanoiDisk from './HanoiDisk.vue'
const props = defineProps({
  disks: Array,
  index: Number,
  isSelected: Boolean,
  palette: Array
})
const emit = defineEmits(['tower-click'])
</script>

<template>
  <div class="tower" :class="{ selected: isSelected }" @click="emit('tower-click', index)">
    <HanoiDisk
      v-for="(disk, idx) in [...disks].reverse()"
      :key="idx"
      :size="disk"
      :color="palette[disk - 1]"
    />
  </div>
</template>

<style scoped>
.tower {
  width: 150px;
  min-height: 200px;
  border: 2px solid #ccc;
  display: flex;
  flex-direction: column-reverse;
  align-items: center;
  padding: 0.5rem;
}
.selected {
  border-color: #646cff;
}
</style>
