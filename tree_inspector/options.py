from typing import NamedTuple


Options = NamedTuple('Options', [
    ('max_elements_to_show_in_list', int),
    ('max_elements_to_show_in_dict', int),
    ('truncate_string_longer_than', int),
])

Options.__new__.__defaults__ = Options(
    max_elements_to_show_in_list=5,
    max_elements_to_show_in_dict=10,
    truncate_string_longer_than=30
)


if __name__ == "__main__":
    options = Options(truncate_string_longer_than=80)
    print(options)
