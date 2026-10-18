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

## IFCの取得

Git LFS導入済みの環境で、確認版のIFC本体のみを取得する。

```sh
GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/buildingsmart-community/Community-Sample-Test-Files.git
cd Community-Sample-Test-Files
git lfs install --local
GIT_LFS_SKIP_SMUDGE=1 git checkout 7ddf57a201f88a0c213d5322b02ed15e94a60a40
git lfs pull --include="*.ifc,*.IFC" --exclude=""
```

## 配布ファイル

確認版の直接配布IFC全171ファイルを掲載。同一SHA-256のIFCはモデルノートをまとめている（166件）。

### IFC 2.3.0.1 (IFC 2x3) / Duplex Apartment

| 配布ファイル | モデル |
| --- | --- |
| [Duplex_A_20110907.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Duplex%20Apartment/Duplex_A_20110907.ifc) | [[models/buildingsmart-community/duplex-a-20110907]] |
| [Duplex_Electrical_20121207.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Duplex%20Apartment/Duplex_Electrical_20121207.ifc) | [[models/buildingsmart-community/duplex-electrical-20121207]] |
| [Duplex_MEP_20110907.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Duplex%20Apartment/Duplex_MEP_20110907.ifc) | [[models/buildingsmart-community/duplex-mep-20110907]] |
| [Duplex_M_20111024_ROOMS_AND_SPACES.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Duplex%20Apartment/Duplex_M_20111024_ROOMS_AND_SPACES.ifc) | [[models/buildingsmart-community/duplex-m-20111024-rooms-and-spaces]] |
| [Duplex_Plumbing_20121113.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Duplex%20Apartment/Duplex_Plumbing_20121113.ifc) | [[models/buildingsmart-community/duplex-plumbing-20121113]] |

### IFC 2.3.0.1 (IFC 2x3) / Esplanades

| 配布ファイル | モデル |
| --- | --- |
| [1807_EP_AR_v18.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Esplanades/1807_EP_AR_v18.ifc) | [[models/buildingsmart-community/1807-ep-ar-v18]] |

### IFC 2.3.0.1 (IFC 2x3) / Medical-Dental Clinic

| 配布ファイル | モデル |
| --- | --- |
| [Clinic_Architectural.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Medical-Dental%20Clinic/Clinic_Architectural.ifc) | [[models/buildingsmart-community/clinic-architectural]] |
| [Clinic_Electrical.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Medical-Dental%20Clinic/Clinic_Electrical.ifc) | [[models/buildingsmart-community/clinic-electrical]] |
| [Clinic_HVAC.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Medical-Dental%20Clinic/Clinic_HVAC.ifc) | [[models/buildingsmart-community/clinic-hvac]] |
| [Clinic_Plumbing.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Medical-Dental%20Clinic/Clinic_Plumbing.ifc) | [[models/buildingsmart-community/clinic-plumbing]] |
| [Clinic_Structural.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Medical-Dental%20Clinic/Clinic_Structural.ifc) | [[models/buildingsmart-community/clinic-structural]] |

### IFC 2.3.0.1 (IFC 2x3) / Molio

| 配布ファイル | モデル |
| --- | --- |
| [Molio_with_URIs.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Molio/Molio_with_URIs.ifc) | [[models/buildingsmart-community/molio-with-uris]] |

### IFC 2.3.0.1 (IFC 2x3) / SDK - S1

| 配布ファイル | モデル |
| --- | --- |
| [bSDD_references_example.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/SDK%20-%20S1/bSDD_references_example.ifc) | [[models/buildingsmart-community/bsdd-references-example]] |

### IFC 2.3.0.1 (IFC 2x3) / Schependomlaan / As Planned models

| 配布ファイル | モデル |
| --- | --- |
| [IFC Schependomlaan incl planningsdata.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/As%20Planned%20models/IFC%20Schependomlaan%20incl%20planningsdata.ifc) | [[models/buildingsmart-community/ifc-schependomlaan-incl-planningsdata]] |
| [Week 26 26 june IFC Schependomlaan incl planningsdata.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/As%20Planned%20models/Week%2026%2026%20june%20IFC%20Schependomlaan%20incl%20planningsdata.ifc) | [[models/buildingsmart-community/week-26-26-june-ifc-schependomlaan-incl-planningsdata]] |
| [Week 27 3 july IFC Schependomlaan incl planningsdata.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/As%20Planned%20models/Week%2027%203%20july%20IFC%20Schependomlaan%20incl%20planningsdata.ifc) | [[models/buildingsmart-community/week-27-3-july-ifc-schependomlaan-incl-planningsdata]] |
| [Week 28 10 july IFC Schependomlaan incl planningsdata.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/As%20Planned%20models/Week%2028%2010%20july%20IFC%20Schependomlaan%20incl%20planningsdata.ifc) | [[models/buildingsmart-community/week-28-10-july-ifc-schependomlaan-incl-planningsdata]] |
| [Week 29 17 july IFC Schependomlaan incl planningsdata.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/As%20Planned%20models/Week%2029%2017%20july%20IFC%20Schependomlaan%20incl%20planningsdata.ifc) | [[models/buildingsmart-community/week-29-17-july-ifc-schependomlaan-incl-planningsdata]] |
| [Week 30 24 july IFC Schependomlaan incl planningsdata.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/As%20Planned%20models/Week%2030%2024%20july%20IFC%20Schependomlaan%20incl%20planningsdata.ifc) | [[models/buildingsmart-community/week-30-24-july-ifc-schependomlaan-incl-planningsdata]] |
| [Week 37 11 sept IFC Schependomlaan incl planningsdata.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/As%20Planned%20models/Week%2037%2011%20sept%20IFC%20Schependomlaan%20incl%20planningsdata.ifc) | [[models/buildingsmart-community/week-37-11-sept-ifc-schependomlaan-incl-planningsdata]] |

