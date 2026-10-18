---
type: dataset
id: buildingsmart-community
name: buildingSMART Community Sample Test Files
source_url: https://github.com/buildingsmart-community/Community-Sample-Test-Files
license: CC-BY-4.0
checked_on: '2026-10-18'
tags:
- sample
- interoperability
- building
- mep
- georeferencing
ifc_schemas:
- IFC2X3
- IFC4
- IFC4X1
- IFC4X3_RC1
- IFC4X3_RC2
---

# buildingSMART Community Sample Test Files

建築・設備・形状表現・地理参照などの実装検証向けサンプルIFC。

- 確認版: [リポジトリ](https://github.com/buildingsmart-community/Community-Sample-Test-Files/tree/7ddf57a201f88a0c213d5322b02ed15e94a60a40)
- 確認時のコミット: `7ddf57a201f88a0c213d5322b02ed15e94a60a40`
- ライセンス: [CC BY 4.0](https://github.com/buildingsmart-community/Community-Sample-Test-Files/blob/7ddf57a201f88a0c213d5322b02ed15e94a60a40/LICENSE)

## IFC・IFCZIPの取得

Git LFS導入済みの環境で、LFSの取得対象をIFC・IFCZIPに限定する。IFCZIPは通常のGit管理のため、clone時に取得される。

```sh
GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/buildingsmart-community/Community-Sample-Test-Files.git
cd Community-Sample-Test-Files
git lfs install --local
GIT_LFS_SKIP_SMUDGE=1 git checkout 7ddf57a201f88a0c213d5322b02ed15e94a60a40
git lfs pull --include="*.ifc,*.IFC,*.ifczip,*.ifcZIP" --exclude=""
```

## 配布ファイル

確認版の直接配布IFC全171ファイルとIFCZIP全27ファイルを掲載。同一SHA-256のIFCはモデルノートをまとめている（展開後も含め180件）。

### IFC 2.3.0.1 (IFC 2x3) / Duplex Apartment

| 配布ファイル | モデル |
| --- | --- |
| Duplex_A_20110907.ifc | [[models/buildingsmart-community/duplex-a-20110907]] |
| Duplex_Electrical_20121207.ifc | [[models/buildingsmart-community/duplex-electrical-20121207]] |
| Duplex_MEP_20110907.ifc | [[models/buildingsmart-community/duplex-mep-20110907]] |
| Duplex_M_20111024_ROOMS_AND_SPACES.ifc | [[models/buildingsmart-community/duplex-m-20111024-rooms-and-spaces]] |
| Duplex_Plumbing_20121113.ifc | [[models/buildingsmart-community/duplex-plumbing-20121113]] |

### IFC 2.3.0.1 (IFC 2x3) / Esplanades

| 配布ファイル | モデル |
| --- | --- |
| 1807_EP_AR_v18.ifc | [[models/buildingsmart-community/1807-ep-ar-v18]] |

### IFC 2.3.0.1 (IFC 2x3) / Medical-Dental Clinic

| 配布ファイル | モデル |
| --- | --- |
| Clinic_Architectural.ifc | [[models/buildingsmart-community/clinic-architectural]] |
| Clinic_Electrical.ifc | [[models/buildingsmart-community/clinic-electrical]] |
| Clinic_HVAC.ifc | [[models/buildingsmart-community/clinic-hvac]] |
| Clinic_Plumbing.ifc | [[models/buildingsmart-community/clinic-plumbing]] |
| Clinic_Structural.ifc | [[models/buildingsmart-community/clinic-structural]] |

### IFC 2.3.0.1 (IFC 2x3) / Molio

| 配布ファイル | モデル |
| --- | --- |
| Molio_with_URIs.ifc | [[models/buildingsmart-community/molio-with-uris]] |

### IFC 2.3.0.1 (IFC 2x3) / SDK - S1

| 配布ファイル | モデル |
| --- | --- |
| bSDD_references_example.ifc | [[models/buildingsmart-community/bsdd-references-example]] |

### IFC 2.3.0.1 (IFC 2x3) / Schependomlaan / As Planned models

| 配布ファイル | モデル |
| --- | --- |
| IFC Schependomlaan incl planningsdata.ifc | [[models/buildingsmart-community/ifc-schependomlaan-incl-planningsdata]] |
| Week 26 26 june IFC Schependomlaan incl planningsdata.ifc | [[models/buildingsmart-community/week-26-26-june-ifc-schependomlaan-incl-planningsdata]] |
| Week 27 3 july IFC Schependomlaan incl planningsdata.ifc | [[models/buildingsmart-community/week-27-3-july-ifc-schependomlaan-incl-planningsdata]] |
| Week 28 10 july IFC Schependomlaan incl planningsdata.ifc | [[models/buildingsmart-community/week-28-10-july-ifc-schependomlaan-incl-planningsdata]] |
| Week 29 17 july IFC Schependomlaan incl planningsdata.ifc | [[models/buildingsmart-community/week-29-17-july-ifc-schependomlaan-incl-planningsdata]] |
| Week 30 24 july IFC Schependomlaan incl planningsdata.ifc | [[models/buildingsmart-community/week-30-24-july-ifc-schependomlaan-incl-planningsdata]] |
| Week 37 11 sept IFC Schependomlaan incl planningsdata.ifc | [[models/buildingsmart-community/week-37-11-sept-ifc-schependomlaan-incl-planningsdata]] |

### IFC 2.3.0.1 (IFC 2x3) / Schependomlaan / Coordination model and subcontractors models / BIMsight Projectdata1

| 配布ファイル | モデル |
| --- | --- |
| BALKONHEKKEN 23-9-2015.IFC | [[models/buildingsmart-community/balkonhekken-23-9-2015]] |
| BERNTS-Staalconstructie.ifc | [[models/buildingsmart-community/bernts-staalconstructie]] |
| FEK - Balkonhekken en borstweringsleuningen.IFC | [[models/buildingsmart-community/fek-balkonhekken-en-borstweringsleuningen]] |
| FEK - Franse balkonhekken en doorvalbeveiliging.IFC | [[models/buildingsmart-community/fek-franse-balkonhekken-en-doorvalbeveiliging]] |
| FEK - Traphekken.IFC | [[models/buildingsmart-community/fek-traphekken]] |
| GEELEN-Breedplaat V1.ifc | [[models/buildingsmart-community/geelen-breedplaat-v1]] |
| GEELEN-Breedplaat V2.ifc | [[models/buildingsmart-community/geelen-breedplaat-v2]] |
| GEELEN-Breedplaat V3.ifc | [[models/buildingsmart-community/geelen-breedplaat-v3]] |
| GEELEN-Dakvloer.ifc | [[models/buildingsmart-community/geelen-dakvloer]] |
| HB_Nutsvoorzieningen.ifc | [[models/buildingsmart-community/hb-nutsvoorzieningen]] |
| JORDAHL-Gevelderagers.ifc | [[models/buildingsmart-community/jordahl-gevelderagers]] |
| MULTICOM-balkons.ifc | [[models/buildingsmart-community/multicom-balkons]] |
| MULTICOM-banden.ifc | [[models/buildingsmart-community/multicom-banden]] |
| MULTICOM-trappen+bordessen.ifc | [[models/buildingsmart-community/multicom-trappen-bordessen]] |
| V_L_Constructief.ifc | [[models/buildingsmart-community/v-l-constructief]] |
| WAARDO-Kanaalplaatvloer.ifc | [[models/buildingsmart-community/waardo-kanaalplaatvloer]] |
| WILLEMSEN-Hoogbouw dakpannen.ifc | [[models/buildingsmart-community/willemsen-hoogbouw-dakpannen]] |
| WILLEMSEN-Hoogbouw.ifc | [[models/buildingsmart-community/willemsen-hoogbouw]] |
| WILLEMSEN-Laagbouw.ifc | [[models/buildingsmart-community/willemsen-laagbouw]] |
| WILLEMSEN-laagbouw dakpannen.ifc | [[models/buildingsmart-community/willemsen-laagbouw-dakpannen]] |
| XELLA-1e verdieping.ifc | [[models/buildingsmart-community/xella-1e-verdieping]] |
| XELLA-2e verdieping.ifc | [[models/buildingsmart-community/xella-2e-verdieping]] |
| XELLA-3e verdieping.ifc | [[models/buildingsmart-community/xella-3e-verdieping]] |
| XELLA-Begane grond.ifc | [[models/buildingsmart-community/xella-begane-grond]] |
| YTONG-Algemeen.ifc | [[models/buildingsmart-community/ytong-algemeen]] |
| YTONG-Kavel 01.ifc | [[models/buildingsmart-community/ytong-kavel-01]] |
| YTONG-Kavel 02.ifc | [[models/buildingsmart-community/ytong-kavel-02]] |
| YTONG-Kavel 03.ifc | [[models/buildingsmart-community/ytong-kavel-03]] |
| YTONG-Kavel 04.ifc | [[models/buildingsmart-community/ytong-kavel-04]] |
| YTONG-Kavel 05.ifc | [[models/buildingsmart-community/ytong-kavel-05]] |
| YTONG-Kavel 06.ifc | [[models/buildingsmart-community/ytong-kavel-06]] |
| YTONG-Kavel 07.ifc | [[models/buildingsmart-community/ytong-kavel-07]] |
| YTONG-Kavel 08.ifc | [[models/buildingsmart-community/ytong-kavel-08]] |
| YTONG-Kavel 09.ifc | [[models/buildingsmart-community/ytong-kavel-09]] |
| YTONG-Kavel 10.ifc | [[models/buildingsmart-community/ytong-kavel-10]] |

### IFC 2.3.0.1 (IFC 2x3) / Schependomlaan / Coordination model and subcontractors models / BIMsight Projectdata1 / ProjectData

| 配布ファイル | モデル |
| --- | --- |
| BERNTS-Staalconstructie.ifc | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-bernts-staalconstructie]] |
| FEK-Leuningen en hekwerken.IFC | [[models/buildingsmart-community/fek-leuningen-en-hekwerken]] |
| GEELEN-Breedplaat V1.ifc | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-geelen-breedplaat-v1]] |
| GEELEN-Breedplaat V2.ifc | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-geelen-breedplaat-v2]] |
| GEELEN-Breedplaat V3.ifc | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-geelen-breedplaat-v3]] |
| GEELEN-Dakvloer.ifc | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-geelen-dakvloer]] |
| HB_Nutsvoorzieningen.ifc | [[models/buildingsmart-community/hb-nutsvoorzieningen]]（同一内容） |
| JORDAHL-Gevelderagers.ifc | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-jordahl-gevelderagers]] |
| MULTICOM-Prefab.ifc | [[models/buildingsmart-community/multicom-prefab]] |
| V_L_Constructief.ifc | [[models/buildingsmart-community/v-l-constructief]]（同一内容） |
| WAARDO-Kanaalplaatvloer.ifc | [[models/buildingsmart-community/waardo-kanaalplaatvloer]]（同一内容） |
| XELLA-1e verdieping.ifc | [[models/buildingsmart-community/xella-1e-verdieping]]（同一内容） |
| XELLA-Begane grond.ifc | [[models/buildingsmart-community/xella-begane-grond]]（同一内容） |
| YTONG-Algemeen.ifc | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-ytong-algemeen]] |
| YTONG-Kavel 01.ifc | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-ytong-kavel-01]] |
| YTONG-Kavel 02.ifc | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-ytong-kavel-02]] |
| YTONG-Kavel 03.ifc | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-ytong-kavel-03]] |
| YTONG-Kavel 04.ifc | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-ytong-kavel-04]] |
| YTONG-Kavel 05.ifc | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-ytong-kavel-05]] |
| YTONG-Kavel 06.ifc | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-ytong-kavel-06]] |
| YTONG-Kavel 07.ifc | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-ytong-kavel-07]] |
| YTONG-Kavel 08.ifc | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-ytong-kavel-08]] |
| YTONG-Kavel 09.ifc | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-ytong-kavel-09]] |
| YTONG-Kavel 10.ifc | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-ytong-kavel-10]] |

