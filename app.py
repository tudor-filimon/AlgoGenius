import streamlit as st
import asyncio
from team.dsa_team import get_dsa_team
from config.docker_utils import start_docker_container, stop_docker_container
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult



st.title("AlgoGenius - The DSA Problem Solver Agent")
st.write("Welcome to AlgoGenius, your personal DSA problem solver! Here you can ask for solutions to various data structures and algorithm problems.")

task = st.text_input("Enter your DSA problem or question:")

async def run(team, docker, task):
    
    team, docker = get_dsa_team()
    await start_docker_container(docker)


    async for message in team.run_stream(task=task):
        if isinstance(message, TextMessage):
            st.write(f"**{message.source}**: {message.content}")
        elif isinstance(message, TaskResult):
            st.write(f"**Stop Reason**: {message.content}")
    
    await stop_docker_container(docker)

if st.button("Run"):
    st.write("Thinking...")
    

