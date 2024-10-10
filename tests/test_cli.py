from io import StringIO

from olympics import cli


def test_top_countries():
    string = StringIO()
    cli.top_countries(file=string)
    text = string.getvalue()
    assert 'Top' in text
    assert 'countries' in text
    assert 'Gold' in text
    assert 'Silver' in text
    assert 'Bronze' in text
    assert 'Total' in text

def test_top_collective():
    string = StringIO()
    cli.top_collective(file=string)
    text = string.getvalue()
    assert 'Top' in text
    assert 'collective events' in text
    assert 'Country' in text
    assert 'Medals' in text

def test_top_individual():
    string = StringIO()
    cli.top_individual(file=string)
    text = string.getvalue()
    assert 'Top' in text
    assert 'individual events' in text
    assert 'Name' in text
    assert 'Gender' in text
    assert 'Country' in text
    assert 'Medals' in text

