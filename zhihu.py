#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2020-11-12 22:04:24
# Project: zhihu

from pyspider.libs.base_handler import *
import pymysql
import random


class Handler(BaseHandler):
    crawl_config = {
        'itag': 'v22',
        'headers': {
            'User-Agent': 'GoogleBot',
            'Host': 'www.zhihu.com',
        }
    }

    def __init__(self):
        self.db = pymysql.connect('localhost', 'root', 'root', 'wenda', charset='utf8')

    def add_question(self, title, content, comment_count):
        try:
            cursor = self.db.cursor()
            sql = 'insert into question(title, content, user_id, created_date, comment_count) values("%s", "%s", %d, now(), %d)' % (
            title, content, random.randint(1, 10), comment_count)
            print(sql)
            cursor.execute(sql)
            print(cursor.lastrowid)
            self.db.commit()
            return qid
        except Exception as e:
            print(e)
            self.db.rollback()
        return 0

    def add_comment(self, qid, comment):
        try:
            cursor = self.db.cursor()
            sql = 'insert into comment(content, entity_type, entity_id, user_id, create_date) values("%s",1, %d, %d, now())' % (
            comment, qid, random.randint(1, 10))
            print(sql)
            cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://www.zhihu.com/topic/19550228/top-answers', callback=self.index_page, validate_cert=False)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a.question.link').items():
            self.crawl(each.attr.href, callback=self.detail_page, validate_cert=False)
        for each in response.doc('div.zm-invite-pager span a').items():
            self.crawl(each.attr.href, callback=self.index_page, validate_cert=False)

    @config(priority=2)
    def detail_page(self, response):
        items = response.doc('div.zm-editable-content.clearfix').items()
        title = response.doc('span.zm-editable-content').text()
        html = response.doc('div.zh-question-detail').html()
        if html == None:
            html = ''
        content = html.replace('"', '\\"')
        qid = self.add_question(title, content, sum(1 for x in items))
        for each in response.doc('div.zm-editable-content.clearfix').items():
            self.add_comment(qid, each.html().replace('"', '\\"'))

        return {
            "url": response.url,
            "title": response.doc('title').text(),
        }
