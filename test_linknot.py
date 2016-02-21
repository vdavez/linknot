import pytest
import vcr
from linknot import helpers, linknot


def test_loaddata():
    """
    Test to see whether getPapersFromSource method gets all papers from CSV
    """
    papers = helpers.getPapersFromSource('data/papers.csv')
    assert len(papers) == 3
    assert papers[1]["url"] == "http://washingtonpost.com"


@vcr.use_cassette(record_mode='once')
def test_linknot_init():
    """
    Test creation of the LinkNot class
    """
    linknotObj = linknot.LinkNot()
    assert len(linknotObj.sources) == 3
