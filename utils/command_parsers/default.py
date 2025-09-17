# Gminal's default command parser :3
import re

def split_command(command: str):
    # this regex matches either quoted text or non-space text
    pattern = r'''("[^"]*"|'[^']*'|\S+)'''
    return re.findall(pattern, command)

def parse(core, user_input):
        command_parts = split_command(user_input)
        if command_parts:
            command_name = command_parts[0]
            args = command_parts[1:]
             
            # Enqueue and process the command using core
            core.enqueue_command(command_name, *args)
            core.process_queue()  # Immediatelly process the queue :3
            
            # if command_name == "core-shell": 
                        # user_input = ""
                        # command_parts= ""
