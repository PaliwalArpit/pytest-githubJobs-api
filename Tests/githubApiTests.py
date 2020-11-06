import pytest
import requests


# Testing github jobs api response content type
# Check api should work without auth
def test_get_github_jobs(get_base_url):
    response = requests.get(get_base_url + "/positions.json")
    assert "application/json" in response.headers["Content-Type"]
    assert response.status_code == 200


# Testing job location in param should be returned in response
def test_job_location_value(get_base_url):
    response = requests.get(get_base_url + "/positions.json?description=testing&location=berlin")
    assert response.status_code == 200
    json_res = response.json()
    for values in range(len(json_res) - 1):
        if json_res[values]['location'] == 'Berlin':
            assert True
        else:
            assert False


# Test git hub job api response with params description and location
@pytest.mark.parametrize('city', ["Berlin", "London"])
def test_get_param_response(get_base_url, city):
    for i in city:
        response = requests.get(get_base_url + "/positions.json?description=sdet&location=" + i + "")
        json_res = response.json()
        for values in range(len(json_res) - 1):
            if json_res[values]['location'] == city:
                assert True
            else:
                assert False  # assert response.status_code == 200


# Check for response objects
def test_reponse_objects(get_base_url):
    response = requests.get(get_base_url + "/positions.json?description=sdet&location=Berlin")
    json_res = response.json()
    for values in json_res:
        if json_res[values]['id'] in json_res or json_res[values]['type'] in json_res or json_res[values]['company_url'] in json_res or json_res[values]['title'] in json_res or json_res[values]['location'] in json_res:
            assert True
        else:
            assert False


# Testing job search query text in param should be returned in response
def test_job_search_value(get_base_url):
    response = requests.get(get_base_url + "/positions.json?search=Django")
    assert response.status_code == 200
    json_res = response.json()
    # Iterating through json response and finding searched value is present in response body
    for values in range(len(json_res) - 1):
        if "Django" in json_res[values]['description'] or "Django" in json_res[values]['title']:
            assert True
        else:
            assert False
