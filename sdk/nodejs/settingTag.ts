// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * ## # configcat.SettingTag Resource
 *
 * Adds/Removes **Tags** to/from **Feature Flags and Settings**.
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
 * const myConfigs = myProducts.then(myProducts => configcat.getConfigs({
 *     productId: myProducts.products?.[0]?.productId,
 *     nameFilterRegex: "Main Config",
 * }));
 * const myTags = myProducts.then(myProducts => configcat.getTags({
 *     productId: myProducts.products?.[0]?.productId,
 *     nameFilterRegex: "Tag",
 * }));
 * const mySettings = myConfigs.then(myConfigs => configcat.getSettings({
 *     configId: myConfigs.configs?.[0]?.configId,
 *     keyFilterRegex: "isAwesomeFeatureEnabled",
 * }));
 * const mySettingTag = new configcat.SettingTag("mySettingTag", {
 *     settingId: mySettings.then(mySettings => mySettings.settings?.[0]?.settingId),
 *     tagId: myTags.then(myTags => myTags.tags?.[0]?.tagId),
 * });
 * ```
 *
 * ## Endpoints used
 *
 * * [Get Flag](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/get-setting)
 * * [Update Flag](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/update-setting)
 *
 * ## Import
 *
 * Tags can be imported using a combined SettingId:TagId ID.
 *
 * Get the SettingId using e.g. the [List Flags API](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/get-settings).
 *
 * Get the TagId using e.g. the [List Tags API](https://api.configcat.com/docs/#tag/Tags/operation/get-tags).
 *
 * ```sh
 * $ pulumi import configcat:index/settingTag:SettingTag example 1234:5678
 * ```
 *
 * Read more about importing.
 */
export class SettingTag extends pulumi.CustomResource {
    /**
     * Get an existing SettingTag resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SettingTagState, opts?: pulumi.CustomResourceOptions): SettingTag {
        return new SettingTag(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'configcat:index/settingTag:SettingTag';

    /**
     * Returns true if the given object is an instance of SettingTag.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is SettingTag {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === SettingTag.__pulumiType;
    }

    /**
     * The ID of the Feature Flag/Setting.
     */
    public readonly settingId!: pulumi.Output<string>;
    /**
     * The ID of the Tag.
     */
    public readonly tagId!: pulumi.Output<string>;

    /**
     * Create a SettingTag resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SettingTagArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SettingTagArgs | SettingTagState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as SettingTagState | undefined;
            resourceInputs["settingId"] = state ? state.settingId : undefined;
            resourceInputs["tagId"] = state ? state.tagId : undefined;
        } else {
            const args = argsOrState as SettingTagArgs | undefined;
            if ((!args || args.settingId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'settingId'");
            }
            if ((!args || args.tagId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'tagId'");
            }
            resourceInputs["settingId"] = args ? args.settingId : undefined;
            resourceInputs["tagId"] = args ? args.tagId : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(SettingTag.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering SettingTag resources.
 */
export interface SettingTagState {
    /**
     * The ID of the Feature Flag/Setting.
     */
    settingId?: pulumi.Input<string>;
    /**
     * The ID of the Tag.
     */
    tagId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a SettingTag resource.
 */
export interface SettingTagArgs {
    /**
     * The ID of the Feature Flag/Setting.
     */
    settingId: pulumi.Input<string>;
    /**
     * The ID of the Tag.
     */
    tagId: pulumi.Input<string>;
}
