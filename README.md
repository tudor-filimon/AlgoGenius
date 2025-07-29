# 🤖 DSA Assistant

Welcome to my first team in my journey to learn Microsoft AutoGen! I was inspired to start this project while starting off my Leetcode DSA-style problem solving journey to have an assistant to help me along my journey :)


https://github.com/user-attachments/assets/6bdccc3e-84c0-451c-bf12-386c271cba8a



## 🎯 What I Learned

- Built an AI agent using **MicrosoftAutogen** and **OpenAI**
- Implement a code executor agent using **Docker** to ensure accuracy of the generated solution
- Created a **Round Robin** style team for continuous feedback for the solution
- Implemented a lightweight frontend interface using **Streamlit** for the ease of interacting with AI apps

## Next Steps
- Use **Model Context Protocol (MCP)** for tool integration to fetch data from Leetcode for enhanced user interaction
- Include **Human In the Loop** interactions for question/constraint clarification

## 🏗️ Project Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────────┐    ┌───────────────────────┐
│   Frontend      │    │ RoundRobinTeam  │    │ Problem Solver Agent│    │  Code Executor Agent  │
│   (Chat UI)     │◄──►│   (AutoGen)     │◄──►│       (OpenAI)      │◄──►│        (Docker)       │
└─────────────────┘    └─────────────────┘    └─────────────────────┘    └───────────────────────┘
                                                        │ Coming Soon
                                                        ▼
                                               ┌─────────────────┐
                                               │  MCP LeetCode   │
                                               │     Server      │
                                               └─────────────────┘
```

## 🚀 Features

- **🧠 Intelligent Problem Solving**: our problem solver agent will craft an all around answer to your questions after refined prompt engineering
- **💻 External Code Execution**: to validate your assistant's solution, another agent will run its proposed code in an external Docker container and provide feedback while working in a team

## 📋 Technologies Used

- **Python 3.12+**
- **Microsoft AutoGen** database (Supabase integration)
- **OpenAI**
- **Streamlit**
- **Docker Extension**

## ⚡ Quick Start

Want to get started immediately? Here's the fastest path:

This project uses `pip` for dependency management. If you don't have `pip` installed, follow the instructions [here](https://pip.pypa.io/en/stable/installation/).

### Start the Chat Interface

```bash
pip install -r requirements.txt
python3 run app.py
```

### Example Interactions

Try these commands to see Ralph in action:

1. **Simple Example**:

   ```
   "Write me a function that will add two numbers."
   ```

2. **Leetcode Problem 20**:

   ```
   "Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type."
   ```

## 📚 Learning Resources I Used and Key Concepts Covered

- **Microsoft AutoGen**: Framework for building teams of AI agents
- **MCP (Model Context Protocol)**: Standard for AI tool integration

- [LangGraph Documentation](https://microsoft.github.io/autogen/stable//index.html)
- [Model Context Protocol](https://modelcontextprotocol.io/)

## 🤝 Contributing

This is a personal project, but contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request
