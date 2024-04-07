import subprocess

def execute_fabric_command(command):
    # Construct the WSL command
    wsl_command = ['wsl', 'fabric', command]  

    # Execute the command
    result = subprocess.run(wsl_command, capture_output=True, text=True)

    # Handle output
    if result.returncode == 0:
        print("Fabric command executed successfully:")
        print(result.stdout)
    else:
        print("Fabric command execution failed:")
        print(result.stderr)

# Example usage
execute_fabric_command("<your Fabric AI command here>") 
