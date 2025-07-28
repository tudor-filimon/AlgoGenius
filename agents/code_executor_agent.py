from autogen_agentchat.agents import CodeExecutorAgent
from config.docker_executor import get_docker_executor

async def get_code_executor_agent():
    '''
    Function to get the code executor agent.
    This agent is responsible for executing code snippets.
    It will work in a team with the problem solver agent to execute the code.
    '''
    docker = get_docker_executor()

    code_executor_agent = CodeExecutorAgent(
            name='Code_Executor_Agent',
            code_executor=docker
        )

    return code_executor_agent, docker