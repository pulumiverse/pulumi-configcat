# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetOrganizationsResult',
    'AwaitableGetOrganizationsResult',
    'get_organizations',
    'get_organizations_output',
]

@pulumi.output_type
class GetOrganizationsResult:
    """
    A collection of values returned by getOrganizations.
    """
    def __init__(__self__, id=None, name_filter_regex=None, organizations=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name_filter_regex and not isinstance(name_filter_regex, str):
            raise TypeError("Expected argument 'name_filter_regex' to be a str")
        pulumi.set(__self__, "name_filter_regex", name_filter_regex)
        if organizations and not isinstance(organizations, list):
            raise TypeError("Expected argument 'organizations' to be a list")
        pulumi.set(__self__, "organizations", organizations)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="nameFilterRegex")
    def name_filter_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_filter_regex")

    @property
    @pulumi.getter
    def organizations(self) -> Sequence['outputs.GetOrganizationsOrganizationResult']:
        """
        An organization list block defined as below.
        """
        return pulumi.get(self, "organizations")


class AwaitableGetOrganizationsResult(GetOrganizationsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOrganizationsResult(
            id=self.id,
            name_filter_regex=self.name_filter_regex,
            organizations=self.organizations)


def get_organizations(name_filter_regex: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOrganizationsResult:
    """
    ## # get_organizations Resource

    Use this data source to access information about existing **Organizations**. [What is an Organization in ConfigCat?](https://configcat.com/docs/main-concepts)

    ## Example Usage

    ```python
    import pulumi
    import pulumi_configcat as configcat

    my_organizations = configcat.get_organizations(name_filter_regex="ConfigCat")
    pulumi.export("organizationId", my_organizations.organizations[0].organization_id)
    ```

    ## Endpoints used

    - [List Organizations](https://api.configcat.com/docs/#tag/Organizations/operation/get-organizations)


    :param str name_filter_regex: Filter the Organizations by name.
    """
    __args__ = dict()
    __args__['nameFilterRegex'] = name_filter_regex
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('configcat:index/getOrganizations:getOrganizations', __args__, opts=opts, typ=GetOrganizationsResult).value

    return AwaitableGetOrganizationsResult(
        id=pulumi.get(__ret__, 'id'),
        name_filter_regex=pulumi.get(__ret__, 'name_filter_regex'),
        organizations=pulumi.get(__ret__, 'organizations'))


@_utilities.lift_output_func(get_organizations)
def get_organizations_output(name_filter_regex: Optional[pulumi.Input[Optional[str]]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOrganizationsResult]:
    """
    ## # get_organizations Resource

    Use this data source to access information about existing **Organizations**. [What is an Organization in ConfigCat?](https://configcat.com/docs/main-concepts)

    ## Example Usage

    ```python
    import pulumi
    import pulumi_configcat as configcat

    my_organizations = configcat.get_organizations(name_filter_regex="ConfigCat")
    pulumi.export("organizationId", my_organizations.organizations[0].organization_id)
    ```

    ## Endpoints used

    - [List Organizations](https://api.configcat.com/docs/#tag/Organizations/operation/get-organizations)


    :param str name_filter_regex: Filter the Organizations by name.
    """
    ...
