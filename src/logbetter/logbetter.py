import datetime
import sys

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    # fallback if colorama not installed
    class DummyColor:
        RESET_ALL = ''
    Fore = Style = DummyColor()


class LogBetter:
    LEVELS = {
        "DEBUG": {"color": Fore.LIGHTBLACK_EX, "emoji": "🐞"},
        "INFO": {"color": Fore.CYAN, "emoji": "ℹ️"},
        "SUCCESS": {"color": Fore.GREEN, "emoji": "✅"},
        "WARNING": {"color": Fore.YELLOW, "emoji": "⚠️"},
        "ERROR": {"color": Fore.RED, "emoji": "❌"},
        "CRITICAL": {"color": Fore.MAGENTA, "emoji": "🚨"},
    }

    def __init__(self):
        self.show_time = True
        self.time_format = "%Y-%m-%d %H:%M:%S"
        self.template = "{time} | {level} | {message}"
        self.output = sys.stdout

    def _get_time(self):
        return datetime.datetime.now().strftime(self.time_format)

    def _format_message(self, level, message):
        time_str = self._get_time() if self.show_time else ""
        emoji = self.LEVELS[level]["emoji"]
        color = self.LEVELS[level]["color"]
        formatted = self.template.format(
            time=time_str,
            level=f"{emoji} {level}",
            message=message
        )
        return f"{color}{formatted}{Style.RESET_ALL}"

    def _log(self, level, message):
        print(self._format_message(level, message), file=self.output)

    def debug(self, message): self._log("DEBUG", message)
    def info(self, message): self._log("INFO", message)
    def success(self, message): self._log("SUCCESS", message)
    def warning(self, message): self._log("WARNING", message)
    def error(self, message): self._log("ERROR", message)
    def critical(self, message): self._log("CRITICAL", message)

    # Customization methods
    def set_format(self, fmt: str):
        """Customize log message format."""
        self.template = fmt

    def set_time_format(self, fmt: str):
        """Change the timestamp format."""
        self.time_format = fmt

    def disable_time(self):
        """Hide timestamps in logs."""
        self.show_time = False


# Create a single global logger
log = LogBetter()
