async def start_docker_container(docker):
    '''
    This function will start the docker container.
    '''
    print("Starting Docker container...")
    await docker.start()

async def stop_docker_container(docker):
    '''
    This function will stop the docker container.
    '''
    print("Stopping Docker container...")
    await docker.start()
    print("Docker Container stopped!")
