// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Configcat
{
    [ConfigcatResourceType("configcat:index/configuration:Configuration")]
    public partial class Configuration : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The description of the Config.
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// The evaluation version of the Config. Possible values: `v1`, `v2`. Default value: `v1`. Using `v2` enables the new
        /// features of [Config V2](https://configcat.com/docs/advanced/config-v2).
        /// </summary>
        [Output("evaluationVersion")]
        public Output<string> EvaluationVersion { get; private set; } = null!;

        /// <summary>
        /// The name of the Config.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The order of the Config within a Product (zero-based). If multiple Configs has the same order, they are displayed in
        /// alphabetical order.
        /// </summary>
        [Output("order")]
        public Output<int> Order { get; private set; } = null!;

        /// <summary>
        /// The ID of the Product.
        /// </summary>
        [Output("productId")]
        public Output<string> ProductId { get; private set; } = null!;


        /// <summary>
        /// Create a Configuration resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Configuration(string name, ConfigurationArgs args, CustomResourceOptions? options = null)
            : base("configcat:index/configuration:Configuration", name, args ?? new ConfigurationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Configuration(string name, Input<string> id, ConfigurationState? state = null, CustomResourceOptions? options = null)
            : base("configcat:index/configuration:Configuration", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "api://github.com/pulumiverse",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Configuration resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Configuration Get(string name, Input<string> id, ConfigurationState? state = null, CustomResourceOptions? options = null)
        {
            return new Configuration(name, id, state, options);
        }
    }

    public sealed class ConfigurationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of the Config.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The evaluation version of the Config. Possible values: `v1`, `v2`. Default value: `v1`. Using `v2` enables the new
        /// features of [Config V2](https://configcat.com/docs/advanced/config-v2).
        /// </summary>
        [Input("evaluationVersion")]
        public Input<string>? EvaluationVersion { get; set; }

        /// <summary>
        /// The name of the Config.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The order of the Config within a Product (zero-based). If multiple Configs has the same order, they are displayed in
        /// alphabetical order.
        /// </summary>
        [Input("order", required: true)]
        public Input<int> Order { get; set; } = null!;

        /// <summary>
        /// The ID of the Product.
        /// </summary>
        [Input("productId", required: true)]
        public Input<string> ProductId { get; set; } = null!;

        public ConfigurationArgs()
        {
        }
        public static new ConfigurationArgs Empty => new ConfigurationArgs();
    }

    public sealed class ConfigurationState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of the Config.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The evaluation version of the Config. Possible values: `v1`, `v2`. Default value: `v1`. Using `v2` enables the new
        /// features of [Config V2](https://configcat.com/docs/advanced/config-v2).
        /// </summary>
        [Input("evaluationVersion")]
        public Input<string>? EvaluationVersion { get; set; }

        /// <summary>
        /// The name of the Config.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The order of the Config within a Product (zero-based). If multiple Configs has the same order, they are displayed in
        /// alphabetical order.
        /// </summary>
        [Input("order")]
        public Input<int>? Order { get; set; }

        /// <summary>
        /// The ID of the Product.
        /// </summary>
        [Input("productId")]
        public Input<string>? ProductId { get; set; }

        public ConfigurationState()
        {
        }
        public static new ConfigurationState Empty => new ConfigurationState();
    }
}
