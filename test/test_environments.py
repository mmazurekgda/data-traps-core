from data_traps_core.trap import Trap
from data_traps_core.defaults import ENVIRONMENTS
from pydantic_core._pydantic_core import ValidationError
import pytest

trap_base = {
    "name": "my-trap-name",
    "namespace": "test-namespace",
    "experiment": "test_experiment_name",
}


def test_empty_environments():
    with pytest.raises(ValidationError):
        Trap(**trap_base, environments=[])


def test_invalid_environments():
    with pytest.raises(ValidationError):
        Trap(**trap_base, environments=["invalid-environment"])


def test_valid_environments():
    Trap(**trap_base, environments=["development"])
    Trap(**trap_base, environments=["development", "staging"])
    Trap(**trap_base, environments=ENVIRONMENTS)
