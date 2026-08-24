# Can be changed to your likings:)
# Note that this file was created to a huge portion by ai.

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m' 
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
LIGHT_GRAY = '\033[37m'
DARK_GRAY = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
WHITE = '\033[97m'

RESET = '\033[0m'

# Tokyo Night palette (24-bit ANSI colors)
TOKYO_RED = '\033[38;2;247;118;142m'
TOKYO_GREEN = '\033[38;2;158;206;106m'
TOKYO_YELLOW = '\033[38;2;224;175;104m'
TOKYO_BLUE = '\033[38;2;122;162;247m'
TOKYO_MAGENTA = '\033[38;2;187;154;247m'
TOKYO_CYAN = '\033[38;2;125;207;255m'
TOKYO_DARK_GRAY = '\033[38;2;86;95;137m'


def set_theme(theme_name):
    """Set the semantic colors used by EDMD."""
    global LOGO_COLOR, PROMPT_COLOR, LINE_NUMBER_COLOR, COMMAND_COLOR
    global INFO_COLOR, SUCCESS_COLOR, WARNING_COLOR, ERROR_COLOR

    if theme_name == "default":
        # Grunddesign: normale Terminalfarben
        LOGO_COLOR = CYAN
        PROMPT_COLOR = BLUE
        LINE_NUMBER_COLOR = LIGHT_GRAY
        COMMAND_COLOR = MAGENTA

        # Rückmeldungen
        INFO_COLOR = CYAN
        SUCCESS_COLOR = GREEN
        WARNING_COLOR = YELLOW
        ERROR_COLOR = RED
        # Markdown-Vorschau (aktuell nicht in main.py genutzt)
        # HEADING_COLOR = BRIGHT_CYAN
        # LINK_COLOR = BRIGHT_BLUE
        # CODE_COLOR = BRIGHT_MAGENTA
        # QUOTE_COLOR = DARK_GRAY
        # LIST_MARKER_COLOR = BLUE

    elif theme_name == "tokyo-night":
        # Grunddesign: Tokyo Night colors
        LOGO_COLOR = TOKYO_CYAN
        PROMPT_COLOR = TOKYO_BLUE
        LINE_NUMBER_COLOR = TOKYO_DARK_GRAY
        COMMAND_COLOR = TOKYO_MAGENTA

        # Rückmeldungen
        INFO_COLOR = TOKYO_CYAN
        SUCCESS_COLOR = TOKYO_GREEN
        WARNING_COLOR = TOKYO_YELLOW
        ERROR_COLOR = TOKYO_RED

        # Markdown-Vorschau (aktuell nicht in main.py genutzt)
        # HEADING_COLOR = TOKYO_CYAN
        # LINK_COLOR = TOKYO_BLUE
        # CODE_COLOR = TOKYO_MAGENTA
        # QUOTE_COLOR = TOKYO_DARK_GRAY
        # LIST_MARKER_COLOR = TOKYO_BLUE

    else:
        raise ValueError(f"Unknown theme: {theme_name}")


# Fallback when colors.py is imported on its own.
set_theme("default")
