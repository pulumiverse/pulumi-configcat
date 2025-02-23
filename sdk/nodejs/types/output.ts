// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export interface GetConfigurationsConfig {
    /**
     * The unique Config ID.
     */
    configId: string;
    /**
     * The description of the Config.
     */
    description: string;
    /**
     * The evaluation version of the Config. Possible values: `v1`|`v2`
     */
    evaluationVersion: string;
    /**
     * The name of the Config.
     */
    name: string;
    /**
     * The order of the Config within a Product (zero-based).
     */
    order: number;
}

export interface GetEnvironmentsEnvironment {
    /**
     * The color of the Environment.
     */
    color: string;
    /**
     * The description of the Environment.
     */
    description: string;
    /**
     * The unique Environment ID.
     */
    environmentId: string;
    /**
     * The name of the Environment.
     */
    name: string;
    /**
     * The order of the Environment within a Product (zero-based).
     */
    order: number;
}

export interface GetOrganizationsOrganization {
    /**
     * The name of the Organization.
     */
    name: string;
    /**
     * The unique Organization ID.
     */
    organizationId: string;
}

export interface GetPermissionGroupsPermissionGroup {
    /**
     * Represent the Feature Management permission. Possible values: readOnly, full, custom
     */
    accesstype: string;
    /**
     * Group members can create/update Configs.
     */
    canCreateorupdateConfig: boolean;
    /**
     * Group members can create/update Environments.
     */
    canCreateorupdateEnvironment: boolean;
    /**
     * Group members can create/update Segments.
     */
    canCreateorupdateSegment: boolean;
    /**
     * Group members can create/update Feature Flags and Settings.
     */
    canCreateorupdateSetting: boolean;
    /**
     * Group members can create/update Tags.
     */
    canCreateorupdateTag: boolean;
    /**
     * Group members can delete Configs.
     */
    canDeleteConfig: boolean;
    /**
     * Group members can delete Environments.
     */
    canDeleteEnvironment: boolean;
    /**
     * Group members can delete Segments.
     */
    canDeleteSegment: boolean;
    /**
     * Group members can delete Feature Flags and Settings.
     */
    canDeleteSetting: boolean;
    /**
     * Group members can delete Tags.
     */
    canDeleteTag: boolean;
    /**
     * Group members can disable two-factor authentication for other members.
     */
    canDisable2fa: boolean;
    /**
     * Group members can add and configure integrations.
     */
    canManageIntegrations: boolean;
    /**
     * Group members can manage team members.
     */
    canManageMembers: boolean;
    /**
     * Group members can update Product preferences.
     */
    canManageProductPreferences: boolean;
    /**
     * Group members can create/update/delete Webhooks.
     */
    canManageWebhook: boolean;
    /**
     * Group members can rotate SDK keys.
     */
    canRotateSdkkey: boolean;
    /**
     * Group members can attach/detach Tags to Feature Flags and Settings.
     */
    canTagSetting: boolean;
    /**
     * Group members can use the export/import feature.
     */
    canUseExportimport: boolean;
    /**
     * Group members has access to audit logs.
     */
    canViewProductAuditlog: boolean;
    /**
     * Group members has access to product statistics.
     */
    canViewProductStatistics: boolean;
    /**
     * Group members has access to SDK keys.
     */
    canViewSdkkey: boolean;
    /**
     * The environment specific permissions map block. Keys are the Environment IDs and the values represent the environment specific Feature Management permission. Possible values: full, readOnly
     */
    environmentAccesses: {[key: string]: string};
    /**
     * The name of the Permission Group.
     */
    name: string;
    /**
     * Represent the environment specific Feature Management permission for new Environments. Possible values: full, readOnly, none
     */
    newEnvironmentAccesstype: string;
    /**
     * The unique Permission Group ID.
     */
    permissionGroupId: number;
}

