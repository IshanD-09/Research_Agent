# Research_Agent

## Introduction
This project is an attempt to simplify the research process through summarization by LLMs.
My main goal was to explore agentic ai and its potential usecases.
This project was also used for Science Fair.

## Requirements
In addition to the requirements.txt, you'll need some more things:

1. Ollama. You'll need to install ollama and pull the models: llama3.2 and nomic-text-embeds. When you want to use the code, run ollama serve in a terminal window. I'm currently using Ollama 0.5.12, not sure if that will make a difference.
2. Best performance. Keep your computer on best performance because your computer needs to be able to use your hardware to its full extent. Embarrassingly, it took me a while to understand that this was a problem for me.
3. Hardware. I'm using a Snapdragon X-11 Elite and it's running quite smoothly. I would recommend a gpu if you'd like to use a larger model.

## Conclusion
When you want to run the code, just run the app.py file and have ollama serve running in the background
Overall, I believe this project could use a lot of work. The papers it retrieves from arxiv are often not super relavant to the prompt, and I could also play around with temperature, chunking methods, and models more to make the results better. That being said, if this helps you, that's pretty cool.
