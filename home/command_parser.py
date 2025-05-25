# command_parser.py

import shlex
class Command:
    """
    A structured representation of a user input command.
    """
    def __init__(self, name, args):
        self.name = name
        self.args = args

def parse_command(input_str: str) -> Command:
    """
    Parse a string input into a command name and argument list.
    """
    try:
        tokens = shlex.split(input_str.strip())
        if not tokens:
            raise ValueError("Empty command.")

        cmd = tokens[0]
        args = tokens[1:]

        if cmd in ['+', '-']:
            if len(args) != 2:
                raise ValueError("Usage: + <item_id> <amount> or - <item_id> <amount>")
            return Command(cmd, args)

        return Command(cmd.lower(), args)
    except Exception as e:
        raise ValueError(f"Invalid command format: {e}")
