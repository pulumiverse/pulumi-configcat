// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Configcat.Inputs
{

    public sealed class SettingValueV2TargetingRuleConditionPrerequisiteFlagConditionGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Prerequisite flag comparison operator used during the evaluation process. Possible values: `equals`,`doesNotEqual`
        /// </summary>
        [Input("comparator", required: true)]
        public Input<string> Comparator { get; set; } = null!;

        /// <summary>
        /// Represents the value of a Feature Flag or Setting.
        /// </summary>
        [Input("comparisonValue", required: true)]
        public Input<Inputs.SettingValueV2TargetingRuleConditionPrerequisiteFlagConditionComparisonValueGetArgs> ComparisonValue { get; set; } = null!;

        /// <summary>
        /// The prerequisite flag's identifier.
        /// </summary>
        [Input("prerequisiteSettingId", required: true)]
        public Input<string> PrerequisiteSettingId { get; set; } = null!;

        public SettingValueV2TargetingRuleConditionPrerequisiteFlagConditionGetArgs()
        {
        }
        public static new SettingValueV2TargetingRuleConditionPrerequisiteFlagConditionGetArgs Empty => new SettingValueV2TargetingRuleConditionPrerequisiteFlagConditionGetArgs();
    }
}
