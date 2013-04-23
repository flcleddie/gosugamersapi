
BOT_NAME = 'gosugamersapi'

SPIDER_MODULES = ['gosugamersapi.spiders']
NEWSPIDER_MODULE = 'gosugamersapi.spiders'

ITEM_PIPELINES = ['gosugamersapi.pipelines.GosugamersapiPipeline',]

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "gosugamers"
MONGODB_COLLECTION = "matches"
