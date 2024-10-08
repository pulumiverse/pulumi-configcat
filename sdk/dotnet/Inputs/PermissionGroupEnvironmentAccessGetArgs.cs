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

    public sealed class PermissionGroupEnvironmentAccessGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Represent the environment specific Feature Management permission. Possible values: full, readOnly, none. Default: none.
        /// </summary>
        [Input("environmentAccesstype")]
        public Input<string>? EnvironmentAccesstype { get; set; }

        /// <summary>
        /// The unique [Environment](https://configcat.com/docs/main-concepts/#environment) ID.
        /// </summary>
        [Input("environmentId", required: true)]
        public Input<string> EnvironmentId { get; set; } = null!;

        public PermissionGroupEnvironmentAccessGetArgs()
        {
        }
        public static new PermissionGroupEnvironmentAccessGetArgs Empty => new PermissionGroupEnvironmentAccessGetArgs();
    }
}
