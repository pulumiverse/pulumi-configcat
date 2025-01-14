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
from . import outputs
from ._inputs import *

__all__ = ['SettingValueArgs', 'SettingValue']

@pulumi.input_type
class SettingValueArgs:
    def __init__(__self__, *,
                 environment_id: pulumi.Input[str],
                 setting_id: pulumi.Input[str],
                 value: pulumi.Input[str],
                 init_only: Optional[pulumi.Input[bool]] = None,
                 mandatory_notes: Optional[pulumi.Input[str]] = None,
                 percentage_items: Optional[pulumi.Input[Sequence[pulumi.Input['SettingValuePercentageItemArgs']]]] = None,
                 rollout_rules: Optional[pulumi.Input[Sequence[pulumi.Input['SettingValueRolloutRuleArgs']]]] = None):
        """
        The set of arguments for constructing a SettingValue resource.
        :param pulumi.Input[str] environment_id: The ID of the Environment.
        :param pulumi.Input[str] setting_id: The ID of the Feature Flag/Setting.
        :param pulumi.Input[str] value: The Setting's value. Type: `string`. It must be compatible with the `setting_type`.
        :param pulumi.Input[bool] init_only: Default: true. Read more below.  
               
               The Feature Flag/Setting's value
        :param pulumi.Input[str] mandatory_notes: Default: "". If the Product's "Mandatory notes" preference is turned on for the Environment the Mandatory note must be passed.
        :param pulumi.Input[Sequence[pulumi.Input['SettingValuePercentageItemArgs']]] percentage_items: A list to define [Percentage items](https://configcat.com/docs/advanced/targeting/#targeting-a-percentage-of-users). Read more below.
        :param pulumi.Input[Sequence[pulumi.Input['SettingValueRolloutRuleArgs']]] rollout_rules: A list to define [Rollout rules](https://configcat.com/docs/advanced/targeting/#anatomy-of-a-targeting-rule). Read more below.
        """
        pulumi.set(__self__, "environment_id", environment_id)
        pulumi.set(__self__, "setting_id", setting_id)
        pulumi.set(__self__, "value", value)
        if init_only is not None:
            pulumi.set(__self__, "init_only", init_only)
        if mandatory_notes is not None:
            pulumi.set(__self__, "mandatory_notes", mandatory_notes)
        if percentage_items is not None:
            pulumi.set(__self__, "percentage_items", percentage_items)
        if rollout_rules is not None:
            pulumi.set(__self__, "rollout_rules", rollout_rules)

    @property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> pulumi.Input[str]:
        """
        The ID of the Environment.
        """
        return pulumi.get(self, "environment_id")

    @environment_id.setter
    def environment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "environment_id", value)

    @property
    @pulumi.getter(name="settingId")
    def setting_id(self) -> pulumi.Input[str]:
        """
        The ID of the Feature Flag/Setting.
        """
        return pulumi.get(self, "setting_id")

    @setting_id.setter
    def setting_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "setting_id", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The Setting's value. Type: `string`. It must be compatible with the `setting_type`.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)

    @property
    @pulumi.getter(name="initOnly")
    def init_only(self) -> Optional[pulumi.Input[bool]]:
        """
        Default: true. Read more below.  

        The Feature Flag/Setting's value
        """
        return pulumi.get(self, "init_only")

    @init_only.setter
    def init_only(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "init_only", value)

    @property
    @pulumi.getter(name="mandatoryNotes")
    def mandatory_notes(self) -> Optional[pulumi.Input[str]]:
        """
        Default: "". If the Product's "Mandatory notes" preference is turned on for the Environment the Mandatory note must be passed.
        """
        return pulumi.get(self, "mandatory_notes")

    @mandatory_notes.setter
    def mandatory_notes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mandatory_notes", value)

    @property
    @pulumi.getter(name="percentageItems")
    def percentage_items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SettingValuePercentageItemArgs']]]]:
        """
        A list to define [Percentage items](https://configcat.com/docs/advanced/targeting/#targeting-a-percentage-of-users). Read more below.
        """
        return pulumi.get(self, "percentage_items")

    @percentage_items.setter
    def percentage_items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SettingValuePercentageItemArgs']]]]):
        pulumi.set(self, "percentage_items", value)

    @property
    @pulumi.getter(name="rolloutRules")
    def rollout_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SettingValueRolloutRuleArgs']]]]:
        """
        A list to define [Rollout rules](https://configcat.com/docs/advanced/targeting/#anatomy-of-a-targeting-rule). Read more below.
        """
        return pulumi.get(self, "rollout_rules")

    @rollout_rules.setter
    def rollout_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SettingValueRolloutRuleArgs']]]]):
        pulumi.set(self, "rollout_rules", value)


