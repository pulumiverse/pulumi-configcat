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
    public static class GetSettings
    {
        /// <summary>
        /// Use this data source to access information about existing **Feature Flags or Settings**. [What is a Feature Flag or Setting in ConfigCat?](https://configcat.com/docs/main-concepts)
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
        ///     var configId = config.Require("configId");
        ///     var settings = Configcat.GetSettings.Invoke(new()
        ///     {
        ///         ConfigId = configId,
        ///         KeyFilterRegex = "isAwesomeFeatureEnabled",
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["settingId"] = settings.Apply(getSettingsResult =&gt; getSettingsResult.Settings[0]?.SettingId),
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Task<GetSettingsResult> InvokeAsync(GetSettingsArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetSettingsResult>("configcat:index/getSettings:getSettings", args ?? new GetSettingsArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to access information about existing **Feature Flags or Settings**. [What is a Feature Flag or Setting in ConfigCat?](https://configcat.com/docs/main-concepts)
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
        ///     var configId = config.Require("configId");
        ///     var settings = Configcat.GetSettings.Invoke(new()
        ///     {
        ///         ConfigId = configId,
        ///         KeyFilterRegex = "isAwesomeFeatureEnabled",
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["settingId"] = settings.Apply(getSettingsResult =&gt; getSettingsResult.Settings[0]?.SettingId),
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Output<GetSettingsResult> Invoke(GetSettingsInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetSettingsResult>("configcat:index/getSettings:getSettings", args ?? new GetSettingsInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// Use this data source to access information about existing **Feature Flags or Settings**. [What is a Feature Flag or Setting in ConfigCat?](https://configcat.com/docs/main-concepts)
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
        ///     var configId = config.Require("configId");
        ///     var settings = Configcat.GetSettings.Invoke(new()
        ///     {
        ///         ConfigId = configId,
        ///         KeyFilterRegex = "isAwesomeFeatureEnabled",
        ///     });
        /// 
        ///     return new Dictionary&lt;string, object?&gt;
        ///     {
        ///         ["settingId"] = settings.Apply(getSettingsResult =&gt; getSettingsResult.Settings[0]?.SettingId),
        ///     };
        /// });
        /// ```
        /// </summary>
        public static Output<GetSettingsResult> Invoke(GetSettingsInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetSettingsResult>("configcat:index/getSettings:getSettings", args ?? new GetSettingsInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetSettingsArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the Config.
        /// </summary>
        [Input("configId", required: true)]
        public string ConfigId { get; set; } = null!;

        /// <summary>
        /// Filter the Feature Flags or Settingss by key.
        /// </summary>
        [Input("keyFilterRegex")]
        public string? KeyFilterRegex { get; set; }

        public GetSettingsArgs()
        {
        }
        public static new GetSettingsArgs Empty => new GetSettingsArgs();
    }

    public sealed class GetSettingsInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the Config.
        /// </summary>
        [Input("configId", required: true)]
        public Input<string> ConfigId { get; set; } = null!;

        /// <summary>
        /// Filter the Feature Flags or Settingss by key.
        /// </summary>
        [Input("keyFilterRegex")]
        public Input<string>? KeyFilterRegex { get; set; }

        public GetSettingsInvokeArgs()
        {
        }
        public static new GetSettingsInvokeArgs Empty => new GetSettingsInvokeArgs();
    }


    [OutputType]
    public sealed class GetSettingsResult
    {
        /// <summary>
        /// The ID of the Config.
        /// </summary>
        public readonly string ConfigId;
        /// <summary>
        /// Internal ID of the data source. Do not use.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Filter the Feature Flags or Settingss by key.
        /// </summary>
        public readonly string? KeyFilterRegex;
        public readonly ImmutableArray<Outputs.GetSettingsSettingResult> Settings;

        [OutputConstructor]
        private GetSettingsResult(
            string configId,

            string id,

            string? keyFilterRegex,

            ImmutableArray<Outputs.GetSettingsSettingResult> settings)
        {
            ConfigId = configId;
            Id = id;
            KeyFilterRegex = keyFilterRegex;
            Settings = settings;
        }
    }
}
