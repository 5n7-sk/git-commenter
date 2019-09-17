import json
import os.path as osp


class DataLoader:
    DATA_PATH = osp.join(osp.abspath(osp.dirname(__file__)), "data/data.json")

    def __init__(self):
        self.data = self.read_data(self.DATA_PATH)

    @staticmethod
    def read_data(path):
        with open(path, mode="r") as f:
            return json.load(f)

    @staticmethod
    def write_data(path, data):
        with open(path, mode="w") as f:
            json.dump(data, f, indent=4)
            f.write("\n")

    def load_emojis(self) -> list:
        """Load emojis list.

        Returns:
            list: List of emojis sorted by frequency.
                [{"name": "name", "emoji": "emoji", "frequency": "frequency"}]
        """
        return sorted(self.data["emoji"], key=lambda x: x["frequency"], reverse=True)

    def load_verbs(self) -> list:
        """Load verbs list.

        Returns:
            list: List of verbs sorted by frequency.
                [{"verb": "verb", "frequency": "frequency"}]
        """
        return sorted(self.data["verb"], key=lambda x: x["frequency"], reverse=True)

    def load_objects(self) -> list:
        """Load objects list.

        Returns:
            list: List of objects sorted by frequency.
                [{"object": "object", "frequency": "frequency"}]
        """
        return sorted(self.data["object"], key=lambda x: x["frequency"], reverse=True)

    def load_templates(self) -> list:
        """Load templates list.

        Returns:
            list: List of templates sorted by frequency.
                [{"template": "template", "frequency": "frequency"}]
        """
        return sorted(self.data["template"], key=lambda x: x["frequency"], reverse=True)

    def store_history(self, emoji=None, verb=None, object_=None, template=None):
        if emoji is not None:
            for e in self.load_emojis():
                if e["emoji"] == emoji:
                    e["frequency"] += 1

        if verb is not None:
            for v in self.load_verbs():
                if v["verb"] == verb:
                    v["frequency"] += 1

        if object_ is not None:
            for o in self.load_objects():
                if o["object"] == object_:
                    o["frequency"] += 1

        if template is not None:
            for t in self.load_templates():
                if t["template"] == template:
                    t["frequency"] += 1

        self.write_data(self.DATA_PATH, self.data)

    def clean_use_history(self):
        for emoji in self.load_emojis():
            emoji["frequency"] = 0
        for verb in self.load_verbs():
            verb["frequency"] = 0
        for object_ in self.load_objects():
            object_["frequency"] = 0
        for template in self.load_templates():
            template["frequency"] = 0

        self.write_data(self.DATA_PATH, self.data)
