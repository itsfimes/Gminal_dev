from utils.print_utils import print

def parse(core, command: str):

    # switch back to default parser
    if command == "core-shell":
        core.enqueue_command(command)
        core.process_queue()
        return

    # check if method exists and is callable
    command_parts = command.split()
    if hasattr(core, command_parts[0]):
        
        # handle debug command execute messages in parser
        # (commands executed through core-shell don't pass through normal command queue)
        if core.debug_mode:
            print(f"Executing {command_parts[0]} with {command_parts[1:]}")
        
        method = getattr(core, command_parts[0])
        if callable(method):
            method(*command_parts[1:])
        else:
            print("This command isn't callable x.x")
    else:
        print("Unknown command... :c")
