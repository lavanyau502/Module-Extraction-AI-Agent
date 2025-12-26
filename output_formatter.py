import json


def format_output(modules):
    output = []

    for module, texts in modules.items():
        submodules = {}

        for i, text in enumerate(texts[:5]):
            submodules[f"Submodule_{i+1}"] = text[:200]

        output.append({
            "module": module,
            "Description": f"Features related to {module.lower()}",
            "Submodules": submodules
        })

    return json.dumps(output, indent=2)
