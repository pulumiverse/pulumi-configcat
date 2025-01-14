# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .configuration import *
from .environment import *
from .get_configurations import *
from .get_environments import *
from .get_organizations import *
from .get_permission_groups import *
from .get_products import *
from .get_sdk_keys import *
from .get_segments import *
from .get_settings import *
from .get_tags import *
from .permission_group import *
from .product import *
from .provider import *
from .segment import *
from .setting import *
from .setting_tag import *
from .setting_value import *
from .tag import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumiverse_configcat.config as __config
    config = __config
else:
    config = _utilities.lazy_import('pulumiverse_configcat.config')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "configcat",
  "mod": "index/configuration",
  "fqn": "pulumiverse_configcat",
  "classes": {
   "configcat:index/configuration:Configuration": "Configuration"
  }
 },
 {
  "pkg": "configcat",
  "mod": "index/environment",
  "fqn": "pulumiverse_configcat",
  "classes": {
   "configcat:index/environment:Environment": "Environment"
  }
 },
 {
  "pkg": "configcat",
  "mod": "index/permissionGroup",
  "fqn": "pulumiverse_configcat",
  "classes": {
   "configcat:index/permissionGroup:PermissionGroup": "PermissionGroup"
  }
 },
 {
  "pkg": "configcat",
  "mod": "index/product",
  "fqn": "pulumiverse_configcat",
  "classes": {
   "configcat:index/product:Product": "Product"
  }
 },
 {
  "pkg": "configcat",
  "mod": "index/segment",
  "fqn": "pulumiverse_configcat",
  "classes": {
   "configcat:index/segment:Segment": "Segment"
  }
 },
 {
  "pkg": "configcat",
  "mod": "index/setting",
  "fqn": "pulumiverse_configcat",
  "classes": {
   "configcat:index/setting:Setting": "Setting"
  }
 },
 {
  "pkg": "configcat",
  "mod": "index/settingTag",
  "fqn": "pulumiverse_configcat",
  "classes": {
   "configcat:index/settingTag:SettingTag": "SettingTag"
  }
 },
 {
  "pkg": "configcat",
  "mod": "index/settingValue",
  "fqn": "pulumiverse_configcat",
  "classes": {
   "configcat:index/settingValue:SettingValue": "SettingValue"
  }
 },
 {
  "pkg": "configcat",
  "mod": "index/tag",
  "fqn": "pulumiverse_configcat",
  "classes": {
   "configcat:index/tag:Tag": "Tag"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "configcat",
  "token": "pulumi:providers:configcat",
  "fqn": "pulumiverse_configcat",
  "class": "Provider"
 }
]
"""
)
