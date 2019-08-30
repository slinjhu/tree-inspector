from typing import NamedTuple


class Options(NamedTuple):
    max_elements_to_show_in_list: int = 5
    max_elements_to_show_in_dict: int = 10
    truncate_string_longer_than: int = 30
    max_size_to_show_in_numpy_ndarray: int = 60


if __name__ == "__main__":
    options = Options()
    print(options)