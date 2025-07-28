from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from config.constants import WORK_DIRECTORY, TIMEOUT

def get_docker_executor():
    '''
    Function to get the Docker command line code executor.
    This executor will run the code in a Docker container.
    '''
    docker_executor = DockerCommandLineCodeExecutor(
        work_dir=WORK_DIRECTORY,
        timeout=TIMEOUT
    )

    return docker_executor