import re

def split_command_parts(command: str):
    # Matches quoted text or unquoted non-space text
    pattern = r'''("[^"]*"|'[^']*'|\S+)'''
    return re.findall(pattern, command)

def split_commands(command_line: str):
    # This regex splits by && only if it's not inside quotes
    # Explanation:
    #   - ("[^"]*"|'[^']*') matches quotes and ignores them
    #   - | matches literal && outside quotes
    #   - uses lookahead/lookbehind to split correctly
    pattern = r'''(?:[^"&']+|"[^"]*"|'[^']*')+'''
    matches = re.findall(pattern, command_line)
    # Clean whitespace and ignore empty strings
    return [m.strip() for m in matches if m.strip()]

def _parse(command_line: str) -> dict[str, list[str]]:
    result = {}
    commands = split_commands(command_line)
    for cmd in commands:
        parts = split_command_parts(cmd)
        if parts:
            name = parts[0]
            # args = [p.strip('"').strip("'") for p in parts[1:]]  # remove quotes
            result[name] = parts[1:]
    return result

def parse(core, user_input):
    commands = _parse(user_input)
    for name, args in commands.items():
        core.enqueue_command(name, *args)
    core.process_queue()  # process immediately :3