### IFC 2.3.0.1 (IFC 2x3) / Schependomlaan / Design model IFC

| 配布ファイル | モデル |
| --- | --- |
| IFC Schependomlaan.ifc | [[models/buildingsmart-community/ifc-schependomlaan]] |
| IFC_Schependomlaan_geo.ifc | [[models/buildingsmart-community/ifc-schependomlaan-geo]] |

### IFC 4.0.2.1 (IFC 4) / Example project location

| 配布ファイル | モデル |
| --- | --- |
| example project location.ifc | [[models/buildingsmart-community/example-project-location]] |

### IFC 4.0.2.1 (IFC 4) / ISO Spec archive

| 配布ファイル | モデル |
| --- | --- |
| air-terminal-element.ifc | [[models/buildingsmart-community/air-terminal-element]] |
| air-terminal-library-object.ifc | [[models/buildingsmart-community/air-terminal-library-object]] |
| basin-advanced-brep.ifc | [[models/buildingsmart-community/basin-advanced-brep]] |
| basin-faceted-brep.ifc | [[models/buildingsmart-community/basin-faceted-brep]] |
| basin-tessellation.ifc | [[models/buildingsmart-community/basin-tessellation]] |
| bath-csg-solid.ifc | [[models/buildingsmart-community/bath-csg-solid]] |
| beam-curved-i-shape-tessellated.ifc | [[models/buildingsmart-community/beam-curved-i-shape-tessellated]] |
| beam-extruded-solid.ifc | [[models/buildingsmart-community/beam-extruded-solid]] |
| beam-revolved-solid.ifc | [[models/buildingsmart-community/beam-revolved-solid]] |
| beam-standard-case.ifc | [[models/buildingsmart-community/beam-standard-case]] |
| beam-straight-i-shape-tessellated.ifc | [[models/buildingsmart-community/beam-straight-i-shape-tessellated]] |
| beam-varying-cardinal-points.ifc | [[models/buildingsmart-community/beam-varying-cardinal-points]] |
| beam-varying-extrusion-paths.ifc | [[models/buildingsmart-community/beam-varying-extrusion-paths]] |
| beam-varying-profiles.ifc | [[models/buildingsmart-community/beam-varying-profiles]] |
| brep-model.ifc | [[models/buildingsmart-community/brep-model]] |
| column-extruded-solid.ifc | [[models/buildingsmart-community/column-extruded-solid]] |
| column-straight-rectangle-tessellation.ifc | [[models/buildingsmart-community/column-straight-rectangle-tessellation]] |
| construction-scheduling-task.ifc | [[models/buildingsmart-community/construction-scheduling-task]] |
| csg-primitive.ifc | [[models/buildingsmart-community/csg-primitive]] |
| cube-advanced-brep.ifc | [[models/buildingsmart-community/cube-advanced-brep]] |
| extruded-solid.ifc | [[models/buildingsmart-community/extruded-solid]] |
| geographic-referencing.ifc | [[models/buildingsmart-community/geographic-referencing]] |
| grid-placement.ifc | [[models/buildingsmart-community/grid-placement]] |
| mapped-shape-with-multiple-items.ifc | [[models/buildingsmart-community/mapped-shape-with-multiple-items]] |
| mapped-shape-with-transformation.ifc | [[models/buildingsmart-community/mapped-shape-with-transformation]] |
| mapped-shape-without-transformation.ifc | [[models/buildingsmart-community/mapped-shape-without-transformation]] |
| reinforcing-assembly.ifc | [[models/buildingsmart-community/reinforcing-assembly]] |
| reinforcing-stirrup.ifc | [[models/buildingsmart-community/reinforcing-stirrup]] |
| slab-openings.ifc | [[models/buildingsmart-community/slab-openings]] |
| slab-standard-case.ifc | [[models/buildingsmart-community/slab-standard-case]] |
| slab-tessellated-unique-vertices.ifc | [[models/buildingsmart-community/slab-tessellated-unique-vertices]] |
| structural-curve-member.ifc | [[models/buildingsmart-community/structural-curve-member]] |
| surface-model.ifc | [[models/buildingsmart-community/surface-model]] |
| tessellated-item.ifc | [[models/buildingsmart-community/tessellated-item]] |
| tessellation-with-blob-texture.ifc | [[models/buildingsmart-community/tessellation-with-blob-texture]] |
| tessellation-with-image-texture.ifc | [[models/buildingsmart-community/tessellation-with-image-texture]] |
| tessellation-with-individual-colors.ifc | [[models/buildingsmart-community/tessellation-with-individual-colors]] |
| tessellation-with-pixel-texture.ifc | [[models/buildingsmart-community/tessellation-with-pixel-texture]] |
| wall-elemented-case.ifc | [[models/buildingsmart-community/wall-elemented-case]] |
| wall-standard-case.ifc | [[models/buildingsmart-community/wall-standard-case]] |
| wall-with-opening-and-window.ifc | [[models/buildingsmart-community/wall-with-opening-and-window]] |

