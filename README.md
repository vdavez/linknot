# linknot

I [wrote a thing](https://esq.io/blog/posts/dear-media/) about how the media doesn't provide links or copies to court filings, and I've [tweeted](https://twitter.com/vdavez/status/701405527612354560) [about](https://twitter.com/vdavez/status/701375145454104576
) [it](https://twitter.com/vdavez/status/701374109997883392) when I find articles with no links or copies. But I want a way to programmatically do this.

## Concept

Using [Newspaper](http://newspaper.readthedocs.org/en/latest/) and [lxml](http://lxml.de/) I will:

1. identify a couple of newspapers
2. build a news source
3. extract the articles
4. pull down the articles' html
5. look for predefined regular expressions
6. check for anchor tags around the regular expressions
7. store and report results

## Why call it linknot?

There's a phenomenon called [link rot](https://en.wikipedia.org/wiki/Link_rot), and this feels like a variation.

## License

MIT
