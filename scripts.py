# Standard Library
import subprocess


def format_code():
    subprocess.run(["black", "--line-length", "120", "."], check=True)


def lint_code():
    subprocess.run(["pylint", "--max-line-length=120", "notion_apilib"], check=True)
