from datetime import datetime


extensions = []
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"

project = u"Opale"
year = datetime.now().year
copyright = u"%d Alessandro Candido " % year

exclude_patterns = ["_build"]

html_theme = "opale"
html_sidebars = {
    "**": [
        "about.html",
        "navigation.html",
        "relations.html",
        "searchbox.html",
        "donate.html",
    ]
}
html_theme_options = {
    "description": "Dark theme based on Alabaster.",
    "github_user": "AleCandido",
    "github_repo": "opale",
    "fixed_sidebar": True,
}

extensions.append("releases")
releases_github_path = "AleCandido/opale"
# Our pre-0.x releases are unstable / mix bugs+features
releases_unstable_prehistory = True
