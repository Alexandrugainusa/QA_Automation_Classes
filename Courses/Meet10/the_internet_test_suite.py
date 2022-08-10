"""

"""
import unittest
import HtmlTestRunner  # pip install html-testRunner

from Courses.Meet10 import authentification_oop, context_menu, multi_tabs


class TestInternetSuite(unittest.TestCase):
    def test_suite(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(authentification_oop.TestAuth),
            unittest.defaultTestLoader.loadTestsFromTestCase(context_menu.TestContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(multi_tabs.TestMultiTabs)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Test Suite',
            report_name='My First Test Result'
        )

        runner.run(smoke_test)  # genereaza raportul HTML