@pulumi.input_type
class _SettingValueState:
    def __init__(__self__, *,
                 environment_id: Optional[pulumi.Input[str]] = None,
                 init_only: Optional[pulumi.Input[bool]] = None,
                 mandatory_notes: Optional[pulumi.Input[str]] = None,
                 percentage_items: Optional[pulumi.Input[Sequence[pulumi.Input['SettingValuePercentageItemArgs']]]] = None,
                 rollout_rules: Optional[pulumi.Input[Sequence[pulumi.Input['SettingValueRolloutRuleArgs']]]] = None,
                 setting_id: Optional[pulumi.Input[str]] = None,
                 setting_type: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SettingValue resources.
        :param pulumi.Input[str] environment_id: The ID of the Environment.
        :param pulumi.Input[bool] init_only: Default: true. Read more below.  
               
               The Feature Flag/Setting's value
        :param pulumi.Input[str] mandatory_notes: Default: "". If the Product's "Mandatory notes" preference is turned on for the Environment the Mandatory note must be passed.
        :param pulumi.Input[Sequence[pulumi.Input['SettingValuePercentageItemArgs']]] percentage_items: A list to define [Percentage items](https://configcat.com/docs/advanced/targeting/#targeting-a-percentage-of-users). Read more below.
        :param pulumi.Input[Sequence[pulumi.Input['SettingValueRolloutRuleArgs']]] rollout_rules: A list to define [Rollout rules](https://configcat.com/docs/advanced/targeting/#anatomy-of-a-targeting-rule). Read more below.
        :param pulumi.Input[str] setting_id: The ID of the Feature Flag/Setting.
        :param pulumi.Input[str] setting_type: The Setting's type.
        :param pulumi.Input[str] value: The Setting's value. Type: `string`. It must be compatible with the `setting_type`.
        """
        if environment_id is not None:
            pulumi.set(__self__, "environment_id", environment_id)
        if init_only is not None:
            pulumi.set(__self__, "init_only", init_only)
        if mandatory_notes is not None:
            pulumi.set(__self__, "mandatory_notes", mandatory_notes)
        if percentage_items is not None:
            pulumi.set(__self__, "percentage_items", percentage_items)
        if rollout_rules is not None:
            pulumi.set(__self__, "rollout_rules", rollout_rules)
        if setting_id is not None:
            pulumi.set(__self__, "setting_id", setting_id)
        if setting_type is not None:
            pulumi.set(__self__, "setting_type", setting_type)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Environment.
        """
        return pulumi.get(self, "environment_id")

    @environment_id.setter
    def environment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "environment_id", value)

    @property
    @pulumi.getter(name="initOnly")
    def init_only(self) -> Optional[pulumi.Input[bool]]:
        """
        Default: true. Read more below.  

        The Feature Flag/Setting's value
        """
        return pulumi.get(self, "init_only")

    @init_only.setter
    def init_only(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "init_only", value)

    @property
    @pulumi.getter(name="mandatoryNotes")
    def mandatory_notes(self) -> Optional[pulumi.Input[str]]:
        """
        Default: "". If the Product's "Mandatory notes" preference is turned on for the Environment the Mandatory note must be passed.
        """
        return pulumi.get(self, "mandatory_notes")

    @mandatory_notes.setter
    def mandatory_notes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mandatory_notes", value)

    @property
    @pulumi.getter(name="percentageItems")
    def percentage_items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SettingValuePercentageItemArgs']]]]:
        """
        A list to define [Percentage items](https://configcat.com/docs/advanced/targeting/#targeting-a-percentage-of-users). Read more below.
        """
        return pulumi.get(self, "percentage_items")

    @percentage_items.setter
    def percentage_items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SettingValuePercentageItemArgs']]]]):
        pulumi.set(self, "percentage_items", value)

    @property
    @pulumi.getter(name="rolloutRules")
    def rollout_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SettingValueRolloutRuleArgs']]]]:
        """
        A list to define [Rollout rules](https://configcat.com/docs/advanced/targeting/#anatomy-of-a-targeting-rule). Read more below.
        """
        return pulumi.get(self, "rollout_rules")

    @rollout_rules.setter
    def rollout_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SettingValueRolloutRuleArgs']]]]):
        pulumi.set(self, "rollout_rules", value)

    @property
    @pulumi.getter(name="settingId")
    def setting_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Feature Flag/Setting.
        """
        return pulumi.get(self, "setting_id")

    @setting_id.setter
    def setting_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "setting_id", value)

    @property
    @pulumi.getter(name="settingType")
    def setting_type(self) -> Optional[pulumi.Input[str]]:
        """
        The Setting's type.
        """
        return pulumi.get(self, "setting_type")

    @setting_type.setter
    def setting_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "setting_type", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        The Setting's value. Type: `string`. It must be compatible with the `setting_type`.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


class SettingValue(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 environment_id: Optional[pulumi.Input[str]] = None,
                 init_only: Optional[pulumi.Input[bool]] = None,
                 mandatory_notes: Optional[pulumi.Input[str]] = None,
                 percentage_items: Optional[pulumi.Input[Sequence[pulumi.Input[Union['SettingValuePercentageItemArgs', 'SettingValuePercentageItemArgsDict']]]]] = None,
                 rollout_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union['SettingValueRolloutRuleArgs', 'SettingValueRolloutRuleArgsDict']]]]] = None,
                 setting_id: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## # SettingValue Resource

        Initializes and updates **Feature Flag and Setting** values. [Read more about the anatomy of a Feature Flag or Setting.](https://configcat.com/docs/main-concepts)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_configcat as configcat
        import pulumiverse_configcat as configcat

        my_products = configcat.get_products(name_filter_regex="ConfigCat's product")
        my_configs = configcat.get_configurations(product_id=my_products.products[0].product_id,
            name_filter_regex="Main Config")
        my_environments = configcat.get_environments(product_id=my_products.products[0].product_id,
            name_filter_regex="Test")
        my_settings = configcat.get_settings(config_id=my_configs.configs[0].config_id,
            key_filter_regex="isAwesomeFeatureEnabled")
        my_setting_value = configcat.SettingValue("my_setting_value",
            environment_id=my_environments.environments[0].environment_id,
            setting_id=my_settings.settings[0].setting_id,
            mandatory_notes="mandatory notes",
            value="true",
            rollout_rules=[
                {
                    "comparison_attribute": "Email",
                    "comparator": "contains",
                    "comparison_value": "@mycompany.com",
                    "value": "true",
                },
                {
                    "comparison_attribute": "custom",
                    "comparator": "isOneOf",
                    "comparison_value": "red",
                    "value": "false",
                },
            ],
            percentage_items=[
                {
                    "percentage": "20",
                    "value": "true",
                },
                {
                    "percentage": "80",
                    "value": "false",
                },
            ])
        ```

        ## Endpoints used

        * [Get Value](https://api.configcat.com/docs/#tag/Feature-Flag-and-Setting-values/operation/get-setting-value)
        * [Replace Value](https://api.configcat.com/docs/#tag/Feature-Flag-and-Setting-values/operation/replace-setting-value)

        ## Import

        Feature Flag/Setting values can be imported using a combined EnvironmentID:SettingId ID.

        Get the SettingId using e.g. the [List Flags API](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/get-settings).

        Get the EnvironmentId using e.g. the [List Environments API](https://api.configcat.com/docs/#tag/Environments/operation/get-environments).

        ```sh
        $ pulumi import configcat:index/settingValue:SettingValue example 08d86d63-2726-47cd-8bfc-59608ecb91e2:1234
        ```

        Read more about importing.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] environment_id: The ID of the Environment.
        :param pulumi.Input[bool] init_only: Default: true. Read more below.  
               
               The Feature Flag/Setting's value
        :param pulumi.Input[str] mandatory_notes: Default: "". If the Product's "Mandatory notes" preference is turned on for the Environment the Mandatory note must be passed.
        :param pulumi.Input[Sequence[pulumi.Input[Union['SettingValuePercentageItemArgs', 'SettingValuePercentageItemArgsDict']]]] percentage_items: A list to define [Percentage items](https://configcat.com/docs/advanced/targeting/#targeting-a-percentage-of-users). Read more below.
        :param pulumi.Input[Sequence[pulumi.Input[Union['SettingValueRolloutRuleArgs', 'SettingValueRolloutRuleArgsDict']]]] rollout_rules: A list to define [Rollout rules](https://configcat.com/docs/advanced/targeting/#anatomy-of-a-targeting-rule). Read more below.
        :param pulumi.Input[str] setting_id: The ID of the Feature Flag/Setting.
        :param pulumi.Input[str] value: The Setting's value. Type: `string`. It must be compatible with the `setting_type`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SettingValueArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## # SettingValue Resource

        Initializes and updates **Feature Flag and Setting** values. [Read more about the anatomy of a Feature Flag or Setting.](https://configcat.com/docs/main-concepts)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_configcat as configcat
        import pulumiverse_configcat as configcat

        my_products = configcat.get_products(name_filter_regex="ConfigCat's product")
        my_configs = configcat.get_configurations(product_id=my_products.products[0].product_id,
            name_filter_regex="Main Config")
        my_environments = configcat.get_environments(product_id=my_products.products[0].product_id,
            name_filter_regex="Test")
        my_settings = configcat.get_settings(config_id=my_configs.configs[0].config_id,
            key_filter_regex="isAwesomeFeatureEnabled")
        my_setting_value = configcat.SettingValue("my_setting_value",
            environment_id=my_environments.environments[0].environment_id,
            setting_id=my_settings.settings[0].setting_id,
            mandatory_notes="mandatory notes",
            value="true",
            rollout_rules=[
                {
                    "comparison_attribute": "Email",
                    "comparator": "contains",
                    "comparison_value": "@mycompany.com",
                    "value": "true",
                },
                {
                    "comparison_attribute": "custom",
                    "comparator": "isOneOf",
                    "comparison_value": "red",
                    "value": "false",
                },
            ],
            percentage_items=[
                {
                    "percentage": "20",
                    "value": "true",
                },
                {
                    "percentage": "80",
                    "value": "false",
                },
            ])
        ```

        ## Endpoints used

        * [Get Value](https://api.configcat.com/docs/#tag/Feature-Flag-and-Setting-values/operation/get-setting-value)
        * [Replace Value](https://api.configcat.com/docs/#tag/Feature-Flag-and-Setting-values/operation/replace-setting-value)

        ## Import

        Feature Flag/Setting values can be imported using a combined EnvironmentID:SettingId ID.

        Get the SettingId using e.g. the [List Flags API](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/get-settings).

        Get the EnvironmentId using e.g. the [List Environments API](https://api.configcat.com/docs/#tag/Environments/operation/get-environments).

        ```sh
        $ pulumi import configcat:index/settingValue:SettingValue example 08d86d63-2726-47cd-8bfc-59608ecb91e2:1234
        ```

        Read more about importing.

        :param str resource_name: The name of the resource.
        :param SettingValueArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SettingValueArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 environment_id: Optional[pulumi.Input[str]] = None,
                 init_only: Optional[pulumi.Input[bool]] = None,
                 mandatory_notes: Optional[pulumi.Input[str]] = None,
                 percentage_items: Optional[pulumi.Input[Sequence[pulumi.Input[Union['SettingValuePercentageItemArgs', 'SettingValuePercentageItemArgsDict']]]]] = None,
                 rollout_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union['SettingValueRolloutRuleArgs', 'SettingValueRolloutRuleArgsDict']]]]] = None,
                 setting_id: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SettingValueArgs.__new__(SettingValueArgs)

            if environment_id is None and not opts.urn:
                raise TypeError("Missing required property 'environment_id'")
            __props__.__dict__["environment_id"] = environment_id
            __props__.__dict__["init_only"] = init_only
            __props__.__dict__["mandatory_notes"] = mandatory_notes
            __props__.__dict__["percentage_items"] = percentage_items
            __props__.__dict__["rollout_rules"] = rollout_rules
            if setting_id is None and not opts.urn:
                raise TypeError("Missing required property 'setting_id'")
            __props__.__dict__["setting_id"] = setting_id
            if value is None and not opts.urn:
                raise TypeError("Missing required property 'value'")
            __props__.__dict__["value"] = value
            __props__.__dict__["setting_type"] = None
        super(SettingValue, __self__).__init__(
            'configcat:index/settingValue:SettingValue',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            environment_id: Optional[pulumi.Input[str]] = None,
            init_only: Optional[pulumi.Input[bool]] = None,
            mandatory_notes: Optional[pulumi.Input[str]] = None,
            percentage_items: Optional[pulumi.Input[Sequence[pulumi.Input[Union['SettingValuePercentageItemArgs', 'SettingValuePercentageItemArgsDict']]]]] = None,
            rollout_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union['SettingValueRolloutRuleArgs', 'SettingValueRolloutRuleArgsDict']]]]] = None,
            setting_id: Optional[pulumi.Input[str]] = None,
            setting_type: Optional[pulumi.Input[str]] = None,
            value: Optional[pulumi.Input[str]] = None) -> 'SettingValue':
        """
        Get an existing SettingValue resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] environment_id: The ID of the Environment.
        :param pulumi.Input[bool] init_only: Default: true. Read more below.  
               
               The Feature Flag/Setting's value
        :param pulumi.Input[str] mandatory_notes: Default: "". If the Product's "Mandatory notes" preference is turned on for the Environment the Mandatory note must be passed.
        :param pulumi.Input[Sequence[pulumi.Input[Union['SettingValuePercentageItemArgs', 'SettingValuePercentageItemArgsDict']]]] percentage_items: A list to define [Percentage items](https://configcat.com/docs/advanced/targeting/#targeting-a-percentage-of-users). Read more below.
        :param pulumi.Input[Sequence[pulumi.Input[Union['SettingValueRolloutRuleArgs', 'SettingValueRolloutRuleArgsDict']]]] rollout_rules: A list to define [Rollout rules](https://configcat.com/docs/advanced/targeting/#anatomy-of-a-targeting-rule). Read more below.
        :param pulumi.Input[str] setting_id: The ID of the Feature Flag/Setting.
        :param pulumi.Input[str] setting_type: The Setting's type.
        :param pulumi.Input[str] value: The Setting's value. Type: `string`. It must be compatible with the `setting_type`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SettingValueState.__new__(_SettingValueState)

        __props__.__dict__["environment_id"] = environment_id
        __props__.__dict__["init_only"] = init_only
        __props__.__dict__["mandatory_notes"] = mandatory_notes
        __props__.__dict__["percentage_items"] = percentage_items
        __props__.__dict__["rollout_rules"] = rollout_rules
        __props__.__dict__["setting_id"] = setting_id
        __props__.__dict__["setting_type"] = setting_type
        __props__.__dict__["value"] = value
        return SettingValue(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> pulumi.Output[str]:
        """
        The ID of the Environment.
        """
        return pulumi.get(self, "environment_id")

    @property
    @pulumi.getter(name="initOnly")
    def init_only(self) -> pulumi.Output[Optional[bool]]:
        """
        Default: true. Read more below.  

        The Feature Flag/Setting's value
        """
        return pulumi.get(self, "init_only")

    @property
    @pulumi.getter(name="mandatoryNotes")
    def mandatory_notes(self) -> pulumi.Output[Optional[str]]:
        """
        Default: "". If the Product's "Mandatory notes" preference is turned on for the Environment the Mandatory note must be passed.
        """
        return pulumi.get(self, "mandatory_notes")

    @property
    @pulumi.getter(name="percentageItems")
    def percentage_items(self) -> pulumi.Output[Optional[Sequence['outputs.SettingValuePercentageItem']]]:
        """
        A list to define [Percentage items](https://configcat.com/docs/advanced/targeting/#targeting-a-percentage-of-users). Read more below.
        """
        return pulumi.get(self, "percentage_items")

    @property
    @pulumi.getter(name="rolloutRules")
    def rollout_rules(self) -> pulumi.Output[Optional[Sequence['outputs.SettingValueRolloutRule']]]:
        """
        A list to define [Rollout rules](https://configcat.com/docs/advanced/targeting/#anatomy-of-a-targeting-rule). Read more below.
        """
        return pulumi.get(self, "rollout_rules")

    @property
    @pulumi.getter(name="settingId")
    def setting_id(self) -> pulumi.Output[str]:
        """
        The ID of the Feature Flag/Setting.
        """
        return pulumi.get(self, "setting_id")

    @property
    @pulumi.getter(name="settingType")
    def setting_type(self) -> pulumi.Output[str]:
        """
        The Setting's type.
        """
        return pulumi.get(self, "setting_type")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        """
        The Setting's value. Type: `string`. It must be compatible with the `setting_type`.
        """
        return pulumi.get(self, "value")

