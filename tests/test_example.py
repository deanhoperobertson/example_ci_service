# test module
from unittest.mock import patch
import pytest

from example_ci_service.example import add_1_to_value, lets_go_further


def test_example():
	assert add_1_to_value(1) == 2


def test_example_2nd(model_number_three):
	data = model_number_three
	assert add_1_to_value(data) == 4


def test_further(model_number_three):
	assert lets_go_further(model_number_three) == 104


@patch("example_ci_service.example.add_1_to_value")
def test_further_with_mocker(mocker, model_number_three):
	mocker.return_value=3
	assert lets_go_further(model_number_three) == 103


def test_value_error():
	with pytest.raises(TypeError):
		add_1_to_value("1")