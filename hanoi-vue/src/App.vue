<script setup>
import { ref, computed, watchEffect } from 'vue'
import HanoiControls from './components/HanoiControls.vue'
import HanoiBoard from './components/HanoiBoard.vue'
import { THEME_PALETTES } from './palettes.js'

const numberOfDisks = ref(3)
const numberOfTowers = ref(3)
const towers = ref([])
const moveCount = ref(0)
const selectedTowerIndex = ref(null)
const gameMessage = ref('')
const isGameInProgress = ref(false)
const isSolving = ref(false)
const currentTheme = ref('theme-default')

const currentPalette = computed(() => THEME_PALETTES[currentTheme.value])

function startGame() {
  towers.value = []
  for (let i = 0; i < numberOfTowers.value; i++) {
    towers.value.push([])
  }
  for (let i = numberOfDisks.value; i >= 1; i--) {
    towers.value[0].push(i)
  }
  moveCount.value = 0
  gameMessage.value = ''
  selectedTowerIndex.value = null
  isGameInProgress.value = true
}

function moveDisk(from, to) {
  const disk = towers.value[from].at(-1)
  if (disk === undefined) return false
  const targetDisk = towers.value[to].at(-1)
  if (targetDisk !== undefined && targetDisk < disk) return false
  towers.value[from].pop()
  towers.value[to].push(disk)
  moveCount.value++
  return true
}

function handleTowerClick(index) {
  if (!isGameInProgress.value || isSolving.value) return
  if (selectedTowerIndex.value === null) {
    selectedTowerIndex.value = index
  } else {
    if (selectedTowerIndex.value !== index) {
      moveDisk(selectedTowerIndex.value, index)
      checkVictory()
    }
    selectedTowerIndex.value = null
  }
}

function checkVictory() {
  if (towers.value[numberOfTowers.value - 1].length === numberOfDisks.value) {
    gameMessage.value = 'Victory!'
    isGameInProgress.value = false
  }
}

async function solveAutomatically() {
  if (isSolving.value) return
  isSolving.value = true
  selectedTowerIndex.value = null
  const delay = (ms) => new Promise(r => setTimeout(r, ms))
  async function solve(n, from, to, aux) {
    if (n <= 0) return
    await solve(n - 1, from, aux, to)
    moveDisk(from, to)
    await delay(300)
    await solve(n - 1, aux, to, from)
  }
  await solve(numberOfDisks.value, 0, numberOfTowers.value - 1, 1)
  checkVictory()
  isSolving.value = false
}

watchEffect(() => {
  document.body.className = currentTheme.value
})
</script>

<template>
  <HanoiControls
    :isSolving="isSolving"
    @change-disks="numberOfDisks = $event"
    @change-towers="numberOfTowers = $event"
    @change-theme="currentTheme = $event"
    @start-game="startGame"
    @solve-game="solveAutomatically"
  />
  <HanoiBoard
    :towers="towers"
    :selectedTowerIndex="selectedTowerIndex"
    :palette="currentPalette"
    @tower-click="handleTowerClick"
  />
  <p>Moves: {{ moveCount }}</p>
  <p>{{ gameMessage }}</p>
</template>

<style scoped>
#app {
  text-align: center;
}
</style>
