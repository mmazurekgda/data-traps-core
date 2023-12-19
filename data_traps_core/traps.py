from pydantic import BaseModel
from typing_extensions import Annotated
from typing import List
from pydantic import AfterValidator
from pydantic import FilePath
from pydantic_yaml import to_yaml_str, parse_yaml_raw_as
from data_traps_core.defaults import K8_NAMESPACE, ENVIRONMENTS
import re


def validate_environments(environments: List[str]) -> List[str]:
    assert len(environments) != 0, "Destination list cannot be empty"
    # check if all environments are valid
    assert all(env in ENVIRONMENTS for env in environments), (
        f"Invalid environments: '{environments}'. "
        f"Must be from '{ENVIRONMENTS}'."
    )
    return environments


def parse_k8_name(name: str) -> str:
    s = name.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_-]+", "-", s)
    s = re.sub(r"^-+|-+$", "", s)
    return s


Environments = Annotated[List[str], AfterValidator(validate_environments)]
K8Name = Annotated[str, AfterValidator(parse_k8_name)]


class Trap(BaseModel):
    name: K8Name
    experiment: K8Name
    namespace: K8Name = K8_NAMESPACE
    environments: Environments = ["development"]
    ignore: bool = False
    bait_file: str = ""

    @staticmethod
    def yaml_to_model(file_path: FilePath) -> "Trap":
        with FilePath(file_path).open("r") as f:
            content = f.read()
        return parse_yaml_raw_as(Trap, content)

    def dump_to_yaml(self, file_path: FilePath) -> None:
        with FilePath(file_path).open("w") as f:
            f.write(to_yaml_str(self))
