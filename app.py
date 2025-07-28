import streamlit as st
import asyncio
from team.dsa_team import get_dsa_team
from config.docker_utils import start_docker_container, stop_docker_container
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult


st.title("AlgoGenius - The DSA Problem Solver Agent")
st.write("Welcome to AlgoGenius, your personal DSA problem solver! Here you can ask for solutions to various data structures and algorithm problems.")

task = st.text_input(task="Enter your DSA problem or question:", value="Write a function to add two numbers...")

async def run(team, docker, task):

    try:
        await start_docker_container(docker)

        async for message in team.run_stream(task=task):
            if isinstance(message, TextMessage):
                print(msg:=f"**{message.source}**: {message.content}")
                yield msg
            elif isinstance(message, TaskResult):
                print(msg:=f"**Stop Reason**: {message.stop_reason}")
                yield msg
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await stop_docker_container(docker)

if st.button("Run"):
    st.write("Thinking...")
    team, docker = get_dsa_team()

    async def collect_messages():
        async for msg in run(team, docker, task):
            if isinstance(msg, str):
                if msg.startswith("User"):
                    with st.chat_message('User', avatar='🧑‍💻'):
                        st.markdown(msg)
                elif msg.startswith("DSA_Problem_Solver_Agent") or msg.startswith("Code_Executor_Agent"):
                    with st.chat_message('Assistant', avatar='🤖'):
                        st.markdown(msg)
            elif isinstance(msg, TaskResult):
                with st.chat_message('Stopper', avatar='🛑'):
                    st.markdown(f"Task Completed: {msg.result}")
    
asyncio.run(collect_messages())





    

