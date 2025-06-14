import subprocess

def run_bash_command(command):
    """
    Executes a bash command and returns its output.
    """
    try:
        # Execute the command
        # 'shell=True' can be a security hazard if the command is constructed from external input.
        # For a fixed command string, it's generally fine.
        # 'capture_output=True' captures stdout and stderr.
        # 'text=True' decodes stdout and stderr as text.
        # 'check=True' will raise a CalledProcessError if the command returns a non-zero exit code.
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        
        # Print stdout
        print(result.stdout)
        
        # Print stderr if any
        if result.stderr:
            print(result.stderr)
            
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(f"Return code: {e.returncode}")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
    except FileNotFoundError:
        print(f"Error: The command '{command.split()[0]}' was not found.")
