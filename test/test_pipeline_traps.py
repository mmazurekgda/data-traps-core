from data_traps_core.pipeline_trap import PipelineTrap
import tempfile
from ruamel.yaml import YAML


def test_writing_pipeline_traps_to_yaml():
    trap = PipelineTrap(
        name="My Pipeline Trap Name :)",
        namespace="test-namespace",
        experiment="test_experiment_name",
        environments=["development", "staging"],
    )
    with tempfile.NamedTemporaryFile() as f:
        trap.dump_to_yaml(f.name)
        yaml = YAML()
        f.seek(0)
        data = yaml.load(f)
        assert data == {
            "name": "my-pipeline-trap-name",
            "namespace": "test-namespace",
            "experiment": "test-experiment-name",
            "environments": ["development", "staging"],
            "ignore": False,
        }
