// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

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
     * The hint of the Feature Flag or Setting.
     */
    public readonly hint!: pulumi.Output<string>;
    /**
     * The key of the Feature Flag or Setting.
     */
    public readonly key!: pulumi.Output<string>;
    /**
     * The name of the Feature Flag or Setting.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The order of the Feature Flag or Setting within a Product (zero-based). If multiple Feature Flags or Settings has the
     * same order, they are displayed in alphabetical order.
     */
    public readonly order!: pulumi.Output<number>;
    /**
     * The type of the Feature Flag or Setting. Available values: `boolean`|`string`|`int`|`double`. Default: `boolean`.
     */
    public readonly settingType!: pulumi.Output<string>;

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
            resourceInputs["order"] = state ? state.order : undefined;
            resourceInputs["settingType"] = state ? state.settingType : undefined;
        } else {
            const args = argsOrState as SettingArgs | undefined;
            if ((!args || args.configId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'configId'");
            }
            if ((!args || args.key === undefined) && !opts.urn) {
                throw new Error("Missing required property 'key'");
            }
            if ((!args || args.order === undefined) && !opts.urn) {
                throw new Error("Missing required property 'order'");
            }
            resourceInputs["configId"] = args ? args.configId : undefined;
            resourceInputs["hint"] = args ? args.hint : undefined;
            resourceInputs["key"] = args ? args.key : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["order"] = args ? args.order : undefined;
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
     * The hint of the Feature Flag or Setting.
     */
    hint?: pulumi.Input<string>;
    /**
     * The key of the Feature Flag or Setting.
     */
    key?: pulumi.Input<string>;
    /**
     * The name of the Feature Flag or Setting.
     */
    name?: pulumi.Input<string>;
    /**
     * The order of the Feature Flag or Setting within a Product (zero-based). If multiple Feature Flags or Settings has the
     * same order, they are displayed in alphabetical order.
     */
    order?: pulumi.Input<number>;
    /**
     * The type of the Feature Flag or Setting. Available values: `boolean`|`string`|`int`|`double`. Default: `boolean`.
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
     * The hint of the Feature Flag or Setting.
     */
    hint?: pulumi.Input<string>;
    /**
     * The key of the Feature Flag or Setting.
     */
    key: pulumi.Input<string>;
    /**
     * The name of the Feature Flag or Setting.
     */
    name?: pulumi.Input<string>;
    /**
     * The order of the Feature Flag or Setting within a Product (zero-based). If multiple Feature Flags or Settings has the
     * same order, they are displayed in alphabetical order.
     */
    order: pulumi.Input<number>;
    /**
     * The type of the Feature Flag or Setting. Available values: `boolean`|`string`|`int`|`double`. Default: `boolean`.
     */
    settingType?: pulumi.Input<string>;
}
