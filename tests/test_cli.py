import pytest

from git_commenter.cli import CLI


class TestCLI:
    @pytest.mark.parametrize(
        "verb, object_, modifier, actual",
        [
            ("verb", "object", "modifier", "Verb object modifier"),
            (None, "object", "modifier", "object modifier"),
            ("verb", None, "modifier", "Verb modifier"),
            ("verb", "object", None, "Verb object"),
            (None, None, None, ""),
        ],
    )
    def test_make_message(self, verb, object_, modifier, actual):
        cli = CLI(message="message")
        expect = cli.make_message(verb, object_, modifier)
        assert expect == actual
