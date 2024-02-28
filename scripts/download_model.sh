# if models folder does not exist, create it
if [ ! -d "models" ]; then
  mkdir models
fi

if [ ! -f "models/phi-2" ]; then
    echo "Downloading Phi 2..."
    curl -L -o ./models/phi-2 https://huggingface.co/TheBloke/phi-2-GGUF/resolve/main/phi-2.Q4_0.gguf
    echo "Done"
fi

