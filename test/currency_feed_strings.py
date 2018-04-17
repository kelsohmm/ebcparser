raw_one_exchange_feed = """<?xml version="1.0" encoding="utf-8"?>
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