### IFC 2.3.0.1 (IFC 2x3) / Schependomlaan / Coordination model and subcontractors models / BIMsight Projectdata1

| 配布ファイル | モデル |
| --- | --- |
| [BALKONHEKKEN 23-9-2015.IFC](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/BALKONHEKKEN%2023-9-2015.IFC) | [[models/buildingsmart-community/balkonhekken-23-9-2015]] |
| [BERNTS-Staalconstructie.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/BERNTS-Staalconstructie.ifc) | [[models/buildingsmart-community/bernts-staalconstructie]] |
| [FEK - Balkonhekken en borstweringsleuningen.IFC](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/FEK%20-%20Balkonhekken%20en%20borstweringsleuningen.IFC) | [[models/buildingsmart-community/fek-balkonhekken-en-borstweringsleuningen]] |
| [FEK - Franse balkonhekken en doorvalbeveiliging.IFC](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/FEK%20-%20Franse%20balkonhekken%20en%20doorvalbeveiliging.IFC) | [[models/buildingsmart-community/fek-franse-balkonhekken-en-doorvalbeveiliging]] |
| [FEK - Traphekken.IFC](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/FEK%20-%20Traphekken.IFC) | [[models/buildingsmart-community/fek-traphekken]] |
| [GEELEN-Breedplaat V1.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/GEELEN-Breedplaat%20V1.ifc) | [[models/buildingsmart-community/geelen-breedplaat-v1]] |
| [GEELEN-Breedplaat V2.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/GEELEN-Breedplaat%20V2.ifc) | [[models/buildingsmart-community/geelen-breedplaat-v2]] |
| [GEELEN-Breedplaat V3.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/GEELEN-Breedplaat%20V3.ifc) | [[models/buildingsmart-community/geelen-breedplaat-v3]] |
| [GEELEN-Dakvloer.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/GEELEN-Dakvloer.ifc) | [[models/buildingsmart-community/geelen-dakvloer]] |
| [HB_Nutsvoorzieningen.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/HB_Nutsvoorzieningen.ifc) | [[models/buildingsmart-community/hb-nutsvoorzieningen]] |
| [JORDAHL-Gevelderagers.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/JORDAHL-Gevelderagers.ifc) | [[models/buildingsmart-community/jordahl-gevelderagers]] |
| [MULTICOM-balkons.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/MULTICOM-balkons.ifc) | [[models/buildingsmart-community/multicom-balkons]] |
| [MULTICOM-banden.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/MULTICOM-banden.ifc) | [[models/buildingsmart-community/multicom-banden]] |
| [MULTICOM-trappen+bordessen.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/MULTICOM-trappen%2Bbordessen.ifc) | [[models/buildingsmart-community/multicom-trappen-bordessen]] |
| [V_L_Constructief.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/V_L_Constructief.ifc) | [[models/buildingsmart-community/v-l-constructief]] |
| [WAARDO-Kanaalplaatvloer.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/WAARDO-Kanaalplaatvloer.ifc) | [[models/buildingsmart-community/waardo-kanaalplaatvloer]] |
| [WILLEMSEN-Hoogbouw dakpannen.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/WILLEMSEN-Hoogbouw%20dakpannen.ifc) | [[models/buildingsmart-community/willemsen-hoogbouw-dakpannen]] |
| [WILLEMSEN-Hoogbouw.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/WILLEMSEN-Hoogbouw.ifc) | [[models/buildingsmart-community/willemsen-hoogbouw]] |
| [WILLEMSEN-Laagbouw.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/WILLEMSEN-Laagbouw.ifc) | [[models/buildingsmart-community/willemsen-laagbouw]] |
| [WILLEMSEN-laagbouw dakpannen.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/WILLEMSEN-laagbouw%20dakpannen.ifc) | [[models/buildingsmart-community/willemsen-laagbouw-dakpannen]] |
| [XELLA-1e verdieping.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/XELLA-1e%20verdieping.ifc) | [[models/buildingsmart-community/xella-1e-verdieping]] |
| [XELLA-2e verdieping.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/XELLA-2e%20verdieping.ifc) | [[models/buildingsmart-community/xella-2e-verdieping]] |
| [XELLA-3e verdieping.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/XELLA-3e%20verdieping.ifc) | [[models/buildingsmart-community/xella-3e-verdieping]] |
| [XELLA-Begane grond.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/XELLA-Begane%20grond.ifc) | [[models/buildingsmart-community/xella-begane-grond]] |
| [YTONG-Algemeen.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/YTONG-Algemeen.ifc) | [[models/buildingsmart-community/ytong-algemeen]] |
| [YTONG-Kavel 01.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/YTONG-Kavel%2001.ifc) | [[models/buildingsmart-community/ytong-kavel-01]] |
| [YTONG-Kavel 02.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/YTONG-Kavel%2002.ifc) | [[models/buildingsmart-community/ytong-kavel-02]] |
| [YTONG-Kavel 03.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/YTONG-Kavel%2003.ifc) | [[models/buildingsmart-community/ytong-kavel-03]] |
| [YTONG-Kavel 04.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/YTONG-Kavel%2004.ifc) | [[models/buildingsmart-community/ytong-kavel-04]] |
| [YTONG-Kavel 05.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/YTONG-Kavel%2005.ifc) | [[models/buildingsmart-community/ytong-kavel-05]] |
| [YTONG-Kavel 06.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/YTONG-Kavel%2006.ifc) | [[models/buildingsmart-community/ytong-kavel-06]] |
| [YTONG-Kavel 07.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/YTONG-Kavel%2007.ifc) | [[models/buildingsmart-community/ytong-kavel-07]] |
| [YTONG-Kavel 08.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/YTONG-Kavel%2008.ifc) | [[models/buildingsmart-community/ytong-kavel-08]] |
| [YTONG-Kavel 09.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/YTONG-Kavel%2009.ifc) | [[models/buildingsmart-community/ytong-kavel-09]] |
| [YTONG-Kavel 10.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/YTONG-Kavel%2010.ifc) | [[models/buildingsmart-community/ytong-kavel-10]] |

