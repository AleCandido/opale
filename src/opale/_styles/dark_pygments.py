from pygments.style import Style
from pygments.token import (
    Text,
    Keyword,
    Name,
    Comment,
    String,
    Error,
    Number,
    Operator,
    Generic,
    Whitespace,
    Punctuation,
    Other,
    Literal,
)


# Originally based on FlaskyStyle which was based on 'tango'.
class Dark(Style):
    background_color = "#0a0c0f"  # doesn't seem to override CSS 'pre' styling?
    border_color = "#434c5e"
    default_style = ""

    styles = {
        # No corresponding class for the following:
        Text: "#7b869d",  # class:  ''
        Whitespace: "underline #7b869d",  # class: 'w'
        Error: "#7b869d",  # class: 'err'
        Other: "#7b869d",  # class 'x'
        Comment: "italic #7b869d",  # class: 'c'
        Comment.Preproc: "noitalic",  # class: 'cp'
        Keyword: "bold #7b869d",  # class: 'k'
        Keyword.Constant: "bold #7b869d",  # class: 'kc'
        Keyword.Declaration: "bold #7b869d",  # class: 'kd'
        Keyword.Namespace: "bold #7b869d",  # class: 'kn'
        Keyword.Pseudo: "bold #7b869d",  # class: 'kp'
        Keyword.Reserved: "bold #7b869d",  # class: 'kr'
        Keyword.Type: "bold #7b869d",  # class: 'kt'
        Operator: "#7b869d",  # class: 'o'
        Operator.Word: "bold #7b869d",  # class: 'ow' - like keywords
        Punctuation: "#7b869d",  # class: 'p'
        # because special names such as Name.Class, Name.Function, etc.
        # are not recognized as such later in the parsing, we choose them
        # to look the same as ordinary variables.
        Name: "#7b869d",  # class: 'n'
        Name.Attribute: "#7b869d",  # class: 'na' - to be revised
        Name.Builtin: "#7b869d",  # class: 'nb'
        Name.Builtin.Pseudo: "#7b869d",  # class: 'bp'
        Name.Class: "#7b869d",  # class: 'nc' - to be revised
        Name.Constant: "#7b869d",  # class: 'no' - to be revised
        Name.Decorator: "#7b869d",  # class: 'nd' - to be revised
        Name.Entity: "#7b869d",  # class: 'ni'
        Name.Exception: "bold #7b869d",  # class: 'ne'
        Name.Function: "#7b869d",  # class: 'nf'
        Name.Property: "#7b869d",  # class: 'py'
        Name.Label: "#7b869d",  # class: 'nl'
        Name.Namespace: "#7b869d",  # class: 'nn' - to be revised
        Name.Other: "#7b869d",  # class: 'nx'
        Name.Tag: "bold #7b869d",  # class: 'nt' - like a keyword
        Name.Variable: "#7b869d",  # class: 'nv' - to be revised
        Name.Variable.Class: "#7b869d",  # class: 'vc' - to be revised
        Name.Variable.Global: "#7b869d",  # class: 'vg' - to be revised
        Name.Variable.Instance: "#7b869d",  # class: 'vi' - to be revised
        Number: "#7b869d",  # class: 'm'
        Literal: "#7b869d",  # class: 'l'
        Literal.Date: "#7b869d",  # class: 'ld'
        String: "#7b869d",  # class: 's'
        String.Backtick: "#7b869d",  # class: 'sb'
        String.Char: "#7b869d",  # class: 'sc'
        String.Doc: "italic #7b869d",  # class: 'sd' - like a comment
        String.Double: "#7b869d",  # class: 's2'
        String.Escape: "#7b869d",  # class: 'se'
        String.Heredoc: "#7b869d",  # class: 'sh'
        String.Interpol: "#7b869d",  # class: 'si'
        String.Other: "#7b869d",  # class: 'sx'
        String.Regex: "#7b869d",  # class: 'sr'
        String.Single: "#7b869d",  # class: 's1'
        String.Symbol: "#7b869d",  # class: 'ss'
        Generic: "#7b869d",  # class: 'g'
        Generic.Deleted: "#7b869d",  # class: 'gd'
        Generic.Emph: "italic #7b869d",  # class: 'ge'
        Generic.Error: "#7b869d",  # class: 'gr'
        Generic.Heading: "bold #7b869d",  # class: 'gh'
        Generic.Inserted: "#7b869d",  # class: 'gi'
        Generic.Output: "#7b869d",  # class: 'go'
        Generic.Prompt: "#7b869d",  # class: 'gp'
        Generic.Strong: "bold #7b869d",  # class: 'gs'
        Generic.Subheading: "bold #7b869d",  # class: 'gu'
        Generic.Traceback: "bold #7b869d",  # class: 'gt'
    }
