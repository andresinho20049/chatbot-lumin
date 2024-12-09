#!/bin/bash

# Start Ollama in the background.
/bin/ollama serve &
# Record Process ID.
pid=$!

# Pause for Ollama to start.
sleep 5

echo "🔴 Retrieve Lumin model..."
ollama pull andresinho20049/lumin
echo "🟢 Done!"

# Wait for Ollama process to finish.
wait $pid