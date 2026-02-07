# PyBambooHR

An unofficial Python wrapper for the [BambooHR API](https://documentation.bamboohr.com/reference).

Originally created by Scott Blevins. Now maintained by Philip Taron.

## Installation

```bash
pip install PyBambooHR
```

## Usage

Configure your API credentials either by passing them directly or via environment variables:

```bash
export BAMBOOHR_API_KEY='yourapikeyhere'
export BAMBOOHR_SUBDOMAIN='yoursub'
```

```python
from PyBambooHR import PyBambooHR

# Credentials from environment variables
bamboo = PyBambooHR()

# Or pass them explicitly
bamboo = PyBambooHR(subdomain='yoursub', api_key='yourapikeyhere')
```

### Get Employee Directory

Note: you must enable sharing the employee directory in BambooHR to use this method.

```python
employees = bamboo.get_employee_directory()
```

### Get Employee

```python
# Jim's employee ID is 123 and we are not specifying fields so this will get all of them.
jim = bamboo.get_employee(123)

# Pam's employee ID is 222 and we are specifying fields so this will get only the ones we request.
pam = bamboo.get_employee(222, ['city', 'workPhone', 'workEmail'])
```

### Add Employee

```python
# The firstName and lastName keys are required...
employee = {'firstName': 'Test', 'lastName': 'Person'}

result = bamboo.add_employee(employee)
# result contains 'id' and 'url' keys
```

### Update Employee

```python
employee = {'firstName': 'Another', 'lastName': 'Namenow'}

result = bamboo.update_employee(333, employee)
# result is True on success
```

### Request a Report

```python
# Get a JSON report by ID
result = bamboo.request_company_report(1, report_format='json', filter_duplicates=True)

for employee in result['employees']:
    print(employee)

# Save a PDF report to disk
result = bamboo.request_company_report(1, report_format='pdf', output_filename='/tmp/report.pdf')
```

### Scheduled Future Information

BambooHR has effective dates for when promotions are scheduled or when new hires will join. To see these events before they happen:

```python
bamboo = PyBambooHR(subdomain='yoursub', api_key='yourapikeyhere', only_current=False)
```

This works for reports and employee information but not the employee directory.

## Development

```bash
pip install -e ".[test]"
pytest
```

## License

MIT