### IFC 4.0.2.1 (IFC 4) / NURBS / Bentley Building Designer / Cylinder

| 配布ファイル | モデル |
| --- | --- |
| BsplineSurf.PolyCurve.ifc | [[models/buildingsmart-community/bsplinesurf-polycurve]] |
| Facet.ifc | [[models/buildingsmart-community/facet]] |
| OnlyBsplines.ifc | [[models/buildingsmart-community/onlybsplines]] |
| Plane.Cyllinder.Ellipse.PolyCurve.ifc | [[models/buildingsmart-community/plane-cyllinder-ellipse-polycurve]] |
| Plane.Cyllinder.PolyCurve.ifc | [[models/buildingsmart-community/plane-cyllinder-polycurve]] |

### IFC 4.0.2.1 (IFC 4) / NURBS / Bentley Building Designer / Faces

| 配布ファイル | モデル |
| --- | --- |
| 1.SimpleRectangle.facet.ifc | [[models/buildingsmart-community/1-simplerectangle-facet]] |
| 1.SimpleRectangle.ifc | [[models/buildingsmart-community/1-simplerectangle]] |
| 3.Torus.facet.ifc | [[models/buildingsmart-community/3-torus-facet]] |
| 3.Torus.ifc | [[models/buildingsmart-community/3-torus]] |
| 4.Jar.facet.ifc | [[models/buildingsmart-community/4-jar-facet]] |
| 4.Jar.ifc | [[models/buildingsmart-community/4-jar]] |
| 5.Cone.facet.ifc | [[models/buildingsmart-community/5-cone-facet]] |
| 5.Cone.ifc | [[models/buildingsmart-community/5-cone]] |
| 6.RectWithHole.facet.ifc | [[models/buildingsmart-community/6-rectwithhole-facet]] |
| 6.RectWithHole.ifc | [[models/buildingsmart-community/6-rectwithhole]] |
| bspline surface.facet.ifc | [[models/buildingsmart-community/bspline-surface-facet]] |
| bspline surface.ifc | [[models/buildingsmart-community/bspline-surface]] |

