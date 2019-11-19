import os
class Config:
    '''
    General configuration parent class
    '''
    #NEWS_API_BASE_URL ='https://newsapi.org/v2/everything?q=bitcoin&from=2019-10-18&sortBy=publishedAt&apiKey ={}'
    NEWS_SOURCES_URL ='https://newsapi.org/v2/sources?apiKey=b8629f2cdc4f4bfa8f50558eb45e194b'
    NEWS_API_KEY =os.environ.get('NEWS_API_KEY')




class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}    