import os
from utils.loader import load_files
from validators.terraform import validate_terraform
from validators.kubernetes import validate_kubernetes
from validators.ai import ai_review

def main(path):
    files = load_files(path)

    for file in files:
        print(f"\n🔍 Checking: {file['name']}")

        if file["type"] == "terraform":
            issues = validate_terraform(file["content"])
        elif file["type"] == "kubernetes":
            issues = validate_kubernetes(file["content"])
        else:
            continue

        for issue in issues:
            print(f"❌ {issue}")

        print("\n🤖 AI Suggestions:")
        ai_output = ai_review(file["content"])
        print(ai_output)

if __name__ == "__main__":
    path = "./sample"
    main(path)
