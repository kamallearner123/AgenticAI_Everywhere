# Evaluation, Reliability & Testing

**Module:** 6 | **Level:** Agent Architect | **XP:** 100 | **Estimated Time:** 4 hours

<XpTracker />
<Settings />

## Learning Objectives
- Master the **LLM-as-a-Judge** pattern for evaluation.
- Understand **Deterministic vs Probabilistic** testing.
- Implement **Evals** using metrics like Faithfulness, Answer Relevancy, and Hallucination Scores.
- Learn **Unit Testing** for Python-based tool calls.
- Use **Benchmarking** datasets (MMLU, HumanEval) to measure agent performance.

## Why This Matters (Real-world Impact)
An agent that works 80% of the time is more dangerous than an agent that works 0% of the time. In production, you need to prove your agent's **Reliability**.
- *Example:* A legal agent that correctly analyzes 9 contracts but hallucinates a clause in the 10th one can cause a massive lawsuit.

## Core Concepts

### 1. The Evaluation Loop (LLM-as-a-Judge)
Since agent outputs are often free-form text, we use a *stronger* model (like Gemini 1.5 Pro) to grade the output of a *smaller* model (like Gemini Flash).
```mermaid
graph LR
    A[User Query] --> B[Agent Response]
    B --> C[Judge Model: "Is this correct based on X?"]
    C --> D{Pass/Fail Score}
    D -- Fail --> E[Developer: Update Prompt/Data]
    D -- Pass --> F[Release to Production]
```

### 2. Key Metrics for Agents
- **Faithfulness:** Does the answer come *only* from the provided context?
- **Answer Relevancy:** Does the answer actually address the user's question?
- **Hallucination Score:** Does the agent make up facts not found in the tools or memory?

## Real-World Examples
1. **RAG Evaluation:** Using the `Ragas` library to automatically score 1000 QA pairs.
2. **Regression Testing:** Before updating a prompt, running a "Golden Dataset" of 50 past questions to ensure the agent didn't get "dumber."

## Code Examples (Python)

### 1. Mocking a Tool State for Unit Testing
```python
import pytest

def calculate_discount(price: float, code: str):
    if code == "SAVE10": return price * 0.9
    return price

def test_calculate_discount():
    # Deterministic Test
    assert calculate_discount(100, "SAVE10") == 90.0
    assert calculate_discount(100, "NONE") == 100.0
```

### 2. LLM-as-a-Judge Logic (Simulation)
```python
async def judge_response(user_query, agent_response, context):
    judge_prompt = f"""
    Context: {context}
    Agent Answer: {agent_response}
    Grade the answer 1-10 based on accuracy.
    Score:
    """
    # In reality, you'd call an LLM here
    return 9 # The simulated score
```

## Best Practices & Pro Tips
- **Build a 'Golden Dataset'.** Collect 50+ real questions and manually verify the "Perfect Answer." 
- **Automate your Evals.** Don't grading manually; it's too slow.
- **Categorize Failures.** Is the agent failing due to bad retrieval, poor reasoning, or tool errors?

## Common Pitfalls & How to Avoid Them
- **Over-reliance on LLM-as-a-Judge.** Judges can have their own biases. Always do manual spot-checks.
- **Testing in Isolation.** An agent might pass a unit test but fail in a multi-turn conversation. Use "Trace" evaluation.

## Hands-on Exercises / Homework
- **Beginner:** Create a list of 5 questions and what you consider the "Perfect Answer" for each.
- **Intermediate:** Write a Python test using `assert` for a function that cleans user input.
- **Advanced:** Use a mock score (1-10) to decide if an agent's output should be shown to a user or sent for "Refinement."

## Gamified Challenge
**Story:** Your agent, *Checkmate*, is the lead auditor for the *Quality Council*.
- *Challenge:* Create a function `audit_agent(score: int, min_score: int)`. If the score is below the minimum, print: "Agent rejected. Re-training required." If above, print: "Agent certified for deployment."

## Knowledge Check – MCQs
1. **What is 'Faithfulness' in RAG evaluation?**
   - A) Whether the agent is nice to the user.
   - B) Whether the answer is derived purely from the retrieved context.
   - C) Whether the agent uses the same words as the user.
2. **What is a 'Golden Dataset'?**
   - A) A dataset that cost a lot of money to buy.
   - B) A collection of verified queries and their perfect ground-truth answers.
   - C) A dataset stored in an expensive database.

---
**© 2026 APT Computing Labs** – Apache License 2.0

<ModuleCompletion moduleId="6-reliability" :xpValue="100" />
