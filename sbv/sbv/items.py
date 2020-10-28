# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SbvItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    category = scrapy.Field()
    # source_url = scrapy.Field()
    create_date = scrapy.Field()
    berief_content = scrapy.Field()
    content = scrapy.Field()
