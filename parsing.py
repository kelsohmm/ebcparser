import feedparser


def parse_currency_feed(rss_source):
    feed = feedparser.parse(rss_source)
    return [
        parse_feed_entry(entry)
        for entry in feed.entries
    ]


def parse_feed_entry(entry):
    date = entry.date.split('T')[0]
    target_currency = entry['cb_targetcurrency']
    [exchange_rate, base_currency] = [word.strip() for word in entry['cb_exchangerate'].split('\n')]
    return (base_currency, target_currency, exchange_rate, date)