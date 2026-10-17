"""IFCの件数とプロジェクトの長さ単位をJSONで出力する。"""

import argparse
import json
from pathlib import Path

import ifcopenshell
import ifcopenshell.util.unit


COUNT_TYPES = {
    "product_count": "IfcProduct",
    "element_count": "IfcElement",
    "property_set_count": "IfcPropertySet",
    "property_count": "IfcProperty",
    "quantity_set_count": "IfcElementQuantity",
    "quantity_count": "IfcPhysicalQuantity",
}


def summarize(model):
    counts = {key: len(model.by_type(parent)) for key, parent in COUNT_TYPES.items()}
    unit = ifcopenshell.util.unit.get_project_unit(model, "LENGTHUNIT")
    return {
        "ifc_schema": model.schema_identifier,
        "instance_count": len(model.entity_names()),
        **counts,
        "length_unit": ifcopenshell.util.unit.get_full_unit_name(unit) if unit else "METRE",
        "length_unit_scale": ifcopenshell.util.unit.calculate_unit_scale(model),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="ifcファイル")
    args = parser.parse_args()
    if not args.path.is_file() or args.path.suffix.lower() != ".ifc":
        parser.error("既存の.ifcファイルを指定してください")
    model = ifcopenshell.open(args.path, lazy=True)
    result = {
        "filename": args.path.name,
        "size_bytes": args.path.stat().st_size,
        "ifcopenshell_version": ifcopenshell.version,
        **summarize(model),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
