import yaml

def validate_kubernetes(content):
    issues = []
    docs = list(yaml.safe_load_all(content))

    for doc in docs:
        if not doc:
            continue

        kind = doc.get("kind", "")
        spec = doc.get("spec", {})

        # Check for missing resource limits
        containers = spec.get("template", {}).get("spec", {}).get("containers", [])
        for c in containers:
            resources = c.get("resources", {})
            if "limits" not in resources:
                issues.append(f"{kind}: Missing resource limits")

        # Check for latest tag
        for c in containers:
            image = c.get("image", "")
            if ":latest" in image:
                issues.append(f"{kind}: Using latest tag in image {image}")

    return issues
