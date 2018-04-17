import feedparser


def parse_currency_feed(rss_source):
    feed = feedparser.parse(rss_source)
    date = feed.entries[0].date.split('T')[0]

    entry = feed.entries[0]
    target_currency = entry['cb_targetcurrency']
    [exchange_rate, base_currency] = [word.strip() for word in entry['cb_exchangerate'].split('\n')]

    return (base_currency, target_currency, exchange_rate, date)