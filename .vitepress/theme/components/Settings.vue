<script setup>
/**
 * Settings.vue - Modal to manage User API Keys in IndexedDB
 * 2026 APT Computing Labs
 */
import { ref, onMounted } from 'vue'

const isOpen = ref(false)
const geminiKey = ref('')
const openaiKey = ref('')
const anthropicKey = ref('')

const DB_NAME = 'AgenticAI_MasteryDB'
const DB_VERSION = 1
const STORE_NAME = 'userSettings'

onMounted(() => {
  loadSettings()
})

const initDB = () => {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open(DB_NAME, DB_VERSION)
    request.onsuccess = (event) => resolve(event.target.result)
    request.onerror = (event) => reject(event.target.error)
  })
}

const loadSettings = async () => {
  try {
    const db = await initDB()
    const transaction = db.transaction(STORE_NAME, 'readonly')
    const store = transaction.objectStore(STORE_NAME)
    const request = store.get('keys')

    request.onsuccess = () => {
      if (request.result) {
        geminiKey.value = request.result.gemini || ''
        openaiKey.value = request.result.openai || ''
        anthropicKey.value = request.result.anthropic || ''
      }
    }
  } catch (e) {
    // DB might not have the store yet
  }
}

const saveSettings = async () => {
  const db = await initDB()
  
  // Ensure store exists before write
  if (!db.objectStoreNames.contains(STORE_NAME)) {
    // This typically happens in onupgradeneeded, but we'll try to trigger if missing
    location.reload() // Re-triggering init with new version is needed for schema change
    return 
  }

  const transaction = db.transaction(STORE_NAME, 'readwrite')
  const store = transaction.objectStore(STORE_NAME)
  store.put({
    id: 'keys',
    gemini: geminiKey.value,
    openai: openaiKey.value,
    anthropic: anthropicKey.value,
    updatedAt: new Date().toISOString()
  })

  isOpen.value = false
  alert('Settings saved securely in your browser!')
}

const toggle = () => {
  isOpen.value = !isOpen.value
}
</script>

<template>
  <div class="settings-trigger" @click="toggle">
    ⚙️ <span>API Settings</span>
  </div>

  <div v-if="isOpen" class="modal-overlay" @click.self="toggle">
    <div class="glass-modal">
      <div class="modal-header">
        <h2>LLM API Settings</h2>
        <button class="close-btn" @click="toggle">&times;</button>
      </div>

      <p class="warning">
        ⚠️ These keys are stored **locally in your browser's IndexedDB**. 
        They are NEVER sent to any server except the direct LLM providers.
      </p>

      <div class="input-group">
        <label>Google Gemini Key</label>
        <input v-model="geminiKey" type="password" placeholder="AIzaSy...">
      </div>

      <div class="input-group">
        <label>OpenAI Key</label>
        <input v-model="openaiKey" type="password" placeholder="sk-...">
      </div>

      <div class="input-group">
        <label>Anthropic Key</label>
        <input v-model="anthropicKey" type="password" placeholder="sk-ant-...">
      </div>

      <div class="modal-footer">
        <button class="save-btn" @click="saveSettings">Save Keys</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.settings-trigger {
  cursor: pointer;
  padding: 8px 12px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  font-size: 0.9rem;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: all 0.2s;
}

.settings-trigger:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: #a855f7;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(5px);
  z-index: 1000;
  display: flex;
  justify-content: center;
  align-items: center;
}

.glass-modal {
  background: rgba(15, 15, 25, 0.85);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.15);
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
  border-radius: 24px;
  width: 90%;
  max-width: 480px;
  padding: 30px;
  color: white;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.modal-header h2 {
  margin: 0;
  font-size: 1.5rem;
  background: linear-gradient(90deg, #a855f7, #3b82f6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.close-btn {
  background: none;
  border: none;
  color: #666;
  font-size: 2rem;
  cursor: pointer;
  line-height: 1;
}

.warning {
  background: rgba(245, 158, 11, 0.1);
  border: 1px solid rgba(245, 158, 11, 0.2);
  padding: 12px;
  border-radius: 12px;
  font-size: 0.85rem;
  color: #fbbf24;
  margin-bottom: 25px;
}

.input-group {
  margin-bottom: 20px;
}

.input-group label {
  display: block;
  font-size: 0.85rem;
  margin-bottom: 8px;
  color: #999;
}

.input-group input {
  width: 100%;
  background: rgba(0, 0, 0, 0.3);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 12px;
  border-radius: 10px;
  color: white;
  font-family: monospace;
}

.input-group input:focus {
  outline: none;
  border-color: #a855f7;
  background: rgba(0, 0, 0, 0.5);
}

.modal-footer {
  margin-top: 30px;
}

.save-btn {
  width: 100%;
  padding: 14px;
  border-radius: 12px;
  background: linear-gradient(90deg, #4f46e5, #a855f7);
  color: white;
  font-weight: bold;
  border: none;
  cursor: pointer;
  box-shadow: 0 4px 15px rgba(109, 40, 217, 0.4);
}

.save-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(109, 40, 217, 0.6);
}
</style>
