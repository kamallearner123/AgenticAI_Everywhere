---
layout: home

hero:
  name: "Agentic AI Mastery"
  text: "Build Production-Ready Autonomous Agents"
  tagline: "A gamified portal for mastering LLMs, RAG, and Orchestration."
  image:
    src: /hero.png
    alt: Agentic AI
  actions:
    - theme: brand
      text: Start Learning
      link: /modules/index
    - theme: alt
      text: View Syllabus
      link: /#syllabus

features:
  - title: "Gamified XP & Levels"
    details: "Earn XP points and climb from Novice to Agent Architect. Track your progress directly in the browser via IndexedDB."
    icon: 🎮
  - title: "Interactive Hub"
    details: "Run real-world Python code examples in the browser with Pyodide. No local setup required."
    icon: ⚡
  - title: "Production Ready"
    details: "Focus on Security, Reliability, and Observability. Move beyond prompts to production deployment."
    icon: 🏗️
---

<div class="user-dashboard glass-card">
  <h3>My Agent Profile</h3>
  <XpTracker />
  <div class="actions">
    <Settings />
  </div>
</div>

## Your Path to Mastery

<div class="badge-grid">
  <div class="badge-card locked">
    <div class="icon">🧪</div>
    <h4>Code Alchemist</h4>
    <p>Module 1 Complete</p>
  </div>
  <div class="badge-card locked">
    <div class="icon">🧙‍♂️</div>
    <h4>Prompt Wizard</h4>
    <p>Module 2 Complete</p>
  </div>
  <div class="badge-card locked">
    <div class="icon">🤖</div>
    <h4>ReAct Pioneer</h4>
    <p>Module 3 Complete</p>
  </div>
</div>

## Syllabus Preview {#syllabus}

| Module | Level | XP |
| :--- | :--- | :--- |
| **1: Foundations** | Novice | 150 |
| **2: LLM Core** | Apprentice | 200 |
| **3: Agents** | Agent Builder | 300 |
| **4: Retrieval** | Knowledge Engineer | 250 |
| **5: Advanced** | Orchestrator | 350 |
| **6: Production** | Agent Architect | 400 |

[Begin your journey →](/modules/index)

<style>
.user-dashboard {
  margin: 40px auto;
  max-width: 600px;
  padding: 30px;
  border-radius: 24px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(20px);
  text-align: center;
}

.user-dashboard h3 {
  margin-top: 0;
  margin-bottom: 20px;
  background: linear-gradient(90deg, #a855f7, #3b82f6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.badge-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 20px;
  margin: 40px 0;
}

.badge-card {
  padding: 25px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 20px;
  text-align: center;
  transition: all 0.3s;
}

.badge-card.locked {
  filter: grayscale(1) opacity(0.5);
}

.badge-card .icon {
  font-size: 3rem;
  margin-bottom: 10px;
}

.badge-card h4 {
  margin: 10px 0 5px;
  color: white;
}

.badge-card p {
  font-size: 0.8rem;
  color: #888;
}

.badge-card:hover:not(.locked) {
  transform: translateY(-5px) scale(1.05);
  border-color: #a855f7;
}

.actions {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}
</style>
