// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Configcat.Outputs
{

    [OutputType]
    public sealed class SettingValueV2TargetingRulePercentageOption
    {
        /// <summary>
        /// A number between 0 and 100 that represents a randomly allocated fraction of the users.
        /// </summary>
        public readonly int Percentage;
        /// <summary>
        /// Represents the value of a Feature Flag or Setting.
        /// </summary>
        public readonly Outputs.SettingValueV2TargetingRulePercentageOptionValue Value;

        [OutputConstructor]
        private SettingValueV2TargetingRulePercentageOption(
            int percentage,

            Outputs.SettingValueV2TargetingRulePercentageOptionValue value)
        {
            Percentage = percentage;
            Value = value;
        }
    }
}
