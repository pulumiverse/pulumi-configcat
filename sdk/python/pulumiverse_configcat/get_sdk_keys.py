# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities

__all__ = [
    'GetSdkKeysResult',
    'AwaitableGetSdkKeysResult',
    'get_sdk_keys',
    'get_sdk_keys_output',
]

@pulumi.output_type
class GetSdkKeysResult:
    """
    A collection of values returned by getSdkKeys.
    """
    def __init__(__self__, config_id=None, environment_id=None, id=None, primary=None, secondary=None):
        if config_id and not isinstance(config_id, str):
            raise TypeError("Expected argument 'config_id' to be a str")
        pulumi.set(__self__, "config_id", config_id)
        if environment_id and not isinstance(environment_id, str):
            raise TypeError("Expected argument 'environment_id' to be a str")
        pulumi.set(__self__, "environment_id", environment_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if primary and not isinstance(primary, str):
            raise TypeError("Expected argument 'primary' to be a str")
        pulumi.set(__self__, "primary", primary)
        if secondary and not isinstance(secondary, str):
            raise TypeError("Expected argument 'secondary' to be a str")
        pulumi.set(__self__, "secondary", secondary)

    @property
    @pulumi.getter(name="configId")
    def config_id(self) -> str:
        return pulumi.get(self, "config_id")

    @property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> str:
        return pulumi.get(self, "environment_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def primary(self) -> str:
        """
        The primary SDK Key associated with your **Config** and **Environment**.
        """
        return pulumi.get(self, "primary")

    @property
    @pulumi.getter
    def secondary(self) -> str:
        """
        The secondary SDK Key associated with your **Config** and **Environment**.
        """
        return pulumi.get(self, "secondary")


class AwaitableGetSdkKeysResult(GetSdkKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSdkKeysResult(
            config_id=self.config_id,
            environment_id=self.environment_id,
            id=self.id,
            primary=self.primary,
            secondary=self.secondary)


def get_sdk_keys(config_id: Optional[str] = None,
                 environment_id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSdkKeysResult:
    """
    ## # get_sdk_keys Resource

    Use this data source to access information about **SDK Keys**.
    ## Example Usage

    ```python
    import pulumi
    import pulumi_configcat as configcat

    my_products = configcat.get_products(name_filter_regex="ConfigCat's product")
    my_configs = configcat.get_configs(product_id=my_products.products[0].product_id,
        name_filter_regex="Main Config")
    my_environments = configcat.get_environments(product_id=my_products.products[0].product_id,
        name_filter_regex="Test")
    my_sdkkey = configcat.get_sdk_keys(config_id=my_configs.configs[0].config_id,
        environment_id=my_environments.environments[0].environment_id)
    pulumi.export("primarySdkkey", my_sdkkey.primary)
    pulumi.export("secondarySdkkey", my_sdkkey.secondary)
    ```

    ## Endpoints used

    - [Get SDK Key](https://api.configcat.com/docs/#tag/SDK-Keys/operation/get-sdk-keys)


    :param str config_id: The ID of the Config.
    :param str environment_id: The ID of the Environment.
    """
    __args__ = dict()
    __args__['configId'] = config_id
    __args__['environmentId'] = environment_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('configcat:index/getSdkKeys:getSdkKeys', __args__, opts=opts, typ=GetSdkKeysResult).value

    return AwaitableGetSdkKeysResult(
        config_id=pulumi.get(__ret__, 'config_id'),
        environment_id=pulumi.get(__ret__, 'environment_id'),
        id=pulumi.get(__ret__, 'id'),
        primary=pulumi.get(__ret__, 'primary'),
        secondary=pulumi.get(__ret__, 'secondary'))
def get_sdk_keys_output(config_id: Optional[pulumi.Input[str]] = None,
                        environment_id: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSdkKeysResult]:
    """
    ## # get_sdk_keys Resource

    Use this data source to access information about **SDK Keys**.
    ## Example Usage

    ```python
    import pulumi
    import pulumi_configcat as configcat

    my_products = configcat.get_products(name_filter_regex="ConfigCat's product")
    my_configs = configcat.get_configs(product_id=my_products.products[0].product_id,
        name_filter_regex="Main Config")
    my_environments = configcat.get_environments(product_id=my_products.products[0].product_id,
        name_filter_regex="Test")
    my_sdkkey = configcat.get_sdk_keys(config_id=my_configs.configs[0].config_id,
        environment_id=my_environments.environments[0].environment_id)
    pulumi.export("primarySdkkey", my_sdkkey.primary)
    pulumi.export("secondarySdkkey", my_sdkkey.secondary)
    ```

    ## Endpoints used

    - [Get SDK Key](https://api.configcat.com/docs/#tag/SDK-Keys/operation/get-sdk-keys)


    :param str config_id: The ID of the Config.
    :param str environment_id: The ID of the Environment.
    """
    __args__ = dict()
    __args__['configId'] = config_id
    __args__['environmentId'] = environment_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('configcat:index/getSdkKeys:getSdkKeys', __args__, opts=opts, typ=GetSdkKeysResult)
    return __ret__.apply(lambda __response__: GetSdkKeysResult(
        config_id=pulumi.get(__response__, 'config_id'),
        environment_id=pulumi.get(__response__, 'environment_id'),
        id=pulumi.get(__response__, 'id'),
        primary=pulumi.get(__response__, 'primary'),
        secondary=pulumi.get(__response__, 'secondary')))
