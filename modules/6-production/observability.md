# Observability

**Module:** 6 | **Level:** Agent Architect | **XP:** 80 | **Estimated Time:** 3 hours

<XpTracker />
<Settings />

## Learning Objectives
- Master **Logging** for Agentic AI.
- Understand **Traces & Spans** (OpenTelemetry).
- Monitor **Token Usage & Costs**.
- Track **Latency & Model Performance**.
- Implement a **User Feedback (Up/Down)** loop.

## Why This Matters (Real-world Impact)
An Agent in production is a "Black Box." If it fails, you need to know *exactly* which step it failed at. **Observability** is the "X-ray" for your agent.
- *Example:* A user complains about "slowness." You check the logs and realize the `search_tool` is taking 30 seconds to return data.

## Core Concepts

### 1. Tracing the "Thought"
Unlike standard apps, an agent's logic is a non-linear loop. We need to see the "Chain of Thought" visually.
```mermaid
graph LR
    A[Request #1] --> B[Step 1: Plan (2s)]
    B --> C[Step 2: Tool Call (5s)]
    C --> D[Step 3: Reasoning (1s)]
    D --> E[Final Output (1s)]
    E --> F[Total Latency: 9s]
```

### 2. Token Counts & Costs
Every interaction has a cost. Monitoring tokens in real-time allows you to see how much money you spend per user or per task.
- **Input Tokens:** The length of your prompt.
- **Output Tokens:** The length of the AI's response.

## Real-World Examples
1. **LangSmith / Arize Phoenix:** Using a professional tracing tool to see a visual tree of every LLM call.
2. **Usage Dashboard:** A simple chart showing how many tokens were used per day.

## Code Examples (Python)

### 1. Basic Structured Logging
```python
import json
import time

def log_agent_interaction(user_id: str, prompt: str, result: str, tokens: int, start_time: float):
    duration = time.time() - start_time
    log_entry = {
        "timestamp": time.time(),
        "user_id": user_id,
        "latency": duration,
        "token_usage": tokens,
        "status": "success"
    }
    # Save to file or send to a monitoring service
    print(f"LOG: {json.dumps(log_entry)}")

# Usage
start = time.time()
log_agent_interaction("User123", "Hi", "Hello!", 10, start)
```

### 2. User Feedback Loop
```python
# A simple way to let users rate the agent
def log_user_feedback(session_id: str, score: int):
    # score: 1 (Up), 0 (Down)
    print(f"FEEDBACK: Session {session_id} received score {score}")
```

## Best Practices & Pro Tips
- **Always Trace Multi-Agent communication.** See who talked to whom and for how long.
- **Use JSON Logs.** Don't just `print()` things. Structured logs (JSON) are easier to search.
- **Set Cost Alerts.** If an agent starts looping infinitely, it can burn hundreds of dollars in tokens before you notice. Set a budget limit!

## Common Pitfalls & How to Avoid Them
- **Log Over-inflation.** Don't log the entire conversation if you only need the token count. Storage can be expensive.
- **Silent Failures.** If an agent "completes" with an empty response, your log should mark it as an ERROR, not a SUCCESS.

## Hands-on Exercises / Homework
- **Beginner:** Calculate the "cost" of a 500-token interaction at $0.002 per 1k tokens.
- **Intermediate:** Use the `time` module to measure how long a function takes to run and print the result.
- **Advanced:** Create a list of 10 interaction logs. Write a function that calculates the "Average Latency" of all logs.

## Gamified Challenge
**Story:** Your agent, *Spectre*, is the lead analyst for the *Insights Hive*.
- *Challenge:* Create an `ObservabilityLayer` class. Every time a `process_query()` method is called, the layer must record the "start_time" and "end_time" and print: "Latency recorded for [agent_id]."

## Knowledge Check – MCQs
1. **What is a 'Trace' in observability?**
   - A) A line in a drawing.
   - B) A recorded path of a single request through multiple steps or models.
   - C) A typo in a prompt.
2. **Why monitor 'Token Usage'?**
   - A) To control the model's speed.
   - B) To track and limit costs.
   - C) To improve the model's intelligence.

---
**© 2026 APT Computing Labs** – Apache License 2.0

<ModuleCompletion moduleId="6-observability" :xpValue="80" />
