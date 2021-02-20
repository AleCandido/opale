"""
Generate actual theme configuration files from the assets in:

    src/opale/_styles

They are compiled to just two files:

- src/opale/theme.conf
- src/opale/static/opale.css_t

"""

from os import fdopen
import pathlib
import json
import re
import sys
import importlib

import pygments.formatters

root = pathlib.Path(__file__).absolute().parents[1]
package = root / "src" / "opale"
styles = package / "_styles"

with open(styles / "styles.json") as namesf:
    names = json.load(namesf)


def make_theme_conf():
    # load ingredients
    with open(styles / "opale.conf") as tcf:
        opale_conf = tcf.read()

    # generate the content
    styles_conf = []
    for name in names:
        with open(styles / f"{name}.conf") as stylef:
            style_conf = stylef.read()

        style_conf = re.sub("(.*) =", fr"{name}_\1 =", style_conf)
        styles_conf.append(style_conf)

    # dump the result
    with open(package / "theme.conf", "w") as gen_theme:
        gen_theme.write("\n".join([opale_conf, *styles_conf]))


def make_opale_css_t():
    # load ingredients
    with open(styles / "opale.css_t") as octf:
        opale_css_t = octf.read()

    # generate the content
    styles_css = []
    for name in names:
        with open(styles / f"{name}.css_t") as csstf:
            style_css = csstf.read()

        lines = []
        for line in style_css.splitlines():
            # __import__("pdb").set_trace()
            if "vim:" in line:
                # skip modelines
                continue
            elif line[:2] != "{%":
                lines.append(line)
            else:
                lines.append(re.sub("theme_", f"theme_{name}_", line))
        style_css = "\n".join(lines)

        style_css = re.sub(r"\{\{ theme_", fr"{{{{ theme_{name}_", style_css)
        style_css = re.sub("themeglobal", "theme", style_css)
        style_css = re.sub(r",(.*)\{", fr",body.{name}\1{{", style_css)
        style_css = re.sub(
            r"^(\s*)(\w.*)\{$", fr"\1body.{name} \2{{", style_css, flags=re.MULTILINE
        )
        style_css = re.sub(
            r"^(.*) body (.*)\{$", fr"\1 \2{{", style_css, flags=re.MULTILINE
        )
        styles_css.append(style_css)

    # dump the result
    with open(package / "static" / "opale.css_t", "w") as gen_css_t:
        gen_css_t.write("\n".join([opale_css_t, *styles_css]))


pygments_box = """pre {{ line-height: 125%; background-color: {bkg}; border: 1px solid {border} }}
td.linenos pre {{ color: #000000; background-color: #f0f0f0; padding-left: 5px; padding-right: 5px; }}
span.linenos {{ color: #000000; background-color: #f0f0f0; padding-left: 5px; padding-right: 5px; }}
td.linenos pre.special {{ color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }}
span.linenos.special {{ color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }}\n"""


def make_opale_pygments_css_t():
    # load ingredients
    sys.path.insert(0, str(styles))

    pygments_styles = []
    for name in names:
        pystyle = importlib.import_module(f"{name}_pygments")
        mystyle = pystyle.__getattribute__(name.capitalize())
        pygments_style = pygments.formatters.HtmlFormatter(
            style=mystyle
        ).get_style_defs(".highlight")
        if not hasattr(mystyle, "border_color"):
            mystyle.border_color = mystyle.background_color

        # TODO: for some reason pip selects pygments 2.3.1, thus prepend the
        # missing part manually, injecting by hand some colors taken from the
        # pygments style
        pygments_style = (
            pygments_box.format(
                bkg=mystyle.background_color, border=mystyle.border_color
            )
            + pygments_style
        )
        pygments_styles.append(
            re.sub(r"^", f"body.{name} ", pygments_style, flags=re.MULTILINE)
        )

    sys.path.pop(0)

    # dump the result
    with open(package / "static" / "opale_pygments.css_t", "w") as gen_pygments_css:
        gen_pygments_css.write("\n".join(pygments_styles))


def all():
    make_theme_conf()
    make_opale_css_t()
    make_opale_pygments_css_t()
