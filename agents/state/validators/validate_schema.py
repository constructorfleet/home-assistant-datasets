import json
import jsonschema
from pathlib import Path


def main():
    base = Path(__file__).parents[1]
    schema_path = base / "v0" / "schemas" / "entity_state.v0.schema.json"
    example_path = base / "v0" / "examples" / "entity_state.example.json"
    schema = json.loads(schema_path.read_text())
    example = json.loads(example_path.read_text())
    jsonschema.validate(example, schema)


if __name__ == "__main__":
    main()
