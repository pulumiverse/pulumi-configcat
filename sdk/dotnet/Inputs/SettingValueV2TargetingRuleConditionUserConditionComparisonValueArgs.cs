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

    public sealed class SettingValueV2TargetingRuleConditionUserConditionComparisonValueArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The number representation of the comparison value.
        /// </summary>
        [Input("doubleValue")]
        public Input<double>? DoubleValue { get; set; }

        [Input("listValues")]
        private InputList<Inputs.SettingValueV2TargetingRuleConditionUserConditionComparisonValueListValueArgs>? _listValues;

        /// <summary>
        /// The list representation of the comparison value.
        /// </summary>
        public InputList<Inputs.SettingValueV2TargetingRuleConditionUserConditionComparisonValueListValueArgs> ListValues
        {
            get => _listValues ?? (_listValues = new InputList<Inputs.SettingValueV2TargetingRuleConditionUserConditionComparisonValueListValueArgs>());
            set => _listValues = value;
        }

        /// <summary>
        /// The string representation of the comparison value.
        /// </summary>
        [Input("stringValue")]
        public Input<string>? StringValue { get; set; }

        public SettingValueV2TargetingRuleConditionUserConditionComparisonValueArgs()
        {
        }
        public static new SettingValueV2TargetingRuleConditionUserConditionComparisonValueArgs Empty => new SettingValueV2TargetingRuleConditionUserConditionComparisonValueArgs();
    }
}
