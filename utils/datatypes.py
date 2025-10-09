# All of the random ahh datatypes for different modules are stored here :3
# if you're a module adding stuff to this file, please add a comment above your datatype with your module name :3
# also pls make sure to not overwrite other datatypes :p

# Class names should follow this format to avoid overwriting:
#   ItemModuleDatatype
# so a gres parser datatype used by the core would be named GresParserCoreDatatype 


from typing import Protocol, Any

# generic
class ParserDatatype(Protocol):
    def parse(self, *args: Any, **kwargs: Any) -> None: ...
# ---------


# core
class GresParserCoreDatatype(Protocol):
    def execute_commands(self, file_path: str, *args, **kwargs) -> None: ...

class HostCoreDatatype(Protocol):
    silent_exit: bool
    # more will be added soon + a less strict structure will be implemented :3
# ---------


# parser_loader
class GminalCoreParserDatatype(Protocol):
    parser_type: str
    command_parser: ParserDatatype
    startingdir: str
# ------------

# gres_parser
class GminalCoreGresParserDatatype(Protocol):
    def enqueue_command(self, *args: Any, **kwargs: Any) -> None: ...
    def process_queue(self) -> None: ...
# -----------
