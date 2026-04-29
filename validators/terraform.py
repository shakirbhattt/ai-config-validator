def validate_terraform(content):
    issues = []

    if "0.0.0.0/0" in content:
        issues.append("Security Risk: Open to the world (0.0.0.0/0)")

    if "instance_type" in content and "t2.micro" in content:
        issues.append("Possible underpowered instance (t2.micro)")

    if "public = true" in content:
        issues.append("Public resource detected")

    return issues
