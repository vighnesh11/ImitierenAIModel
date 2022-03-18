
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}

# Enter Open API Key here
OPENAI_API_KEY = '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'
