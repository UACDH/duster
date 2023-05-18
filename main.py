##
# Author: Bahaa Abdulraheem
# Description: Duster is a cli tool that summarizes git commit messages
#                by sending a diff of the working tree to GPT-3 and asking it
#                to summarize the diff. 
##

import typer
from rich.console import Console
from diff import getDiff
from aiengine import AIEngine
import os

app = typer.Typer()
console = Console(width=80)

@app.command("run")
def run(
    path: str = typer.Option("./", "--path", help="Path to the Git repository"),
    pathspec: str = typer.Option(..., "--pathspec", "-p", help="Git pathspec to use. Use this argument to specify which files or directories to include in the commit message. You can use wildcards and exclude patterns to fine-tune your selection. For example, to include all Python files in the 'src' directory, use 'src/*.py'. To exclude all files with the '.txt' extension, use '!*.txt'.")
):
    """Generate the commit message"""
    git_diff = getDiff(path, pathspec)
    ai_engine = AIEngine(git_diff)
    commit_message = ai_engine.generate_commit_message()
    console.log(commit_message)

if __name__ == '__main__':
    app()
