from olympics.__main__ import main
import pytest
import argparse

def test_countries():
    argv = ['countries', '--top', '10']
    main(argv)

def test_collective():
    argv = ['collective', '--top', '5']
    main(argv)

def test_individual():
    argv = ['individual', '--top', '10']
    main(argv)

