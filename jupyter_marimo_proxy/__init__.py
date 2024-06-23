import os


def setup_marimoserver():
    path = os.getenv("PATH", "")

    userbin = os.path.join(os.environ["HOME"], "bin")
    if os.path.exists(userbin) and not userbin in path:
        path = userbin + os.pathsep + path

    userbin = os.path.join(os.environ["HOME"], ".local", "bin")
    if os.path.exists(userbin) and not userbin in path:
        path = userbin + os.pathsep + path

    return {
        "command": [
            "marimo",
            "edit",
            "--port",
            "{port}",
            "--base-url",
            os.environ["JUPYTERHUB_SERVICE_PREFIX"] + "marimo",
            "--no-token",
            "--headless",
        ],
        "environment": {"PATH": path},
        "timeout": 60,
        "absolute_url": True,
        "launcher_entry": {
            "title": "Marimo",
            "icon_path": os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "icon.svg"
            ),
        },
    }
