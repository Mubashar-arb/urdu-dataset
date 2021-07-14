# pylint: disable=no-self-use, too-few-public-methods
"""Module for Item Pipeline after extrection from response."""

import json
import os
from itemadapter import ItemAdapter


class NawaiwaqtPipeline:
    """Scrapy Item Pipeline class. Extrated objects pass through here."""

    def process_item(self, item, _):
        """Processes the extracted item."""
        adapted = ItemAdapter(item).asdict()
        date = adapted["date"]
        news_id = adapted["id"]
        _, month, year = date.split('-')

        os.makedirs(f"scraped_data/{year}/{month}/", exist_ok=True)
        with open(f"scraped_data/{year}/{month}/{date}-{news_id}.json", "w") as outfile:
            json.dump(adapted["item"], outfile, ensure_ascii = False)

        return item
