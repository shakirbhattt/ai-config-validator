import os

def load_files(path):
    files = []

    for root, _, filenames in os.walk(path):
        for f in filenames:
            full_path = os.path.join(root, f)

            if f.endswith(".tf"):
                file_type = "terraform"
            elif f.endswith(".yaml") or f.endswith(".yml"):
                file_type = "kubernetes"
            else:
                continue

            with open(full_path, "r") as file:
                content = file.read()

            files.append({
                "name": f,
                "type": file_type,
                "content": content
            })

    return files
