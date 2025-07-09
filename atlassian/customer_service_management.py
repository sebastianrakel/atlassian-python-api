# coding=utf-8
import logging

from .rest_client import AtlassianRestAPI

log = logging.getLogger(__name__)

ADMIN_URL = "https://api.atlassian.com"


class CustomerServiceManagement(AtlassianRestAPI):
    def __init__(self, cloud_id, *args, **kwargs):
        kwargs["api_root"] = f"jsm/csm/cloudid/{cloud_id}/api"
        kwargs["api_version"] = "v1"
        super(CustomerServiceManagement, self).__init__(url=ADMIN_URL, *args, **kwargs)

    def get_organization_detail_fields(self):
        """
        Returns a list of your organizations (based on your API key).
        :return:
        """
        url = self.resource_url("organization/details")
        return self.get(url)

    def create_organization_detail_fields(self, name, type_name, options=None):
        """
        Returns information about a single organization by ID
        :param name:
        :param type_name:
        :param options:
        :return:
        """
        data = {
            'name': name,
            'type': {
                'name': type_name,
                'options': options
            }
        }
        
        url = self.resource_url(f"organization/details", data)
        return self.post(url, data)

    def get_managed_accounts_in_organization(self, org_id, cursor=None):
        """
        Returns a list of accounts managed by the organization
        :param org_id:
        :param cursor:
        :return:
        """
        url = self.resource_url(f"orgs/{org_id}/users")
        params = {}
        if cursor:
            params["cursor"] = cursor
        return self.get(url, params=params)

    def get_organization(self, org_id):
        """
        Returns information about a single organization by ID
        :param org_id:
        :return:
        """
        
        url = self.resource_url(f"organization/{org_id}")
        return self.get(url)

    def set_organization_detail(self, org_id, field_name, values):
        """
        Returns information about a single organization by ID
        :param org_id:
        :param field_name:
        :param values:
        :return:
        """

        data = {
            "values": values
        }
        
        url = self.resource_url(f"organization/{org_id}/details?fieldName={field_name}")
        return self.put(url, data)

    def get_customer_detail_fields(self):
        """
        Returns a list of your customer (based on your API key).
        :return:
        """
        url = self.resource_url("customer/details")
        return self.get(url)

    def create_customer_detail_fields(self, name, type_name, options=None):
        """
        :param name:
        :param type_name:
        :param options:
        :return:
        """
        data = {
            'name': name,
            'type': {
                'name': type_name,
                'options': options
            }
        }
        
        url = self.resource_url(f"customer/details", data)
        return self.post(url, data)

    def get_customer(self, account_id):
        """
        Returns information about a single customer by account id
        :param account_id:
        :return:
        """
        
        url = self.resource_url(f"customer/{account_id}")
        return self.get(url)

    def set_customer_detail(self, account_id, field_name, values):
        """
        Set customer detail field
        :param account_id:
        :param field_name:
        :param values:
        :return:
        """

        data = {
            "values": values
        }
        
        url = self.resource_url(f"customer/{account_id}/details?fieldName={field_name}")
        return self.put(url, data)
