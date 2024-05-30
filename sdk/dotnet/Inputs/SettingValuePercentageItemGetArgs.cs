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

    public sealed class SettingValuePercentageItemGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Any [number](https://configcat.com/docs/advanced/targeting/#-value) between 0 and 100 that represents a randomly allocated fraction of your users.
        /// </summary>
        [Input("percentage", required: true)]
        public Input<string> Percentage { get; set; } = null!;

        /// <summary>
        /// The exact [value](https://configcat.com/docs/advanced/targeting/#served-value-1) that will be served to the users that fall into that fraction. Type: `string`. It must be compatible with the `setting_type`.
        /// </summary>
        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public SettingValuePercentageItemGetArgs()
        {
        }
        public static new SettingValuePercentageItemGetArgs Empty => new SettingValuePercentageItemGetArgs();
    }
}
