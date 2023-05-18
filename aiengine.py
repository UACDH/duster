import openai
import os

class AIEngine:
    def __init__(self, git_diff):
        self.git_diff = git_diff
        self.prompt = "Please generate a commit title message for the following git diff:\n\n" + self.git_diff
        self.sysmsg = """You are a software developer that writes excellent commit messages.
                        You will keep your response to 50 characters or less, and only respond with the commit title. The title you
                        respond with will be descriptive and representative of the code changes. If the input is empty or doesn't make sense,
                        respond with \"Invalid input - please try again.\""""

    def generate_commit_message(self):
        openai.api_key = os.environ["OPENAI_API_KEY"]
        model_engine = "gpt-3.5-turbo"
        response = openai.ChatCompletion.create(
            model=model_engine,
            messages=[
                {"role": "system", "content": self.sysmsg},
                {"role": "user", "content": self.prompt}
            ],
            max_tokens=60,
            n=1,
            stop=None,
            temperature=0.5,
        )
        response = response["choices"][0]
        if response["finish_reason"] != "stop":
            raise Exception("AI response too long for commit title.")
        return response["message"]["content"]