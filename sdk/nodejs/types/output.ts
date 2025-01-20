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
     * The environment specific permissions map block defined as below.
     */
    environmentAccesses?: {[key: string]: string};
    /**
     * The name of the Permission Group.
     */
    name: string;
    /**
     * Represent the environment specific Feature Management permission for new Environments. Possible values: full, readOnly, none
     */
    newEnvironmentAccesstype: string;
    /**
     * The unique Permission Groups ID.
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
     * The order of the Product within an Organization (zero-based).
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
     * The hint of the Setting.
     */
    hint: string;
    /**
     * The key of the Feature Flag/Setting.
     */
    key: string;
    /**
     * The name of the Setting.
     */
    name: string;
    /**
     * The order of the Setting within a Config (zero-based).
     */
    order: number;
    /**
     * The unique Setting ID.
     */
    settingId: string;
    /**
     * The Setting's type. Available values: `boolean`|`string`|`int`|`double`.
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
    comparator?: string;
    /**
     * The [comparison attribute](https://configcat.com/docs/advanced/targeting/#attribute).
     */
    comparisonAttribute?: string;
    /**
     * The [comparison value](https://configcat.com/docs/advanced/targeting/#comparison-value).
     */
    comparisonValue?: string;
    /**
     * The segment_comparator. Possible values: isIn, isNotIn.
     */
    segmentComparator?: string;
    /**
     * The [Segment's](https://configcat.com/docs/advanced/segments) unique identifier.
     */
    segmentId?: string;
    /**
     * The exact [value](https://configcat.com/docs/advanced/targeting/#served-value) that will be served to the users who match the targeting rule. Type: `string`. It must be compatible with the `settingType`.
     */
    value: string;
}

