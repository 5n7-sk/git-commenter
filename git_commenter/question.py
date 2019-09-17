import re

from PyInquirer import prompt

from .color import STYLE
from .data import DataLoader


class Question:
    def __init__(self):
        self.data_loader = DataLoader()

    @staticmethod
    def format_choices(choices, formatter):
        formatted_choices = [formatter(rank) for rank in range(len(choices))]
        return formatted_choices

    @staticmethod
    def remove_frequency(string):
        # "(0) add" -> "add"
        return re.sub(r"^\([0-9]+\)\ ", "", string, 1)

    def ask_emoji(self):
        """Display CLI to select an emoji.

        Returns:
            str: Selected emoji
        """
        emojis = self.data_loader.load_emojis()

        def formatter(rank):
            return "({}) {} : {}".format(emojis[rank]["frequency"], emojis[rank]["emoji"], emojis[rank]["name"],)

        question = {
            "type": "list",
            "name": "emoji_list",
            "message": "Select emoji",
            "choices": [*self.format_choices(emojis, formatter)],
        }

        return self.remove_frequency(prompt(question, style=STYLE)["emoji_list"])[0]

    def ask_verb(self):
        """Display CLI to select a verb.

        If N/A is selected, go to input question.

        Returns:
            str: Selected verb
        """
        verbs = self.data_loader.load_verbs()

        def formatter(rank):
            return "({}) {}".format(verbs[rank]["frequency"], verbs[rank]["verb"])

        question = {
            "type": "list",
            "name": "verb_list",
            "message": "Select verb",
            "choices": ["N/A", *self.format_choices(verbs, formatter)],
        }

        verb = self.remove_frequency(prompt(question, style=STYLE)["verb_list"])
        if verb != "N/A":
            return verb

        alt_question = {
            "type": "input",
            "name": "verb_input",
            "message": "Input verb",
        }

        return prompt(alt_question, style=STYLE)["verb_input"]

    def ask_object(self):
        """Display CLI to select a object.

        If N/A is selected, go to input question.

        Returns:
            str: Selected object
        """
        objects = self.data_loader.load_objects()

        def formatter(rank):
            return "({}) {}".format(objects[rank]["frequency"], objects[rank]["object"])

        question = {
            "type": "list",
            "name": "object_list",
            "message": "Select object",
            "choices": ["N/A", *self.format_choices(objects, formatter)],
        }

        object_ = self.remove_frequency(prompt(question, style=STYLE)["object_list"])
        if object_ != "N/A":
            return object_

        alt_question = {
            "type": "input",
            "name": "object_input",
            "message": "Input object",
        }

        return prompt(alt_question, style=STYLE)["object_input"]

    def ask_modifier(self):
        """Display CLI to input modifier.

        Returns:
            str: Input modifier
        """
        question = {
            "type": "input",
            "name": "modifier_input",
            "message": "Input modifier",
        }

        return prompt(question, style=STYLE)["modifier_input"]

    def ask_message(self):
        """Display CLI to input message.

        Returns:
            str: Input message
        """
        question = {
            "type": "input",
            "name": "message_input",
            "message": "Input message",
        }

        return prompt(question, style=STYLE)["message_input"]

    def ask_template(self):
        """Display CLI to select a template.

        If N/A is selected, go to emoji/message question.

        Returns:
            str: Selected template
        """
        templates = self.data_loader.load_templates()

        def formatter(rank):
            return "({}) {}".format(templates[rank]["frequency"], templates[rank]["template"])

        question = {
            "type": "list",
            "name": "template_list",
            "message": "Select template",
            "choices": ["N/A", *self.format_choices(templates, formatter)],
        }

        template = self.remove_frequency(prompt(question, style=STYLE)["template_list"])
        if template != "N/A":
            return template

        return "{} {}".format(self.ask_emoji(), self.ask_message())

    def ask_commit(self, commit_message):
        """Display CLI to confirm a commit message.

        Args:
            commit_message (str): A processed commit message

        Returns:
            bool: Is committable
        """
        question = {
            "type": "confirm",
            "name": "commit_confirm",
            "message": f"Commit `{commit_message}`?",
        }

        return prompt(question, style=STYLE)["commit_confirm"]

    def ask_clean_use_history(self):
        """Display CLI to confirm whether to clean use history.

        Returns:
            bool: Is cleanable
        """
        question = {
            "type": "confirm",
            "name": "clean_confirm",
            "message": "Clean use history?",
        }

        return prompt(question, style=STYLE)["clean_confirm"]
