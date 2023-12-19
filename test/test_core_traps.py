from data_traps_core.traps import Trap
import tempfile
from ruamel.yaml import YAML


def test_writing_core_traps_to_yaml():
    trap = Trap(
        name="My Trap Name :)",
        namespace="test-namespace",
        experiment="test_experiment_name",
        environments=["development", "staging"],
        ignore=True,
    )
    with tempfile.NamedTemporaryFile() as f:
        trap.dump_to_yaml(f.name)
        yaml = YAML()
        f.seek(0)
        data = yaml.load(f)
        assert data == {
            "name": "my-trap-name",
            "namespace": "test-namespace",
            "experiment": "test-experiment-name",
            "environments": ["development", "staging"],
            "ignore": True,
        }