### IFC 2.3.0.1 (IFC 2x3) / Schependomlaan / Coordination model and subcontractors models / BIMsight Projectdata1 / ProjectData

| 配布ファイル | モデル |
| --- | --- |
| [BERNTS-Staalconstructie.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/ProjectData/BERNTS-Staalconstructie.ifc) | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-bernts-staalconstructie]] |
| [FEK-Leuningen en hekwerken.IFC](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/ProjectData/FEK-Leuningen%20en%20hekwerken.IFC) | [[models/buildingsmart-community/fek-leuningen-en-hekwerken]] |
| [GEELEN-Breedplaat V1.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/ProjectData/GEELEN-Breedplaat%20V1.ifc) | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-geelen-breedplaat-v1]] |
| [GEELEN-Breedplaat V2.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/ProjectData/GEELEN-Breedplaat%20V2.ifc) | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-geelen-breedplaat-v2]] |
| [GEELEN-Breedplaat V3.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/ProjectData/GEELEN-Breedplaat%20V3.ifc) | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-geelen-breedplaat-v3]] |
| [GEELEN-Dakvloer.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/ProjectData/GEELEN-Dakvloer.ifc) | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-geelen-dakvloer]] |
| [HB_Nutsvoorzieningen.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/ProjectData/HB_Nutsvoorzieningen.ifc) | [[models/buildingsmart-community/hb-nutsvoorzieningen]]（同一内容） |
| [JORDAHL-Gevelderagers.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/ProjectData/JORDAHL-Gevelderagers.ifc) | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-jordahl-gevelderagers]] |
| [MULTICOM-Prefab.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/ProjectData/MULTICOM-Prefab.ifc) | [[models/buildingsmart-community/multicom-prefab]] |
| [V_L_Constructief.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/ProjectData/V_L_Constructief.ifc) | [[models/buildingsmart-community/v-l-constructief]]（同一内容） |
| [WAARDO-Kanaalplaatvloer.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/ProjectData/WAARDO-Kanaalplaatvloer.ifc) | [[models/buildingsmart-community/waardo-kanaalplaatvloer]]（同一内容） |
| [XELLA-1e verdieping.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/ProjectData/XELLA-1e%20verdieping.ifc) | [[models/buildingsmart-community/xella-1e-verdieping]]（同一内容） |
| [XELLA-Begane grond.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/ProjectData/XELLA-Begane%20grond.ifc) | [[models/buildingsmart-community/xella-begane-grond]]（同一内容） |
| [YTONG-Algemeen.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/ProjectData/YTONG-Algemeen.ifc) | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-ytong-algemeen]] |
| [YTONG-Kavel 01.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/ProjectData/YTONG-Kavel%2001.ifc) | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-ytong-kavel-01]] |
| [YTONG-Kavel 02.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/ProjectData/YTONG-Kavel%2002.ifc) | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-ytong-kavel-02]] |
| [YTONG-Kavel 03.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/ProjectData/YTONG-Kavel%2003.ifc) | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-ytong-kavel-03]] |
| [YTONG-Kavel 04.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/ProjectData/YTONG-Kavel%2004.ifc) | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-ytong-kavel-04]] |
| [YTONG-Kavel 05.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/ProjectData/YTONG-Kavel%2005.ifc) | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-ytong-kavel-05]] |
| [YTONG-Kavel 06.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/ProjectData/YTONG-Kavel%2006.ifc) | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-ytong-kavel-06]] |
| [YTONG-Kavel 07.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/ProjectData/YTONG-Kavel%2007.ifc) | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-ytong-kavel-07]] |
| [YTONG-Kavel 08.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/ProjectData/YTONG-Kavel%2008.ifc) | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-ytong-kavel-08]] |
| [YTONG-Kavel 09.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/ProjectData/YTONG-Kavel%2009.ifc) | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-ytong-kavel-09]] |
| [YTONG-Kavel 10.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Coordination%20model%20and%20subcontractors%20models/BIMsight%20Projectdata1/ProjectData/YTONG-Kavel%2010.ifc) | [[models/buildingsmart-community/ifc-2-3-0-1-ifc-2x3-schependomlaan-coordination-model-and-subcontractors-models-bimsight-projectdata1-projectdata-ytong-kavel-10]] |

