# -*- coding: utf-8 -*-
from scrapy import cmdline


# cmdline.execute('scrapy crawl ask -o ask.json -s FEED_EXPORT_ENCODING=utf-8'.split())
cmdline.execute('scrapy crawl ask -o ask.csv -s FEED_EXPORT_ENCODING=gbk'.split())