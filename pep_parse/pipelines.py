import datetime
import csv
from collections import defaultdict

from pep_parse.settings import (BASE_DIR, COUNT, DT_FORMAT,
                                RESULTS, STATUS_CSV, STATUS_SUMMARY,
                                SUMMARY, CSV)


class PepParsePipeline:
    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        self.status_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        date_time = datetime.datetime.utcnow().strftime(DT_FORMAT)
        filename = f'{STATUS_SUMMARY}_{date_time}.{CSV}'
        fieldnames = [STATUS_CSV, COUNT]
        with open(
                f'{self.results_dir}/{filename}', 'w', newline=''
        ) as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for status, count in self.count_pep_status.items():
                writer.writerow({STATUS_CSV: status, COUNT: count})
            total_count = sum(self.count_pep_status.values())
            writer.writerow({STATUS_CSV: SUMMARY, COUNT: total_count})
