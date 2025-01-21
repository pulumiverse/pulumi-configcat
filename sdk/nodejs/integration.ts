// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class Integration extends pulumi.CustomResource {
    /**
     * Get an existing Integration resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IntegrationState, opts?: pulumi.CustomResourceOptions): Integration {
        return new Integration(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'configcat:index/integration:Integration';

    /**
     * Returns true if the given object is an instance of Integration.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Integration {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Integration.__pulumiType;
    }

    /**
     * List of Config IDs that are connected with this Integration. If the list is empty, all of the Configs are connected.
     */
    public readonly configs!: pulumi.Output<string[]>;
    /**
     * List of Environment IDs that are connected with this Integration. If the list is empty, all of the Environments are
     * connected.
     */
    public readonly environments!: pulumi.Output<string[]>;
    /**
     * The integration type of the Integration. Possible values: `dataDog`, `slack`, `amplitude`, `mixPanel`, `segment`,
     * `pubNub`.
     */
    public readonly integrationType!: pulumi.Output<string>;
    /**
     * The name of the Integration.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Parameters of the integration. The Parameters dictionary differs for each IntegrationType. See available options per
     * integration type at the Example usage section.
     */
    public readonly parameters!: pulumi.Output<{[key: string]: string}>;
    /**
     * The ID of the Product.
     */
    public readonly productId!: pulumi.Output<string>;

    /**
     * Create a Integration resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: IntegrationArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: IntegrationArgs | IntegrationState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as IntegrationState | undefined;
            resourceInputs["configs"] = state ? state.configs : undefined;
            resourceInputs["environments"] = state ? state.environments : undefined;
            resourceInputs["integrationType"] = state ? state.integrationType : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["parameters"] = state ? state.parameters : undefined;
            resourceInputs["productId"] = state ? state.productId : undefined;
        } else {
            const args = argsOrState as IntegrationArgs | undefined;
            if ((!args || args.integrationType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'integrationType'");
            }
            if ((!args || args.productId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'productId'");
            }
            resourceInputs["configs"] = args ? args.configs : undefined;
            resourceInputs["environments"] = args ? args.environments : undefined;
            resourceInputs["integrationType"] = args ? args.integrationType : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["parameters"] = args ? args.parameters : undefined;
            resourceInputs["productId"] = args ? args.productId : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Integration.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Integration resources.
 */
export interface IntegrationState {
    /**
     * List of Config IDs that are connected with this Integration. If the list is empty, all of the Configs are connected.
     */
    configs?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * List of Environment IDs that are connected with this Integration. If the list is empty, all of the Environments are
     * connected.
     */
    environments?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The integration type of the Integration. Possible values: `dataDog`, `slack`, `amplitude`, `mixPanel`, `segment`,
     * `pubNub`.
     */
    integrationType?: pulumi.Input<string>;
    /**
     * The name of the Integration.
     */
    name?: pulumi.Input<string>;
    /**
     * Parameters of the integration. The Parameters dictionary differs for each IntegrationType. See available options per
     * integration type at the Example usage section.
     */
    parameters?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The ID of the Product.
     */
    productId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Integration resource.
 */
export interface IntegrationArgs {
    /**
     * List of Config IDs that are connected with this Integration. If the list is empty, all of the Configs are connected.
     */
    configs?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * List of Environment IDs that are connected with this Integration. If the list is empty, all of the Environments are
     * connected.
     */
    environments?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The integration type of the Integration. Possible values: `dataDog`, `slack`, `amplitude`, `mixPanel`, `segment`,
     * `pubNub`.
     */
    integrationType: pulumi.Input<string>;
    /**
     * The name of the Integration.
     */
    name?: pulumi.Input<string>;
    /**
     * Parameters of the integration. The Parameters dictionary differs for each IntegrationType. See available options per
     * integration type at the Example usage section.
     */
    parameters?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The ID of the Product.
     */
    productId: pulumi.Input<string>;
}
