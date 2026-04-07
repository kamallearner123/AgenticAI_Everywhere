<script setup>
/**
 * XpTracker.vue - A gamified progress tracker using IndexedDB
 * 2026 APT Computing Labs
 */
import { ref, onMounted } from 'vue'

const DB_NAME = 'AgenticAI_MasteryDB'
const DB_VERSION = 1
const STORE_NAME = 'userProgress'

const xp = ref(0)
const level = ref('Novice')
const completedModules = ref([])

onMounted(() => {
  initDB()
})

const initDB = () => {
  const request = indexedDB.open(DB_NAME, DB_VERSION)

  request.onupgradeneeded = (event) => {
    const db = event.target.result
    if (!db.objectStoreNames.contains(STORE_NAME)) {
      db.createObjectStore(STORE_NAME, { keyPath: 'id' })
    }
  }

  request.onsuccess = (event) => {
    const db = event.target.result
    loadUserData(db)
  }
}

const loadUserData = (db) => {
  const transaction = db.transaction(STORE_NAME, 'readonly')
  const store = transaction.objectStore(STORE_NAME)
  const request = store.get('currentUser')

  request.onsuccess = () => {
    if (request.result) {
      xp.value = request.result.xp || 0
      completedModules.value = request.result.completedModules || []
      updateLevel()
    } else {
      // First time user
      saveUserData(db, { id: 'currentUser', xp: 0, completedModules: [] })
    }
  }
}

const saveUserData = (db, data) => {
  const transaction = db.transaction(STORE_NAME, 'readwrite')
  const store = transaction.objectStore(STORE_NAME)
  store.put(data)
}

const updateLevel = () => {
  if (xp.value >= 1500) level.value = 'Master Agent Builder'
  else if (xp.value >= 800) level.value = 'Agent Architect'
  else if (xp.value >= 300) level.value = 'Agent Builder'
  else if (xp.value >= 150) level.value = 'Apprentice'
  else level.value = 'Novice'
}

// Function to add XP (for use in other components)
const addXp = (amount) => {
  xp.value += amount
  updateLevel()
  const request = indexedDB.open(DB_NAME, DB_VERSION)
  request.onsuccess = (event) => {
    saveUserData(event.target.result, { 
      id: 'currentUser', 
      xp: xp.value, 
      completedModules: completedModules.value 
    })
  }
}
</script>

<template>
  <div class="xp-badge-container">
    <div class="xp-info">
      <span class="level-tag">{{ level }}</span>
      <span class="xp-count">{{ xp }} XP</span>
    </div>
    <div class="xp-bar-total">
      <div class="xp-progress-fill" :style="{ width: (xp / 1650) * 100 + '%' }"></div>
    </div>
  </div>
</template>

<style scoped>
.xp-badge-container {
  padding: 10px 16px;
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  min-width: 180px;
  margin: 10px 0;
}

.xp-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.level-tag {
  font-size: 0.75rem;
  font-weight: bold;
  text-transform: uppercase;
  color: #a855f7;
  letter-spacing: 0.5px;
}

.xp-count {
  font-size: 0.85rem;
  font-weight: 800;
  color: white;
}

.xp-bar-total {
  width: 100%;
  height: 6px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 3px;
  overflow: hidden;
}

.xp-progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #a855f7, #3b82f6);
  transition: width 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}
</style>
