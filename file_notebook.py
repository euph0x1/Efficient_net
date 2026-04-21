import json

with open("EfficientNet_Final.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)

# Remove broken widget metadata completely
if "metadata" in nb and "widgets" in nb["metadata"]:
    del nb["metadata"]["widgets"]

with open("EfficientNet_Final_fixed.ipynb", "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1)