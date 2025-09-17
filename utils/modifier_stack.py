from collections import deque
from dataclasses import dataclass

@dataclass
class Modifier:
    component: str   # which component manages it
    display_name: str
    id: str          # unique string identifier >w<
    color: str       # color for GUI

class ModifierStack:
    def __init__(self):
        self._stack = deque()

    def activate(self, modifier: Modifier):
        """Activate a modifier (push to top of stack)."""
        # remove old instance if it already exists
        self._stack = deque([m for m in self._stack if m.id != modifier.id])
        self._stack.appendleft(modifier)

    def deactivate(self, modifier_id: str):
        """Deactivate a modifier by ID."""
        self._stack = deque([m for m in self._stack if m.id != modifier_id])

    def __iter__(self):
        """Iterate in most-recently-activated order."""
        return iter(self._stack)

    def get_last_active(self):
        """Get most recently active modifier, or None."""
        return self._stack[0] if self._stack else None

    def is_active(self, modifier_id: str) -> bool:
        return any(m.id == modifier_id for m in self._stack)

