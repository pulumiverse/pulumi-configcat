// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Creates and manages an **Environment**. [What is an Environment in ConfigCat?](https://configcat.com/docs/main-concepts)
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as configcat from "@pulumiverse/configcat";
 *
 * const config = new pulumi.Config();
 * const productId = config.require("productId");
 * const myEnvironment = new configcat.Environment("my_environment", {
 *     productId: productId,
 *     name: "Staging",
 *     description: "Staging description",
 *     color: "blue",
 *     order: 0,
 * });
 * export const environmentId = myEnvironment.id;
 * ```
 *
 * ## Import
 *
 * Environments can be imported using the EnvironmentId. Get the EnvironmentId using the [List Environments API](https://api.configcat.com/docs/#tag/Environments/operation/get-environments) for example.
 *
 * ```sh
 * $ pulumi import configcat:index/environment:Environment example 08d86d63-2726-47cd-8bfc-59608ecb91e2
 * ```
 */
export class Environment extends pulumi.CustomResource {
    /**
     * Get an existing Environment resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EnvironmentState, opts?: pulumi.CustomResourceOptions): Environment {
        return new Environment(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'configcat:index/environment:Environment';

    /**
     * Returns true if the given object is an instance of Environment.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Environment {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Environment.__pulumiType;
    }

    /**
     * The color of the Environment.
     */
    public readonly color!: pulumi.Output<string>;
    /**
     * The description of the Environment.
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * The name of the Environment.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The order of the Environment within a Product (zero-based). If multiple Environments has the same order, they are displayed in alphabetical order.
     */
    public readonly order!: pulumi.Output<number>;
    /**
     * The ID of the Product.
     */
    public readonly productId!: pulumi.Output<string>;

    /**
     * Create a Environment resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: EnvironmentArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: EnvironmentArgs | EnvironmentState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as EnvironmentState | undefined;
            resourceInputs["color"] = state ? state.color : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["order"] = state ? state.order : undefined;
            resourceInputs["productId"] = state ? state.productId : undefined;
        } else {
            const args = argsOrState as EnvironmentArgs | undefined;
            if ((!args || args.order === undefined) && !opts.urn) {
                throw new Error("Missing required property 'order'");
            }
            if ((!args || args.productId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'productId'");
            }
            resourceInputs["color"] = args ? args.color : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["order"] = args ? args.order : undefined;
            resourceInputs["productId"] = args ? args.productId : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Environment.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Environment resources.
 */
export interface EnvironmentState {
    /**
     * The color of the Environment.
     */
    color?: pulumi.Input<string>;
    /**
     * The description of the Environment.
     */
    description?: pulumi.Input<string>;
    /**
     * The name of the Environment.
     */
    name?: pulumi.Input<string>;
    /**
     * The order of the Environment within a Product (zero-based). If multiple Environments has the same order, they are displayed in alphabetical order.
     */
    order?: pulumi.Input<number>;
    /**
     * The ID of the Product.
     */
    productId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Environment resource.
 */
export interface EnvironmentArgs {
    /**
     * The color of the Environment.
     */
    color?: pulumi.Input<string>;
    /**
     * The description of the Environment.
     */
    description?: pulumi.Input<string>;
    /**
     * The name of the Environment.
     */
    name?: pulumi.Input<string>;
    /**
     * The order of the Environment within a Product (zero-based). If multiple Environments has the same order, they are displayed in alphabetical order.
     */
    order: pulumi.Input<number>;
    /**
     * The ID of the Product.
     */
    productId: pulumi.Input<string>;
}
