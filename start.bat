@echo off
REM start.bat - Start the Agentic AI Mastery Portal Locally on Windows

echo 🚀 Starting Agentic AI Mastery Portal...

IF NOT EXIST node_modules (
    echo 📦 node_modules not found. Installing dependencies first...
    npm install
)

REM Run the VitePress dev server
npm run docs:dev