### IFC 2.3.0.1 (IFC 2x3) / Schependomlaan / Design model IFC

| 配布ファイル | モデル |
| --- | --- |
| [IFC Schependomlaan.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Design%20model%20IFC/IFC%20Schependomlaan.ifc) | [[models/buildingsmart-community/ifc-schependomlaan]] |
| [IFC_Schependomlaan_geo.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%202.3.0.1%20%28IFC%202x3%29/Schependomlaan/Design%20model%20IFC/IFC_Schependomlaan_geo.ifc) | [[models/buildingsmart-community/ifc-schependomlaan-geo]] |

### IFC 4.0.2.1 (IFC 4) / Example project location

| 配布ファイル | モデル |
| --- | --- |
| [example project location.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/Example%20project%20location/example%20project%20location.ifc) | [[models/buildingsmart-community/example-project-location]] |

### IFC 4.0.2.1 (IFC 4) / ISO Spec archive

| 配布ファイル | モデル |
| --- | --- |
| [air-terminal-element.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/air-terminal-element.ifc) | [[models/buildingsmart-community/air-terminal-element]] |
| [air-terminal-library-object.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/air-terminal-library-object.ifc) | [[models/buildingsmart-community/air-terminal-library-object]] |
| [basin-advanced-brep.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/basin-advanced-brep.ifc) | [[models/buildingsmart-community/basin-advanced-brep]] |
| [basin-faceted-brep.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/basin-faceted-brep.ifc) | [[models/buildingsmart-community/basin-faceted-brep]] |
| [basin-tessellation.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/basin-tessellation.ifc) | [[models/buildingsmart-community/basin-tessellation]] |
| [bath-csg-solid.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/bath-csg-solid.ifc) | [[models/buildingsmart-community/bath-csg-solid]] |
| [beam-curved-i-shape-tessellated.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/beam-curved-i-shape-tessellated.ifc) | [[models/buildingsmart-community/beam-curved-i-shape-tessellated]] |
| [beam-extruded-solid.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/beam-extruded-solid.ifc) | [[models/buildingsmart-community/beam-extruded-solid]] |
| [beam-revolved-solid.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/beam-revolved-solid.ifc) | [[models/buildingsmart-community/beam-revolved-solid]] |
| [beam-standard-case.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/beam-standard-case.ifc) | [[models/buildingsmart-community/beam-standard-case]] |
| [beam-straight-i-shape-tessellated.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/beam-straight-i-shape-tessellated.ifc) | [[models/buildingsmart-community/beam-straight-i-shape-tessellated]] |
| [beam-varying-cardinal-points.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/beam-varying-cardinal-points.ifc) | [[models/buildingsmart-community/beam-varying-cardinal-points]] |
| [beam-varying-extrusion-paths.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/beam-varying-extrusion-paths.ifc) | [[models/buildingsmart-community/beam-varying-extrusion-paths]] |
| [beam-varying-profiles.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/beam-varying-profiles.ifc) | [[models/buildingsmart-community/beam-varying-profiles]] |
| [brep-model.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/brep-model.ifc) | [[models/buildingsmart-community/brep-model]] |
| [column-extruded-solid.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/column-extruded-solid.ifc) | [[models/buildingsmart-community/column-extruded-solid]] |
| [column-straight-rectangle-tessellation.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/column-straight-rectangle-tessellation.ifc) | [[models/buildingsmart-community/column-straight-rectangle-tessellation]] |
| [construction-scheduling-task.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/construction-scheduling-task.ifc) | [[models/buildingsmart-community/construction-scheduling-task]] |
| [csg-primitive.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/csg-primitive.ifc) | [[models/buildingsmart-community/csg-primitive]] |
| [cube-advanced-brep.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/cube-advanced-brep.ifc) | [[models/buildingsmart-community/cube-advanced-brep]] |
| [extruded-solid.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/extruded-solid.ifc) | [[models/buildingsmart-community/extruded-solid]] |
| [geographic-referencing.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/geographic-referencing.ifc) | [[models/buildingsmart-community/geographic-referencing]] |
| [grid-placement.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/grid-placement.ifc) | [[models/buildingsmart-community/grid-placement]] |
| [mapped-shape-with-multiple-items.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/mapped-shape-with-multiple-items.ifc) | [[models/buildingsmart-community/mapped-shape-with-multiple-items]] |
| [mapped-shape-with-transformation.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/mapped-shape-with-transformation.ifc) | [[models/buildingsmart-community/mapped-shape-with-transformation]] |
| [mapped-shape-without-transformation.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/mapped-shape-without-transformation.ifc) | [[models/buildingsmart-community/mapped-shape-without-transformation]] |
| [reinforcing-assembly.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/reinforcing-assembly.ifc) | [[models/buildingsmart-community/reinforcing-assembly]] |
| [reinforcing-stirrup.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/reinforcing-stirrup.ifc) | [[models/buildingsmart-community/reinforcing-stirrup]] |
| [slab-openings.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/slab-openings.ifc) | [[models/buildingsmart-community/slab-openings]] |
| [slab-standard-case.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/slab-standard-case.ifc) | [[models/buildingsmart-community/slab-standard-case]] |
| [slab-tessellated-unique-vertices.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/slab-tessellated-unique-vertices.ifc) | [[models/buildingsmart-community/slab-tessellated-unique-vertices]] |
| [structural-curve-member.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/structural-curve-member.ifc) | [[models/buildingsmart-community/structural-curve-member]] |
| [surface-model.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/surface-model.ifc) | [[models/buildingsmart-community/surface-model]] |
| [tessellated-item.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/tessellated-item.ifc) | [[models/buildingsmart-community/tessellated-item]] |
| [tessellation-with-blob-texture.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/tessellation-with-blob-texture.ifc) | [[models/buildingsmart-community/tessellation-with-blob-texture]] |
| [tessellation-with-image-texture.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/tessellation-with-image-texture.ifc) | [[models/buildingsmart-community/tessellation-with-image-texture]] |
| [tessellation-with-individual-colors.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/tessellation-with-individual-colors.ifc) | [[models/buildingsmart-community/tessellation-with-individual-colors]] |
| [tessellation-with-pixel-texture.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/tessellation-with-pixel-texture.ifc) | [[models/buildingsmart-community/tessellation-with-pixel-texture]] |
| [wall-elemented-case.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/wall-elemented-case.ifc) | [[models/buildingsmart-community/wall-elemented-case]] |
| [wall-standard-case.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/wall-standard-case.ifc) | [[models/buildingsmart-community/wall-standard-case]] |
| [wall-with-opening-and-window.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/ISO%20Spec%20archive/wall-with-opening-and-window.ifc) | [[models/buildingsmart-community/wall-with-opening-and-window]] |

