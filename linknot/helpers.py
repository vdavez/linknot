import csv


def getPapersFromSource(papersFile="data/papers.csv"):
    """Get a dictionary of news sources from a csv file

    Args:
        papersFile: a CSV file with a source column and a url column. Defaults to "data/papers.csv"

    Returns:
        A dict of the papers in the CSV
    """
    with open(papersFile, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        papers = [papers for papers in reader]
    return papers
