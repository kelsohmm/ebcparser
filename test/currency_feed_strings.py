raw_one_entry_feed = """<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF  xmlns = "http://purl.org/rss/1.0/" xmlns:cb = "http://www.cbwiki.net/wiki/index.php/Specification_1.1" xmlns:dc = "http://purl.org/dc/elements/1.1/" xmlns:dcterms = "http://purl.org/dc/terms/" xmlns:rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:xsi = "http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation = "http://www.w3.org/1999/02/22-rdf-syntax-ns# rdf.xsd" >
    <channel  rdf:about = "http://www.ecb.europa.eu/rss/czk.html">
        <title>ECB | Czech koruna (CZK) - Euro foreign exchange reference rates</title>
        <link>http://www.ecb.europa.eu/home/html/rss.en.html</link>
        <description>The reference rates are based on the regular daily concertation procedure between central banks within and outside the European System of Central Banks, which normally takes place at 2.15 p.m. (14:15) ECB time.</description>
        <items>
            <rdf:Seq>
                <rdf:li rdf:resource="http://www.ecb.europa.eu/stats/exchange/eurofxref/html/eurofxref-graph-czk.en.html?date=2018-04-17&amp;rate=25.254" />
            </rdf:Seq>
        </items>
        <dc:publisher>European Central Bank</dc:publisher>
        <dcterms:license>http://www.ecb.europa.eu/home/html/disclaimer.en.html</dcterms:license>
    </channel>
    <item rdf:about="http://www.ecb.europa.eu/stats/exchange/eurofxref/html/eurofxref-graph-czk.en.html?date=2018-04-17&amp;rate=25.254">
        <title xml:lang="en">25.254 CZK = 1 EUR 2018-04-17 ECB Reference rate</title>
        <link>http://www.ecb.europa.eu/stats/exchange/eurofxref/html/eurofxref-graph-czk.en.html?date=2018-04-17&amp;rate=25.254</link>
        <description xml:lang="en">1 EUR buys 25.254 Czech koruna (CZK) - The reference exchange rates are published both by electronic market information providers and on the ECB's website shortly after the concertation procedure has been completed. Reference rates are published according to the same  calendar as the TARGET system.</description>
        <dc:date>2018-04-17T14:15:00+01:00</dc:date>
        <dc:language>en</dc:language>
        <cb:statistics>
            <cb:country>U2</cb:country>
            <cb:institutionAbbrev>ECB</cb:institutionAbbrev>
            <cb:exchangeRate>
                <cb:value frequency="daily" decimals="3">25.254</cb:value>
                <cb:baseCurrency unit_mult="0">EUR</cb:baseCurrency>
                <cb:targetCurrency>CZK</cb:targetCurrency>
                <cb:rateType>Reference rate</cb:rateType>
            </cb:exchangeRate>
        </cb:statistics>
    </item>
</rdf:RDF>
"""

