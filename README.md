# Depression Detection Model

This repository contains an AI model for depression detection through audio analysis.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.12 or higher
- pip (Python package installer)
- Git

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/QinWenYan1/depression-detection-model.git
   cd depression-detection-model
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Install OpenAI GPT-3.5 Turbo:**

   ```bash
   pip install openai
   ```

## Setting Up Environment Variables

To use the OpenAI API, you need to set your API key as an environment variable.

### macOS/Linux

1. **Open Terminal**

2. **Set the Environment Variable Temporarily:**

   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

3. **Set the Environment Variable Permanently:**

   Add the export command to your shell configuration file (e.g., `~/.bashrc`, `~/.zshrc`):

   ```bash
   echo 'export OPENAI_API_KEY="your-api-key-here"' >> ~/.bashrc
   # or for zsh
   echo 'export OPENAI_API_KEY="your-api-key-here"' >> ~/.zshrc
   ```

4. **Reload the Configuration:**

   ```bash
   source ~/.bashrc
   # or for zsh
   source ~/.zshrc
   ```

### Windows

1. **Open Command Prompt or PowerShell**

2. **Set the Environment Variable Temporarily:**

   ```cmd
   set OPENAI_API_KEY=your-api-key-here
   ```

3. **Set the Environment Variable Permanently:**

   ```cmd
   setx OPENAI_API_KEY "your-api-key-here"
   ```

4. **Restart Command Prompt**

   Close and reopen the Command Prompt to apply the changes.

## Usage

1. **Audio Transcription:**

   ```bash
   python transcribe.py [depression_detection_model/transcripts]
   ```

   This will generate a transcript in the `transcripts` folder.

## Project Structure
```

## Common Issues and Solutions

### Large File Issues
If you encounter GitHub large file issues, make sure to:
1. Not commit the virtual environment (`env/` folder)
2. Use Git LFS for large model files if necessary

### Virtual Environment Issues
If you encounter issues with the virtual environment:
1. Make sure you'\''re using Python 3.12
2. Try removing and recreating the environment:
   ```bash
   rm -rf env/
   python -m venv env
   source env/bin/activate  # or env\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m '\''Add some AmazingFeature'\''`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

[No license so far]

## Contact
Project Link: [https://github.com/QinWenYan1/depression-detection-model](https://github.com/QinWenYan1/depression-detection-model)

# Commit and push the changes
git add README.md
git commit -m "Update README with installation and environment variable instructions"
git push origin main