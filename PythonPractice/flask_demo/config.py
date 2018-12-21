# -*- coding: utf-8 -*-

# @Time    : 2018/12/4 10:48
# @Author  : songq001
# @Comment : 

import os
import hashlib

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    # oracle配置
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    SQLALCHEMY_POOL_SIZE = 20       # 数据库连接池的大小。默认是引擎默认值（通常 是 5 ），此处最重要。
    SQLALCHEMY_POOL_TIMEOUT = 5     # 指定数据库连接池的超时时间。默认是10s。
    SQLALCHEMY_POOL_RECYCLE = 3000  # 配置连接池的 recyle 时间。默认是7200s。
    SECRET_KEY = os.environ.get('SECRET_KEY') or hashlib.new(name='md5', string='ousi keji hawk@#').hexdigest()
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    OUSI_POSTS_PER_PAGE = 100


    @staticmethod
    # 此注释可表明使用类名可以直接调用该方法
    def init_app(app):  # 执行当前需要的环境的初始化
        pass


class DevelopmentConfig(Config):  # 开发环境
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'oracle+cx_oracle://' + os.path.join(basedir, 'data-dev.oracle')      # oracle://scott:redhat@192.168.0.107:1521/xe
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):     # 测试环境
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'oracle://' + os.path.join(basedir, 'data-test.oracle')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'oracle+cx_oracle://testmgr:%s@FTSZ-NB0045.cmrh.com:1521/testmgr' % 'test2018'


class ProductionConfig(Config):  # 生产环境
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'oracle://' + os.path.join(basedir, 'data.oracle')


config = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,
        'default': DevelopmentConfig
        }

