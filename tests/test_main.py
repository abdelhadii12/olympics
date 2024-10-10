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

def test_top_negative():
    argv = ['countries', '--top', '-1']
    with pytest.raises(SystemExit):
        main(argv)

def test_top_zero():
    argv = ['collective', '--top', '0']
    with pytest.raises(SystemExit):
        main(argv)

def test_invalid_command():
    argv = ['invalid_command', '--top', '10']
    with pytest.raises(SystemExit):
        main(argv)

def test_no_top_value():
    argv = ['countries']
    with pytest.raises(SystemExit):
        main(argv)

