import os

#os.environ.get('SQLALCHEMY_DATABASE_URI')
#os.environ.get('SECRET_KEY')
class Config:
    SECRET_KEY = 'af36fc748988ffff334c167f6d386ae2'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')