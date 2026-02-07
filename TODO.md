# PyBambooHR API Coverage

Cross-reference of the [BambooHR API](https://documentation.bamboohr.com/reference)
against what PyBambooHR implements. Checked February 2026.

## Employees

| Endpoint | Method | PyBambooHR | Notes |
|---|---|---|---|
| POST `/employees` | Create employee | `add_employee` | Requires firstName + lastName |
| GET `/employees/{id}` | Get employee | `get_employee` | Supports field_list filter |
| POST `/employees/{id}` | Update employee | `update_employee` | |
| GET `/employees/directory` | Get employee directory | `get_employee_directory` | Requires directory sharing enabled |
| GET `/company` | Get company information | -- | Not implemented |

`get_all_employees` is a composite method (not a single API call) that combines
`get_meta_users` + `get_employee_directory` + `get_employee` per user.

## Employee Photos

| Endpoint | Method | PyBambooHR | Notes |
|---|---|---|---|
| GET `/employees/{id}/photo/{size}` | Get employee photo | `get_employee_photo` | Returns (bytes, content_type) |
| POST `/employees/{id}/photo` | Upload employee photo | -- | Not implemented |

## Employee Files

| Endpoint | Method | PyBambooHR | Notes |
|---|---|---|---|
| GET `/employees/{id}/files/view/` | List employee files and categories | `get_employee_files` | Requests XML; parses with transform_table_data |
| POST `/employees/{id}/files/` | Upload employee file | `upload_employee_file` | |
| POST `/employees/files/category` | Create employee file category | -- | Not implemented |
| GET `/employees/files/{fileId}` | Download employee file | -- | Not implemented |
| POST `/employees/files/{fileId}` | Update employee file | -- | Not implemented |
| DELETE `/employees/files/{fileId}` | Delete employee file | -- | Not implemented |

## Company Files

| Endpoint | Method | PyBambooHR | Notes |
|---|---|---|---|
| GET `/files/view/` | List company files and categories | -- | Not implemented |
| POST `/files/` | Upload company file | -- | Not implemented |
| POST `/files/category` | Create company file category | -- | Not implemented |
| GET `/files/{fileId}` | Download company file | -- | Not implemented |
| POST `/files/{fileId}` | Update company file | -- | Not implemented |
| DELETE `/files/{fileId}` | Delete company file | -- | Not implemented |

## Tabular Data

| Endpoint | Method | PyBambooHR | Notes |
|---|---|---|---|
| GET `/employees/{id}/tables/{table}` | Get employee table rows | `get_tabular_data` | Requests XML; parses with transform_tabular_data |
| POST `/employees/{id}/tables/{table}/` | Add table row | `add_row` | |
| POST `/employees/{id}/tables/{table}/{rowId}/` | Update table row | `update_row` | |
| DELETE `/employees/{id}/tables/{table}/{rowId}` | Delete table row | -- | Not implemented |
| GET `/employees/changed/tables/{table}` | Get changed employee table data | `get_employee_changed_table` | Requires since datetime |

## Last Change Information

| Endpoint | Method | PyBambooHR | Notes |
|---|---|---|---|
| GET `/employees/changed/` | Get updated employee IDs | `get_employee_changes` | Requires since datetime; optional type filter |

## Reports

| Endpoint | Method | PyBambooHR | Notes |
|---|---|---|---|
| GET `/reports/{id}` | Get company report | `request_company_report` | Supports json/csv/pdf/xls/xml formats |
| POST `/reports/custom/` | Request custom report | `request_custom_report` | Supports field list + format + last_changed filter |

## Time Off

| Endpoint | Method | PyBambooHR | Notes |
|---|---|---|---|
| GET `/time_off/whos_out` | Get who's out | `get_whos_out` | Optional start/end date range |
| GET `/time_off/requests` | Get time off requests | `get_time_off_requests` | Optional start/end/status/type/employee filters |
| PUT `/time_off/requests` | Create time off request | -- | Not implemented |
| PUT `/time_off/requests/{id}/status` | Update time off request status | -- | Not implemented |
| PUT `/time_off/requests/{id}/history` | Add time off request history item | -- | Not implemented |
| GET `/time_off/policies` | Get time off policies | -- | Not implemented |
| GET `/time_off/types` | Get time off types | -- | Not implemented |
| GET `/time_off/estimate` | Estimate future time off balances | -- | Not implemented |
| PUT `/employees/{id}/time_off/balance` | Adjust time off balance | -- | Not implemented |
| PUT `/employees/{id}/time_off/policies` | Assign time off policies to employee | -- | Not implemented |
| GET `/employees/{id}/time_off/policies` | Get time off policies for employee | -- | Not implemented |

## Metadata

| Endpoint | Method | PyBambooHR | Notes |
|---|---|---|---|
| GET `/meta/fields/` | Get field metadata | `get_meta_fields` | |
| GET `/meta/tables/` | Get table metadata | `get_meta_tables` | Requests XML (no Accept header); parses with transform_table_data |
| GET `/meta/lists/` | Get list field values | `get_meta_lists` | Returns 403 with some API keys |
| GET `/meta/users/` | Get users | `get_meta_users` | |
| GET `/meta/countries/` | Get countries | -- | Not implemented |
| GET `/meta/countries/{countryId}/states/` | Get states by country | -- | Not implemented |
| PUT `/meta/lists/{listFieldId}` | Create or update list field values | -- | Not implemented |

## Goals

None of the Goals API is implemented.

| Endpoint | Method | Notes |
|---|---|---|
| POST `/goals` | Create goal | |
| GET `/goals` | Get goals | |
| GET `/goals/{id}` | Get goal aggregate | |
| PUT `/goals/{id}` | Update goal | Deprecated; use v1.1 |
| PUT `/goals/{id}` (v1.1) | Update goal v1.1 | |
| DELETE `/goals/{id}` | Delete goal | |
| POST `/goals/{id}/close` | Close goal | |
| POST `/goals/{id}/reopen` | Reopen goal | |
| PUT `/goals/{id}/progress` | Update goal progress | |
| PUT `/goals/{id}/milestone_progress` | Update milestone progress | |
| PUT `/goals/{id}/shared_with` | Update goal sharing | |
| POST `/goals/{id}/comments` | Create goal comment | |
| GET `/goals/{id}/comments` | Get goal comments | |
| PUT `/goals/{id}/comments/{commentId}` | Update goal comment | |
| DELETE `/goals/{id}/comments/{commentId}` | Delete goal comment | |
| GET `/goals/alignment_options` | Get alignable goal options | |
| GET `/goals/sharing_options` | Get goal sharing options | |
| GET `/goals/can_create` | Check goal creation permission | |
| GET `/goals/filters` (v1.1) | Get goal filters | |
| GET `/goals/status_counts` (v1.2) | Get goal status counts | |
| GET `/goals/aggregate` (v1.2) | Get goals aggregate | |

## Training

None of the Training API is implemented.

| Endpoint | Method | Notes |
|---|---|---|
| POST `/training/category` | Create training category | |
| GET `/training/category` | Get training categories | |
| PUT `/training/category/{id}` | Update training category | |
| DELETE `/training/category/{id}` | Delete training category | |
| POST `/training/type` | Create training type | |
| GET `/training/type` | Get training types | |
| PUT `/training/type/{id}` | Update training type | |
| DELETE `/training/type/{id}` | Delete training type | |
| POST `/employees/{id}/training` | Create employee training record | |
| GET `/employees/{id}/training` | Get employee training records | |
| PUT `/employees/{id}/training/{recordId}` | Update employee training record | |
| DELETE `/employees/{id}/training/{recordId}` | Delete employee training record | |

## Benefits

None of the Benefits API is implemented.

| Endpoint | Method | Notes |
|---|---|---|
| GET `/benefits` | Get company benefits | |
| GET `/employees/{id}/benefits` | Get employee benefits | |
| GET `/benefits/members/{id}` | Get member benefits | |
| GET `/benefits/members/{id}/events` | Get member benefit events | |
| GET `/benefits/coverages` | Get benefit coverages | |
| GET `/benefits/deduction_types` | Get benefit deduction types | |
| POST `/employees/{id}/dependents` | Create employee dependent | |
| GET `/employees/{id}/dependents` | Get employee dependents | |
| GET `/employees/{id}/dependents/{depId}` | Get employee dependent | |
| PUT `/employees/{id}/dependents/{depId}` | Update employee dependent | |

## Applicant Tracking (ATS)

None of the ATS API is implemented.

| Endpoint | Method | Notes |
|---|---|---|
| GET `/jobs` | Get job summaries | |
| POST `/jobs` | Create job opening | |
| GET `/locations` | Get company locations | |
| POST `/applicants` | Create candidate | |
| GET `/applicants/applications` | Get job applications | |
| GET `/applicants/applications/{id}` | Get job application details | |
| POST `/applicants/applications/{id}/comments` | Create job application comment | |
| GET `/applicants/statuses` | Get applicant statuses | |
| POST `/applicants/status` | Update applicant status | |
| GET `/hiring_leads` | Get hiring leads | |

## Hours and Time Tracking

None of the Hours or Time Tracking API is implemented.

| Endpoint | Method | Notes |
|---|---|---|
| POST `/hours` | Create hour record | |
| GET `/hours/{id}` | Get hour record | |
| PUT `/hours/{id}` | Update hour record | |
| DELETE `/hours/{id}` | Delete hour record | |
| POST `/hours/bulk` | Create or update hour records in bulk | |
| GET `/timesheet/entries` | Get timesheet entries | |
| POST `/timesheet/clock_in` | Clock in | |
| POST `/timesheet/clock_out` | Clock out | |
| POST `/timesheet/clock_entries` | Create or update timesheet clock entries | |
| POST `/timesheet/hour_entries` | Create or update timesheet hour entries | |
| POST `/timesheet/delete_clock_entries` | Delete timesheet clock entries | |
| POST `/timesheet/delete_hour_entries` | Delete timesheet hour entries | |
| POST `/time_tracking/project` | Create time tracking project | |

## Datasets

None of the Datasets API is implemented.

| Endpoint | Method | Notes |
|---|---|---|
| GET `/datasets` | Get datasets | |
| GET `/datasets/{id}/fields` | Get fields from dataset | |
| POST `/datasets/field_options` | Get field options | |
| POST `/datasets/data` | Get data from dataset | |

v1.2 variants also exist for datasets and field endpoints.

## Webhooks

None of the Webhooks API is implemented.

| Endpoint | Method | Notes |
|---|---|---|
| POST `/webhooks` | Create webhook | |
| GET `/webhooks` | Get webhooks | |
| GET `/webhooks/{id}` | Get webhook | |
| PUT `/webhooks/{id}` | Update webhook | |
| DELETE `/webhooks/{id}` | Delete webhook | |
| GET `/webhooks/{id}/logs` | Get webhook logs | |
| GET `/webhooks/fields` | Get monitor fields | |

## Login

| Endpoint | Method | Notes |
|---|---|---|
| POST `/login` | User login | Deprecated by BambooHR |
