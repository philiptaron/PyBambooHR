"""Integration tests against the live BambooHR API.

These tests require BAMBOOHR_API_KEY and BAMBOOHR_SUBDOMAIN environment
variables to be set. They are skipped automatically when credentials are
not available.
"""

import datetime
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

    def _get_first_employee_id(self):
        employees = self.bamboo.get_employee_directory()
        return employees[0]["id"]

    # --- Employee endpoints ---

    def test_get_employee_directory(self):
        employees = self.bamboo.get_employee_directory()
        self.assertIsInstance(employees, list)
        self.assertGreater(len(employees), 0)
        first = employees[0]
        self.assertIn("id", first)

    def test_get_employee(self):
        employee_id = self._get_first_employee_id()
        employee = self.bamboo.get_employee(employee_id, ["firstName", "lastName"])
        self.assertIn("firstName", employee)
        self.assertIn("lastName", employee)

    def test_get_employee_all_fields(self):
        employee_id = self._get_first_employee_id()
        employee = self.bamboo.get_employee(employee_id)
        self.assertIn("id", employee)

    def test_get_all_employees(self):
        employees = self.bamboo.get_all_employees(field_list=["firstName", "lastName"])
        self.assertIsInstance(employees, dict)
        self.assertGreater(len(employees), 0)
        first_key = next(iter(employees))
        self.assertIn("firstName", employees[first_key])

    def test_get_employee_photo(self):
        employee_id = self._get_first_employee_id()
        try:
            content, content_type = self.bamboo.get_employee_photo(employee_id)
            # If the employee has a photo, we get bytes back
            self.assertIsInstance(content, bytes)
            self.assertGreater(len(content), 0)
        except Exception as e:
            # 404 is acceptable — employee may not have a photo
            if "404" in str(e):
                self.skipTest("Employee has no photo uploaded")
            raise

    def test_get_employee_files(self):
        employee_id = self._get_first_employee_id()
        files = self.bamboo.get_employee_files(employee_id)
        # Returns a dict with file category information
        self.assertIsInstance(files, dict)

    # --- Tabular data ---

    def test_get_tabular_data(self):
        data = self.bamboo.get_tabular_data("jobInfo")
        self.assertIsInstance(data, dict)

    def test_get_tabular_data_single_employee(self):
        employee_id = self._get_first_employee_id()
        data = self.bamboo.get_tabular_data("jobInfo", employee_id=employee_id)
        self.assertIsInstance(data, dict)

    # --- Change tracking ---

    def test_get_employee_changed_table(self):
        since = datetime.datetime(2020, 1, 1)
        result = self.bamboo.get_employee_changed_table(table_name="jobInfo", since=since)
        # Returns JSON with employee changes; could be a dict or list
        self.assertIsNotNone(result)

    def test_get_employee_changes(self):
        since = datetime.datetime(2020, 1, 1)
        result = self.bamboo.get_employee_changes(since=since)
        self.assertIsInstance(result, dict)
        # The response has an "employees" key
        self.assertIn("employees", result)

    # --- Time off ---

    def test_get_whos_out(self):
        result = self.bamboo.get_whos_out()
        # Returns a list of time-off events (may be empty)
        self.assertIsInstance(result, list)

    def test_get_whos_out_date_range(self):
        start = datetime.date.today()
        end = start + datetime.timedelta(days=30)
        result = self.bamboo.get_whos_out(start_date=start, end_date=end)
        self.assertIsInstance(result, list)

    def test_get_time_off_requests(self):
        start = datetime.date(2020, 1, 1)
        end = datetime.date.today()
        result = self.bamboo.get_time_off_requests(start_date=start, end_date=end)
        # Returns a list or dict depending on whether there are requests
        self.assertIsNotNone(result)

    # --- Reports ---

    def test_request_custom_report_json(self):
        result = self.bamboo.request_custom_report(
            ["firstName", "lastName"], report_format="json", title="Integration Test"
        )
        self.assertIsInstance(result, dict)
        self.assertIn("employees", result)

    def test_request_custom_report_csv(self):
        result = self.bamboo.request_custom_report(
            ["firstName", "lastName"], report_format="csv", title="Integration Test"
        )
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    # --- Metadata ---

    def test_get_meta_fields(self):
        fields = self.bamboo.get_meta_fields()
        self.assertIsInstance(fields, list)
        self.assertGreater(len(fields), 0)

    def test_get_meta_tables(self):
        tables = self.bamboo.get_meta_tables()
        self.assertIsInstance(tables, list)
        self.assertGreater(len(tables), 0)

    def test_get_meta_users(self):
        users = self.bamboo.get_meta_users()
        self.assertIsInstance(users, dict)
        self.assertGreater(len(users), 0)