### IFC 4.0.2.1 (IFC 4) / NURBS / Bentley Building Designer / SolidsAndSheets

| 配布ファイル | モデル |
| --- | --- |
| BsplinePathExtrusion.facet.ifc | [[models/buildingsmart-community/bsplinepathextrusion-facet]] |
| BsplinePathExtrusion.ifc | [[models/buildingsmart-community/bsplinepathextrusion]] |
| BsplineProfileInCSG.facet.ifc | [[models/buildingsmart-community/bsplineprofileincsg-facet]] |
| BsplineProfileInCSG.ifc | [[models/buildingsmart-community/bsplineprofileincsg]] |
| WithArcBoundary.facet.ifc | [[models/buildingsmart-community/witharcboundary-facet]] |
| WithArcBoundary.ifc | [[models/buildingsmart-community/witharcboundary]] |
| WithPlaneSurface.facet.ifc | [[models/buildingsmart-community/withplanesurface-facet]] |
| WithPlaneSurface.ifc | [[models/buildingsmart-community/withplanesurface]] |
| jarSplit.facet.ifc | [[models/buildingsmart-community/jarsplit-facet]] |
| jarSplit.ifc | [[models/buildingsmart-community/jarsplit]] |

### dev archive / IFC 4.3.RC Archive / Georeferencing-1 (RC2)

