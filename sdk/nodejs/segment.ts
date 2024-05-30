// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * ## # configcat.Segment Resource
 *
 * Creates and manages a **Segment**. [What is a Segment in ConfigCat?](https://configcat.com/docs/advanced/segments)
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
 * const mySegment = new configcat.Segment("mySegment", {
 *     productId: myProducts.then(myProducts => myProducts.products?.[0]?.productId),
 *     description: "Beta users' description",
 *     comparisonAttribute: "email",
 *     comparator: "sensitiveIsOneOf",
 *     comparisonValue: "betauser1@example.com,betauser2@example.com",
 * });
 * export const segmentId = mySegment.id;
 * ```
 *
 * ## Endpoints used
 *
 * * [Get Segment](https://api.configcat.com/docs/#tag/Segments/operation/get-segment)
 * * [Create Segment](https://api.configcat.com/docs/#tag/Segments/operation/create-segment)
 * * [Update Segment](https://api.configcat.com/docs/#tag/Segments/operation/update-segment)
 * * [Delete Segment](https://api.configcat.com/docs/#tag/Segments/operation/delete-segment)
 *
 * ## Import
 *
 * Segments can be imported using the SegmentId. Get the SegmentId using the [List Segments API](https://api.configcat.com/docs/#tag/Segments/operation/get-segments) for example.
 *
 * ```sh
 * $ pulumi import configcat:index/segment:Segment example 08d86d63-2726-47cd-8bfc-59608ecb91e2
 * ```
 * Read more about importing.
 */
export class Segment extends pulumi.CustomResource {
    /**
     * Get an existing Segment resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SegmentState, opts?: pulumi.CustomResourceOptions): Segment {
        return new Segment(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'configcat:index/segment:Segment';

    /**
     * Returns true if the given object is an instance of Segment.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Segment {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Segment.__pulumiType;
    }

    /**
     * The [comparator](https://configcat.com/docs/advanced/targeting/#comparator).
     */
    public readonly comparator!: pulumi.Output<string>;
    /**
     * The [comparison attribute](https://configcat.com/docs/advanced/targeting/#attribute).
     */
    public readonly comparisonAttribute!: pulumi.Output<string>;
    /**
     * The [comparison value](https://configcat.com/docs/advanced/targeting/#comparison-value).
     */
    public readonly comparisonValue!: pulumi.Output<string>;
    /**
     * The description of the Segment.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The name of the Segment.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The ID of the Product.
     */
    public readonly productId!: pulumi.Output<string>;

    /**
     * Create a Segment resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SegmentArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SegmentArgs | SegmentState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as SegmentState | undefined;
            resourceInputs["comparator"] = state ? state.comparator : undefined;
            resourceInputs["comparisonAttribute"] = state ? state.comparisonAttribute : undefined;
            resourceInputs["comparisonValue"] = state ? state.comparisonValue : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["productId"] = state ? state.productId : undefined;
        } else {
            const args = argsOrState as SegmentArgs | undefined;
            if ((!args || args.comparator === undefined) && !opts.urn) {
                throw new Error("Missing required property 'comparator'");
            }
            if ((!args || args.comparisonAttribute === undefined) && !opts.urn) {
                throw new Error("Missing required property 'comparisonAttribute'");
            }
            if ((!args || args.comparisonValue === undefined) && !opts.urn) {
                throw new Error("Missing required property 'comparisonValue'");
            }
            if ((!args || args.productId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'productId'");
            }
            resourceInputs["comparator"] = args ? args.comparator : undefined;
            resourceInputs["comparisonAttribute"] = args ? args.comparisonAttribute : undefined;
            resourceInputs["comparisonValue"] = args ? args.comparisonValue : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["productId"] = args ? args.productId : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Segment.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Segment resources.
 */
export interface SegmentState {
    /**
     * The [comparator](https://configcat.com/docs/advanced/targeting/#comparator).
     */
    comparator?: pulumi.Input<string>;
    /**
     * The [comparison attribute](https://configcat.com/docs/advanced/targeting/#attribute).
     */
    comparisonAttribute?: pulumi.Input<string>;
    /**
     * The [comparison value](https://configcat.com/docs/advanced/targeting/#comparison-value).
     */
    comparisonValue?: pulumi.Input<string>;
    /**
     * The description of the Segment.
     */
    description?: pulumi.Input<string>;
    /**
     * The name of the Segment.
     */
    name?: pulumi.Input<string>;
    /**
     * The ID of the Product.
     */
    productId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Segment resource.
 */
export interface SegmentArgs {
    /**
     * The [comparator](https://configcat.com/docs/advanced/targeting/#comparator).
     */
    comparator: pulumi.Input<string>;
    /**
     * The [comparison attribute](https://configcat.com/docs/advanced/targeting/#attribute).
     */
    comparisonAttribute: pulumi.Input<string>;
    /**
     * The [comparison value](https://configcat.com/docs/advanced/targeting/#comparison-value).
     */
    comparisonValue: pulumi.Input<string>;
    /**
     * The description of the Segment.
     */
    description?: pulumi.Input<string>;
    /**
     * The name of the Segment.
     */
    name?: pulumi.Input<string>;
    /**
     * The ID of the Product.
     */
    productId: pulumi.Input<string>;
}
