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

This project uses `uv` for dependency management. If you don't have `uv` installed, follow the instructions [here](https://docs.astral.sh/uv/guides/install-python/).

1. **Setup**:

   ```bash
   git clone <your-repo-url>
   cd crm-agent
   uv sync  # Install dependencies
   ```

2. **Configure environment**:

   ```bash
   cp .env.example .env
   # Edit .env with your OpenAI API key and Supabase URI
   ```

3. **Setup database** (create free Supabase account at [supabase.com](https://supabase.com)):

   - Create a new Supabase project. Use the generate_password feature to generate a secure password, copy it into the .env file for use later.
   - Copy the connection string from the Supabase project settings and paste it into the .env file (you'll see a 'connect' button at the top of the dashboard), replacing the placeholder with the actual connection string.
   - Replace the password placeholder with the password you generated earlier.
   - Copy and paste the sql from `db/migration-create-tables.sql` into the Supabase SQL editor. This will automatically create all of the db tables for you.
   - Import each CSV file from the `data` directory into the corresponding table in Supabase.

4. **Verify and run**:
   ```bash
   cd frontend && uv run python chat_local.py  # Start chatting with Ralph!
   ```

## 🎮 Running the Application

### Start the Chat Interface

```bash
cd frontend
uv run python chat_local.py
```

You should see Ralph introduce himself:

```
---- 🤖 Assistant ----

Hi there! I'm Ralph, your customer service agent and marketing expert. I'm here to help you understand your customers better and create targeted marketing campaigns that drive results.

I have access to your CRM database with customer information, transaction history, and RFM analysis. I can help you:

🎯 Analyze customer behavior and segments
📧 Create personalized marketing campaigns
📊 Generate insights from your customer data
✉️ Send targeted emails to specific customer groups

What would you like to work on today?
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
