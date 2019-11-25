import unittest
from unittest.mock import patch
from rss_reader import collect_news
from expected_results import normal_result, json_result, html_result


def testCollectNews(self):
    self.assertEqual(collect_news.collectNews(1, False, '', '', ['','',''], self.item), normal_result)
    self.assertEqual(collect_news.collectNews(1, True, '', '', ['','',''], self.item)[2], json_result)
    self.assertEqual(collect_news.collectNews(1, False, 'tohtml', '', ['','',''], self.item), html_result)

