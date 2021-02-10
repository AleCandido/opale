"""
Generate actual theme configuration files from the assets in:

    src/opale/_styles

They are compiled to just two files:

- src/opale/theme.conf
- src/opale/static/opale.css_t

"""

import pathlib
import json
import re

root = pathlib.Path(__file__).absolute().parents[1]
package = root / "src" / "opale"
styles = package / "_styles"


def make_theme_conf():
    # load ingredients
    with open(styles / "opale.conf") as tcf:
        opale_conf = tcf.read()

    with open(styles / "styles.json") as namesf:
        names = json.load(namesf)

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

    with open(styles / "styles.json") as namesf:
        names = json.load(namesf)

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
        style_css = re.sub(
            r"^(\s*)(\w.*)\{$", fr"\1body.{name} \2{{", style_css, flags=re.MULTILINE
        )
        styles_css.append(style_css)

    # dump the result
    with open(package / "static" / "opale.css_t", "w") as gen_css_t:
        gen_css_t.write("\n".join([opale_css_t, *styles_css]))


def all():
    make_theme_conf()
    make_opale_css_t()