### IFC 4.0.2.1 (IFC 4) / NURBS / Bentley Building Designer / Cylinder

| 配布ファイル | モデル |
| --- | --- |
| [BsplineSurf.PolyCurve.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/NURBS/Bentley%20Building%20Designer/Cylinder/BsplineSurf.PolyCurve.ifc) | [[models/buildingsmart-community/bsplinesurf-polycurve]] |
| [Facet.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/NURBS/Bentley%20Building%20Designer/Cylinder/Facet.ifc) | [[models/buildingsmart-community/facet]] |
| [OnlyBsplines.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/NURBS/Bentley%20Building%20Designer/Cylinder/OnlyBsplines.ifc) | [[models/buildingsmart-community/onlybsplines]] |
| [Plane.Cyllinder.Ellipse.PolyCurve.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/NURBS/Bentley%20Building%20Designer/Cylinder/Plane.Cyllinder.Ellipse.PolyCurve.ifc) | [[models/buildingsmart-community/plane-cyllinder-ellipse-polycurve]] |
| [Plane.Cyllinder.PolyCurve.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/NURBS/Bentley%20Building%20Designer/Cylinder/Plane.Cyllinder.PolyCurve.ifc) | [[models/buildingsmart-community/plane-cyllinder-polycurve]] |

### IFC 4.0.2.1 (IFC 4) / NURBS / Bentley Building Designer / Faces

