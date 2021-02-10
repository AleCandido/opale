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

# TODO: remove all the write statements


def make_theme_conf():
    # load ingredients
    with open(styles / "theme.conf") as tcf:
        theme_conf = tcf.read()

    with open(styles / "styles.json") as namesf:
        names = json.load(namesf)

    # generate the content
    styles_conf = []
    for name in names:
        with open(styles / f"{name}.conf") as stylef:
            style_conf = stylef.read()

        style_conf = re.sub(" =", f"_{name} =", style_conf)
        styles_conf.append(style_conf)

    # dump the result
    with open(package / "theme.conf", "w") as gen_theme:
        gen_theme.write("\n".join([theme_conf, *styles_conf]))


def make_opale_css_t():
    # load ingredients
    with open(styles / "opale.css_t") as octf:
        opale_css_t = octf.read()

    with open(styles / "styles.json") as namesf:
        names = json.load(namesf)

    # generate the content
    styles_css = []
    for name in names:
        with open(styles / f"{name}.conf") as csstf:
            styles_css = csstf.read()

        # styles_css = re.sub(" =", f"_{name} =", style_css)
        # styles_css.append(style_css)

    # dump the result
    with open(package / "static" / "opale.css_t", "w") as gen_css_t:
        gen_css_t.write("\n".join([opale_css_t, *styles_css]))


def all():
    import datetime

    with open("ciao.md", "a") as f:
        f.write(f"\t{datetime.datetime.now()}\n")

    make_theme_conf()
    make_opale_css_t()

    with open("ciao.md", "a") as f:
        f.write(f"{datetime.datetime.now()}\n\n")
