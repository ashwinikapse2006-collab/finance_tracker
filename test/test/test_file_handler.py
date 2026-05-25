from finance_tracker.file_handler import FileHandler


def test_save_and_load(tmp_path):
    file_path = tmp_path / "test.json"

    data = [{"name": "test"}]

    FileHandler.save_data(file_path, data)

    loaded = FileHandler.load_data(file_path)

    assert loaded == data