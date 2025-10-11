import utils.command_parsers.default as default_parser  
from utils.datatypes import GminalCoreGresParserDatatype, ParserDatatype
from utils.parser_loader import get_command_parser, get_parser_path
import re


# TODO: Make this a decorator
def ensure_correct_amount_of_empty_args(*args,
                                        treshold: int = 1, 
                                        error_message: str = "Too many non-empty arguments! :c", 
                                        ) -> None:
    
    non_empty_count = sum(bool(arg) for arg in args)
    if non_empty_count > treshold:
        raise ValueError(error_message)


def is_inside_quotes(text: str, substring: str) -> bool:
    # find all quoted segments (single or double)
    pattern = r'(["\'])(?:(?=(\\?))\2.)*?\1'
    for match in re.finditer(pattern, text):
        start, end = match.span()
        if substring in text[start:end]:
            return True
    return False


class GresParser:
    def __init__(self, core: GminalCoreGresParserDatatype) -> None:
        
        self.parser: ParserDatatype = default_parser
        self.default_parser: ParserDatatype = default_parser
        self.core = core

    
    def remove_comments(self, file_path: str = "", text: list[str] = [""]) -> list[str]:
        def _remove(text: list[str]) -> list[str]:
            lines = []
            for item in text:
                if not item.startswith("//") and not is_inside_quotes(item, "//"):
                    lines.append(item.split("//")[0])
            return lines 
        ensure_correct_amount_of_empty_args(file_path, text, error_message="Failed to remove comments: Expected either a file_path or text, not both :p")

        lines: list[str] = []
        
        if file_path != "":
            with open(file_path, "r") as f:
                lines = _remove(f.readlines())
        else:
            lines = _remove(text)

        return lines
    
    def remove_empty_lines(self, text: list[str]) -> list[str]:
        return [line for line in text if line != ""]
    
    def switch_parsers(self, parser_name: str):
        self.parser = get_command_parser(get_parser_path(parser_name), parser_name)

    def execute_commands(self, file_path: str = "", text: list[str] = [], automatically_remove_comments: bool = True) -> None:
        ensure_correct_amount_of_empty_args(file_path, text, error_message="Failed to execute commands: Expected either a file_path or text, not both :c")

        data: list[str] = []
        if text:
            data = text
        else:
            with open(file_path, "r") as f:
                data = f.readlines()

        if automatically_remove_comments and "//" in "".join(data):
            data = self.remove_comments(text=data)
        
        for command in self.remove_empty_lines(data):
            if command.startswith("#!"):
                self.switch_parsers(command.replace(" ", "").split("#!")[1].strip())
            else:
                self.parser.parse(self.core, command)

            
            


 



