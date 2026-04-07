<script setup>
/**
 * ModuleCompletion.vue - Button to mark a module as complete and earn XP
 * Stored in IndexedDB
 */
import { ref, onMounted } from 'vue'

const props = defineProps({
  moduleId: { type: String, required: true },
  xpValue: { type: Number, default: 30 },
  badgeName: { type: String, default: '' }
})

const isCompleted = ref(false)
const showCelebration = ref(false)

const DB_NAME = 'AgenticAI_MasteryDB'
const DB_VERSION = 1
const STORE_NAME = 'userProgress'

onMounted(() => {
  checkCompletion()
})

const checkCompletion = () => {
  const request = indexedDB.open(DB_NAME, DB_VERSION)
  request.onsuccess = (event) => {
    const db = event.target.result
    const transaction = db.transaction(STORE_NAME, 'readonly')
    const store = transaction.objectStore(STORE_NAME)
    const getRequest = store.get('currentUser')

    getRequest.onsuccess = () => {
      if (getRequest.result && getRequest.result.completedModules.includes(props.moduleId)) {
        isCompleted.value = true
      }
    }
  }
}

const completeModule = () => {
  if (isCompleted.value) return

  const request = indexedDB.open(DB_NAME, DB_VERSION)
  request.onsuccess = (event) => {
    const db = event.target.result
    const transaction = db.transaction(STORE_NAME, 'readwrite')
    const store = transaction.objectStore(STORE_NAME)
    const getRequest = store.get('currentUser')

    getRequest.onsuccess = () => {
      const userData = getRequest.result || { id: 'currentUser', xp: 0, completedModules: [] }
      
      if (!userData.completedModules.includes(props.moduleId)) {
        userData.completedModules.push(props.moduleId)
        userData.xp += props.xpValue
        
        store.put(userData)
        isCompleted.value = true
        showCelebration.value = true
        
        // Refresh local cache via event or reload (for simplicity reload/reactive state)
        setTimeout(() => location.reload(), 1500)
      }
    }
  }
}
</script>

<template>
  <div class="completion-container">
    <button 
      class="complete-btn" 
      :class="{ 'is-completed': isCompleted }"
      @click="completeModule"
      :disabled="isCompleted"
    >
      <span v-if="!isCompleted">Mark as Completed (+{{ xpValue }} XP)</span>
      <span v-else>🎉 Module Completed</span>
    </button>
    <div v-if="showCelebration" class="celebration">
       +{{ xpValue }} XP Earned! 🚀
    </div>
  </div>
</template>

<style scoped>
.completion-container {
  margin: 40px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.complete-btn {
  padding: 12px 30px;
  font-weight: 800;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  border: 4px solid transparent;
  background: linear-gradient(45deg, #4f46e5, #a855f7);
  color: white;
  box-shadow: 0 4px 15px rgba(109, 40, 217, 0.4);
}

.complete-btn:hover:not(:disabled) {
  transform: scale(1.05);
  box-shadow: 0 6px 20px rgba(109, 40, 217, 0.6);
}

.complete-btn.is-completed {
  background: rgba(16, 185, 129, 0.1);
  border: 1px solid #10b981;
  color: #10b981;
  cursor: default;
  box-shadow: none;
}

.celebration {
  margin-top: 15px;
  font-weight: bold;
  color: #a855f7;
  animation: bounce 1s infinite;
}

@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}
</style>
