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
    [ConfigcatResourceType("configcat:index/settingValueV2:SettingValueV2")]
    public partial class SettingValueV2 : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The ID of the Environment.
        /// </summary>
        [Output("environmentId")]
        public Output<string> EnvironmentId { get; private set; } = null!;

        [Output("initOnly")]
        public Output<bool> InitOnly { get; private set; } = null!;

        /// <summary>
        /// If the Product's "Mandatory notes" preference is turned on for the Environment the Mandatory note must be passed.
        /// </summary>
        [Output("mandatoryNotes")]
        public Output<string?> MandatoryNotes { get; private set; } = null!;

        /// <summary>
        /// The user attribute used for percentage evaluation. If not set, it defaults to the Identifier user object attribute.
        /// </summary>
        [Output("percentageEvaluationAttribute")]
        public Output<string?> PercentageEvaluationAttribute { get; private set; } = null!;

        /// <summary>
        /// The ID of the Feature Flag or Setting.
        /// </summary>
        [Output("settingId")]
        public Output<string> SettingId { get; private set; } = null!;

        /// <summary>
        /// The type of the Feature Flag or Setting. Available values: `boolean`|`string`|`int`|`double`.
        /// </summary>
        [Output("settingType")]
        public Output<string> SettingType { get; private set; } = null!;

        /// <summary>
        /// The targeting rules of the Feature Flag or Setting
        /// </summary>
        [Output("targetingRules")]
        public Output<ImmutableArray<Outputs.SettingValueV2TargetingRule>> TargetingRules { get; private set; } = null!;

        /// <summary>
        /// Represents the value of a Feature Flag or Setting.
        /// </summary>
        [Output("value")]
        public Output<Outputs.SettingValueV2Value> Value { get; private set; } = null!;


        /// <summary>
        /// Create a SettingValueV2 resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SettingValueV2(string name, SettingValueV2Args args, CustomResourceOptions? options = null)
            : base("configcat:index/settingValueV2:SettingValueV2", name, args ?? new SettingValueV2Args(), MakeResourceOptions(options, ""))
        {
        }

        private SettingValueV2(string name, Input<string> id, SettingValueV2State? state = null, CustomResourceOptions? options = null)
            : base("configcat:index/settingValueV2:SettingValueV2", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing SettingValueV2 resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SettingValueV2 Get(string name, Input<string> id, SettingValueV2State? state = null, CustomResourceOptions? options = null)
        {
            return new SettingValueV2(name, id, state, options);
        }
    }

    public sealed class SettingValueV2Args : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the Environment.
        /// </summary>
        [Input("environmentId", required: true)]
        public Input<string> EnvironmentId { get; set; } = null!;

        [Input("initOnly")]
        public Input<bool>? InitOnly { get; set; }

        /// <summary>
        /// If the Product's "Mandatory notes" preference is turned on for the Environment the Mandatory note must be passed.
        /// </summary>
        [Input("mandatoryNotes")]
        public Input<string>? MandatoryNotes { get; set; }

        /// <summary>
        /// The user attribute used for percentage evaluation. If not set, it defaults to the Identifier user object attribute.
        /// </summary>
        [Input("percentageEvaluationAttribute")]
        public Input<string>? PercentageEvaluationAttribute { get; set; }

        /// <summary>
        /// The ID of the Feature Flag or Setting.
        /// </summary>
        [Input("settingId", required: true)]
        public Input<string> SettingId { get; set; } = null!;

        [Input("targetingRules")]
        private InputList<Inputs.SettingValueV2TargetingRuleArgs>? _targetingRules;

        /// <summary>
        /// The targeting rules of the Feature Flag or Setting
        /// </summary>
        public InputList<Inputs.SettingValueV2TargetingRuleArgs> TargetingRules
        {
            get => _targetingRules ?? (_targetingRules = new InputList<Inputs.SettingValueV2TargetingRuleArgs>());
            set => _targetingRules = value;
        }

        /// <summary>
        /// Represents the value of a Feature Flag or Setting.
        /// </summary>
        [Input("value", required: true)]
        public Input<Inputs.SettingValueV2ValueArgs> Value { get; set; } = null!;

        public SettingValueV2Args()
        {
        }
        public static new SettingValueV2Args Empty => new SettingValueV2Args();
    }

    public sealed class SettingValueV2State : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the Environment.
        /// </summary>
        [Input("environmentId")]
        public Input<string>? EnvironmentId { get; set; }

        [Input("initOnly")]
        public Input<bool>? InitOnly { get; set; }

        /// <summary>
        /// If the Product's "Mandatory notes" preference is turned on for the Environment the Mandatory note must be passed.
        /// </summary>
        [Input("mandatoryNotes")]
        public Input<string>? MandatoryNotes { get; set; }

        /// <summary>
        /// The user attribute used for percentage evaluation. If not set, it defaults to the Identifier user object attribute.
        /// </summary>
        [Input("percentageEvaluationAttribute")]
        public Input<string>? PercentageEvaluationAttribute { get; set; }

        /// <summary>
        /// The ID of the Feature Flag or Setting.
        /// </summary>
        [Input("settingId")]
        public Input<string>? SettingId { get; set; }

        /// <summary>
        /// The type of the Feature Flag or Setting. Available values: `boolean`|`string`|`int`|`double`.
        /// </summary>
        [Input("settingType")]
        public Input<string>? SettingType { get; set; }

        [Input("targetingRules")]
        private InputList<Inputs.SettingValueV2TargetingRuleGetArgs>? _targetingRules;

        /// <summary>
        /// The targeting rules of the Feature Flag or Setting
        /// </summary>
        public InputList<Inputs.SettingValueV2TargetingRuleGetArgs> TargetingRules
        {
            get => _targetingRules ?? (_targetingRules = new InputList<Inputs.SettingValueV2TargetingRuleGetArgs>());
            set => _targetingRules = value;
        }

        /// <summary>
        /// Represents the value of a Feature Flag or Setting.
        /// </summary>
        [Input("value")]
        public Input<Inputs.SettingValueV2ValueGetArgs>? Value { get; set; }

        public SettingValueV2State()
        {
        }
        public static new SettingValueV2State Empty => new SettingValueV2State();
    }
}
