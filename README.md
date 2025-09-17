# Dev version of Gminal
- meowmeowmeowmeow :3
- as of right now the dev version of Gminal(core 2.0) is not officially supported on Python 3.11 and lower. It might work, but I can't guarantee it :c


## Stable releases available here: [Official Gminal Repo](https://www.github.com/ItzFimes/Gminal) :3
 - no core V2 :c

## --Updates!--
### **Beta 0.0.8** - The _things_ update >w<

#### Core and CLI Improvements

* **Enhanced Shell Input:** The shell now features a dynamic input line. It includes the current path and special status indicators for active modes like `debug` or `core-shell`. This is all configurable via a new `shellinput.conf` file.
* **Centralized Parser:** A new `parser_loader` utility dynamically loads command parsers. This allows for centralized parser swithching - making implementing custom parsers easier :3
* **Improved Startup:** The core now includes a `host_running` flag, ensuring all modules and core functionalities are properly initialized before the main command loop begins. 

#### New Commands and Utilities

* **`core-shell`:** A new command that allows direct access to the core's functions. This is useful for development and debugging purposes - and also really fun to mess around with >< (variable modifications coming soon)
* **`sysvar`:** A command that lists all variables stored by Gminal, providing insight into the system's state.
* **`su_manager`:** A new utility for managing superuser permissions and executing commands with `sudo`, including a check for `sudo` access.
* **`modifier_stack`:** A utility for managing and displaying active shell modifiers, such as debug mode. This utilitiy allows modules to easily add custom shell modifiers :3
* **`debug`:** This command now not only switches the debug mode on or off, but also activates and deactivates the new `debugger` utility. The new debugger is integrated directly into Gminal's core - allowing you to see (in realtime) what core functions are being called with what args ><


#### Command and File Changes

* **`cd` command:** The `cd` command is now more flexible, with the ability to handle paths enclosed in single or double quotes.
* **`ls` command:** The `ls` command now includes a message for empty directories and better handles directory arguments.
* **`.gitignore`:** `.vscode` and `shellinput.conf` added to gitignore :p
* **`su` command:** The `su` command now provides a message indicating when it is already running as root.
* **`command_completion`:** The command completion logic was updated to include command matches, file and directory matches, and command history matches. (still kinda sucks tho :c)

#### Internal Refactoring and Bug Fixes

* **`print_utils`:** The `print` utility has been simplified. The `false_condition` argument was removed, and `condition` now controls all conditional printing.
* **`debug.py` and `core.py`:** These files were refactored to incorporate the new `debugger` utility, providing more detailed logging for core functions.
* **`command_parsers`:** A new `command_parsers` directory was created to hold parser modules.
* **Type Hinting:** New type hints were added throughout the codebase to improve readability and maintainability. (- even more will be added in future updates :3)
* **Bug Fixes:** Several minor bugs and inconsistencies were addressed across multiple files, including issues with command execution and error handling ><

- this update will probably make it to the stable release repo soon :3
(also, these repos will get merged in the future ><)


### Beta 0.0.7 - coreV2 migration
- COREV2 :33333
- and uhh stuff idk, the whole codebase was rewritten ><

### Beta 0.0.6  - Current stable release. Check it out [Here!](https://github.com/ItzFimes/Gminal)
- Minor bug fixes
- Optimized dirchck
- Optimized startingdir
- Removed a lot of unnecessary imports
- Removed a lot of time.sleeps
- Optimized basically every function
- Logo drawing is a lot faster
- Fixed an issue where Gminal randomly started running Fore.RESET commands
- Removed some unnecessary code

### Beta 0.0.5
- Redesigned the UI
- Added a few new commands
- Updated the help menu
- Gminal now doesn't need to use the setup-storage command to delete stuff in directories!

