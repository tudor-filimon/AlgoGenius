from agents.problem_solver_agent import get_problem_solver_agent
from agents.code_executor_agent import get_code_executor_agent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from config.constants import TEXT_MENTION, MAX_TURNS

async def get_dsa_team():
    # Load in agents
    problem_solver_agent = get_problem_solver_agent()
    code_executor_agent, docker = get_code_executor_agent()

    # Termination Condition
    termination_condition = TextMentionTermination(TEXT_MENTION)

    team = RoundRobinGroupChat(
        participants=[problem_solver_agent, code_executor_agent],
        termination_condition=termination_condition,
        max_turns=MAX_TURNS
    )

    return team, docker