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

__all__ = ['ProviderArgs', 'Provider']

@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *,
                 base_path: Optional[pulumi.Input[str]] = None,
                 basic_auth_password: Optional[pulumi.Input[str]] = None,
                 basic_auth_username: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input[str] base_path: ConfigCat Public Management API's `base_path`. Defaults to [https://api.configcat.com](https://api.configcat.com). This
               can also be sourced from the `CONFIGCAT_BASE_PATH` Environment Variable.
        :param pulumi.Input[str] basic_auth_password: Get your `basic_auth_password` at [ConfigCat Public API
               credentials](https://app.configcat.com/my-account/public-api-credentials). This can also be sourced from the
               `CONFIGCAT_BASIC_AUTH_PASSWORD` Environment Variable.
        :param pulumi.Input[str] basic_auth_username: Get your `basic_auth_username` at [ConfigCat Public API
               credentials](https://app.configcat.com/my-account/public-api-credentials). This can also be sourced from the
               `CONFIGCAT_BASIC_AUTH_USERNAME` Environment Variable.
        """
        if base_path is None:
            base_path = _utilities.get_env('CONFIGCAT_BASE_PATH')
        if base_path is not None:
            pulumi.set(__self__, "base_path", base_path)
        if basic_auth_password is None:
            basic_auth_password = _utilities.get_env('CONFIGCAT_BASIC_AUTH_PASSWORD')
        if basic_auth_password is not None:
            pulumi.set(__self__, "basic_auth_password", basic_auth_password)
        if basic_auth_username is None:
            basic_auth_username = _utilities.get_env('CONFIGCAT_BASIC_AUTH_USERNAME')
        if basic_auth_username is not None:
            pulumi.set(__self__, "basic_auth_username", basic_auth_username)

    @property
    @pulumi.getter(name="basePath")
    def base_path(self) -> Optional[pulumi.Input[str]]:
        """
        ConfigCat Public Management API's `base_path`. Defaults to [https://api.configcat.com](https://api.configcat.com). This
        can also be sourced from the `CONFIGCAT_BASE_PATH` Environment Variable.
        """
        return pulumi.get(self, "base_path")

    @base_path.setter
    def base_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "base_path", value)

    @property
    @pulumi.getter(name="basicAuthPassword")
    def basic_auth_password(self) -> Optional[pulumi.Input[str]]:
        """
        Get your `basic_auth_password` at [ConfigCat Public API
        credentials](https://app.configcat.com/my-account/public-api-credentials). This can also be sourced from the
        `CONFIGCAT_BASIC_AUTH_PASSWORD` Environment Variable.
        """
        return pulumi.get(self, "basic_auth_password")

    @basic_auth_password.setter
    def basic_auth_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "basic_auth_password", value)

    @property
    @pulumi.getter(name="basicAuthUsername")
    def basic_auth_username(self) -> Optional[pulumi.Input[str]]:
        """
        Get your `basic_auth_username` at [ConfigCat Public API
        credentials](https://app.configcat.com/my-account/public-api-credentials). This can also be sourced from the
        `CONFIGCAT_BASIC_AUTH_USERNAME` Environment Variable.
        """
        return pulumi.get(self, "basic_auth_username")

    @basic_auth_username.setter
    def basic_auth_username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "basic_auth_username", value)


class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 base_path: Optional[pulumi.Input[str]] = None,
                 basic_auth_password: Optional[pulumi.Input[str]] = None,
                 basic_auth_username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The provider type for the configcat package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] base_path: ConfigCat Public Management API's `base_path`. Defaults to [https://api.configcat.com](https://api.configcat.com). This
               can also be sourced from the `CONFIGCAT_BASE_PATH` Environment Variable.
        :param pulumi.Input[str] basic_auth_password: Get your `basic_auth_password` at [ConfigCat Public API
               credentials](https://app.configcat.com/my-account/public-api-credentials). This can also be sourced from the
               `CONFIGCAT_BASIC_AUTH_PASSWORD` Environment Variable.
        :param pulumi.Input[str] basic_auth_username: Get your `basic_auth_username` at [ConfigCat Public API
               credentials](https://app.configcat.com/my-account/public-api-credentials). This can also be sourced from the
               `CONFIGCAT_BASIC_AUTH_USERNAME` Environment Variable.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ProviderArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The provider type for the configcat package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param ProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 base_path: Optional[pulumi.Input[str]] = None,
                 basic_auth_password: Optional[pulumi.Input[str]] = None,
                 basic_auth_username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProviderArgs.__new__(ProviderArgs)

            if base_path is None:
                base_path = _utilities.get_env('CONFIGCAT_BASE_PATH')
            __props__.__dict__["base_path"] = base_path
            if basic_auth_password is None:
                basic_auth_password = _utilities.get_env('CONFIGCAT_BASIC_AUTH_PASSWORD')
            __props__.__dict__["basic_auth_password"] = None if basic_auth_password is None else pulumi.Output.secret(basic_auth_password)
            if basic_auth_username is None:
                basic_auth_username = _utilities.get_env('CONFIGCAT_BASIC_AUTH_USERNAME')
            __props__.__dict__["basic_auth_username"] = basic_auth_username
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["basicAuthPassword"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Provider, __self__).__init__(
            'configcat',
            resource_name,
            __props__,
            opts)

    @property
    @pulumi.getter(name="basePath")
    def base_path(self) -> pulumi.Output[Optional[str]]:
        """
        ConfigCat Public Management API's `base_path`. Defaults to [https://api.configcat.com](https://api.configcat.com). This
        can also be sourced from the `CONFIGCAT_BASE_PATH` Environment Variable.
        """
        return pulumi.get(self, "base_path")

    @property
    @pulumi.getter(name="basicAuthPassword")
    def basic_auth_password(self) -> pulumi.Output[Optional[str]]:
        """
        Get your `basic_auth_password` at [ConfigCat Public API
        credentials](https://app.configcat.com/my-account/public-api-credentials). This can also be sourced from the
        `CONFIGCAT_BASIC_AUTH_PASSWORD` Environment Variable.
        """
        return pulumi.get(self, "basic_auth_password")

    @property
    @pulumi.getter(name="basicAuthUsername")
    def basic_auth_username(self) -> pulumi.Output[Optional[str]]:
        """
        Get your `basic_auth_username` at [ConfigCat Public API
        credentials](https://app.configcat.com/my-account/public-api-credentials). This can also be sourced from the
        `CONFIGCAT_BASIC_AUTH_USERNAME` Environment Variable.
        """
        return pulumi.get(self, "basic_auth_username")