export interface GetProductsProduct {
    /**
     * The description of the Product.
     */
    description: string;
    /**
     * The name of the Product.
     */
    name: string;
    /**
     * The order of the Product within a Product (zero-based).
     */
    order: number;
    /**
     * The unique Product ID.
     */
    productId: string;
}

export interface GetSegmentsSegment {
    /**
     * The description of the Segment.
     */
    description: string;
    /**
     * The name of the Segment.
     */
    name: string;
    /**
     * The unique Segment ID.
     */
    segmentId: string;
}

export interface GetSettingsSetting {
    /**
     * The hint of the Feature Flag or Setting.
     */
    hint: string;
    /**
     * The key of the Feature Flag or Setting.
     */
    key: string;
    /**
     * The name of the Feature Flag or Setting.
     */
    name: string;
    /**
     * The order of the Feature Flag or Setting within a Config (zero-based).
     */
    order: number;
    /**
     * The unique Feature Flag or Setting ID.
     */
    settingId: string;
    /**
     * The Feature Flag or Setting's type. Available values: `boolean`|`string`|`int`|`double`.
     */
    settingType: string;
}

export interface GetTagsTag {
    /**
     * The color of the Tag.
     */
    color: string;
    /**
     * The name of the Tag.
     */
    name: string;
    /**
     * The unique Tag ID.
     */
    tagId: string;
}

export interface SettingValuePercentageItem {
    /**
     * Any [number](https://configcat.com/docs/advanced/targeting/#-value) between 0 and 100 that represents a randomly allocated fraction of your users.
     */
    percentage: string;
    /**
     * The exact [value](https://configcat.com/docs/advanced/targeting/#served-value-1) that will be served to the users that fall into that fraction. Type: `string`. It must be compatible with the `settingType`.
     */
    value: string;
}

export interface SettingValueRolloutRule {
    /**
     * The [comparator](https://configcat.com/docs/advanced/targeting/#comparator).
     */
    comparator: string;
    /**
     * The [comparison attribute](https://configcat.com/docs/advanced/targeting/#comparison-attribute).
     */
    comparisonAttribute: string;
    /**
     * The [comparison value](https://configcat.com/docs/advanced/targeting/#comparison-value).
     */
    comparisonValue: string;
    /**
     * The segment_comparator. Possible values: isIn, isNotIn.
     */
    segmentComparator: string;
    /**
     * The [Segment's](https://configcat.com/docs/advanced/segments) unique identifier.
     */
    segmentId: string;
    /**
     * The exact [value](https://configcat.com/docs/advanced/targeting/#served-value) that will be served to the users who match the targeting rule. Type: `string`. It must be compatible with the `settingType`.
     */
    value: string;
}

export interface SettingValueV2TargetingRule {
    /**
     * The conditions that are combined with the AND logical operator.
     */
    conditions?: outputs.SettingValueV2TargetingRuleCondition[];
    /**
     * The percentage options from where the evaluation process will choose a value based on the flag's percentage evaluation attribute.
     */
    percentageOptions?: outputs.SettingValueV2TargetingRulePercentageOption[];
    /**
     * Represents the value of a Feature Flag or Setting.
     */
    value?: outputs.SettingValueV2TargetingRuleValue;
}

export interface SettingValueV2TargetingRuleCondition {
    /**
     * Describes a condition that is based on a prerequisite flag.
     */
    prerequisiteFlagCondition?: outputs.SettingValueV2TargetingRuleConditionPrerequisiteFlagCondition;
    /**
     * Describes a condition that is based on a segment.
     */
    segmentCondition?: outputs.SettingValueV2TargetingRuleConditionSegmentCondition;
    /**
     * Describes a condition that is based on user attributes.
     */
    userCondition?: outputs.SettingValueV2TargetingRuleConditionUserCondition;
}

export interface SettingValueV2TargetingRuleConditionPrerequisiteFlagCondition {
    /**
     * Prerequisite flag comparison operator used during the evaluation process. Possible values: `equals`,`doesNotEqual`
     */
    comparator: string;
    /**
     * Represents the value of a Feature Flag or Setting.
     */
    comparisonValue: outputs.SettingValueV2TargetingRuleConditionPrerequisiteFlagConditionComparisonValue;
    /**
     * The prerequisite flag's identifier.
     */
    prerequisiteSettingId: string;
}