| 配布ファイル | モデル |
| --- | --- |
| UT_GeoRef_1.ifc | [[models/buildingsmart-community/ut-georef-1]] |

### dev archive / IFC 4.3.RC Archive / Georeferencing_Tin_1 (RC1)

| 配布ファイル | モデル |
| --- | --- |
| UT_Tin_in_MGA_56.ifc | [[models/buildingsmart-community/ut-tin-in-mga-56]] |

### dev archive / IFC 4.3.RC Archive / Georeferencing_Tin_2 (RC1)

| 配布ファイル | モデル |
| --- | --- |
| UT_Tin_ifcMapConversion_to_place_in_MGA_56.ifc | [[models/buildingsmart-community/ut-tin-ifcmapconversion-to-place-in-mga-56]] |

### dev archive / IFC 4.3.RC Archive / Georeferencing_Tin_3 (RC1)

| 配布ファイル | モデル |
| --- | --- |
| UT_Tin_with_one_hole_in_MGA_56.ifc | [[models/buildingsmart-community/ut-tin-with-one-hole-in-mga-56]] |

### dev archive / IFC 4.3.RC Archive / Georeferencing_Tin_4 (RC1)

| 配布ファイル | モデル |
| --- | --- |
| UT_Tin_with_two colours_in_MGA2020_56.ifc | [[models/buildingsmart-community/ut-tin-with-two-colours-in-mga2020-56]] |

