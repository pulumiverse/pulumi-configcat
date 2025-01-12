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
    /// <summary>
    /// ## # configcat.Setting Resource
    /// 
    /// Creates and manages a **Feature Flag/Setting**. [Read more about the anatomy of a Feature Flag or Setting.](https://configcat.com/docs/main-concepts)
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Configcat = Pulumi.Configcat;
    /// using Configcat = Pulumiverse.Configcat;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var myProducts = Configcat.GetProducts.Invoke(new()
    ///     {
    ///         NameFilterRegex = "ConfigCat's product",
    ///     });
    /// 
    ///     var myConfigs = Configcat.GetConfigs.Invoke(new()
    ///     {
    ///         ProductId = myProducts.Apply(getProductsResult =&gt; getProductsResult.Products[0]?.ProductId),
    ///         NameFilterRegex = "Main Config",
    ///     });
    /// 
    ///     var mySetting = new Configcat.Setting("my_setting", new()
    ///     {
    ///         ConfigId = myConfigs.Apply(getConfigsResult =&gt; getConfigsResult.Configs[0]?.ConfigId),
    ///         Key = "isAwesomeFeatureEnabled",
    ///         Name = "My awesome feature flag",
    ///         Hint = "This is the hint for my awesome feature flag",
    ///         SettingType = "boolean",
    ///     });
    /// 
    ///     return new Dictionary&lt;string, object?&gt;
    ///     {
    ///         ["settingId"] = mySetting.Id,
    ///     };
    /// });
    /// ```
    /// 
    /// ## Endpoints used
    /// 
    /// * [Get Flag](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/get-setting)
    /// * [Create Flag](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/create-setting)
    /// * [Update Flag](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/update-setting)
    /// * [Delete Flag](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/delete-setting)
    /// 
    /// ## Import
    /// 
    /// Feature Flags/Settings can be imported using the SettingId. Get the SettingId using e.g. the [List Flags API](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/get-settings).
    /// 
    /// ```sh
    /// $ pulumi import configcat:index/setting:Setting example 1234
    /// ```
    /// Read more about importing.
    /// </summary>
    [ConfigcatResourceType("configcat:index/setting:Setting")]
    public partial class Setting : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The ID of the Config.
        /// </summary>
        [Output("configId")]
        public Output<string> ConfigId { get; private set; } = null!;

        /// <summary>
        /// The hint of the Setting.
        /// </summary>
        [Output("hint")]
        public Output<string?> Hint { get; private set; } = null!;

        /// <summary>
        /// The key of the Feature Flag/Setting.
        /// </summary>
        [Output("key")]
        public Output<string> Key { get; private set; } = null!;

        /// <summary>
        /// The name of the Setting.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Default: `boolean`. The Setting's type.  
        /// Available values: `boolean`|`string`|`int`|`double`.
        /// </summary>
        [Output("settingType")]
        public Output<string?> SettingType { get; private set; } = null!;


        /// <summary>
        /// Create a Setting resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Setting(string name, SettingArgs args, CustomResourceOptions? options = null)
            : base("configcat:index/setting:Setting", name, args ?? new SettingArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Setting(string name, Input<string> id, SettingState? state = null, CustomResourceOptions? options = null)
            : base("configcat:index/setting:Setting", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Setting resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Setting Get(string name, Input<string> id, SettingState? state = null, CustomResourceOptions? options = null)
        {
            return new Setting(name, id, state, options);
        }
    }

    public sealed class SettingArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the Config.
        /// </summary>
        [Input("configId", required: true)]
        public Input<string> ConfigId { get; set; } = null!;

        /// <summary>
        /// The hint of the Setting.
        /// </summary>
        [Input("hint")]
        public Input<string>? Hint { get; set; }

        /// <summary>
        /// The key of the Feature Flag/Setting.
        /// </summary>
        [Input("key", required: true)]
        public Input<string> Key { get; set; } = null!;

        /// <summary>
        /// The name of the Setting.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Default: `boolean`. The Setting's type.  
        /// Available values: `boolean`|`string`|`int`|`double`.
        /// </summary>
        [Input("settingType")]
        public Input<string>? SettingType { get; set; }

        public SettingArgs()
        {
        }
        public static new SettingArgs Empty => new SettingArgs();
    }

    public sealed class SettingState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the Config.
        /// </summary>
        [Input("configId")]
        public Input<string>? ConfigId { get; set; }

        /// <summary>
        /// The hint of the Setting.
        /// </summary>
        [Input("hint")]
        public Input<string>? Hint { get; set; }

        /// <summary>
        /// The key of the Feature Flag/Setting.
        /// </summary>
        [Input("key")]
        public Input<string>? Key { get; set; }

        /// <summary>
        /// The name of the Setting.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Default: `boolean`. The Setting's type.  
        /// Available values: `boolean`|`string`|`int`|`double`.
        /// </summary>
        [Input("settingType")]
        public Input<string>? SettingType { get; set; }

        public SettingState()
        {
        }
        public static new SettingState Empty => new SettingState();
    }
}
