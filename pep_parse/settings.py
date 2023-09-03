from pathlib import Path

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'


ROBOTSTXT_OBEY = True

BASE_DIR = Path(__file__).resolve().parent.parent
NUMBER = 'number'
RESULTS = 'results'
NAME = 'name'
STATUS_CSV = 'Статус'
COUNT = 'Количество'
SUMMARY = 'Всего'
STATUS_SUMMARY = 'status_summary'
DT_FORMAT = '%Y-%m-%d_%H-%M-%S'

FEEDS = {
    f'{RESULTS}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
