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

    public sealed class SettingValueV2TargetingRuleConditionUserConditionComparisonValueListValueArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// An optional hint for the comparison value.
        /// </summary>
        [Input("hint")]
        public Input<string>? Hint { get; set; }

        /// <summary>
        /// The actual comparison value.
        /// </summary>
        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public SettingValueV2TargetingRuleConditionUserConditionComparisonValueListValueArgs()
        {
        }
        public static new SettingValueV2TargetingRuleConditionUserConditionComparisonValueListValueArgs Empty => new SettingValueV2TargetingRuleConditionUserConditionComparisonValueListValueArgs();
    }
}
