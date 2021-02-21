from invoke import task, Collection
from invocations import docs, checks
from invocations.packaging import release

import pathlib

here = pathlib.Path(__file__).parent


@task
def clean(c):
    """
    Clean generated assets.
    """
    static = here / "src" / "opale" / "static"
    generated_assets = [
        static / f
        for f in [
            "components.js",
            "components.js.LICENSE.txt",
            "style.css",
            "style.js",
        ]
    ]
    for f in generated_assets:
        f.unlink(missing_ok=True)


ns = Collection(release, docs, checks.blacken)
ns.add_task(clean)
ns.configure(
    {
        "packaging": {
            "sign": True,
            "wheel": True,
            "changelog_file": "docs/changelog.rst",
        }
    }
)
