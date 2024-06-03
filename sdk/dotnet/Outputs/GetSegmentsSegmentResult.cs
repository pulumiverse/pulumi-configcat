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
    public sealed class GetSegmentsSegmentResult
    {
        /// <summary>
        /// The description of the Segment.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// The name of the Segment.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The unique Segment ID.
        /// </summary>
        public readonly string SegmentId;

        [OutputConstructor]
        private GetSegmentsSegmentResult(
            string description,

            string name,

            string segmentId)
        {
            Description = description;
            Name = name;
            SegmentId = segmentId;
        }
    }
}