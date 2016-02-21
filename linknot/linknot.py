import newspaper
from linknot import helpers


class LinkNot():
    """ The main class

    Attributes:
        sources: A dict of the newspaper sources
    """
    def __init__(self):
        self.sources = self.makeNewsSource('data/papers.csv')

    @staticmethod
    def makeNewsSource(papersFile):
        """ Generate a dict of the news sources using `newspaper`

        Args:
            papersFile: the csv of sources
        Returns:
            A dict of the newspaper sources
        """
        sources = {}
        papers = helpers.getPapersFromSource(papersFile)
        for paper in papers:
            sources[paper["source"]] = newspaper.build(paper["url"], memoize_articles=False)
        return sources

if __name__ == "__main__":
    print(LinkNot().sources)
