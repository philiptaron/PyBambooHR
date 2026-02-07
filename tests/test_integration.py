"""Integration tests against the live BambooHR API.

These tests require BAMBOOHR_API_KEY and BAMBOOHR_SUBDOMAIN environment
variables to be set. They are skipped automatically when credentials are
not available.
"""

import os
import unittest

from PyBambooHR import PyBambooHR

API_KEY = os.environ.get("BAMBOOHR_API_KEY", "")
SUBDOMAIN = os.environ.get("BAMBOOHR_SUBDOMAIN", "")
HAVE_CREDENTIALS = bool(API_KEY and SUBDOMAIN)


@unittest.skipUnless(HAVE_CREDENTIALS, "BAMBOOHR_API_KEY and BAMBOOHR_SUBDOMAIN not set")
class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.bamboo = PyBambooHR(subdomain=SUBDOMAIN, api_key=API_KEY)

    def test_get_employee_directory(self):
        employees = self.bamboo.get_employee_directory()
        self.assertIsInstance(employees, list)
        # A BambooHR account should have at least one employee
        self.assertGreater(len(employees), 0)
        # Each entry should have an id
        first = employees[0]
        self.assertIn("id", first)

    def test_get_employee(self):
        # Employee 0 is a special "all" sentinel in BambooHR; use the
        # directory to find a real employee ID.
        employees = self.bamboo.get_employee_directory()
        employee_id = employees[0]["id"]

        employee = self.bamboo.get_employee(employee_id, ["firstName", "lastName"])
        self.assertIn("firstName", employee)
        self.assertIn("lastName", employee)

    def test_get_meta_fields(self):
        fields = self.bamboo.get_meta_fields()
        self.assertIsInstance(fields, list)
        self.assertGreater(len(fields), 0)

    def test_get_meta_users(self):
        users = self.bamboo.get_meta_users()
        self.assertIsInstance(users, dict)
        self.assertGreater(len(users), 0)

    def test_get_meta_lists(self):
        lists = self.bamboo.get_meta_lists()
        self.assertIsInstance(lists, list)