### dev archive / IFC 4.3.RC Archive / Georeferencing_Tin_5 (RC1)

| 配布ファイル | モデル |
| --- | --- |
| UT_Tin_ifcMapConversion_to_place_in_MGA_56_Standard_origin.ifc | [[models/buildingsmart-community/ut-tin-ifcmapconversion-to-place-in-mga-56-standard-origin]] |

### dev archive / IFC 4.3.RC Archive / Georeferencing_Tiny_Survey_1 (RC1)

| 配布ファイル | モデル |
| --- | --- |
| UT_one_string_one_pont.ifc | [[models/buildingsmart-community/ut-one-string-one-pont]] |

### dev archive / IFC 4.3.RC Archive / LinearPlacement_1 (RC2)

| 配布ファイル | モデル |
| --- | --- |
| UT_LinearPlacement_1.ifc | [[models/buildingsmart-community/ut-linearplacement-1]] |

### dev archive / IFC 4.3.RC Archive / LinearPlacement_2 (RC2)

| 配布ファイル | モデル |
| --- | --- |
| LinearPlacement_2.ifc | [[models/buildingsmart-community/linearplacement-2]] |
| LinearPlacement_2_4X1.ifc | [[models/buildingsmart-community/linearplacement-2-4x1]] |

### dev archive / IFC 4.3.RC Archive / ProjectSetup_1 (RC1)

| 配布ファイル | モデル |
| --- | --- |
| UT_ProjectSetup_1.ifc | [[models/buildingsmart-community/ut-projectsetup-1]] |

### dev archive / IFC 4.3.RC Archive / ProjectSetup_2 (RC1)

| 配布ファイル | モデル |
| --- | --- |
| UT_ProjectSetup_2.ifc | [[models/buildingsmart-community/ut-projectsetup-2]] |

### dev archive / IFC 4.3.RC Archive / SpatialDecomposition_1 (RC2)

