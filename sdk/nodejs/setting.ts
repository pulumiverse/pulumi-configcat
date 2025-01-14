// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * ## # configcat.Setting Resource
 *
 * Creates and manages a **Feature Flag/Setting**. [Read more about the anatomy of a Feature Flag or Setting.](https://configcat.com/docs/main-concepts)
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as configcat from "@pulumi/configcat";
 * import * as configcat from "@pulumiverse/configcat";
 *
 * const myProducts = configcat.getProducts({
 *     nameFilterRegex: "ConfigCat's product",
 * });
 * const myConfigs = myProducts.then(myProducts => configcat.getConfigurations({
 *     productId: myProducts.products?.[0]?.productId,
 *     nameFilterRegex: "Main Config",
 * }));
 * const mySetting = new configcat.Setting("my_setting", {
 *     configId: myConfigs.then(myConfigs => myConfigs.configs?.[0]?.configId),
 *     key: "isAwesomeFeatureEnabled",
 *     name: "My awesome feature flag",
 *     hint: "This is the hint for my awesome feature flag",
 *     settingType: "boolean",
 * });
 * export const settingId = mySetting.id;
 * ```
 *
 * ## Endpoints used
 *
 * * [Get Flag](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/get-setting)
 * * [Create Flag](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/create-setting)
 * * [Update Flag](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/update-setting)
 * * [Delete Flag](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/delete-setting)
 *
 * ## Import
 *
 * Feature Flags/Settings can be imported using the SettingId. Get the SettingId using e.g. the [List Flags API](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/get-settings).
 *
 * ```sh
 * $ pulumi import configcat:index/setting:Setting example 1234
 * ```
 * Read more about importing.
 */
export class Setting extends pulumi.CustomResource {
    /**
     * Get an existing Setting resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SettingState, opts?: pulumi.CustomResourceOptions): Setting {
        return new Setting(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'configcat:index/setting:Setting';

    /**
     * Returns true if the given object is an instance of Setting.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Setting {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Setting.__pulumiType;
    }

    /**
     * The ID of the Config.
     */
    public readonly configId!: pulumi.Output<string>;
    /**
     * The hint of the Setting.
     */
    public readonly hint!: pulumi.Output<string | undefined>;
    /**
     * The key of the Feature Flag/Setting.
     */
    public readonly key!: pulumi.Output<string>;
    /**
     * The name of the Setting.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Default: `boolean`. The Setting's type.  
     * Available values: `boolean`|`string`|`int`|`double`.
     */
    public readonly settingType!: pulumi.Output<string | undefined>;

    /**
     * Create a Setting resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SettingArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SettingArgs | SettingState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as SettingState | undefined;
            resourceInputs["configId"] = state ? state.configId : undefined;
            resourceInputs["hint"] = state ? state.hint : undefined;
            resourceInputs["key"] = state ? state.key : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["settingType"] = state ? state.settingType : undefined;
        } else {
            const args = argsOrState as SettingArgs | undefined;
            if ((!args || args.configId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'configId'");
            }
            if ((!args || args.key === undefined) && !opts.urn) {
                throw new Error("Missing required property 'key'");
            }
            resourceInputs["configId"] = args ? args.configId : undefined;
            resourceInputs["hint"] = args ? args.hint : undefined;
            resourceInputs["key"] = args ? args.key : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["settingType"] = args ? args.settingType : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Setting.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Setting resources.
 */
export interface SettingState {
    /**
     * The ID of the Config.
     */
    configId?: pulumi.Input<string>;
    /**
     * The hint of the Setting.
     */
    hint?: pulumi.Input<string>;
    /**
     * The key of the Feature Flag/Setting.
     */
    key?: pulumi.Input<string>;
    /**
     * The name of the Setting.
     */
    name?: pulumi.Input<string>;
    /**
     * Default: `boolean`. The Setting's type.  
     * Available values: `boolean`|`string`|`int`|`double`.
     */
    settingType?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Setting resource.
 */
export interface SettingArgs {
    /**
     * The ID of the Config.
     */
    configId: pulumi.Input<string>;
    /**
     * The hint of the Setting.
     */
    hint?: pulumi.Input<string>;
    /**
     * The key of the Feature Flag/Setting.
     */
    key: pulumi.Input<string>;
    /**
     * The name of the Setting.
     */
    name?: pulumi.Input<string>;
    /**
     * Default: `boolean`. The Setting's type.  
     * Available values: `boolean`|`string`|`int`|`double`.
     */
    settingType?: pulumi.Input<string>;
}
