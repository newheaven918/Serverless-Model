from samtranslator.model import PropertyType, Resource
from samtranslator.model.intrinsics import ref
from samtranslator.model.types import is_type, one_of, is_str


class CodeDeployApplication(Resource):
    resource_type = "AWS::CodeDeploy::Application"
    property_types = {"ComputePlatform": PropertyType(False, one_of(is_str(), is_type(dict)))}  # type: ignore[no-untyped-call, no-untyped-call, no-untyped-call, no-untyped-call]

    runtime_attrs = {"name": lambda self: ref(self.logical_id)}  # type: ignore[no-untyped-call]


class CodeDeployDeploymentGroup(Resource):
    resource_type = "AWS::CodeDeploy::DeploymentGroup"
    property_types = {
        "AlarmConfiguration": PropertyType(False, is_type(dict)),  # type: ignore[no-untyped-call, no-untyped-call]
        "ApplicationName": PropertyType(True, one_of(is_str(), is_type(dict))),  # type: ignore[no-untyped-call, no-untyped-call, no-untyped-call, no-untyped-call]
        "AutoRollbackConfiguration": PropertyType(False, is_type(dict)),  # type: ignore[no-untyped-call, no-untyped-call]
        "DeploymentConfigName": PropertyType(False, one_of(is_str(), is_type(dict))),  # type: ignore[no-untyped-call, no-untyped-call, no-untyped-call, no-untyped-call]
        "DeploymentStyle": PropertyType(False, is_type(dict)),  # type: ignore[no-untyped-call, no-untyped-call]
        "ServiceRoleArn": PropertyType(True, one_of(is_str(), is_type(dict))),  # type: ignore[no-untyped-call, no-untyped-call, no-untyped-call, no-untyped-call]
        "TriggerConfigurations": PropertyType(False, is_type(list)),  # type: ignore[no-untyped-call, no-untyped-call]
    }

    runtime_attrs = {"name": lambda self: ref(self.logical_id)}  # type: ignore[no-untyped-call]