| 配布ファイル | モデル |
| --- | --- |
| [1.SimpleRectangle.facet.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/NURBS/Bentley%20Building%20Designer/Faces/1.SimpleRectangle.facet.ifc) | [[models/buildingsmart-community/1-simplerectangle-facet]] |
| [1.SimpleRectangle.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/NURBS/Bentley%20Building%20Designer/Faces/1.SimpleRectangle.ifc) | [[models/buildingsmart-community/1-simplerectangle]] |
| [3.Torus.facet.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/NURBS/Bentley%20Building%20Designer/Faces/3.Torus.facet.ifc) | [[models/buildingsmart-community/3-torus-facet]] |
| [3.Torus.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/NURBS/Bentley%20Building%20Designer/Faces/3.Torus.ifc) | [[models/buildingsmart-community/3-torus]] |
| [4.Jar.facet.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/NURBS/Bentley%20Building%20Designer/Faces/4.Jar.facet.ifc) | [[models/buildingsmart-community/4-jar-facet]] |
| [4.Jar.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/NURBS/Bentley%20Building%20Designer/Faces/4.Jar.ifc) | [[models/buildingsmart-community/4-jar]] |
| [5.Cone.facet.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/NURBS/Bentley%20Building%20Designer/Faces/5.Cone.facet.ifc) | [[models/buildingsmart-community/5-cone-facet]] |
| [5.Cone.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/NURBS/Bentley%20Building%20Designer/Faces/5.Cone.ifc) | [[models/buildingsmart-community/5-cone]] |
| [6.RectWithHole.facet.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/NURBS/Bentley%20Building%20Designer/Faces/6.RectWithHole.facet.ifc) | [[models/buildingsmart-community/6-rectwithhole-facet]] |
| [6.RectWithHole.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/NURBS/Bentley%20Building%20Designer/Faces/6.RectWithHole.ifc) | [[models/buildingsmart-community/6-rectwithhole]] |
| [bspline surface.facet.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/NURBS/Bentley%20Building%20Designer/Faces/bspline%20surface.facet.ifc) | [[models/buildingsmart-community/bspline-surface-facet]] |
| [bspline surface.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/NURBS/Bentley%20Building%20Designer/Faces/bspline%20surface.ifc) | [[models/buildingsmart-community/bspline-surface]] |

### IFC 4.0.2.1 (IFC 4) / NURBS / Bentley Building Designer / SolidsAndSheets

| 配布ファイル | モデル |
| --- | --- |
| [BsplinePathExtrusion.facet.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/NURBS/Bentley%20Building%20Designer/SolidsAndSheets/BsplinePathExtrusion.facet.ifc) | [[models/buildingsmart-community/bsplinepathextrusion-facet]] |
| [BsplinePathExtrusion.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/NURBS/Bentley%20Building%20Designer/SolidsAndSheets/BsplinePathExtrusion.ifc) | [[models/buildingsmart-community/bsplinepathextrusion]] |
| [BsplineProfileInCSG.facet.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/NURBS/Bentley%20Building%20Designer/SolidsAndSheets/BsplineProfileInCSG.facet.ifc) | [[models/buildingsmart-community/bsplineprofileincsg-facet]] |
| [BsplineProfileInCSG.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/NURBS/Bentley%20Building%20Designer/SolidsAndSheets/BsplineProfileInCSG.ifc) | [[models/buildingsmart-community/bsplineprofileincsg]] |
| [WithArcBoundary.facet.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/NURBS/Bentley%20Building%20Designer/SolidsAndSheets/WithArcBoundary.facet.ifc) | [[models/buildingsmart-community/witharcboundary-facet]] |
| [WithArcBoundary.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/NURBS/Bentley%20Building%20Designer/SolidsAndSheets/WithArcBoundary.ifc) | [[models/buildingsmart-community/witharcboundary]] |
| [WithPlaneSurface.facet.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/NURBS/Bentley%20Building%20Designer/SolidsAndSheets/WithPlaneSurface.facet.ifc) | [[models/buildingsmart-community/withplanesurface-facet]] |
| [WithPlaneSurface.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/NURBS/Bentley%20Building%20Designer/SolidsAndSheets/WithPlaneSurface.ifc) | [[models/buildingsmart-community/withplanesurface]] |
| [jarSplit.facet.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/NURBS/Bentley%20Building%20Designer/SolidsAndSheets/jarSplit.facet.ifc) | [[models/buildingsmart-community/jarsplit-facet]] |
| [jarSplit.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/IFC%204.0.2.1%20%28IFC%204%29/NURBS/Bentley%20Building%20Designer/SolidsAndSheets/jarSplit.ifc) | [[models/buildingsmart-community/jarsplit]] |

