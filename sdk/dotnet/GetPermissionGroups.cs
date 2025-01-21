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
    public static class GetPermissionGroups
    {
        /// <summary>
        /// Use this data source to access information about existing **Permission Groups**. [What is a Permission Group in ConfigCat?](https://configcat.com/docs/advanced/team-management/team-management-basics/#permissions--permission-groups-product-level)
        /// 
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Configcat = Pulumi.Configcat;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var config = new Config();
        ///     var productId = config.Require("productId");
        ///     var myPermissionGroups = Configcat.GetPermissionGroups.Invoke(new()
        ///     {
        ///         ProductId = productId,
        ///         NameFilterRegex = "Administrators",
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["permissionGroupId"] = myPermissionGroups.Apply(getPermissionGroupsResult =&gt; getPermissionGroupsResult.PermissionGroups[0]?.PermissionGroupId),
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Task<GetPermissionGroupsResult> InvokeAsync(GetPermissionGroupsArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetPermissionGroupsResult>("configcat:index/getPermissionGroups:getPermissionGroups", args ?? new GetPermissionGroupsArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to access information about existing **Permission Groups**. [What is a Permission Group in ConfigCat?](https://configcat.com/docs/advanced/team-management/team-management-basics/#permissions--permission-groups-product-level)
        /// 
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Configcat = Pulumi.Configcat;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var config = new Config();
        ///     var productId = config.Require("productId");
        ///     var myPermissionGroups = Configcat.GetPermissionGroups.Invoke(new()
        ///     {
        ///         ProductId = productId,
        ///         NameFilterRegex = "Administrators",
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["permissionGroupId"] = myPermissionGroups.Apply(getPermissionGroupsResult =&gt; getPermissionGroupsResult.PermissionGroups[0]?.PermissionGroupId),
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Output<GetPermissionGroupsResult> Invoke(GetPermissionGroupsInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetPermissionGroupsResult>("configcat:index/getPermissionGroups:getPermissionGroups", args ?? new GetPermissionGroupsInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to access information about existing **Permission Groups**. [What is a Permission Group in ConfigCat?](https://configcat.com/docs/advanced/team-management/team-management-basics/#permissions--permission-groups-product-level)
        /// 
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Configcat = Pulumi.Configcat;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var config = new Config();
        ///     var productId = config.Require("productId");
        ///     var myPermissionGroups = Configcat.GetPermissionGroups.Invoke(new()
        ///     {
        ///         ProductId = productId,
        ///         NameFilterRegex = "Administrators",
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["permissionGroupId"] = myPermissionGroups.Apply(getPermissionGroupsResult =&gt; getPermissionGroupsResult.PermissionGroups[0]?.PermissionGroupId),
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Output<GetPermissionGroupsResult> Invoke(GetPermissionGroupsInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetPermissionGroupsResult>("configcat:index/getPermissionGroups:getPermissionGroups", args ?? new GetPermissionGroupsInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPermissionGroupsArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Filter the Permission Groups by name.
        /// </summary>
        [Input("nameFilterRegex")]
        public string? NameFilterRegex { get; set; }

        /// <summary>
        /// The ID of the Product.
        /// </summary>
        [Input("productId", required: true)]
        public string ProductId { get; set; } = null!;

        public GetPermissionGroupsArgs()
        {
        }
        public static new GetPermissionGroupsArgs Empty => new GetPermissionGroupsArgs();
    }

    public sealed class GetPermissionGroupsInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Filter the Permission Groups by name.
        /// </summary>
        [Input("nameFilterRegex")]
        public Input<string>? NameFilterRegex { get; set; }

        /// <summary>
        /// The ID of the Product.
        /// </summary>
        [Input("productId", required: true)]
        public Input<string> ProductId { get; set; } = null!;

        public GetPermissionGroupsInvokeArgs()
        {
        }
        public static new GetPermissionGroupsInvokeArgs Empty => new GetPermissionGroupsInvokeArgs();
    }


    [OutputType]
    public sealed class GetPermissionGroupsResult
    {
        /// <summary>
        /// Internal ID of the data source. Do not use.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Filter the Permission Groups by name.
        /// </summary>
        public readonly string? NameFilterRegex;
        public readonly ImmutableArray<Outputs.GetPermissionGroupsPermissionGroupResult> PermissionGroups;
        /// <summary>
        /// The ID of the Product.
        /// </summary>
        public readonly string ProductId;

        [OutputConstructor]
        private GetPermissionGroupsResult(
            string id,

            string? nameFilterRegex,

            ImmutableArray<Outputs.GetPermissionGroupsPermissionGroupResult> permissionGroups,

            string productId)
        {
            Id = id;
            NameFilterRegex = nameFilterRegex;
            PermissionGroups = permissionGroups;
            ProductId = productId;
        }
    }
}
