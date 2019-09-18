from git_commenter.data import DataLoader


class TestDataLoader:
    def test_data_freq_initialized(self):
        data = DataLoader().read_data(path=DataLoader.DATA_PATH)

        sum_freq = 0
        for emoji in data["emoji"]:
            sum_freq += emoji["frequency"]
        for verb in data["verb"]:
            sum_freq += verb["frequency"]
        for object_ in data["object"]:
            sum_freq += object_["frequency"]
        for template in data["template"]:
            sum_freq += template["frequency"]

        assert sum_freq == 0
