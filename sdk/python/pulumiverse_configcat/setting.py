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

__all__ = ['SettingArgs', 'Setting']

@pulumi.input_type
class SettingArgs:
    def __init__(__self__, *,
                 config_id: pulumi.Input[str],
                 key: pulumi.Input[str],
                 order: pulumi.Input[int],
                 hint: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 setting_type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Setting resource.
        :param pulumi.Input[str] config_id: The ID of the Config.
        :param pulumi.Input[str] key: The key of the Feature Flag/Setting.
        :param pulumi.Input[int] order: The order of the Setting within a Config (zero-based). If multiple Settings has the same order, they are displayed in alphabetical order.
        :param pulumi.Input[str] hint: The hint of the Setting.
        :param pulumi.Input[str] name: The name of the Setting.
        :param pulumi.Input[str] setting_type: Default: `boolean`. The Setting's type.  
               Available values: `boolean`|`string`|`int`|`double`.
        """
        pulumi.set(__self__, "config_id", config_id)
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "order", order)
        if hint is not None:
            pulumi.set(__self__, "hint", hint)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if setting_type is not None:
            pulumi.set(__self__, "setting_type", setting_type)

    @property
    @pulumi.getter(name="configId")
    def config_id(self) -> pulumi.Input[str]:
        """
        The ID of the Config.
        """
        return pulumi.get(self, "config_id")

    @config_id.setter
    def config_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "config_id", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key of the Feature Flag/Setting.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def order(self) -> pulumi.Input[int]:
        """
        The order of the Setting within a Config (zero-based). If multiple Settings has the same order, they are displayed in alphabetical order.
        """
        return pulumi.get(self, "order")

    @order.setter
    def order(self, value: pulumi.Input[int]):
        pulumi.set(self, "order", value)

    @property
    @pulumi.getter
    def hint(self) -> Optional[pulumi.Input[str]]:
        """
        The hint of the Setting.
        """
        return pulumi.get(self, "hint")

    @hint.setter
    def hint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hint", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Setting.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="settingType")
    def setting_type(self) -> Optional[pulumi.Input[str]]:
        """
        Default: `boolean`. The Setting's type.  
        Available values: `boolean`|`string`|`int`|`double`.
        """
        return pulumi.get(self, "setting_type")

    @setting_type.setter
    def setting_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "setting_type", value)


@pulumi.input_type
class _SettingState:
    def __init__(__self__, *,
                 config_id: Optional[pulumi.Input[str]] = None,
                 hint: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 order: Optional[pulumi.Input[int]] = None,
                 setting_type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Setting resources.
        :param pulumi.Input[str] config_id: The ID of the Config.
        :param pulumi.Input[str] hint: The hint of the Setting.
        :param pulumi.Input[str] key: The key of the Feature Flag/Setting.
        :param pulumi.Input[str] name: The name of the Setting.
        :param pulumi.Input[int] order: The order of the Setting within a Config (zero-based). If multiple Settings has the same order, they are displayed in alphabetical order.
        :param pulumi.Input[str] setting_type: Default: `boolean`. The Setting's type.  
               Available values: `boolean`|`string`|`int`|`double`.
        """
        if config_id is not None:
            pulumi.set(__self__, "config_id", config_id)
        if hint is not None:
            pulumi.set(__self__, "hint", hint)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if order is not None:
            pulumi.set(__self__, "order", order)
        if setting_type is not None:
            pulumi.set(__self__, "setting_type", setting_type)

    @property
    @pulumi.getter(name="configId")
    def config_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Config.
        """
        return pulumi.get(self, "config_id")

    @config_id.setter
    def config_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config_id", value)

    @property
    @pulumi.getter
    def hint(self) -> Optional[pulumi.Input[str]]:
        """
        The hint of the Setting.
        """
        return pulumi.get(self, "hint")

    @hint.setter
    def hint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hint", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        The key of the Feature Flag/Setting.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Setting.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input[int]]:
        """
        The order of the Setting within a Config (zero-based). If multiple Settings has the same order, they are displayed in alphabetical order.
        """
        return pulumi.get(self, "order")

    @order.setter
    def order(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "order", value)

    @property
    @pulumi.getter(name="settingType")
    def setting_type(self) -> Optional[pulumi.Input[str]]:
        """
        Default: `boolean`. The Setting's type.  
        Available values: `boolean`|`string`|`int`|`double`.
        """
        return pulumi.get(self, "setting_type")

    @setting_type.setter
    def setting_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "setting_type", value)


class Setting(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config_id: Optional[pulumi.Input[str]] = None,
                 hint: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 order: Optional[pulumi.Input[int]] = None,
                 setting_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## # Setting Resource

        Creates and manages a **Feature Flag/Setting**. [Read more about the anatomy of a Feature Flag or Setting.](https://configcat.com/docs/main-concepts)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_configcat as configcat
        import pulumiverse_configcat as configcat

        my_products = configcat.get_products(name_filter_regex="ConfigCat's product")
        my_configs = configcat.get_configurations(product_id=my_products.products[0].product_id,
            name_filter_regex="Main Config")
        my_setting = configcat.Setting("my_setting",
            config_id=my_configs.configs[0].config_id,
            key="isAwesomeFeatureEnabled",
            name="My awesome feature flag",
            hint="This is the hint for my awesome feature flag",
            setting_type="boolean",
            order=0)
        pulumi.export("settingId", my_setting.id)
        ```

        ## Endpoints used

        * [Get Flag](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/get-setting)
        * [Create Flag](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/create-setting)
        * [Update Flag](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/update-setting)
        * [Delete Flag](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/delete-setting)

        ## Import

        Feature Flags/Settings can be imported using the SettingId. Get the SettingId using e.g. the [List Flags API](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/get-settings).

        ```sh
        $ pulumi import configcat:index/setting:Setting example 1234
        ```
        Read more about importing.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] config_id: The ID of the Config.
        :param pulumi.Input[str] hint: The hint of the Setting.
        :param pulumi.Input[str] key: The key of the Feature Flag/Setting.
        :param pulumi.Input[str] name: The name of the Setting.
        :param pulumi.Input[int] order: The order of the Setting within a Config (zero-based). If multiple Settings has the same order, they are displayed in alphabetical order.
        :param pulumi.Input[str] setting_type: Default: `boolean`. The Setting's type.  
               Available values: `boolean`|`string`|`int`|`double`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SettingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## # Setting Resource

        Creates and manages a **Feature Flag/Setting**. [Read more about the anatomy of a Feature Flag or Setting.](https://configcat.com/docs/main-concepts)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_configcat as configcat
        import pulumiverse_configcat as configcat

        my_products = configcat.get_products(name_filter_regex="ConfigCat's product")
        my_configs = configcat.get_configurations(product_id=my_products.products[0].product_id,
            name_filter_regex="Main Config")
        my_setting = configcat.Setting("my_setting",
            config_id=my_configs.configs[0].config_id,
            key="isAwesomeFeatureEnabled",
            name="My awesome feature flag",
            hint="This is the hint for my awesome feature flag",
            setting_type="boolean",
            order=0)
        pulumi.export("settingId", my_setting.id)
        ```

        ## Endpoints used

        * [Get Flag](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/get-setting)
        * [Create Flag](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/create-setting)
        * [Update Flag](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/update-setting)
        * [Delete Flag](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/delete-setting)

        ## Import

        Feature Flags/Settings can be imported using the SettingId. Get the SettingId using e.g. the [List Flags API](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/get-settings).

        ```sh
        $ pulumi import configcat:index/setting:Setting example 1234
        ```
        Read more about importing.

        :param str resource_name: The name of the resource.
        :param SettingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SettingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config_id: Optional[pulumi.Input[str]] = None,
                 hint: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 order: Optional[pulumi.Input[int]] = None,
                 setting_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SettingArgs.__new__(SettingArgs)

            if config_id is None and not opts.urn:
                raise TypeError("Missing required property 'config_id'")
            __props__.__dict__["config_id"] = config_id
            __props__.__dict__["hint"] = hint
            if key is None and not opts.urn:
                raise TypeError("Missing required property 'key'")
            __props__.__dict__["key"] = key
            __props__.__dict__["name"] = name
            if order is None and not opts.urn:
                raise TypeError("Missing required property 'order'")
            __props__.__dict__["order"] = order
            __props__.__dict__["setting_type"] = setting_type
        super(Setting, __self__).__init__(
            'configcat:index/setting:Setting',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            config_id: Optional[pulumi.Input[str]] = None,
            hint: Optional[pulumi.Input[str]] = None,
            key: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            order: Optional[pulumi.Input[int]] = None,
            setting_type: Optional[pulumi.Input[str]] = None) -> 'Setting':
        """
        Get an existing Setting resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] config_id: The ID of the Config.
        :param pulumi.Input[str] hint: The hint of the Setting.
        :param pulumi.Input[str] key: The key of the Feature Flag/Setting.
        :param pulumi.Input[str] name: The name of the Setting.
        :param pulumi.Input[int] order: The order of the Setting within a Config (zero-based). If multiple Settings has the same order, they are displayed in alphabetical order.
        :param pulumi.Input[str] setting_type: Default: `boolean`. The Setting's type.  
               Available values: `boolean`|`string`|`int`|`double`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SettingState.__new__(_SettingState)

        __props__.__dict__["config_id"] = config_id
        __props__.__dict__["hint"] = hint
        __props__.__dict__["key"] = key
        __props__.__dict__["name"] = name
        __props__.__dict__["order"] = order
        __props__.__dict__["setting_type"] = setting_type
        return Setting(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="configId")
    def config_id(self) -> pulumi.Output[str]:
        """
        The ID of the Config.
        """
        return pulumi.get(self, "config_id")

    @property
    @pulumi.getter
    def hint(self) -> pulumi.Output[Optional[str]]:
        """
        The hint of the Setting.
        """
        return pulumi.get(self, "hint")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        """
        The key of the Feature Flag/Setting.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Setting.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def order(self) -> pulumi.Output[int]:
        """
        The order of the Setting within a Config (zero-based). If multiple Settings has the same order, they are displayed in alphabetical order.
        """
        return pulumi.get(self, "order")

    @property
    @pulumi.getter(name="settingType")
    def setting_type(self) -> pulumi.Output[Optional[str]]:
        """
        Default: `boolean`. The Setting's type.  
        Available values: `boolean`|`string`|`int`|`double`.
        """
        return pulumi.get(self, "setting_type")

