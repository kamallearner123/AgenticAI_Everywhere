#!/bin/bash
# start.sh - Start the Agentic AI Mastery Portal Locally

echo "🚀 Starting Agentic AI Mastery Portal..."

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "📦 node_modules not found. Installing dependencies first..."
    npm install
fi

# Run the VitePress dev server
npm run docs:dev
