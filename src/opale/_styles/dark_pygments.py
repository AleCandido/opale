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
        Text: "#dddee1",  # class:  ''
        Whitespace: "underline #181d25",  # class: 'w'
        Error: "#bf616a",  # class: 'err'
        Other: "",  # class 'x'
        Comment: "italic #424754",  # class: 'c'
        Comment.Hashbang: "#7b869d",  # class: 'ch'
        Comment.Multiline: "",  # class:
        Comment.Preproc: "noitalic #7884a0",  # class: 'cp'
        Comment.PreprocFile: "#9d97c3",  # class: 'cpf'
        Comment.Single: "",  # class: 'cl'
        Comment.Special: "",  # class:
        Keyword: "#5e81ac",  # class: 'k'
        Keyword.Constant: "bold #5e81ac",  # class: 'kc'
        # Keyword.Declaration: "bold #7b869d",  # class: 'kd'
        # Keyword.Namespace: "bold #7b869d",  # class: 'kn'
        # Keyword.Pseudo: "bold #7b869d",  # class: 'kp'
        # Keyword.Reserved: "bold #7b869d",  # class: 'kr'
        # Keyword.Type: "bold #7b869d",  # class: 'kt'
        Literal: "",  # class: 'l'
        Literal.Date: "",  # class: 'ld'
        Name: "",  # class: 'n'
        Name.Attribute: "",  # class: 'na' - to be revised
        Name.Builtin: "italic #81a1c1",  # class: 'nb'
        Name.Builtin.Pseudo: "#5e81ac",  # class: 'bp'
        Name.Class: "#88c0d0",  # class: 'nc' - to be revised
        Name.Constant: "",  # class: 'no' - to be revised
        Name.Decorator: "",  # class: 'nd' - to be revised
        Name.Entity: "",  # class: 'ni'
        Name.Exception: "#bf616a",  # class: 'ne'
        Name.Function: "#88c0d0",  # class: 'nf'
        Name.Property: "",  # class: 'py'
        Name.Label: "",  # class: 'nl'
        Name.Namespace: "",  # class: 'nn' - to be revised
        Name.Other: "",  # class: 'nx'
        Name.Tag: "bold",  # class: 'nt' - like a keyword
        Name.Variable: "",  # class: 'nv' - to be revised
        Name.Variable.Class: "",  # class: 'vc' - to be revised
        Name.Variable.Global: "",  # class: 'vg' - to be revised
        Name.Variable.Instance: "",  # class: 'vi' - to be revised
        Number: "#b48ead",  # class: 'm'
        Number.Float: "#b48ead",  # class: 'mf'
        Operator: "#eaddc8",  # class: 'o'
        Operator.Word: "bold",  # class: 'ow' - like keywords
        Punctuation: "",  # class: 'p'
        String: "#a3be8c",  # class: 's'
        # String.Backtick: "#7b869d",  # class: 'sb'
        # String.Char: "#7b869d",  # class: 'sc'
        String.Doc: "italic #88a37b",  # class: 'sd' - like a comment
        # String.Double: "#7b869d",  # class: 's2'
        String.Escape: "#ebcb8b",  # class: 'se'
        # String.Heredoc: "#7b869d",  # class: 'sh'
        String.Interpol: "bold #97b67c",  # class: 'si'
        # String.Other: "#7b869d",  # class: 'sx'
        String.Regex: "#d08770",  # class: 'sr'
        # String.Single: "#7b869d",  # class: 's1'
        # String.Symbol: "#7b869d",  # class: 'ss'
        Generic: "#d08770",  # class: 'g'
        Generic.Deleted: "",  # class: 'gd'
        Generic.Emph: "italic",  # class: 'ge'
        Generic.Error: "",  # class: 'gr'
        Generic.Heading: "bold",  # class: 'gh'
        Generic.Inserted: "",  # class: 'gi'
        Generic.Output: "",  # class: 'go'
        Generic.Prompt: "",  # class: 'gp'
        Generic.Strong: "bold",  # class: 'gs'
        Generic.Subheading: "bold",  # class: 'gu'
        Generic.Traceback: "bold",  # class: 'gt'
    }
