<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  isSolving: Boolean
})
const emit = defineEmits(['change-disks', 'change-towers', 'change-theme', 'start-game', 'solve-game'])

const disks = ref(3)
const towers = ref(3)
const theme = ref('theme-default')

watch(disks, (val) => emit('change-disks', Number(val)))
watch(towers, (val) => emit('change-towers', Number(val)))
watch(theme, (val) => emit('change-theme', val))
</script>

<template>
  <div class="controls">
    <label>
      Disks
      <input type="number" v-model="disks" min="1" />
    </label>
    <label>
      Towers
      <input type="number" v-model="towers" min="3" />
    </label>
    <label>
      Theme
      <select v-model="theme">
        <option value="theme-default">Default</option>
        <option value="theme-forest">Forest</option>
        <option value="theme-ocean">Ocean</option>
      </select>
    </label>
    <button @click="emit('start-game')" :disabled="isSolving">Start</button>
    <button @click="emit('solve-game')" :disabled="isSolving">Solve</button>
  </div>
</template>

<style scoped>
.controls {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin-bottom: 1rem;
}
</style>
