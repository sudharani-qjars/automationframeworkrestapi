import pytest
from endpoints.api_endpoints import PostsEndpoints
from schemas.post_schema import POST_SCHEMA

@pytest.mark.rest_api_sanity
def test_posts_api_validation(posts_client, test_data_reader, validator):
    post_id = test_data_reader["post_id"]
    get_posts_url = PostsEndpoints.GET_POST.format(post_id=post_id)
    response = posts_client.get(get_posts_url)
    assert response.status_code == 200
    assert (response.json()).get("userId") is not None, "The userId field is empty"
    assert (response.json()).get("id") is not None, "The id field is empty"
    assert (response.json()).get("title") is not None, "The title field is empty"
    assert (response.json()).get("body") is not None, "The body field is empty"
    print(response.text)
    validator.validate_schema(response.json(),POST_SCHEMA)


