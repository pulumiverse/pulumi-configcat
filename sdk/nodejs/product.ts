// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * ## # configcat.Product Resource
 *
 * Creates and manages a **Product**. [What is a Product in ConfigCat?](https://configcat.com/docs/main-concepts)
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as configcat from "@pulumi/configcat";
 * import * as configcat from "@pulumiverse/configcat";
 *
 * const myOrganizations = configcat.getOrganizations({
 *     nameFilterRegex: "ConfigCat",
 * });
 * const myProduct = new configcat.Product("my_product", {
 *     organizationId: myOrganizations.then(myOrganizations => myOrganizations.organizations?.[0]?.organizationId),
 *     name: "My product",
 *     description: "My product description",
 *     order: 0,
 * });
 * export const productId = myProduct.id;
 * ```
 *
 * ## Endpoints used
 *
 * * [Get Product](https://api.configcat.com/docs/#tag/Products/operation/get-product)
 * * [Create Product](https://api.configcat.com/docs/#tag/Products/operation/create-product)
 * * [Update Product](https://api.configcat.com/docs/#tag/Products/operation/update-product)
 * * [Delete Product](https://api.configcat.com/docs/#tag/Products/operation/delete-product)
 *
 * ## Import
 *
 * Products can be imported using the ProductId. Get the ProductId using the [List Products API](https://api.configcat.com/docs/#tag/Products/operation/get-products) for example.
 *
 * ```sh
 * $ pulumi import configcat:index/product:Product example 08d86d63-2726-47cd-8bfc-59608ecb91e2
 * ```
 * Read more about importing.
 */
export class Product extends pulumi.CustomResource {
    /**
     * Get an existing Product resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProductState, opts?: pulumi.CustomResourceOptions): Product {
        return new Product(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'configcat:index/product:Product';

    /**
     * Returns true if the given object is an instance of Product.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Product {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Product.__pulumiType;
    }

    /**
     * The description of the Product.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The name of the Product.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The order of the Product within an Organization (zero-based). If multiple Products has the same order, they are displayed in alphabetical order.
     */
    public readonly order!: pulumi.Output<number>;
    /**
     * The ID of the Organization.
     */
    public readonly organizationId!: pulumi.Output<string>;

    /**
     * Create a Product resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ProductArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ProductArgs | ProductState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ProductState | undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["order"] = state ? state.order : undefined;
            resourceInputs["organizationId"] = state ? state.organizationId : undefined;
        } else {
            const args = argsOrState as ProductArgs | undefined;
            if ((!args || args.order === undefined) && !opts.urn) {
                throw new Error("Missing required property 'order'");
            }
            if ((!args || args.organizationId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'organizationId'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["order"] = args ? args.order : undefined;
            resourceInputs["organizationId"] = args ? args.organizationId : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Product.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Product resources.
 */
export interface ProductState {
    /**
     * The description of the Product.
     */
    description?: pulumi.Input<string>;
    /**
     * The name of the Product.
     */
    name?: pulumi.Input<string>;
    /**
     * The order of the Product within an Organization (zero-based). If multiple Products has the same order, they are displayed in alphabetical order.
     */
    order?: pulumi.Input<number>;
    /**
     * The ID of the Organization.
     */
    organizationId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Product resource.
 */
export interface ProductArgs {
    /**
     * The description of the Product.
     */
    description?: pulumi.Input<string>;
    /**
     * The name of the Product.
     */
    name?: pulumi.Input<string>;
    /**
     * The order of the Product within an Organization (zero-based). If multiple Products has the same order, they are displayed in alphabetical order.
     */
    order: pulumi.Input<number>;
    /**
     * The ID of the Organization.
     */
    organizationId: pulumi.Input<string>;
}
