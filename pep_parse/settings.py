from pathlib import Path

BOT_NAME = 'pep_parse'
NEWSPIDER_MODULE = f'{BOT_NAME}.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]
ALLOWED_DOMAINS = [
    'peps.python.org',
]

ROBOTSTXT_OBEY = True

BASE_DIR = Path(__file__).resolve().parent.parent
NUMBER = 'number'
RESULTS = 'results'
NAME = 'name'
STATUS_CSV = 'Статус'
COUNT = 'Количество'
SUMMARY = 'Всего'
STATUS_SUMMARY = 'status_summary'
CSV = 'csv'
DT_FORMAT = '%Y-%m-%d_%H-%M-%S'

FEEDS = {
    f'{RESULTS}/pep_%(time)s.CSV': {
        'format': 'CSV',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
