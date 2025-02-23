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

__all__ = ['SettingTagArgs', 'SettingTag']

@pulumi.input_type
class SettingTagArgs:
    def __init__(__self__, *,
                 setting_id: pulumi.Input[str],
                 tag_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a SettingTag resource.
        :param pulumi.Input[str] setting_id: The ID of the Feature Flag or Setting.
        :param pulumi.Input[str] tag_id: The ID of the Tag.
        """
        pulumi.set(__self__, "setting_id", setting_id)
        pulumi.set(__self__, "tag_id", tag_id)

    @property
    @pulumi.getter(name="settingId")
    def setting_id(self) -> pulumi.Input[str]:
        """
        The ID of the Feature Flag or Setting.
        """
        return pulumi.get(self, "setting_id")

    @setting_id.setter
    def setting_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "setting_id", value)

    @property
    @pulumi.getter(name="tagId")
    def tag_id(self) -> pulumi.Input[str]:
        """
        The ID of the Tag.
        """
        return pulumi.get(self, "tag_id")

    @tag_id.setter
    def tag_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "tag_id", value)


@pulumi.input_type
class _SettingTagState:
    def __init__(__self__, *,
                 setting_id: Optional[pulumi.Input[str]] = None,
                 tag_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SettingTag resources.
        :param pulumi.Input[str] setting_id: The ID of the Feature Flag or Setting.
        :param pulumi.Input[str] tag_id: The ID of the Tag.
        """
        if setting_id is not None:
            pulumi.set(__self__, "setting_id", setting_id)
        if tag_id is not None:
            pulumi.set(__self__, "tag_id", tag_id)

    @property
    @pulumi.getter(name="settingId")
    def setting_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Feature Flag or Setting.
        """
        return pulumi.get(self, "setting_id")

    @setting_id.setter
    def setting_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "setting_id", value)

    @property
    @pulumi.getter(name="tagId")
    def tag_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Tag.
        """
        return pulumi.get(self, "tag_id")

    @tag_id.setter
    def tag_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tag_id", value)


class SettingTag(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 setting_id: Optional[pulumi.Input[str]] = None,
                 tag_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Adds/Removes **Tags** to/from **Feature Flags or Settings**.

        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_configcat as configcat

        config = pulumi.Config()
        setting_id = config.require("settingId")
        tag_id = config.require("tagId")
        my_setting_tag = configcat.SettingTag("my_setting_tag",
            setting_id=setting_id,
            tag_id=tag_id)
        ```

        ## Import

        Setting Tags can be imported using a combined SettingId:TagId ID.

        Get the SettingId using e.g. the [List Flags API](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/get-settings).

        Get the TagId using e.g. the [List Tags API](https://api.configcat.com/docs/#tag/Tags/operation/get-tags).

        ```sh
        $ pulumi import configcat:index/settingTag:SettingTag example 1234:5678
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] setting_id: The ID of the Feature Flag or Setting.
        :param pulumi.Input[str] tag_id: The ID of the Tag.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SettingTagArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Adds/Removes **Tags** to/from **Feature Flags or Settings**.

        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_configcat as configcat

        config = pulumi.Config()
        setting_id = config.require("settingId")
        tag_id = config.require("tagId")
        my_setting_tag = configcat.SettingTag("my_setting_tag",
            setting_id=setting_id,
            tag_id=tag_id)
        ```

        ## Import

        Setting Tags can be imported using a combined SettingId:TagId ID.

        Get the SettingId using e.g. the [List Flags API](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/get-settings).

        Get the TagId using e.g. the [List Tags API](https://api.configcat.com/docs/#tag/Tags/operation/get-tags).

        ```sh
        $ pulumi import configcat:index/settingTag:SettingTag example 1234:5678
        ```

        :param str resource_name: The name of the resource.
        :param SettingTagArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SettingTagArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 setting_id: Optional[pulumi.Input[str]] = None,
                 tag_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SettingTagArgs.__new__(SettingTagArgs)

            if setting_id is None and not opts.urn:
                raise TypeError("Missing required property 'setting_id'")
            __props__.__dict__["setting_id"] = setting_id
            if tag_id is None and not opts.urn:
                raise TypeError("Missing required property 'tag_id'")
            __props__.__dict__["tag_id"] = tag_id
        super(SettingTag, __self__).__init__(
            'configcat:index/settingTag:SettingTag',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            setting_id: Optional[pulumi.Input[str]] = None,
            tag_id: Optional[pulumi.Input[str]] = None) -> 'SettingTag':
        """
        Get an existing SettingTag resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] setting_id: The ID of the Feature Flag or Setting.
        :param pulumi.Input[str] tag_id: The ID of the Tag.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SettingTagState.__new__(_SettingTagState)

        __props__.__dict__["setting_id"] = setting_id
        __props__.__dict__["tag_id"] = tag_id
        return SettingTag(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="settingId")
    def setting_id(self) -> pulumi.Output[str]:
        """
        The ID of the Feature Flag or Setting.
        """
        return pulumi.get(self, "setting_id")

    @property
    @pulumi.getter(name="tagId")
    def tag_id(self) -> pulumi.Output[str]:
        """
        The ID of the Tag.
        """
        return pulumi.get(self, "tag_id")

