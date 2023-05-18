# Duster
This is a Python command line tool that generates a commit message based on the changes in your Git repository using ChatGPT

## Installation
Clone the repository: git clone https://github.com/UACDH/duster.git
Install the required packages: pip install -r requirements.txt
## Usage
Before running the tool, make sure to set the `OPENAI_API_KEY` environment variable to your OpenAI API key. You can do this by running the following command in your terminal:
`export OPENAI_API_KEY=<YOUR_OPENAI_KEY>`
To generate a commit message, run the following command:
`python3 main.py --pathspec "*.py"`
This will generate a commit message based on the changes to all Python files in the repository.

You can also specify a different pathspec to include different files or directories in the commit message. For example:
`python3 main.py -p "src/*.py"`
This will generate a commit message based on the changes to all Python files in the src directory.

## Contributing
If you find a bug or have a feature request, please open an issue on GitHub. Pull requests are also welcome!
