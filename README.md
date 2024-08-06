# AskTheLabPI: Your Voice-Controlled Lab Assistant on Raspberry Pi

AskTheLabPI is a voice-controlled question-answering system designed to provide hands-free assistance in a lab setting. Built on a Raspberry Pi, this project leverages the power of natural language processing (NLP) and speech recognition to answer your lab-related queries. Ask questions from lab manuals or instructions, and AskTheLabPI will find the answers for you, making your lab experience smoother and more efficient.

## Features

* **Voice Interaction:** Ask questions naturally using your voice, thanks to the integrated speech recognition.
* **Document-Based Q&A:**  AskTheLabPI can be loaded with specific lab manuals, instructions, or any PDF document relevant to your work.
* **Retrieval Augmented Generation (RAG):** Utilizes advanced NLP techniques (LangChain, OpenAI embeddings, ChromaDB) for accurate information retrieval and question answering.
* **Raspberry Pi Integration:** Designed to run on a Raspberry Pi, enabling a compact and portable lab assistant solution.
* **Interactive Feedback:** Provides clear audio responses and uses an LCD display for visual feedback during interactions. 
* **Hardware Buttons:** Offers a user-friendly interface with buttons for triggering voice input, repeating responses, and more.

## How it Works

1. **Voice Input:** Speak your question clearly when prompted by the system.
2. **Speech Recognition:**  The Raspberry Pi uses speech recognition to convert your spoken words into text. 
3. **Question Processing:**  The text is processed and sent to the NLP engine (powered by OpenAI's language model and LangChain).
4. **Information Retrieval:**  The system searches the loaded lab manuals or documents for relevant information using ChromaDB as a vector database. 
5. **Answer Generation:**  An answer is generated based on the retrieved information and presented through both text-to-speech (audio) and on the LCD display.

## Getting Started

### Prerequisites

* **Hardware:**
    * Raspberry Pi (Model 3 or above recommended)
    * USB Microphone
    * I2C LCD Display
    * 3 Buttons
    * Jumper Wires
* **Software:**
    * Raspberry Pi OS (with desktop recommended for easier setup)
    * Python 3.7 or higher

### Installation

1. **Clone the Repository:** `git clone https://github.com/your-username/AskTheLabPI.git`
2. **Navigate to the project directory:**  `cd AskTheLabPI`
3. **Install Dependencies:** `pip install -r requirements.txt`
4. **Configure OpenAI API Key:**
    * Create an account on [https://platform.openai.com/](https://platform.openai.com/) and obtain an API key.
    * Set the API key as an environment variable: Enter the key in the `.env` file
5. **Load your Lab Manuals:**
   * Place your lab manuals (in PDF format) in the project directory.
   * Update the filename in `lab_qa.py` (`ldr = PyPDFLoader("your_lab_manual.pdf")`) to point to your document.

### Running the Application

1. Run the main script: `python lab_assistant.py`
2. Follow the on-screen prompts and use the buttons to interact:
    * **Button 1:**  Press to start speaking your question.
    * **Button 2:**  Repeats the last answer.
    * **Button 3:**  Repeats the last question you asked. 

## Customization

* **Hardware Setup:** Adjust the GPIO pin assignments in `lab_assistant.py` according to your button and LCD connections.
* **Lab Documents:**  Easily switch to different lab manuals by updating the filename in `lab_qa.py`. 
