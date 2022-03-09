import subprocess as sp

def get_managed_container_list():
    command_output = sp.getoutput("sudo docker container ls")
    containers = []
    print("Managed Containers list\n")
    for line in command_output.splitlines():
        cols = line.split(" ")        
        print(cols)
        if cols[0] != "CONTAINER":
            containers.append(cols[0])
            print(cols[0])
    return containers

def get_running_container_list():
    command_output = sp.getoutput("sudo docker ps -a")
    containers = []
    print("Running Containers list \n")
    for line in command_output.splitlines():
        cols = line.split(" ")                
        if cols[0] != "CONTAINER":
            containers.append(cols[0])
            print(cols[0]," - ",cols[13])
        
    return containers    

def stop_running_container(container_list):
    for container in container_list:
        sp.run(["sudo","docker","stop",container])

def remove_managed_container(container_list):
    for container in container_list:
        sp.run(["sudo", "docker", "container", "rm", container])

if __name__ == "__main__" :
    print("Docker container cleaning started.\n")

    print("Stopping running containers ...\n")
    
    running_ctx = get_running_container_list()
    stop_running_container(running_ctx)

    print("Removing containers ..\n")
    remove_managed_container(running_ctx)
