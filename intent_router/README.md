
# LLM Prompt Router for Intent Classification

## Overview

This project implements an **LLM-powered prompt routing system** that detects a user's intent and routes the request to a specialized expert prompt.

Instead of using a single large prompt for all tasks, the system first **classifies the user's intent** and then **delegates the request to an appropriate expert persona**.

This improves response accuracy and allows the AI to behave like different specialists such as:

* Software Engineer
* Data Analyst
* Writing Coach
* Career Advisor

---

# Architecture

The system follows a **two-step AI workflow**:

```
User Message
      ↓
Intent Classifier (LLM Call 1)
      ↓
Detected Intent + Confidence
      ↓
Prompt Router
      ↓
Expert Persona Prompt
      ↓
LLM Response Generator (LLM Call 2)
      ↓
Final Response
      ↓
Request Logging
```

---

# Supported Intents

The classifier identifies the following intents:

| Intent  | Expert Role                |
| ------- | -------------------------- |
| code    | Software Engineer          |
| data    | Data Analyst               |
| writing | Writing Coach              |
| career  | Career Advisor             |
| unclear | Ask user for clarification |

---

# Project Structure

```
intent_router/
│
├── app.py           # Main application loop
├── classifier.py    # Detects user intent using an LLM
├── router.py        # Routes request to expert prompt
├── prompts.py       # Stores expert system prompts
├── logger.py        # Logs all requests
├── route_log.jsonl  # JSON log file
└── README.md
```

---

# How It Works

### 1️⃣ Intent Classification

The system first calls an LLM to classify the user's intent.

Example output:

```json
{
 "intent": "code",
 "confidence": 0.95
}
```

---

### 2️⃣ Prompt Routing

Based on the detected intent, the system selects the appropriate **expert prompt**.

Example:

```
Intent: code
↓
Use Code Expert Prompt
```

---

### 3️⃣ Response Generation

A second LLM call generates the final response using the selected expert persona.

---

### 4️⃣ Logging

Each request is logged in `route_log.jsonl`.

Example log entry:

```json
{
 "intent": "code",
 "confidence": 0.95,
 "message": "how do i sort a list in python",
 "response": "Use Python's sorted() function..."
}
```

---

# Installation

### 1️⃣ Clone the repository

```
git clone <repository_url>
cd intent_router
```

---

### 2️⃣ Install dependencies

```
pip install groq
```

---

### 3️⃣ Set the API key

In VS Code terminal (PowerShell):

```
$env:GROQ_API_KEY="your_api_key_here"
```

---

# Running the Application

Start the program with:

```
python app.py
```

Example interaction:

```
Enter message: how do i sort a list in python

Detected Intent: code
Confidence: 0.95

Response:
Use Python's sorted() function...
```

---

# Manual Intent Override (Optional Feature)

Users can manually specify intent using prefixes:

| Prefix   | Intent         |
| -------- | -------------- |
| @code    | Code expert    |
| @data    | Data analysis  |
| @writing | Writing coach  |
| @career  | Career advisor |

Example:

```
@code fix this bug: for i in range(10) print(i)
```

---

# Example Test Inputs

```
how do i sort a list in python
explain this sql query
my boss says my writing is too verbose
i am preparing for a job interview
what is the average of 12,45,23,67
help me make this better
```

---

# Key Features

* LLM-powered intent classification
* Prompt routing architecture
* Multiple expert personas
* Confidence threshold handling
* Request logging
* CLI-based interaction
* Manual intent override

---

# Technologies Used

* Python
* Groq API
* Llama 3.1 LLM
* JSON logging

---

