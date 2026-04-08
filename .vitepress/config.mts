import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "Agentic AI Mastery",
  description: "Gamified Learning Portal for Agentic AI",
  themeConfig: {
    logo: '/logo.png', // Placeholder
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Syllabus', link: '/modules/index' }
    ],
    sidebar: [
      {
        text: 'Module 1: Foundations',
        items: [
          { text: 'Python Essentials', link: '/modules/1-foundations/python-essentials' },
          { text: 'Async Programming', link: '/modules/1-foundations/async-programming' },
          { text: 'REST APIs & JSON', link: '/modules/1-foundations/rest-apis' },
          { text: 'Linux for AI Engineers', link: '/modules/1-foundations/linux-basics' },
          { text: 'Data Handling', link: '/modules/1-foundations/data-handling' }
        ]
      },
      {
        text: 'Module 2: LLM Core Concepts',
        items: [
          { text: 'LLM Fundamentals', link: '/modules/2-llm-core/llm-fundamentals' },
          { text: 'Prompt Engineering', link: '/modules/2-llm-core/prompt-engineering' }
        ]
      },
      {
        text: 'Module 3: Building Intelligent Agents',
        items: [
          { text: 'Tool & Function Calling', link: '/modules/3-agents/tool-calling' },
          { text: 'Agent Architecture', link: '/modules/3-agents/architecture' },
          { text: 'Memory Systems', link: '/modules/3-agents/memory' }
        ]
      },
      {
        text: 'Module 4: Retrieval Systems',
        items: [
          { text: 'RAG Fundamentals', link: '/modules/4-rag/rag-fundamentals' }
        ]
      },
      {
        text: 'Module 5: Advanced Automation',
        items: [
          { text: 'Workflow Automation', link: '/modules/5-automation/workflows' },
          { text: 'Multi-Agent Systems', link: '/modules/5-automation/multi-agent' }
        ]
      },
      {
        text: 'Module 6: Production & Security',
        items: [
          { text: 'Evaluation & Reliability', link: '/modules/6-production/reliability' },
          { text: 'Deployment', link: '/modules/6-production/deployment' },
          { text: 'Security & Governance', link: '/modules/6-production/security' },
          { text: 'Observability', link: '/modules/6-production/observability' },
          { text: 'Frameworks Deep Dive', link: '/modules/6-production/frameworks' }
        ]
      }
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/kamal/GoogleAgenticAICourse' }
    ],
    footer: {
      message: 'Found a bug? [Raise an Issue](https://github.com/kamallearner123/AgenticAI_Everywhere/issues/new/choose)',
      copyright: 'Copyright © 2026 APT Computing Labs'
    }
  },
  appearance: 'dark', // Force dark mode for premium feel
  markdown: {
    lineNumbers: true,
    mermaid: true // Enable mermaid diagrams
  }
})
