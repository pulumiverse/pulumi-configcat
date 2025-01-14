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
    /// ## # configcat.SettingValue Resource
    /// 
    /// Initializes and updates **Feature Flag and Setting** values. [Read more about the anatomy of a Feature Flag or Setting.](https://configcat.com/docs/main-concepts)
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
    ///     var myConfigs = Configcat.GetConfigurations.Invoke(new()
    ///     {
    ///         ProductId = myProducts.Apply(getProductsResult =&gt; getProductsResult.Products[0]?.ProductId),
    ///         NameFilterRegex = "Main Config",
    ///     });
    /// 
    ///     var myEnvironments = Configcat.GetEnvironments.Invoke(new()
    ///     {
    ///         ProductId = myProducts.Apply(getProductsResult =&gt; getProductsResult.Products[0]?.ProductId),
    ///         NameFilterRegex = "Test",
    ///     });
    /// 
    ///     var mySettings = Configcat.GetSettings.Invoke(new()
    ///     {
    ///         ConfigId = myConfigs.Apply(getConfigurationsResult =&gt; getConfigurationsResult.Configs[0]?.ConfigId),
    ///         KeyFilterRegex = "isAwesomeFeatureEnabled",
    ///     });
    /// 
    ///     var mySettingValue = new Configcat.SettingValue("my_setting_value", new()
    ///     {
    ///         EnvironmentId = myEnvironments.Apply(getEnvironmentsResult =&gt; getEnvironmentsResult.Environments[0]?.EnvironmentId),
    ///         SettingId = mySettings.Apply(getSettingsResult =&gt; getSettingsResult.Settings[0]?.SettingId),
    ///         MandatoryNotes = "mandatory notes",
    ///         Value = "true",
    ///         RolloutRules = new[]
    ///         {
    ///             new Configcat.Inputs.SettingValueRolloutRuleArgs
    ///             {
    ///                 ComparisonAttribute = "Email",
    ///                 Comparator = "contains",
    ///                 ComparisonValue = "@mycompany.com",
    ///                 Value = "true",
    ///             },
    ///             new Configcat.Inputs.SettingValueRolloutRuleArgs
    ///             {
    ///                 ComparisonAttribute = "custom",
    ///                 Comparator = "isOneOf",
    ///                 ComparisonValue = "red",
    ///                 Value = "false",
    ///             },
    ///         },
    ///         PercentageItems = new[]
    ///         {
    ///             new Configcat.Inputs.SettingValuePercentageItemArgs
    ///             {
    ///                 Percentage = "20",
    ///                 Value = "true",
    ///             },
    ///             new Configcat.Inputs.SettingValuePercentageItemArgs
    ///             {
    ///                 Percentage = "80",
    ///                 Value = "false",
    ///             },
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Endpoints used
    /// 
    /// * [Get Value](https://api.configcat.com/docs/#tag/Feature-Flag-and-Setting-values/operation/get-setting-value)
    /// * [Replace Value](https://api.configcat.com/docs/#tag/Feature-Flag-and-Setting-values/operation/replace-setting-value)
    /// 
    /// ## Import
    /// 
    /// Feature Flag/Setting values can be imported using a combined EnvironmentID:SettingId ID.
    /// 
    /// Get the SettingId using e.g. the [List Flags API](https://api.configcat.com/docs/#tag/Feature-Flags-and-Settings/operation/get-settings).
    /// 
    /// Get the EnvironmentId using e.g. the [List Environments API](https://api.configcat.com/docs/#tag/Environments/operation/get-environments).
    /// 
    /// ```sh
    /// $ pulumi import configcat:index/settingValue:SettingValue example 08d86d63-2726-47cd-8bfc-59608ecb91e2:1234
    /// ```
    /// 
    /// Read more about importing.
    /// </summary>
    [ConfigcatResourceType("configcat:index/settingValue:SettingValue")]
    public partial class SettingValue : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The ID of the Environment.
        /// </summary>
        [Output("environmentId")]
        public Output<string> EnvironmentId { get; private set; } = null!;

        /// <summary>
        /// Default: true. Read more below.  
        /// 
        /// The Feature Flag/Setting's value
        /// </summary>
        [Output("initOnly")]
        public Output<bool?> InitOnly { get; private set; } = null!;

        /// <summary>
        /// Default: "". If the Product's "Mandatory notes" preference is turned on for the Environment the Mandatory note must be passed.
        /// </summary>
        [Output("mandatoryNotes")]
        public Output<string?> MandatoryNotes { get; private set; } = null!;

        /// <summary>
        /// A list to define [Percentage items](https://configcat.com/docs/advanced/targeting/#targeting-a-percentage-of-users). Read more below.
        /// </summary>
        [Output("percentageItems")]
        public Output<ImmutableArray<Outputs.SettingValuePercentageItem>> PercentageItems { get; private set; } = null!;

        /// <summary>
        /// A list to define [Rollout rules](https://configcat.com/docs/advanced/targeting/#anatomy-of-a-targeting-rule). Read more below.
        /// </summary>
        [Output("rolloutRules")]
        public Output<ImmutableArray<Outputs.SettingValueRolloutRule>> RolloutRules { get; private set; } = null!;

        /// <summary>
        /// The ID of the Feature Flag/Setting.
        /// </summary>
        [Output("settingId")]
        public Output<string> SettingId { get; private set; } = null!;

        /// <summary>
        /// The Setting's type.
        /// </summary>
        [Output("settingType")]
        public Output<string> SettingType { get; private set; } = null!;

        /// <summary>
        /// The Setting's value. Type: `string`. It must be compatible with the `setting_type`.
        /// </summary>
        [Output("value")]
        public Output<string> Value { get; private set; } = null!;


        /// <summary>
        /// Create a SettingValue resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SettingValue(string name, SettingValueArgs args, CustomResourceOptions? options = null)
            : base("configcat:index/settingValue:SettingValue", name, args ?? new SettingValueArgs(), MakeResourceOptions(options, ""))
        {
        }

        private SettingValue(string name, Input<string> id, SettingValueState? state = null, CustomResourceOptions? options = null)
            : base("configcat:index/settingValue:SettingValue", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing SettingValue resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SettingValue Get(string name, Input<string> id, SettingValueState? state = null, CustomResourceOptions? options = null)
        {
            return new SettingValue(name, id, state, options);
        }
    }

    public sealed class SettingValueArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the Environment.
        /// </summary>
        [Input("environmentId", required: true)]
        public Input<string> EnvironmentId { get; set; } = null!;

        /// <summary>
        /// Default: true. Read more below.  
        /// 
        /// The Feature Flag/Setting's value
        /// </summary>
        [Input("initOnly")]
        public Input<bool>? InitOnly { get; set; }

        /// <summary>
        /// Default: "". If the Product's "Mandatory notes" preference is turned on for the Environment the Mandatory note must be passed.
        /// </summary>
        [Input("mandatoryNotes")]
        public Input<string>? MandatoryNotes { get; set; }

        [Input("percentageItems")]
        private InputList<Inputs.SettingValuePercentageItemArgs>? _percentageItems;

        /// <summary>
        /// A list to define [Percentage items](https://configcat.com/docs/advanced/targeting/#targeting-a-percentage-of-users). Read more below.
        /// </summary>
        public InputList<Inputs.SettingValuePercentageItemArgs> PercentageItems
        {
            get => _percentageItems ?? (_percentageItems = new InputList<Inputs.SettingValuePercentageItemArgs>());
            set => _percentageItems = value;
        }

        [Input("rolloutRules")]
        private InputList<Inputs.SettingValueRolloutRuleArgs>? _rolloutRules;

        /// <summary>
        /// A list to define [Rollout rules](https://configcat.com/docs/advanced/targeting/#anatomy-of-a-targeting-rule). Read more below.
        /// </summary>
        public InputList<Inputs.SettingValueRolloutRuleArgs> RolloutRules
        {
            get => _rolloutRules ?? (_rolloutRules = new InputList<Inputs.SettingValueRolloutRuleArgs>());
            set => _rolloutRules = value;
        }

        /// <summary>
        /// The ID of the Feature Flag/Setting.
        /// </summary>
        [Input("settingId", required: true)]
        public Input<string> SettingId { get; set; } = null!;

        /// <summary>
        /// The Setting's value. Type: `string`. It must be compatible with the `setting_type`.
        /// </summary>
        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public SettingValueArgs()
        {
        }
        public static new SettingValueArgs Empty => new SettingValueArgs();
    }

    public sealed class SettingValueState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the Environment.
        /// </summary>
        [Input("environmentId")]
        public Input<string>? EnvironmentId { get; set; }

        /// <summary>
        /// Default: true. Read more below.  
        /// 
        /// The Feature Flag/Setting's value
        /// </summary>
        [Input("initOnly")]
        public Input<bool>? InitOnly { get; set; }

        /// <summary>
        /// Default: "". If the Product's "Mandatory notes" preference is turned on for the Environment the Mandatory note must be passed.
        /// </summary>
        [Input("mandatoryNotes")]
        public Input<string>? MandatoryNotes { get; set; }

        [Input("percentageItems")]
        private InputList<Inputs.SettingValuePercentageItemGetArgs>? _percentageItems;

        /// <summary>
        /// A list to define [Percentage items](https://configcat.com/docs/advanced/targeting/#targeting-a-percentage-of-users). Read more below.
        /// </summary>
        public InputList<Inputs.SettingValuePercentageItemGetArgs> PercentageItems
        {
            get => _percentageItems ?? (_percentageItems = new InputList<Inputs.SettingValuePercentageItemGetArgs>());
            set => _percentageItems = value;
        }

        [Input("rolloutRules")]
        private InputList<Inputs.SettingValueRolloutRuleGetArgs>? _rolloutRules;

        /// <summary>
        /// A list to define [Rollout rules](https://configcat.com/docs/advanced/targeting/#anatomy-of-a-targeting-rule). Read more below.
        /// </summary>
        public InputList<Inputs.SettingValueRolloutRuleGetArgs> RolloutRules
        {
            get => _rolloutRules ?? (_rolloutRules = new InputList<Inputs.SettingValueRolloutRuleGetArgs>());
            set => _rolloutRules = value;
        }

        /// <summary>
        /// The ID of the Feature Flag/Setting.
        /// </summary>
        [Input("settingId")]
        public Input<string>? SettingId { get; set; }

        /// <summary>
        /// The Setting's type.
        /// </summary>
        [Input("settingType")]
        public Input<string>? SettingType { get; set; }

        /// <summary>
        /// The Setting's value. Type: `string`. It must be compatible with the `setting_type`.
        /// </summary>
        [Input("value")]
        public Input<string>? Value { get; set; }

        public SettingValueState()
        {
        }
        public static new SettingValueState Empty => new SettingValueState();
    }
}