raw_three_entries_feed = """<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF  xmlns = "http://purl.org/rss/1.0/" xmlns:cb = "http://www.cbwiki.net/wiki/index.php/Specification_1.1" xmlns:dc = "http://purl.org/dc/elements/1.1/" xmlns:dcterms = "http://purl.org/dc/terms/" xmlns:rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:xsi = "http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation = "http://www.w3.org/1999/02/22-rdf-syntax-ns# rdf.xsd" >
    <channel  rdf:about = "http://www.ecb.europa.eu/rss/czk.html">
        <title>ECB | Czech koruna (CZK) - Euro foreign exchange reference rates</title>
        <link>http://www.ecb.europa.eu/home/html/rss.en.html</link>
        <description>The reference rates are based on the regular daily concertation procedure between central banks within and outside the European System of Central Banks, which normally takes place at 2.15 p.m. (14:15) ECB time.</description>
        <items>
            <rdf:Seq>
                <rdf:li rdf:resource="http://www.ecb.europa.eu/stats/exchange/eurofxref/html/eurofxref-graph-czk.en.html?date=2018-04-17&amp;rate=25.254" />
                <rdf:li rdf:resource="http://www.ecb.europa.eu/stats/exchange/eurofxref/html/eurofxref-graph-czk.en.html?date=2018-04-16&amp;rate=25.265" />
                <rdf:li rdf:resource="http://www.ecb.europa.eu/stats/exchange/eurofxref/html/eurofxref-graph-czk.en.html?date=2018-04-13&amp;rate=25.307" />
            </rdf:Seq>
        </items>
        <dc:publisher>European Central Bank</dc:publisher>
        <dcterms:license>http://www.ecb.europa.eu/home/html/disclaimer.en.html</dcterms:license>
    </channel>
    <item rdf:about="http://www.ecb.europa.eu/stats/exchange/eurofxref/html/eurofxref-graph-czk.en.html?date=2018-04-17&amp;rate=25.254">
        <title xml:lang="en">25.254 CZK = 1 EUR 2018-04-17 ECB Reference rate</title>
        <link>http://www.ecb.europa.eu/stats/exchange/eurofxref/html/eurofxref-graph-czk.en.html?date=2018-04-17&amp;rate=25.254</link>
        <description xml:lang="en">1 EUR buys 25.254 Czech koruna (CZK) - The reference exchange rates are published both by electronic market information providers and on the ECB's website shortly after the concertation procedure has been completed. Reference rates are published according to the same  calendar as the TARGET system.</description>
        <dc:date>2018-04-17T14:15:00+01:00</dc:date>
        <dc:language>en</dc:language>
        <cb:statistics>
            <cb:country>U2</cb:country>
            <cb:institutionAbbrev>ECB</cb:institutionAbbrev>
            <cb:exchangeRate>
                <cb:value frequency="daily" decimals="3">25.254</cb:value>
                <cb:baseCurrency unit_mult="0">EUR</cb:baseCurrency>
                <cb:targetCurrency>CZK</cb:targetCurrency>
                <cb:rateType>Reference rate</cb:rateType>
            </cb:exchangeRate>
        </cb:statistics>
    </item>
    <item rdf:about="http://www.ecb.europa.eu/stats/exchange/eurofxref/html/eurofxref-graph-czk.en.html?date=2018-04-16&amp;rate=25.265">
        <title xml:lang="en">25.265 CZK = 1 EUR 2018-04-16 ECB Reference rate</title>
        <link>http://www.ecb.europa.eu/stats/exchange/eurofxref/html/eurofxref-graph-czk.en.html?date=2018-04-16&amp;rate=25.265</link>
        <description xml:lang="en">1 EUR buys 25.265 Czech koruna (CZK) - The reference exchange rates are published both by electronic market information providers and on the ECB's website shortly after the concertation procedure has been completed. Reference rates are published according to the same  calendar as the TARGET system.</description>
        <dc:date>2018-04-16T14:15:00+01:00</dc:date>
        <dc:language>en</dc:language>
        <cb:statistics>
            <cb:country>U2</cb:country>
            <cb:institutionAbbrev>ECB</cb:institutionAbbrev>
            <cb:exchangeRate>
                <cb:value frequency="daily" decimals="3">25.265</cb:value>
                <cb:baseCurrency unit_mult="0">EUR</cb:baseCurrency>
                <cb:targetCurrency>CZK</cb:targetCurrency>
                <cb:rateType>Reference rate</cb:rateType>
            </cb:exchangeRate>
        </cb:statistics>
    </item>
    <item rdf:about="http://www.ecb.europa.eu/stats/exchange/eurofxref/html/eurofxref-graph-czk.en.html?date=2018-04-13&amp;rate=25.307">
        <title xml:lang="en">25.307 CZK = 1 EUR 2018-04-13 ECB Reference rate</title>
        <link>http://www.ecb.europa.eu/stats/exchange/eurofxref/html/eurofxref-graph-czk.en.html?date=2018-04-13&amp;rate=25.307</link>
        <description xml:lang="en">1 EUR buys 25.307 Czech koruna (CZK) - The reference exchange rates are published both by electronic market information providers and on the ECB's website shortly after the concertation procedure has been completed. Reference rates are published according to the same  calendar as the TARGET system.</description>
        <dc:date>2018-04-13T14:15:00+01:00</dc:date>
        <dc:language>en</dc:language>
        <cb:statistics>
            <cb:country>U2</cb:country>
            <cb:institutionAbbrev>ECB</cb:institutionAbbrev>
            <cb:exchangeRate>
                <cb:value frequency="daily" decimals="3">25.307</cb:value>
                <cb:baseCurrency unit_mult="0">EUR</cb:baseCurrency>
                <cb:targetCurrency>CZK</cb:targetCurrency>
                <cb:rateType>Reference rate</cb:rateType>
            </cb:exchangeRate>
        </cb:statistics>
    </item>
</rdf:RDF>
"""