export interface SettingValueV2TargetingRuleConditionPrerequisiteFlagConditionComparisonValue {
    /**
     * The boolean representation of the value.
     */
    boolValue?: boolean;
    /**
     * The decimal number representation of the value.
     */
    doubleValue?: number;
    /**
     * The whole number representation of the value.
     */
    intValue?: number;
    /**
     * The string representation of the value.
     */
    stringValue?: string;
}

export interface SettingValueV2TargetingRuleConditionSegmentCondition {
    /**
     * The segment comparison operator used during the evaluation process. Possible values: `isIn`,`isNotIn`
     */
    comparator: string;
    /**
     * The segment's identifier.
     */
    segmentId: string;
}

export interface SettingValueV2TargetingRuleConditionUserCondition {
    /**
     * The comparison operator which defines the relation between the comparison attribute and the comparison value. For possible values check the [documentation](https://api.configcat.com/docs/index.html#tag/Feature-Flag-and-Setting-values-V2/operation/replace-setting-value-v2).
     */
    comparator: string;
    /**
     * The User Object attribute that the condition is based on.
     */
    comparisonAttribute: string;
    /**
     * The value that the user object's attribute is compared to.
     */
    comparisonValue: outputs.SettingValueV2TargetingRuleConditionUserConditionComparisonValue;
}

export interface SettingValueV2TargetingRuleConditionUserConditionComparisonValue {
    /**
     * The number representation of the comparison value.
     */
    doubleValue?: number;
    /**
     * The list representation of the comparison value.
     */
    listValues?: outputs.SettingValueV2TargetingRuleConditionUserConditionComparisonValueListValue[];
    /**
     * The string representation of the comparison value.
     */
    stringValue?: string;
}

export interface SettingValueV2TargetingRuleConditionUserConditionComparisonValueListValue {
    /**
     * An optional hint for the comparison value.
     */
    hint?: string;
    /**
     * The actual comparison value.
     */
    value: string;
}

export interface SettingValueV2TargetingRulePercentageOption {
    /**
     * A number between 0 and 100 that represents a randomly allocated fraction of the users.
     */
    percentage: number;
    /**
     * Represents the value of a Feature Flag or Setting.
     */
    value: outputs.SettingValueV2TargetingRulePercentageOptionValue;
}

export interface SettingValueV2TargetingRulePercentageOptionValue {
    /**
     * The boolean representation of the value.
     */
    boolValue?: boolean;
    /**
     * The decimal number representation of the value.
     */
    doubleValue?: number;
    /**
     * The whole number representation of the value.
     */
    intValue?: number;
    /**
     * The string representation of the value.
     */
    stringValue?: string;
}

export interface SettingValueV2TargetingRuleValue {
    /**
     * The boolean representation of the value.
     */
    boolValue?: boolean;
    /**
     * The decimal number representation of the value.
     */
    doubleValue?: number;
    /**
     * The whole number representation of the value.
     */
    intValue?: number;
    /**
     * The string representation of the value.
     */
    stringValue?: string;
}

export interface SettingValueV2Value {
    /**
     * The boolean representation of the value.
     */
    boolValue?: boolean;
    /**
     * The decimal number representation of the value.
     */
    doubleValue?: number;
    /**
     * The whole number representation of the value.
     */
    intValue?: number;
    /**
     * The string representation of the value.
     */
    stringValue?: string;
}

export interface WebhookSecureWebhookHeader {
    /**
     * The HTTP header key.
     */
    key: string;
    /**
     * The HTTP header value.
     */
    value: string;
}

export interface WebhookWebhookHeader {
    /**
     * The HTTP header key.
     */
    key: string;
    /**
     * The HTTP header value.
     */
    value: string;
}

