from autogen_agentchat.agents import AssistantAgent
from config.settings import get_model_client
from agents.problem_solver_prompt import PROMPT

model_client = get_model_client()

async def get_problem_solver_agent():
    problem_solver_agent = AssistantAgent(
        name="DSA_Problem_Solver_Agent",
        description="An agent that will solve DSA related problems!",
        model_client=model_client,
        system_message=PROMPT
    )

    return problem_solver_agent