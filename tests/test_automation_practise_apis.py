import pytest
from endpoints.api_endpoints import AutomationPracticeEndpoints
from schemas.automation_pratice import AUTO_PRACTICE_ENDPOINTS_SCHEMA

@pytest.mark.rest_api_sanity
def test_automation_practice_api_validation(automation_practice_client, validator):
    get_automation_practice_url = AutomationPracticeEndpoints.GET_ALL_BRANDS
    response = automation_practice_client.get(get_automation_practice_url)
    assert response.status_code == 200
    assert (response.json()).get("responseCode") == 200, "The responseCode field is empty"
    assert (response.json()).get("brands") >= 1, "The brands field is empty"

    print(response.text)
    validator.validate_schema(response.json(),AUTO_PRACTICE_ENDPOINTS_SCHEMA)


