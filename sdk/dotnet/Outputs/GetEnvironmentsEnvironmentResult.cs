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
    public sealed class GetEnvironmentsEnvironmentResult
    {
        /// <summary>
        /// The color of the Environment.
        /// </summary>
        public readonly string Color;
        /// <summary>
        /// The description of the Environment.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// The unique Environment ID.
        /// </summary>
        public readonly string EnvironmentId;
        /// <summary>
        /// The name of the Environment.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The order of the Environment within a Product (zero-based).
        /// </summary>
        public readonly int Order;

        [OutputConstructor]
        private GetEnvironmentsEnvironmentResult(
            string color,

            string description,

            string environmentId,

            string name,

            int order)
        {
            Color = color;
            Description = description;
            EnvironmentId = environmentId;
            Name = name;
            Order = order;
        }
    }
}