raw_full_feed_currency_sgd = """<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF  xmlns = "http://purl.org/rss/1.0/" xmlns:cb = "http://www.cbwiki.net/wiki/index.php/Specification_1.1" xmlns:dc = "http://purl.org/dc/elements/1.1/" xmlns:dcterms = "http://purl.org/dc/terms/" xmlns:rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:xsi = "http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation = "http://www.w3.org/1999/02/22-rdf-syntax-ns# rdf.xsd" >
    <channel  rdf:about = "http://www.ecb.europa.eu/rss/sgd.html">
        <title>ECB | Singapore dollar (SGD) - Euro foreign exchange reference rates</title>
        <link>http://www.ecb.europa.eu/home/html/rss.en.html</link>
        <description>The reference rates are based on the regular daily concertation procedure between central banks within and outside the European System of Central Banks, which normally takes place at 2.15 p.m. (14:15) ECB time.</description>
        <items>
            <rdf:Seq>
                <rdf:li rdf:resource="http://www.ecb.europa.eu/stats/exchange/eurofxref/html/eurofxref-graph-sgd.en.html?date=2018-04-17&amp;rate=1.6192" />
                <rdf:li rdf:resource="http://www.ecb.europa.eu/stats/exchange/eurofxref/html/eurofxref-graph-sgd.en.html?date=2018-04-16&amp;rate=1.6221" />
                <rdf:li rdf:resource="http://www.ecb.europa.eu/stats/exchange/eurofxref/html/eurofxref-graph-sgd.en.html?date=2018-04-13&amp;rate=1.6158" />
                <rdf:li rdf:resource="http://www.ecb.europa.eu/stats/exchange/eurofxref/html/eurofxref-graph-sgd.en.html?date=2018-04-12&amp;rate=1.6155" />
                <rdf:li rdf:resource="http://www.ecb.europa.eu/stats/exchange/eurofxref/html/eurofxref-graph-sgd.en.html?date=2018-04-11&amp;rate=1.6204" />
            </rdf:Seq>
        </items>
        <dc:publisher>European Central Bank</dc:publisher>
        <dcterms:license>http://www.ecb.europa.eu/home/html/disclaimer.en.html</dcterms:license>
    </channel>
    <item rdf:about="http://www.ecb.europa.eu/stats/exchange/eurofxref/html/eurofxref-graph-sgd.en.html?date=2018-04-17&amp;rate=1.6192">
        <title xml:lang="en">1.6192 SGD = 1 EUR 2018-04-17 ECB Reference rate</title>
        <link>http://www.ecb.europa.eu/stats/exchange/eurofxref/html/eurofxref-graph-sgd.en.html?date=2018-04-17&amp;rate=1.6192</link>
        <description xml:lang="en">1 EUR buys 1.6192 Singapore dollar (SGD) - The reference exchange rates are published both by electronic market information providers and on the ECB's website shortly after the concertation procedure has been completed. Reference rates are published according to the same  calendar as the TARGET system.</description>
        <dc:date>2018-04-17T14:15:00+01:00</dc:date>
        <dc:language>en</dc:language>
        <cb:statistics>
            <cb:country>U2</cb:country>
            <cb:institutionAbbrev>ECB</cb:institutionAbbrev>
            <cb:exchangeRate>
                <cb:value frequency="daily" decimals="4">1.6192</cb:value>
                <cb:baseCurrency unit_mult="0">EUR</cb:baseCurrency>
                <cb:targetCurrency>SGD</cb:targetCurrency>
                <cb:rateType>Reference rate</cb:rateType>
            </cb:exchangeRate>
        </cb:statistics>
    </item>
    <item rdf:about="http://www.ecb.europa.eu/stats/exchange/eurofxref/html/eurofxref-graph-sgd.en.html?date=2018-04-16&amp;rate=1.6221">
        <title xml:lang="en">1.6221 SGD = 1 EUR 2018-04-16 ECB Reference rate</title>
        <link>http://www.ecb.europa.eu/stats/exchange/eurofxref/html/eurofxref-graph-sgd.en.html?date=2018-04-16&amp;rate=1.6221</link>
        <description xml:lang="en">1 EUR buys 1.6221 Singapore dollar (SGD) - The reference exchange rates are published both by electronic market information providers and on the ECB's website shortly after the concertation procedure has been completed. Reference rates are published according to the same  calendar as the TARGET system.</description>
        <dc:date>2018-04-16T14:15:00+01:00</dc:date>
        <dc:language>en</dc:language>
        <cb:statistics>
            <cb:country>U2</cb:country>
            <cb:institutionAbbrev>ECB</cb:institutionAbbrev>
            <cb:exchangeRate>
                <cb:value frequency="daily" decimals="4">1.6221</cb:value>
                <cb:baseCurrency unit_mult="0">EUR</cb:baseCurrency>
                <cb:targetCurrency>SGD</cb:targetCurrency>
                <cb:rateType>Reference rate</cb:rateType>
            </cb:exchangeRate>
        </cb:statistics>
    </item>
    <item rdf:about="http://www.ecb.europa.eu/stats/exchange/eurofxref/html/eurofxref-graph-sgd.en.html?date=2018-04-13&amp;rate=1.6158">
        <title xml:lang="en">1.6158 SGD = 1 EUR 2018-04-13 ECB Reference rate</title>
        <link>http://www.ecb.europa.eu/stats/exchange/eurofxref/html/eurofxref-graph-sgd.en.html?date=2018-04-13&amp;rate=1.6158</link>
        <description xml:lang="en">1 EUR buys 1.6158 Singapore dollar (SGD) - The reference exchange rates are published both by electronic market information providers and on the ECB's website shortly after the concertation procedure has been completed. Reference rates are published according to the same  calendar as the TARGET system.</description>
        <dc:date>2018-04-13T14:15:00+01:00</dc:date>
        <dc:language>en</dc:language>
        <cb:statistics>
            <cb:country>U2</cb:country>
            <cb:institutionAbbrev>ECB</cb:institutionAbbrev>
            <cb:exchangeRate>
                <cb:value frequency="daily" decimals="4">1.6158</cb:value>
                <cb:baseCurrency unit_mult="0">EUR</cb:baseCurrency>
                <cb:targetCurrency>SGD</cb:targetCurrency>
                <cb:rateType>Reference rate</cb:rateType>
            </cb:exchangeRate>
        </cb:statistics>
    </item>
    <item rdf:about="http://www.ecb.europa.eu/stats/exchange/eurofxref/html/eurofxref-graph-sgd.en.html?date=2018-04-12&amp;rate=1.6155">
        <title xml:lang="en">1.6155 SGD = 1 EUR 2018-04-12 ECB Reference rate</title>
        <link>http://www.ecb.europa.eu/stats/exchange/eurofxref/html/eurofxref-graph-sgd.en.html?date=2018-04-12&amp;rate=1.6155</link>
        <description xml:lang="en">1 EUR buys 1.6155 Singapore dollar (SGD) - The reference exchange rates are published both by electronic market information providers and on the ECB's website shortly after the concertation procedure has been completed. Reference rates are published according to the same  calendar as the TARGET system.</description>
        <dc:date>2018-04-12T14:15:00+01:00</dc:date>
        <dc:language>en</dc:language>
        <cb:statistics>
            <cb:country>U2</cb:country>
            <cb:institutionAbbrev>ECB</cb:institutionAbbrev>
            <cb:exchangeRate>
                <cb:value frequency="daily" decimals="4">1.6155</cb:value>
                <cb:baseCurrency unit_mult="0">EUR</cb:baseCurrency>
                <cb:targetCurrency>SGD</cb:targetCurrency>
                <cb:rateType>Reference rate</cb:rateType>
            </cb:exchangeRate>
        </cb:statistics>
    </item>
    <item rdf:about="http://www.ecb.europa.eu/stats/exchange/eurofxref/html/eurofxref-graph-sgd.en.html?date=2018-04-11&amp;rate=1.6204">
        <title xml:lang="en">1.6204 SGD = 1 EUR 2018-04-11 ECB Reference rate</title>
        <link>http://www.ecb.europa.eu/stats/exchange/eurofxref/html/eurofxref-graph-sgd.en.html?date=2018-04-11&amp;rate=1.6204</link>
        <description xml:lang="en">1 EUR buys 1.6204 Singapore dollar (SGD) - The reference exchange rates are published both by electronic market information providers and on the ECB's website shortly after the concertation procedure has been completed. Reference rates are published according to the same  calendar as the TARGET system.</description>
        <dc:date>2018-04-11T14:15:00+01:00</dc:date>
        <dc:language>en</dc:language>
        <cb:statistics>
            <cb:country>U2</cb:country>
            <cb:institutionAbbrev>ECB</cb:institutionAbbrev>
            <cb:exchangeRate>
                <cb:value frequency="daily" decimals="4">1.6204</cb:value>
                <cb:baseCurrency unit_mult="0">EUR</cb:baseCurrency>
                <cb:targetCurrency>SGD</cb:targetCurrency>
                <cb:rateType>Reference rate</cb:rateType>
            </cb:exchangeRate>
        </cb:statistics>
    </item>
</rdf:RDF>
"""