| 配布ファイル | モデル |
| --- | --- |
| UT_SpatialDecomposition_1.ifc | [[models/buildingsmart-community/ut-spatialdecomposition-1]] |

### dev archive / IFC 4.3.RC Archive / SpatialStructure_2 (RC2)

| 配布ファイル | モデル |
| --- | --- |
| SpatialStructure_2.ifc | [[models/buildingsmart-community/spatialstructure-2]] |

### dev archive / IFC 4.3.RC Archive / SpatialStructure_3 (RC2)

| 配布ファイル | モデル |
| --- | --- |
| SpatialStructure_3.ifc | [[models/buildingsmart-community/spatialstructure-3]] |

### dev archive / IFC 4.3.RC Archive / Tin_1 (RC1)

| 配布ファイル | モデル |
| --- | --- |
| UT_Tin_1.ifc | [[models/buildingsmart-community/ut-tin-1]] |

### dev archive / IFC 4.3.RC Archive / Tin_2 (RC1)

| 配布ファイル | モデル |
| --- | --- |
| UT_Tin_2.ifc | [[models/buildingsmart-community/ut-tin-2]] |

### dev archive / IFC 4.3.RC Archive / Tin_3 (RC1)

| 配布ファイル | モデル |
| --- | --- |
| UT_Tin_3.ifc | [[models/buildingsmart-community/ut-tin-3]] |

### dev archive / IFC 4.3.RC Archive / Tin_4 (RC1)

| 配布ファイル | モデル |
| --- | --- |
| UT_Tin_4.ifc | [[models/buildingsmart-community/ut-tin-4]] |

### dev archive / IFC 4.3.RC Archive / UT_Alignment_12d_11  (RC2)

| 配布ファイル | モデル |
| --- | --- |
| UT_Alignment_12d_11.ifc | [[models/buildingsmart-community/ut-alignment-12d-11]] |

### dev archive / IFC 4.3.RC Archive / UT_SpatialStructure_4 (RC4)

| 配布ファイル | モデル |
| --- | --- |
| UT_SpatialStructure_4.ifc | [[models/buildingsmart-community/ut-spatialstructure-4]] |

## IFCZIP配布ファイル

### IFC 2.3.0.1 (IFC 2x3) / Schependomlaan / Coordination model and subcontractors models / BIMsight Projectdata1

| 配布ファイル | 圧縮ファイルサイズ（bytes） | ZIP内のIFC | モデル |
| --- | --- | --- | --- |
| LINDEN - Kozijnen.ifcZIP | 460876 | `002.ifc` | [[models/buildingsmart-community/002]] |
| ROOT-Compleet.ifczip | 8873221 | `IFC-gebouw.ifc` | [[models/buildingsmart-community/ifc-gebouw]] |
| ROOT-Vebo.ifczip | 232375 | `IFC-Vebo.ifc` | [[models/buildingsmart-community/ifc-vebo]] |
| ROOT-breedplaatvloeren.ifczip | 116132 | `IFC-breedplaatvloeren.ifc` | [[models/buildingsmart-community/ifc-breedplaatvloeren]] |
| ROOT-houten kozijnen.ifczip | 1898930 | `IFC-houten kozijnen.ifc` | [[models/buildingsmart-community/ifc-houten-kozijnen]] |
| ROOT-kalkzandsteen.ifczip | 262213 | `IFC-kalkzandsteen.ifc` | [[models/buildingsmart-community/ifc-kalkzandsteen]] |
| ROOT-kanaalplaatvloer.ifczip | 76281 | `IFC-kanaalplaatvloer.ifc` | [[models/buildingsmart-community/ifc-kanaalplaatvloer]] |
| ROOT-kapconstructie_dakkapellen_platdak.ifczip | 348082 | `IFC-kapconstructie_dakkapellen_platdak.ifc` | [[models/buildingsmart-community/ifc-kapconstructie-dakkapellen-platdak]] |
| ROOT-lateien_en_geveldragers.ifczip | 85708 | `IFC-lateien_en_geveldragers.ifc` | [[models/buildingsmart-community/ifc-lateien-en-geveldragers]] |
| ROOT-prefab_balkons.ifczip | 12864 | `IFC-prefab_balkons.ifc` | [[models/buildingsmart-community/ifc-prefab-balkons]] |
| ROOT-prefab_trappen.ifczip | 39017 | `IFC-prefab_trappen.ifc` | [[models/buildingsmart-community/ifc-prefab-trappen]] |
| ROOT-prefab_vloer_lifttop.ifczip | 7961 | `IFC-prefab_vloer_lifttop.ifc` | [[models/buildingsmart-community/ifc-prefab-vloer-lifttop]] |
| ROOT-staal.ifczip | 170769 | `IFC-staal.ifc` | [[models/buildingsmart-community/ifc-staal]] |
| ROOT-traphekken.ifczip | 65394 | `IFC-traphekken.ifc` | [[models/buildingsmart-community/ifc-traphekken]] |

