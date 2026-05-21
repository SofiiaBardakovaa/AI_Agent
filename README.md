# AI Study Assistant Agent

## Overview

AI Study Assistant Agent is a Python-based AI assistant that combines the Gemini API with external tools to help users solve educational and informational tasks.

The system demonstrates an agent-based workflow where an intelligent assistant analyzes user requests, selects appropriate tools, processes data, and generates natural language responses.

---

## Features

* AI-powered educational assistant
* Gemini API integration
* Mathematical calculations
* File reading and summarization
* Educational search functionality
* Structured response generation
* Error handling and validation
* Modular project architecture
* Testing support

---

## System Architecture

The project is organized into several modules:

```text
AI_Agent/
│
├── agent/
│   └── assistant_agent.py
│
├── tools/
│   ├── calculator_tool.py
│   ├── file_reader_tool.py
│   └── search_tool.py
│
├── tests/
│   └── test_agent.py
│
├── data/
│   └── notes.txt
│
├── .env
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python
* Gemini API
* Object-Oriented Programming (OOP)
* dotenv
* unittest / pytest
* Git & GitHub

---

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root directory:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## Running the Application

Run the assistant using:

```bash
python main.py
```

---

## Example Commands

### Calculator Tool

```text
calculate 25 * 8
```

### Search Tool

```text
search python
```

### File Reader Tool

```text
read file data/notes.txt
```

### General AI Request

```text
Explain what artificial intelligence is
```

---

## Tool Integration

The system integrates external tools into the AI workflow:

### Calculator Tool

Performs mathematical calculations and sends the result to Gemini for explanation.

### File Reader Tool

Reads local text files and sends their contents to Gemini for summarization.

### Search Tool

Retrieves educational information and passes it to Gemini for detailed explanation generation.

---

## Testing

Testing includes:

* functional testing,
* tool testing,
* input validation,
* error handling verification.

Example test execution:

```bash
python -m unittest discover tests
```

---

## Deployment Preparation

The system is prepared for local deployment as a command-line application.

Deployment preparation includes:

* dependency management,
* environment variable configuration,
* startup instructions,
* modular project structure,
* and GitHub version control.

---

## Security

API keys are stored securely using environment variables and excluded from version control through `.gitignore`.

---

## Future Improvements

Possible future extensions:

* web application deployment,
* database integration,
* real web search support,
* multi-agent workflow,
* Docker containerization,
* cloud deployment.

---

## Author

Developed by Sofiia Bardakova as part of a university AI Agent software engineering project.
