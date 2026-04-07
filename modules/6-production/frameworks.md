# Frameworks & Tools Deep Dive

**Module:** 6 | **Level:** Agent Architect | **XP:** 120 | **Estimated Time:** 5 hours

<XpTracker />
<Settings />

## Learning Objectives
- Master the **LangChain** ecosystem.
- Master **LlamaIndex** for specialized data agents.
- Explore **CrewAI & AutoGen** for MAS (Multi-Agent Systems).
- Use **Ollama** for local agent development.
- Evaluate and select the best tool for your specific agentic use case.

## Why This Matters (Real-world Impact)
You've learned the "Foundations" and built your own loops. In professional projects, you don't build everything from scratch. You use **Frameworks** to save hundreds of hours of coding.
- *Example:* Instead of building your own RAG loop, use 5 lines of **LlamaIndex** to index 1000 PDFs in minutes.

## Core Concepts

### 1. Framework Selection Matrix
Which framework should you use?
| Use Case | Best Framework | Key Strength |
| :--- | :--- | :--- |
| **Connecting everything** | LangChain | Huge library of integrations |
| **Data-heavy agents** | LlamaIndex | Optimized for RAG and search |
| **Autonomous Teams** | CrewAI / AutoGen | Easy multi-agent coordination |
| **Local / Offline** | Ollama | Run GGUF models on your laptop |

### 2. LangChain Expression Language (LCEL)
The "Chain" part is where you link prompts, models, and output parsers.
```python
# Simple Chain Visualization
# Prompt -> Model -> Parser
```

## Real-World Examples
1. **Corporate Wiki Agent:** Using LlamaIndex to create a "Chat with your codebase" feature.
2. **Sales Swarm:** Using CrewAI to build an agent team: Researcher (Finds leads) + Outreach (Writes the email).

## Code Examples (Python)

### 1. A Simple LangChain Chain (Simulation)
```python
def mock_chain(input_text: str):
    # Prompt
    prompt = f"Summarize this: {input_text}"
    # Model (Simulated)
    response = f"Summary: AI is the future of {input_text[0:10]}..."
    # Parser
    return response.strip().lower()

print(mock_chain("Agentic AI Frameworks are very powerful..."))
```

### 2. Initializing a Multi-Agent Crew (Pseudo-code)
```python
class CrewAgent:
    def __init__(self, name: str, goal: str):
        self.name = name
        self.goal = goal

# Defining the crew
researcher = CrewAgent("Researcher", "Find the best AI tools")
writer = CrewAgent("Writer", "Write a LinkedIn post about them")

crew = [researcher, writer]
print(f"Crew ready with {len(crew)} agents.")
```

## Best Practices & Pro Tips
- **Start Simple.** Don't jump into a complex framework if a 20-line Python script can do the job. 
- **Don't over-engineer.** Frameworks can be heavy; only use the parts you need (modular approach).
- **Keep models local for testing.** Use **Ollama** to iterate on prompts without spending tokens.

## Common Pitfalls & How to Avoid Them
- **"Black Box" Frameworks:** If you don't understand how a framework works internally, you can't debug it when it fails. (That's why we learned the foundations first!).
- **API Versioning:** Frameworks update quickly. Always pin your versions in `requirements.txt`.

## Hands-on Exercises / Homework
- **Beginner:** Research LangChain and find 3 "Tools" (Integrations) it supports (e.g., Google Search, Wikipedia).
- **Intermediate:** Install Ollama on your computer and try to "chat" with a local model like Llama 3 or Gemma.
- **Advanced:** Draw a "Chain" diagram for an agent that researches a topic, summarizes it, and then emails the summary to a user.

## Gamified Challenge
**Story:** Your agent, *Mastery*, is the final boss of the *Development Forge*.
- *Challenge:* Using any framework's pseudo-code, design a "Three-Agent Team" (Plan, Build, Test). Label each agent's role and explain how they pass information.

## Knowledge Check – MCQs
1. **Which framework is best optimized for RAG and Vector search?**
   - A) LangChain
   - B) LlamaIndex
   - C) Ollama
2. **What does 'LCEL' stand for in LangChain?**
   - A) Local Code Execution Language
   - B) LangChain Expression Language
   - C) Light Code Entry Link

---
**© 2026 APT Computing Labs** – Apache License 2.0

<ModuleCompletion moduleId="6-frameworks" :xpValue="120" />
