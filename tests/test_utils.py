from json import JSONDecodeError

import pytest

from main.utils import open_json, get_filtered_list, get_sorted_list, get_last_operations, formatted_date, mask_number
from tests.file_for_test import (expected_result_json_file, expected_result_filtered, expected_result_sorted,
                                 expected_result_last_operations, expected_result_format_date,
                                 expected_result_musk_number)
from tests.file_for_test import (test_filtered, test_sorted, test_five_last_operations, test_format_date,
                                 test_mask_number)

import json


def test_json():
    assert open_json("test_file.json") == expected_result_json_file


def test_filtered_list():
    assert get_filtered_list(test_filtered) == expected_result_filtered


def test_sorted_list():
    assert get_sorted_list(test_sorted) == expected_result_sorted


def test_last_operations():
    assert get_last_operations(test_five_last_operations) == expected_result_last_operations


def test_formatted_date():
    assert formatted_date(test_format_date) == expected_result_format_date


def test_mask_num():
    assert mask_number(test_mask_number, 'from', 'to') == expected_result_musk_number
