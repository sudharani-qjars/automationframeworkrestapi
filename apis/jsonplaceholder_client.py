from apis.base_client import BaseClient
from endpoints.api_endpoints import PostsEndpoints

class PostsClient(BaseClient):

    def get_post(self):
        return self.get(PostsEndpoints.GET_POST)