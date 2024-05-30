// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * ## # configcat.PermissionGroup Resource
 *
 * Creates and manages a **Permission Group**. [What is a Permission Group in ConfigCat?](https://configcat.com/docs/advanced/team-management/team-management-basics/#permissions--permission-groups-product-level)
 *
 * ## Example Usage
 *
 * ### S
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as configcat from "@pulumi/configcat";
 * import * as configcat from "@pulumiverse/configcat";
 *
 * const myProducts = configcat.getProducts({
 *     nameFilterRegex: "ConfigCat's product",
 * });
 * const myPermissionGroup = new configcat.PermissionGroup("myPermissionGroup", {
 *     productId: myProducts.then(myProducts => myProducts.products?.[0]?.productId),
 *     accesstype: "full",
 *     canManageMembers: true,
 *     canCreateorupdateConfig: true,
 *     canDeleteConfig: true,
 *     canCreateorupdateEnvironment: true,
 *     canDeleteEnvironment: true,
 *     canCreateorupdateSetting: true,
 *     canTagSetting: true,
 *     canDeleteSetting: true,
 *     canCreateorupdateTag: true,
 *     canDeleteTag: true,
 *     canManageWebhook: true,
 *     canUseExportimport: true,
 *     canManageProductPreferences: true,
 *     canManageIntegrations: true,
 *     canViewSdkkey: true,
 *     canRotateSdkkey: true,
 *     canCreateorupdateSegment: true,
 *     canDeleteSegment: true,
 *     canViewProductAuditlog: true,
 *     canViewProductStatistics: true,
 * });
 * export const permissionGroupId = myPermissionGroup.id;
 * ```
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as configcat from "@pulumi/configcat";
 * import * as configcat from "@pulumiverse/configcat";
 *
 * const myProducts = configcat.getProducts({
 *     nameFilterRegex: "ConfigCat's product",
 * });
 * const myTestEnvironments = configcat.getEnvironments({
 *     nameFilterRegex: "Test",
 * });
 * const myProductionEnvironments = configcat.getEnvironments({
 *     nameFilterRegex: "Production",
 * });
 * const myPermissionGroup = new configcat.PermissionGroup("myPermissionGroup", {
 *     productId: myProducts.then(myProducts => myProducts.products?.[0]?.productId),
 *     accesstype: "custom",
 *     environmentAccesses: [
 *         {
 *             environmentId: myTestEnvironments.then(myTestEnvironments => myTestEnvironments.environments?.[0]?.environmentId),
 *             environmentAccesstype: "full",
 *         },
 *         {
 *             environmentId: myProductionEnvironments.then(myProductionEnvironments => myProductionEnvironments.environments?.[0]?.environmentId),
 *             environmentAccesstype: "none",
 *         },
 *     ],
 * });
 * export const permissionGroupId = myPermissionGroup.id;
 * ```
 *
 * ## Endpoints used
 *
 * * [Get Permission Group](https://api.configcat.com/docs/#tag/Permission-Groups/operation/get-permission-group)
 * * [Create Permission Group](https://api.configcat.com/docs/#tag/Permission-Groups/operation/create-permission-group)
 * * [Update Permission Group](https://api.configcat.com/docs/#tag/Permission-Groups/operation/update-permission-group)
 * * [Delete Permission Group](https://api.configcat.com/docs/#tag/Permission-Groups/operation/delete-permission-group)
 *
 * ## Import
 *
 * Permission Groups can be imported using the PermissionGroupId. Get the PermissionGroupId using the [List Permission Groups API](https://api.configcat.com/docs/#tag/Permission-Groups/operation/get-permission-groups) for example.
 *
 * ```sh
 * $ pulumi import configcat:index/permissionGroup:PermissionGroup example 123
 * ```
 * Read more about importing.
 */
export class PermissionGroup extends pulumi.CustomResource {
    /**
     * Get an existing PermissionGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PermissionGroupState, opts?: pulumi.CustomResourceOptions): PermissionGroup {
        return new PermissionGroup(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'configcat:index/permissionGroup:PermissionGroup';

    /**
     * Returns true if the given object is an instance of PermissionGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PermissionGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PermissionGroup.__pulumiType;
    }

    /**
     * Represent the Feature Management permission. Possible values: readOnly, full, custom. Default: custom
     */
    public readonly accesstype!: pulumi.Output<string | undefined>;
    /**
     * Group members can create/update Configs. Default: false.
     */
    public readonly canCreateorupdateConfig!: pulumi.Output<boolean | undefined>;
    /**
     * Group members can create/update Environments. Default: false.
     */
    public readonly canCreateorupdateEnvironment!: pulumi.Output<boolean | undefined>;
    public readonly canCreateorupdateSegment!: pulumi.Output<boolean | undefined>;
    /**
     * Group members can create/update Feature Flags and Settings. Default: false.
     */
    public readonly canCreateorupdateSetting!: pulumi.Output<boolean | undefined>;
    /**
     * Group members can create/update Tags. Default: false.
     */
    public readonly canCreateorupdateTag!: pulumi.Output<boolean | undefined>;
    /**
     * Group members can delete Configs. Default: false.
     */
    public readonly canDeleteConfig!: pulumi.Output<boolean | undefined>;
    /**
     * Group members can delete Environments. Default: false.
     */
    public readonly canDeleteEnvironment!: pulumi.Output<boolean | undefined>;
    public readonly canDeleteSegment!: pulumi.Output<boolean | undefined>;
    /**
     * Group members can delete Feature Flags and Settings. Default: false.
     */
    public readonly canDeleteSetting!: pulumi.Output<boolean | undefined>;
    /**
     * Group members can delete Tags. Default: false.
     */
    public readonly canDeleteTag!: pulumi.Output<boolean | undefined>;
    /**
     * Group members can add and configure integrations. Default: false.
     */
    public readonly canManageIntegrations!: pulumi.Output<boolean | undefined>;
    /**
     * Group members can manage team members. Default: false.
     */
    public readonly canManageMembers!: pulumi.Output<boolean | undefined>;
    /**
     * Group members can update Product preferences. Default: false.
     */
    public readonly canManageProductPreferences!: pulumi.Output<boolean | undefined>;
    /**
     * Group members can create/update/delete Webhooks. Default: false.
     */
    public readonly canManageWebhook!: pulumi.Output<boolean | undefined>;
    /**
     * Group members can rotate SDK keys. Default: false.
     */
    public readonly canRotateSdkkey!: pulumi.Output<boolean | undefined>;
    /**
     * Group members can attach/detach Tags to Feature Flags and Settings. Default: false.
     */
    public readonly canTagSetting!: pulumi.Output<boolean | undefined>;
    /**
     * Group members can use the export/import feature. Default: false.
     */
    public readonly canUseExportimport!: pulumi.Output<boolean | undefined>;
    /**
     * Group members has access to audit logs. Default: false.
     */
    public readonly canViewProductAuditlog!: pulumi.Output<boolean | undefined>;
    /**
     * Group members has access to product statistics. Default: false.
     */
    public readonly canViewProductStatistics!: pulumi.Output<boolean | undefined>;
    /**
     * Group members has access to SDK keys. Default: false.
     */
    public readonly canViewSdkkey!: pulumi.Output<boolean | undefined>;
    /**
     * The environment specific permissions list block defined as below.
     */
    public readonly environmentAccesses!: pulumi.Output<outputs.PermissionGroupEnvironmentAccess[] | undefined>;
    /**
     * The name of the Permission Group.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Represent the environment specific Feature Management permission for new Environments and for those that are not specified in the environmentAccess list. Possible values: full, readOnly, none. Default: none.
     */
    public readonly newEnvironmentAccesstype!: pulumi.Output<string | undefined>;
    /**
     * The ID of the Product.
     */
    public readonly productId!: pulumi.Output<string>;

    /**
     * Create a PermissionGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PermissionGroupArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PermissionGroupArgs | PermissionGroupState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as PermissionGroupState | undefined;
            resourceInputs["accesstype"] = state ? state.accesstype : undefined;
            resourceInputs["canCreateorupdateConfig"] = state ? state.canCreateorupdateConfig : undefined;
            resourceInputs["canCreateorupdateEnvironment"] = state ? state.canCreateorupdateEnvironment : undefined;
            resourceInputs["canCreateorupdateSegment"] = state ? state.canCreateorupdateSegment : undefined;
            resourceInputs["canCreateorupdateSetting"] = state ? state.canCreateorupdateSetting : undefined;
            resourceInputs["canCreateorupdateTag"] = state ? state.canCreateorupdateTag : undefined;
            resourceInputs["canDeleteConfig"] = state ? state.canDeleteConfig : undefined;
            resourceInputs["canDeleteEnvironment"] = state ? state.canDeleteEnvironment : undefined;
            resourceInputs["canDeleteSegment"] = state ? state.canDeleteSegment : undefined;
            resourceInputs["canDeleteSetting"] = state ? state.canDeleteSetting : undefined;
            resourceInputs["canDeleteTag"] = state ? state.canDeleteTag : undefined;
            resourceInputs["canManageIntegrations"] = state ? state.canManageIntegrations : undefined;
            resourceInputs["canManageMembers"] = state ? state.canManageMembers : undefined;
            resourceInputs["canManageProductPreferences"] = state ? state.canManageProductPreferences : undefined;
            resourceInputs["canManageWebhook"] = state ? state.canManageWebhook : undefined;
            resourceInputs["canRotateSdkkey"] = state ? state.canRotateSdkkey : undefined;
            resourceInputs["canTagSetting"] = state ? state.canTagSetting : undefined;
            resourceInputs["canUseExportimport"] = state ? state.canUseExportimport : undefined;
            resourceInputs["canViewProductAuditlog"] = state ? state.canViewProductAuditlog : undefined;
            resourceInputs["canViewProductStatistics"] = state ? state.canViewProductStatistics : undefined;
            resourceInputs["canViewSdkkey"] = state ? state.canViewSdkkey : undefined;
            resourceInputs["environmentAccesses"] = state ? state.environmentAccesses : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["newEnvironmentAccesstype"] = state ? state.newEnvironmentAccesstype : undefined;
            resourceInputs["productId"] = state ? state.productId : undefined;
        } else {
            const args = argsOrState as PermissionGroupArgs | undefined;
            if ((!args || args.productId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'productId'");
            }
            resourceInputs["accesstype"] = args ? args.accesstype : undefined;
            resourceInputs["canCreateorupdateConfig"] = args ? args.canCreateorupdateConfig : undefined;
            resourceInputs["canCreateorupdateEnvironment"] = args ? args.canCreateorupdateEnvironment : undefined;
            resourceInputs["canCreateorupdateSegment"] = args ? args.canCreateorupdateSegment : undefined;
            resourceInputs["canCreateorupdateSetting"] = args ? args.canCreateorupdateSetting : undefined;
            resourceInputs["canCreateorupdateTag"] = args ? args.canCreateorupdateTag : undefined;
            resourceInputs["canDeleteConfig"] = args ? args.canDeleteConfig : undefined;
            resourceInputs["canDeleteEnvironment"] = args ? args.canDeleteEnvironment : undefined;
            resourceInputs["canDeleteSegment"] = args ? args.canDeleteSegment : undefined;
            resourceInputs["canDeleteSetting"] = args ? args.canDeleteSetting : undefined;
            resourceInputs["canDeleteTag"] = args ? args.canDeleteTag : undefined;
            resourceInputs["canManageIntegrations"] = args ? args.canManageIntegrations : undefined;
            resourceInputs["canManageMembers"] = args ? args.canManageMembers : undefined;
            resourceInputs["canManageProductPreferences"] = args ? args.canManageProductPreferences : undefined;
            resourceInputs["canManageWebhook"] = args ? args.canManageWebhook : undefined;
            resourceInputs["canRotateSdkkey"] = args ? args.canRotateSdkkey : undefined;
            resourceInputs["canTagSetting"] = args ? args.canTagSetting : undefined;
            resourceInputs["canUseExportimport"] = args ? args.canUseExportimport : undefined;
            resourceInputs["canViewProductAuditlog"] = args ? args.canViewProductAuditlog : undefined;
            resourceInputs["canViewProductStatistics"] = args ? args.canViewProductStatistics : undefined;
            resourceInputs["canViewSdkkey"] = args ? args.canViewSdkkey : undefined;
            resourceInputs["environmentAccesses"] = args ? args.environmentAccesses : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["newEnvironmentAccesstype"] = args ? args.newEnvironmentAccesstype : undefined;
            resourceInputs["productId"] = args ? args.productId : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(PermissionGroup.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering PermissionGroup resources.
 */
export interface PermissionGroupState {
    /**
     * Represent the Feature Management permission. Possible values: readOnly, full, custom. Default: custom
     */
    accesstype?: pulumi.Input<string>;
    /**
     * Group members can create/update Configs. Default: false.
     */
    canCreateorupdateConfig?: pulumi.Input<boolean>;
    /**
     * Group members can create/update Environments. Default: false.
     */
    canCreateorupdateEnvironment?: pulumi.Input<boolean>;
    canCreateorupdateSegment?: pulumi.Input<boolean>;
    /**
     * Group members can create/update Feature Flags and Settings. Default: false.
     */
    canCreateorupdateSetting?: pulumi.Input<boolean>;
    /**
     * Group members can create/update Tags. Default: false.
     */
    canCreateorupdateTag?: pulumi.Input<boolean>;
    /**
     * Group members can delete Configs. Default: false.
     */
    canDeleteConfig?: pulumi.Input<boolean>;
    /**
     * Group members can delete Environments. Default: false.
     */
    canDeleteEnvironment?: pulumi.Input<boolean>;
    canDeleteSegment?: pulumi.Input<boolean>;
    /**
     * Group members can delete Feature Flags and Settings. Default: false.
     */
    canDeleteSetting?: pulumi.Input<boolean>;
    /**
     * Group members can delete Tags. Default: false.
     */
    canDeleteTag?: pulumi.Input<boolean>;
    /**
     * Group members can add and configure integrations. Default: false.
     */
    canManageIntegrations?: pulumi.Input<boolean>;
    /**
     * Group members can manage team members. Default: false.
     */
    canManageMembers?: pulumi.Input<boolean>;
    /**
     * Group members can update Product preferences. Default: false.
     */
    canManageProductPreferences?: pulumi.Input<boolean>;
    /**
     * Group members can create/update/delete Webhooks. Default: false.
     */
    canManageWebhook?: pulumi.Input<boolean>;
    /**
     * Group members can rotate SDK keys. Default: false.
     */
    canRotateSdkkey?: pulumi.Input<boolean>;
    /**
     * Group members can attach/detach Tags to Feature Flags and Settings. Default: false.
     */
    canTagSetting?: pulumi.Input<boolean>;
    /**
     * Group members can use the export/import feature. Default: false.
     */
    canUseExportimport?: pulumi.Input<boolean>;
    /**
     * Group members has access to audit logs. Default: false.
     */
    canViewProductAuditlog?: pulumi.Input<boolean>;
    /**
     * Group members has access to product statistics. Default: false.
     */
    canViewProductStatistics?: pulumi.Input<boolean>;
    /**
     * Group members has access to SDK keys. Default: false.
     */
    canViewSdkkey?: pulumi.Input<boolean>;
    /**
     * The environment specific permissions list block defined as below.
     */
    environmentAccesses?: pulumi.Input<pulumi.Input<inputs.PermissionGroupEnvironmentAccess>[]>;
    /**
     * The name of the Permission Group.
     */
    name?: pulumi.Input<string>;
    /**
     * Represent the environment specific Feature Management permission for new Environments and for those that are not specified in the environmentAccess list. Possible values: full, readOnly, none. Default: none.
     */
    newEnvironmentAccesstype?: pulumi.Input<string>;
    /**
     * The ID of the Product.
     */
    productId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a PermissionGroup resource.
 */
export interface PermissionGroupArgs {
    /**
     * Represent the Feature Management permission. Possible values: readOnly, full, custom. Default: custom
     */
    accesstype?: pulumi.Input<string>;
    /**
     * Group members can create/update Configs. Default: false.
     */
    canCreateorupdateConfig?: pulumi.Input<boolean>;
    /**
     * Group members can create/update Environments. Default: false.
     */
    canCreateorupdateEnvironment?: pulumi.Input<boolean>;
    canCreateorupdateSegment?: pulumi.Input<boolean>;
    /**
     * Group members can create/update Feature Flags and Settings. Default: false.
     */
    canCreateorupdateSetting?: pulumi.Input<boolean>;
    /**
     * Group members can create/update Tags. Default: false.
     */
    canCreateorupdateTag?: pulumi.Input<boolean>;
    /**
     * Group members can delete Configs. Default: false.
     */
    canDeleteConfig?: pulumi.Input<boolean>;
    /**
     * Group members can delete Environments. Default: false.
     */
    canDeleteEnvironment?: pulumi.Input<boolean>;
    canDeleteSegment?: pulumi.Input<boolean>;
    /**
     * Group members can delete Feature Flags and Settings. Default: false.
     */
    canDeleteSetting?: pulumi.Input<boolean>;
    /**
     * Group members can delete Tags. Default: false.
     */
    canDeleteTag?: pulumi.Input<boolean>;
    /**
     * Group members can add and configure integrations. Default: false.
     */
    canManageIntegrations?: pulumi.Input<boolean>;
    /**
     * Group members can manage team members. Default: false.
     */
    canManageMembers?: pulumi.Input<boolean>;
    /**
     * Group members can update Product preferences. Default: false.
     */
    canManageProductPreferences?: pulumi.Input<boolean>;
    /**
     * Group members can create/update/delete Webhooks. Default: false.
     */
    canManageWebhook?: pulumi.Input<boolean>;
    /**
     * Group members can rotate SDK keys. Default: false.
     */
    canRotateSdkkey?: pulumi.Input<boolean>;
    /**
     * Group members can attach/detach Tags to Feature Flags and Settings. Default: false.
     */
    canTagSetting?: pulumi.Input<boolean>;
    /**
     * Group members can use the export/import feature. Default: false.
     */
    canUseExportimport?: pulumi.Input<boolean>;
    /**
     * Group members has access to audit logs. Default: false.
     */
    canViewProductAuditlog?: pulumi.Input<boolean>;
    /**
     * Group members has access to product statistics. Default: false.
     */
    canViewProductStatistics?: pulumi.Input<boolean>;
    /**
     * Group members has access to SDK keys. Default: false.
     */
    canViewSdkkey?: pulumi.Input<boolean>;
    /**
     * The environment specific permissions list block defined as below.
     */
    environmentAccesses?: pulumi.Input<pulumi.Input<inputs.PermissionGroupEnvironmentAccess>[]>;
    /**
     * The name of the Permission Group.
     */
    name?: pulumi.Input<string>;
    /**
     * Represent the environment specific Feature Management permission for new Environments and for those that are not specified in the environmentAccess list. Possible values: full, readOnly, none. Default: none.
     */
    newEnvironmentAccesstype?: pulumi.Input<string>;
    /**
     * The ID of the Product.
     */
    productId: pulumi.Input<string>;
}
