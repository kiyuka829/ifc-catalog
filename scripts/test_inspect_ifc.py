"""実行: uv run python -m unittest discover -s scripts"""

import tempfile
import unittest
from pathlib import Path

import ifcopenshell

from inspect_ifc import COUNT_TYPES, summarize


class SummaryTest(unittest.TestCase):
    def test_projected_crs_name(self):
        for schema in ("IFC2X3", "IFC4", "IFC4X3_ADD2"):
            with self.subTest(schema=schema), tempfile.TemporaryDirectory() as directory:
                model = ifcopenshell.file(schema=schema)
                project = model.create_entity("IfcProject", GlobalId=ifcopenshell.guid.new())
                self.assertIsNone(summarize(model)["projected_crs_name"])
                if schema == "IFC2X3":
                    prop = model.create_entity("IfcPropertySingleValue", Name="Name", NominalValue=model.create_entity("IfcLabel", "EPSG:32760"))
                    pset = model.create_entity("IfcPropertySet", GlobalId=ifcopenshell.guid.new(), Name="ePSet_ProjectedCRS", HasProperties=[prop])
                    model.create_entity("IfcRelDefinesByProperties", GlobalId=ifcopenshell.guid.new(), RelatedObjects=[project], RelatingPropertyDefinition=pset)
                else:
                    contexts = []
                    for name in ("EPSG:32760", "EPSG:6668"):
                        origin = model.create_entity("IfcCartesianPoint", Coordinates=(0.0, 0.0, 0.0))
                        placement = model.create_entity("IfcAxis2Placement3D", Location=origin)
                        context = model.create_entity("IfcGeometricRepresentationContext", CoordinateSpaceDimension=3, WorldCoordinateSystem=placement)
                        crs = model.create_entity("IfcProjectedCRS", Name=name)
                        model.create_entity("IfcMapConversion", SourceCRS=context, TargetCRS=crs, Eastings=0.0, Northings=0.0, OrthogonalHeight=0.0)
                        contexts.append(context)
                    project.RepresentationContexts = contexts
                path = Path(directory) / "crs.ifc"
                model.write(path)
                for lazy in (False, True):
                    self.assertEqual(summarize(ifcopenshell.open(path, lazy=lazy))["projected_crs_name"], "EPSG:32760")

    def test_lazy_matches_eager(self):
        for schema in ("IFC2X3", "IFC4", "IFC4X3_ADD2"):
            with self.subTest(schema=schema), tempfile.TemporaryDirectory() as directory:
                model = ifcopenshell.file(schema=schema)
                unit = model.create_entity("IfcSIUnit", UnitType="LENGTHUNIT", Prefix="MILLI", Name="METRE")
                assignment = model.create_entity("IfcUnitAssignment", Units=[unit])
                model.create_entity("IfcProject", GlobalId=ifcopenshell.guid.new(), UnitsInContext=assignment)
                model.create_entity("IfcWall", GlobalId=ifcopenshell.guid.new())
                prop = model.create_entity("IfcPropertySingleValue", Name="Test")
                model.create_entity("IfcPropertySet", GlobalId=ifcopenshell.guid.new(), HasProperties=[prop])
                quantity = model.create_entity("IfcQuantityLength", Name="Length", LengthValue=1.0)
                model.create_entity("IfcElementQuantity", GlobalId=ifcopenshell.guid.new(), Quantities=[quantity])
                path = Path(directory) / "test.ifc"
                model.write(path)
                eager = ifcopenshell.open(path)
                lazy = ifcopenshell.open(path, lazy=True)
                actual = summarize(lazy)
                self.assertTrue(lazy.lazy_loading())
                self.assertEqual(actual, summarize(eager))
                self.assertEqual(actual["instance_count"], len(list(eager)))
                for key, entity in COUNT_TYPES.items():
                    self.assertEqual(actual[key], len(eager.by_type(entity)))
                    self.assertEqual(actual[key], 1)
                self.assertEqual(actual["length_unit"], "MILLIMETRE")
                self.assertEqual(actual["length_unit_scale"], 0.001)

    def test_missing_unit_defaults_to_metre(self):
        model = ifcopenshell.file(schema="IFC4")
        model.create_entity("IfcProject", GlobalId=ifcopenshell.guid.new())
        actual = summarize(model)
        self.assertEqual(actual["length_unit"], "METRE")
        self.assertEqual(actual["length_unit_scale"], 1)

    def test_conversion_based_unit(self):
        model = ifcopenshell.file(schema="IFC4")
        metre = model.create_entity("IfcSIUnit", UnitType="LENGTHUNIT", Name="METRE")
        factor = model.create_entity("IfcMeasureWithUnit", ValueComponent=model.create_entity("IfcLengthMeasure", 0.3048), UnitComponent=metre)
        dimensions = model.create_entity("IfcDimensionalExponents", 1, 0, 0, 0, 0, 0, 0)
        foot = model.create_entity("IfcConversionBasedUnit", Dimensions=dimensions, UnitType="LENGTHUNIT", Name="foot", ConversionFactor=factor)
        assignment = model.create_entity("IfcUnitAssignment", Units=[foot])
        model.create_entity("IfcProject", GlobalId=ifcopenshell.guid.new(), UnitsInContext=assignment)
        actual = summarize(model)
        self.assertEqual(actual["length_unit"], "FOOT")
        self.assertAlmostEqual(actual["length_unit_scale"], 0.3048)


if __name__ == "__main__":
    unittest.main()