### IFC 2.3.0.1 (IFC 2x3) / Schependomlaan / Coordination model and subcontractors models / BIMsight Projectdata1 / ProjectData

| 配布ファイル | 圧縮ファイルサイズ（bytes） | ZIP内のIFC | モデル |
| --- | --- | --- | --- |
| ROOT-Compleet.ifczip | 8873221 | `IFC-gebouw.ifc` | [[models/buildingsmart-community/ifc-gebouw]]（同一内容） |
| ROOT-Vebo.ifczip | 232375 | `IFC-Vebo.ifc` | [[models/buildingsmart-community/ifc-vebo]]（同一内容） |
| ROOT-breedplaatvloeren.ifczip | 116132 | `IFC-breedplaatvloeren.ifc` | [[models/buildingsmart-community/ifc-breedplaatvloeren]]（同一内容） |
| ROOT-houten kozijnen.ifczip | 1898930 | `IFC-houten kozijnen.ifc` | [[models/buildingsmart-community/ifc-houten-kozijnen]]（同一内容） |
| ROOT-kalkzandsteen.ifczip | 262213 | `IFC-kalkzandsteen.ifc` | [[models/buildingsmart-community/ifc-kalkzandsteen]]（同一内容） |
| ROOT-kanaalplaatvloer.ifczip | 76281 | `IFC-kanaalplaatvloer.ifc` | [[models/buildingsmart-community/ifc-kanaalplaatvloer]]（同一内容） |
| ROOT-kapconstructie_dakkapellen_platdak.ifczip | 348082 | `IFC-kapconstructie_dakkapellen_platdak.ifc` | [[models/buildingsmart-community/ifc-kapconstructie-dakkapellen-platdak]]（同一内容） |
| ROOT-lateien_en_geveldragers.ifczip | 85708 | `IFC-lateien_en_geveldragers.ifc` | [[models/buildingsmart-community/ifc-lateien-en-geveldragers]]（同一内容） |
| ROOT-prefab_balkons.ifczip | 12864 | `IFC-prefab_balkons.ifc` | [[models/buildingsmart-community/ifc-prefab-balkons]]（同一内容） |
| ROOT-prefab_trappen.ifczip | 39017 | `IFC-prefab_trappen.ifc` | [[models/buildingsmart-community/ifc-prefab-trappen]]（同一内容） |
| ROOT-prefab_vloer_lifttop.ifczip | 7961 | `IFC-prefab_vloer_lifttop.ifc` | [[models/buildingsmart-community/ifc-prefab-vloer-lifttop]]（同一内容） |
| ROOT-staal.ifczip | 170769 | `IFC-staal.ifc` | [[models/buildingsmart-community/ifc-staal]]（同一内容） |
| ROOT-traphekken.ifczip | 65394 | `IFC-traphekken.ifc` | [[models/buildingsmart-community/ifc-traphekken]]（同一内容） |

## メモ

- 旧 `buildingSMART/Sample-Test-Files` のコミュニティ収録分の移管先。移管の説明は [Certification datasetsのREADME](https://github.com/buildingSMART/Certification-datasets#readme) を参照。
