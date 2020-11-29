import pathlib

import pygit2


def version_info(major, minor, micro):
    repo_path = pathlib.Path(__file__).absolute().parent
    repo = pygit2.Repository(repo_path)

    # determine ids of tagged commits
    tags_commit_sha = [
        repo.resolve_refish("/".join(r.split("/")[2:]))[0].id
        for r in repo.references
        if "/tags/" in r
    ]

    return {
        "major": major,
        "minor": minor,
        "micro": micro,
        "is_released": "main" in repo.head.name or repo.head.target in tags_commit_sha,
        "short_version": "%d.%d" % (major, minor),
        "version": "%d.%d.%d" % (major, minor, micro),
        "full_version": "%d.%d.%d" % (major, minor, micro),
    }


def write_version_py(version, filename="src/opale/version.py"):
    content = """
# THIS FILE IS GENERATED FROM SETUP.PY
major = %(major)d
short_version = '%(short_version)s'
version = '%(version)s'
full_version = '%(full_version)s'
is_released = %(is_released)s
"""
    version = version_info(*version)
    if not version["is_released"]:
        version["full_version"] += "-develop"

    a = open(filename, "w")
    try:
        a.write(content % version)
    finally:
        a.close()
