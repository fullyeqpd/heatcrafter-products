#!/usr/bin/env python3
"""Validate every products/*.json against the schema. Exit 1 on any problem."""
import json, sys, glob, os

try:
    import jsonschema
except ImportError:
    sys.exit("pip install jsonschema first")

schema = json.load(open(os.path.join(os.path.dirname(__file__), "..", "schema", "product.schema.json")))
errors = 0
ids = set()
for f in sorted(glob.glob(os.path.join(os.path.dirname(__file__), "..", "products", "*.json"))):
    name = os.path.basename(f)
    try:
        doc = json.load(open(f))
    except json.JSONDecodeError as e:
        print(f"ERROR {name}: not valid JSON — {e}")
        errors += 1
        continue
    for e in jsonschema.Draft202012Validator(schema).iter_errors(doc):
        print(f"ERROR {name}: {'/'.join(map(str, e.path)) or '(root)'}: {e.message}")
        errors += 1
    if doc.get("id") and doc["id"] + ".json" != name:
        print(f"ERROR {name}: id '{doc['id']}' must match the filename")
        errors += 1
    if doc.get("id") in ids:
        print(f"ERROR {name}: duplicate id")
        errors += 1
    ids.add(doc.get("id"))
print(f"{len(ids)} products checked, {errors} error(s)")
sys.exit(1 if errors else 0)