### dev archive / IFC 4.3.RC Archive / Georeferencing-1 (RC2)

| 配布ファイル | モデル |
| --- | --- |
| [UT_GeoRef_1.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/dev%20archive/IFC%204.3.RC%20Archive/Georeferencing-1%20%28RC2%29/UT_GeoRef_1.ifc) | [[models/buildingsmart-community/ut-georef-1]] |

### dev archive / IFC 4.3.RC Archive / Georeferencing_Tin_1 (RC1)

| 配布ファイル | モデル |
| --- | --- |
| [UT_Tin_in_MGA_56.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/dev%20archive/IFC%204.3.RC%20Archive/Georeferencing_Tin_1%20%28RC1%29/UT_Tin_in_MGA_56.ifc) | [[models/buildingsmart-community/ut-tin-in-mga-56]] |

### dev archive / IFC 4.3.RC Archive / Georeferencing_Tin_2 (RC1)

| 配布ファイル | モデル |
| --- | --- |
| [UT_Tin_ifcMapConversion_to_place_in_MGA_56.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/dev%20archive/IFC%204.3.RC%20Archive/Georeferencing_Tin_2%20%28RC1%29/UT_Tin_ifcMapConversion_to_place_in_MGA_56.ifc) | [[models/buildingsmart-community/ut-tin-ifcmapconversion-to-place-in-mga-56]] |

### dev archive / IFC 4.3.RC Archive / Georeferencing_Tin_3 (RC1)

| 配布ファイル | モデル |
| --- | --- |
| [UT_Tin_with_one_hole_in_MGA_56.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/dev%20archive/IFC%204.3.RC%20Archive/Georeferencing_Tin_3%20%28RC1%29/UT_Tin_with_one_hole_in_MGA_56.ifc) | [[models/buildingsmart-community/ut-tin-with-one-hole-in-mga-56]] |

### dev archive / IFC 4.3.RC Archive / Georeferencing_Tin_4 (RC1)

| 配布ファイル | モデル |
| --- | --- |
| [UT_Tin_with_two colours_in_MGA2020_56.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/dev%20archive/IFC%204.3.RC%20Archive/Georeferencing_Tin_4%20%28RC1%29/UT_Tin_with_two%20colours_in_MGA2020_56.ifc) | [[models/buildingsmart-community/ut-tin-with-two-colours-in-mga2020-56]] |

### dev archive / IFC 4.3.RC Archive / Georeferencing_Tin_5 (RC1)

| 配布ファイル | モデル |
| --- | --- |
| [UT_Tin_ifcMapConversion_to_place_in_MGA_56_Standard_origin.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/dev%20archive/IFC%204.3.RC%20Archive/Georeferencing_Tin_5%20%28RC1%29/UT_Tin_ifcMapConversion_to_place_in_MGA_56_Standard_origin.ifc) | [[models/buildingsmart-community/ut-tin-ifcmapconversion-to-place-in-mga-56-standard-origin]] |

### dev archive / IFC 4.3.RC Archive / Georeferencing_Tiny_Survey_1 (RC1)

| 配布ファイル | モデル |
| --- | --- |
| [UT_one_string_one_pont.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/dev%20archive/IFC%204.3.RC%20Archive/Georeferencing_Tiny_Survey_1%20%28RC1%29/UT_one_string_one_pont.ifc) | [[models/buildingsmart-community/ut-one-string-one-pont]] |

### dev archive / IFC 4.3.RC Archive / LinearPlacement_1 (RC2)

| 配布ファイル | モデル |
| --- | --- |
| [UT_LinearPlacement_1.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/dev%20archive/IFC%204.3.RC%20Archive/LinearPlacement_1%20%28RC2%29/UT_LinearPlacement_1.ifc) | [[models/buildingsmart-community/ut-linearplacement-1]] |

### dev archive / IFC 4.3.RC Archive / LinearPlacement_2 (RC2)

| 配布ファイル | モデル |
| --- | --- |
| [LinearPlacement_2.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/dev%20archive/IFC%204.3.RC%20Archive/LinearPlacement_2%20%28RC2%29/LinearPlacement_2.ifc) | [[models/buildingsmart-community/linearplacement-2]] |
| [LinearPlacement_2_4X1.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/dev%20archive/IFC%204.3.RC%20Archive/LinearPlacement_2%20%28RC2%29/LinearPlacement_2_4X1.ifc) | [[models/buildingsmart-community/linearplacement-2-4x1]] |

