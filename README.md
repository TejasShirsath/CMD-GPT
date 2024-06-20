# CMD-GPT

CMD-GPT is a command-line tool leveraging GEMINI AI to generate responses to user commands. It uses the Flask framework to host the GPT model via HTTP, facilitating seamless interaction through Command Prompt and Terminal. This tool provides quick access to AI-generated responses for various queries.

## Table of Contents
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
  - [Using CMD](#1-using-cmd)
  - [Using VS Code Terminal (Windows)](#2-using-vs-code-terminal-windows)
- [Example Queries](#example-queries)

## Installation

1. Clone the repository:
```
git clone https://github.com/TejasShirsath/CMD-GPT.git
cd CMD-GPT
```
   
2. Install the required dependencies:
```
pip install -r requirements.txt
```
## Configuration

1. Add your GEMINI API key in the server.py file:
```
genai.configure(api_key="your_gemini_api_key_here")
```

## Usage
## 1. Using CMD:
Run the server.py file:
```
python server.py
```

Open Command Prompt and type the following command:
```
curl -s http://HOST_ADDRESS_OF_SERVER/?question=YOUR_QUESTION
```
Example:
```
curl -s http://127.0.0.1:5000/?question=writejavacodeforcalculator
```
Note: Do not use white spaces in the URL.
## 2. Using VS Code Terminal (Windows):
i. Run the server.py file:
```
python server.py
```
ii. Open Terminal in VS Code and type the following commands:
```
$content = Invoke-WebRequest -Uri "http://HOST_ADDRESS_OF_SERVER/?question=YOUR_QUESTION"
$content.Content
```
Example:
```
$content = Invoke-WebRequest -Uri "http://127.0.0.1:5000/?question=writejavacodeforcalculator"
$content.Content
```
Note: Do not use white spaces in the URL.
## Example Queries
```
curl -s http://127.0.0.1:5000/?question=write_java_code_for_calculator
```
```  
curl -s http://127.0.0.1:5000/?question=howtomakepasta
```
```
curl -s http://127.0.0.1:5000/?question=what-is-the-capital-of-india
```
