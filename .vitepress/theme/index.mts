import { Theme } from 'vitepress'
import DefaultTheme from 'vitepress/theme'
import './index.css'
import XpTracker from './components/XpTracker.vue'
import ModuleCompletion from './components/ModuleCompletion.vue'
import Settings from './components/Settings.vue'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    // Register global components
    app.component('XpTracker', XpTracker)
    app.component('ModuleCompletion', ModuleCompletion)
    app.component('Settings', Settings)
  }
} satisfies Theme
