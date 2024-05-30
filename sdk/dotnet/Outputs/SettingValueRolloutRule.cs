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
    public sealed class SettingValueRolloutRule
    {
        /// <summary>
        /// The [comparator](https://configcat.com/docs/advanced/targeting/#comparator).
        /// </summary>
        public readonly string? Comparator;
        /// <summary>
        /// The [comparison attribute](https://configcat.com/docs/advanced/targeting/#attribute).
        /// </summary>
        public readonly string? ComparisonAttribute;
        /// <summary>
        /// The [comparison value](https://configcat.com/docs/advanced/targeting/#comparison-value).
        /// </summary>
        public readonly string? ComparisonValue;
        /// <summary>
        /// The segment_comparator. Possible values: isIn, isNotIn.
        /// </summary>
        public readonly string? SegmentComparator;
        /// <summary>
        /// The [Segment's](https://configcat.com/docs/advanced/segments) unique identifier.
        /// </summary>
        public readonly string? SegmentId;
        /// <summary>
        /// The exact [value](https://configcat.com/docs/advanced/targeting/#served-value) that will be served to the users who match the targeting rule. Type: `string`. It must be compatible with the `setting_type`.
        /// </summary>
        public readonly string Value;

        [OutputConstructor]
        private SettingValueRolloutRule(
            string? comparator,

            string? comparisonAttribute,

            string? comparisonValue,

            string? segmentComparator,

            string? segmentId,

            string value)
        {
            Comparator = comparator;
            ComparisonAttribute = comparisonAttribute;
            ComparisonValue = comparisonValue;
            SegmentComparator = segmentComparator;
            SegmentId = segmentId;
            Value = value;
        }
    }
}
