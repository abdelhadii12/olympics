from olympics.__main__ import main
import pytest
import argparse

def test_countries():
    argv = ['countries', '--top', '10']
    with patch('your_module.cli.top_countries') as mock_top_countries:
        main(argv)
        mock_top_countries.assert_called_once_with(10)

def test_collective():
    argv = ['collective', '--top', '5']
    with patch('your_module.cli.top_collective') as mock_top_collective:
        main(argv)
        mock_top_collective.assert_called_once_with(5)

def test_individual():
    argv = ['individual', '--top', '10']
    with patch('your_module.cli.top_individual') as mock_top_individual:
        main(argv)
        mock_top_individual.assert_called_once_with(10)


