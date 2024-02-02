# if models folder does not exist, create it

if [ ! -d "models" ]; then
  mkdir models
fi

# download the model
if [ ! -f "models/luna-ai-llama2" ]; then
    echo "Downloading Luna AI Llama2..."
    wget https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GGUF/resolve/main/luna-ai-llama2-uncensored.Q4_0.gguf -O models/luna-ai-llama2
    echo "Done"
fi

# TheBloke/phi-2-GGUF
if [ ! -f "models/phi-2" ]; then
    echo "Downloading Phi 2..."
    wget https://huggingface.co/TheBloke/phi-2-GGUF/resolve/main/phi-2.Q4_0.gguf -O models/phi-2
    echo "Done"
fi


