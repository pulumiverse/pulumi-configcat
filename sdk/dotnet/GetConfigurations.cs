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
    public static class GetConfigurations
    {
        /// <summary>
        /// Use this data source to access information about existing **Configs**. [What is a Config in ConfigCat?](https://configcat.com/docs/main-concepts)
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
        ///     var myConfigs = Configcat.GetConfigurations.Invoke(new()
        ///     {
        ///         ProductId = productId,
        ///         NameFilterRegex = "Main Config",
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["configId"] = myConfigs.Apply(getConfigurationsResult =&gt; getConfigurationsResult.Configs[0]?.ConfigId),
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Task<GetConfigurationsResult> InvokeAsync(GetConfigurationsArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetConfigurationsResult>("configcat:index/getConfigurations:getConfigurations", args ?? new GetConfigurationsArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to access information about existing **Configs**. [What is a Config in ConfigCat?](https://configcat.com/docs/main-concepts)
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
        ///     var myConfigs = Configcat.GetConfigurations.Invoke(new()
        ///     {
        ///         ProductId = productId,
        ///         NameFilterRegex = "Main Config",
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["configId"] = myConfigs.Apply(getConfigurationsResult =&gt; getConfigurationsResult.Configs[0]?.ConfigId),
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Output<GetConfigurationsResult> Invoke(GetConfigurationsInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetConfigurationsResult>("configcat:index/getConfigurations:getConfigurations", args ?? new GetConfigurationsInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to access information about existing **Configs**. [What is a Config in ConfigCat?](https://configcat.com/docs/main-concepts)
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
        ///     var myConfigs = Configcat.GetConfigurations.Invoke(new()
        ///     {
        ///         ProductId = productId,
        ///         NameFilterRegex = "Main Config",
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["configId"] = myConfigs.Apply(getConfigurationsResult =&gt; getConfigurationsResult.Configs[0]?.ConfigId),
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Output<GetConfigurationsResult> Invoke(GetConfigurationsInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetConfigurationsResult>("configcat:index/getConfigurations:getConfigurations", args ?? new GetConfigurationsInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetConfigurationsArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Filter the Configs by name.
        /// </summary>
        [Input("nameFilterRegex")]
        public string? NameFilterRegex { get; set; }

        /// <summary>
        /// The ID of the Product.
        /// </summary>
        [Input("productId", required: true)]
        public string ProductId { get; set; } = null!;

        public GetConfigurationsArgs()
        {
        }
        public static new GetConfigurationsArgs Empty => new GetConfigurationsArgs();
    }

    public sealed class GetConfigurationsInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Filter the Configs by name.
        /// </summary>
        [Input("nameFilterRegex")]
        public Input<string>? NameFilterRegex { get; set; }

        /// <summary>
        /// The ID of the Product.
        /// </summary>
        [Input("productId", required: true)]
        public Input<string> ProductId { get; set; } = null!;

        public GetConfigurationsInvokeArgs()
        {
        }
        public static new GetConfigurationsInvokeArgs Empty => new GetConfigurationsInvokeArgs();
    }


    [OutputType]
    public sealed class GetConfigurationsResult
    {
        public readonly ImmutableArray<Outputs.GetConfigurationsConfigResult> Configs;
        /// <summary>
        /// Internal ID of the data source. Do not use.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Filter the Configs by name.
        /// </summary>
        public readonly string? NameFilterRegex;
        /// <summary>
        /// The ID of the Product.
        /// </summary>
        public readonly string ProductId;

        [OutputConstructor]
        private GetConfigurationsResult(
            ImmutableArray<Outputs.GetConfigurationsConfigResult> configs,

            string id,

            string? nameFilterRegex,

            string productId)
        {
            Configs = configs;
            Id = id;
            NameFilterRegex = nameFilterRegex;
            ProductId = productId;
        }
    }
}
