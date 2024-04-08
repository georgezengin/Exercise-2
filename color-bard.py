import sys

class Color:
    """
    A class representing an ANSI color.

    Attributes:
        foreground: The foreground color.
        background: The background color.
        attrs: The attributes.
    """

    def __init__(self, foreground, background, attrs=None):
        """
        Initialize a Color object.

        Args:
            foreground: The foreground color.
            background: The background color.
            attrs: The attributes.
        """
        self.foreground = foreground
        self.background = background
        self.attrs = attrs or []

    def __repr__(self):
        """
        Represent the Color object as a string.

        Returns:
            A string representing the Color object.
        """
        return "Color(foreground=%s, background=%s, attrs=%s)" % (self.foreground, self.background, self.attrs)

    def __str__(self):
        """
        Render the Color object as ANSI escape codes.

        Returns:
            A string containing ANSI escape codes that render the Color object.
        """
        attrs = "".join(["\x1b[%sm" % attr for attr in self.attrs])
        fg = "\x1b[%dm" % self.foreground
        bg = "\x1b[%dm" % self.background
        return attrs + fg + bg + sys.stdout.buffer.write

def print_color(text, color):
    """
    Print the text in the specified color.

    Args:
        text: The text to print.
        color: The Color object representing the color to print the text in.
    """
    color.__str__()
    sys.stdout.buffer.write(text)

red = Color("red")
blue = Color("blue", "yellow")
bold = Color(attrs=["bold"])

print("This is red text.")
print_color("This is blue text.", blue)
print_color("This is bold red text.", red, bold)