### dev archive / IFC 4.3.RC Archive / ProjectSetup_1 (RC1)

| 配布ファイル | モデル |
| --- | --- |
| [UT_ProjectSetup_1.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/dev%20archive/IFC%204.3.RC%20Archive/ProjectSetup_1%20%28RC1%29/UT_ProjectSetup_1.ifc) | [[models/buildingsmart-community/ut-projectsetup-1]] |

### dev archive / IFC 4.3.RC Archive / ProjectSetup_2 (RC1)

| 配布ファイル | モデル |
| --- | --- |
| [UT_ProjectSetup_2.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/dev%20archive/IFC%204.3.RC%20Archive/ProjectSetup_2%20%28RC1%29/UT_ProjectSetup_2.ifc) | [[models/buildingsmart-community/ut-projectsetup-2]] |

### dev archive / IFC 4.3.RC Archive / SpatialDecomposition_1 (RC2)

| 配布ファイル | モデル |
| --- | --- |
| [UT_SpatialDecomposition_1.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/dev%20archive/IFC%204.3.RC%20Archive/SpatialDecomposition_1%20%28RC2%29/UT_SpatialDecomposition_1.ifc) | [[models/buildingsmart-community/ut-spatialdecomposition-1]] |

### dev archive / IFC 4.3.RC Archive / SpatialStructure_2 (RC2)

| 配布ファイル | モデル |
| --- | --- |
| [SpatialStructure_2.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/dev%20archive/IFC%204.3.RC%20Archive/SpatialStructure_2%20%28RC2%29/SpatialStructure_2.ifc) | [[models/buildingsmart-community/spatialstructure-2]] |

### dev archive / IFC 4.3.RC Archive / SpatialStructure_3 (RC2)

| 配布ファイル | モデル |
| --- | --- |
| [SpatialStructure_3.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/dev%20archive/IFC%204.3.RC%20Archive/SpatialStructure_3%20%28RC2%29/SpatialStructure_3.ifc) | [[models/buildingsmart-community/spatialstructure-3]] |

### dev archive / IFC 4.3.RC Archive / Tin_1 (RC1)

| 配布ファイル | モデル |
| --- | --- |
| [UT_Tin_1.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/dev%20archive/IFC%204.3.RC%20Archive/Tin_1%20%28RC1%29/UT_Tin_1.ifc) | [[models/buildingsmart-community/ut-tin-1]] |

### dev archive / IFC 4.3.RC Archive / Tin_2 (RC1)

| 配布ファイル | モデル |
| --- | --- |
| [UT_Tin_2.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/dev%20archive/IFC%204.3.RC%20Archive/Tin_2%20%28RC1%29/UT_Tin_2.ifc) | [[models/buildingsmart-community/ut-tin-2]] |

### dev archive / IFC 4.3.RC Archive / Tin_3 (RC1)

| 配布ファイル | モデル |
| --- | --- |
| [UT_Tin_3.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/dev%20archive/IFC%204.3.RC%20Archive/Tin_3%20%28RC1%29/UT_Tin_3.ifc) | [[models/buildingsmart-community/ut-tin-3]] |

### dev archive / IFC 4.3.RC Archive / Tin_4 (RC1)

| 配布ファイル | モデル |
| --- | --- |
| [UT_Tin_4.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/dev%20archive/IFC%204.3.RC%20Archive/Tin_4%20%28RC1%29/UT_Tin_4.ifc) | [[models/buildingsmart-community/ut-tin-4]] |

### dev archive / IFC 4.3.RC Archive / UT_Alignment_12d_11  (RC2)

| 配布ファイル | モデル |
| --- | --- |
| [UT_Alignment_12d_11.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/dev%20archive/IFC%204.3.RC%20Archive/UT_Alignment_12d_11%20%20%28RC2%29/UT_Alignment_12d_11.ifc) | [[models/buildingsmart-community/ut-alignment-12d-11]] |

### dev archive / IFC 4.3.RC Archive / UT_SpatialStructure_4 (RC4)

| 配布ファイル | モデル |
| --- | --- |
| [UT_SpatialStructure_4.ifc](https://media.githubusercontent.com/media/buildingsmart-community/Community-Sample-Test-Files/7ddf57a201f88a0c213d5322b02ed15e94a60a40/dev%20archive/IFC%204.3.RC%20Archive/UT_SpatialStructure_4%20%28RC4%29/UT_SpatialStructure_4.ifc) | [[models/buildingsmart-community/ut-spatialstructure-4]] |

## メモ

- 旧 `buildingSMART/Sample-Test-Files` のコミュニティ収録分の移管先。移管の説明は [Certification datasetsのREADME](https://github.com/buildingSMART/Certification-datasets#readme) を参照。
