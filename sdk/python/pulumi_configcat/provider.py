# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProviderArgs', 'Provider']

@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *,
                 basic_auth_password: pulumi.Input[str],
                 basic_auth_username: pulumi.Input[str],
                 base_path: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input[str] basic_auth_password: ConfigCat Public API credential - Basic Auth Password
        :param pulumi.Input[str] basic_auth_username: ConfigCat Public API credential - Basic Auth Username.
        :param pulumi.Input[str] base_path: ConfigCat Public Management API Base Path (defaults to production).
        """
        pulumi.set(__self__, "basic_auth_password", basic_auth_password)
        pulumi.set(__self__, "basic_auth_username", basic_auth_username)
        if base_path is not None:
            pulumi.set(__self__, "base_path", base_path)

    @property
    @pulumi.getter(name="basicAuthPassword")
    def basic_auth_password(self) -> pulumi.Input[str]:
        """
        ConfigCat Public API credential - Basic Auth Password
        """
        return pulumi.get(self, "basic_auth_password")

    @basic_auth_password.setter
    def basic_auth_password(self, value: pulumi.Input[str]):
        pulumi.set(self, "basic_auth_password", value)

    @property
    @pulumi.getter(name="basicAuthUsername")
    def basic_auth_username(self) -> pulumi.Input[str]:
        """
        ConfigCat Public API credential - Basic Auth Username.
        """
        return pulumi.get(self, "basic_auth_username")

    @basic_auth_username.setter
    def basic_auth_username(self, value: pulumi.Input[str]):
        pulumi.set(self, "basic_auth_username", value)

    @property
    @pulumi.getter(name="basePath")
    def base_path(self) -> Optional[pulumi.Input[str]]:
        """
        ConfigCat Public Management API Base Path (defaults to production).
        """
        return pulumi.get(self, "base_path")

    @base_path.setter
    def base_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "base_path", value)


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
        :param pulumi.Input[str] base_path: ConfigCat Public Management API Base Path (defaults to production).
        :param pulumi.Input[str] basic_auth_password: ConfigCat Public API credential - Basic Auth Password
        :param pulumi.Input[str] basic_auth_username: ConfigCat Public API credential - Basic Auth Username.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProviderArgs,
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
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProviderArgs.__new__(ProviderArgs)

            __props__.__dict__["base_path"] = base_path
            if basic_auth_password is None and not opts.urn:
                raise TypeError("Missing required property 'basic_auth_password'")
            __props__.__dict__["basic_auth_password"] = basic_auth_password
            if basic_auth_username is None and not opts.urn:
                raise TypeError("Missing required property 'basic_auth_username'")
            __props__.__dict__["basic_auth_username"] = basic_auth_username
        super(Provider, __self__).__init__(
            'configcat',
            resource_name,
            __props__,
            opts)

    @property
    @pulumi.getter(name="basePath")
    def base_path(self) -> pulumi.Output[Optional[str]]:
        """
        ConfigCat Public Management API Base Path (defaults to production).
        """
        return pulumi.get(self, "base_path")

    @property
    @pulumi.getter(name="basicAuthPassword")
    def basic_auth_password(self) -> pulumi.Output[str]:
        """
        ConfigCat Public API credential - Basic Auth Password
        """
        return pulumi.get(self, "basic_auth_password")

    @property
    @pulumi.getter(name="basicAuthUsername")
    def basic_auth_username(self) -> pulumi.Output[str]:
        """
        ConfigCat Public API credential - Basic Auth Username.
        """
        return pulumi.get(self, "basic_auth_username")

