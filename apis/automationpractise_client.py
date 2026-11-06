from apis.base_client import BaseClient
from endpoints.api_endpoints import AutomationPracticeEndpoints

class AutomationPracticeClient(BaseClient):

    def get_all_brands(self):
        return self.get(AutomationPracticeEndpoints.GET_ALL_BRANDS)