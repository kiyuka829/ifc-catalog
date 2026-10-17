# ifc-catalog

公開IFCの出典・配布情報と、実物を確認した結果を管理するObsidian用カタログ。

## 開き方

1. Obsidianでこのリポジトリのフォルダを「保管庫として開く」で開く。
2. コアプラグインの「ベース（Bases）」を有効にする。
3. [カタログ.base](カタログ.base)を開き、「データセット」「IFCモデル」を切り替える。

## 保存場所

```text
datasets/       データセットごとのノート（公開元・ライセンス・配布ファイル）
models/         データセットごとのフォルダに個別IFCのノートを保存
  <dataset-id>/ ファイル名・サイズ・スキーマ・ハッシュ
templates/      新規ノート用のひな形
カタログ.base   一覧の表示設定
local/          元データの作業領域（Git管理対象外、必要時に作成）
```

## 追加・更新

- データセットを登録するときは [ひな形](templates/dataset.md)を `datasets/<dataset-id>.md` にコピーし、プロパティと本文を埋める。
- IFCを登録するときは [ひな形](templates/model.md)を `models/<dataset-id>/<モデル名>.md` にコピーし、`dataset` に `"[[datasets/<dataset-id>]]"` を指定する。
- ひな形の `{{title}}` はノート名に置き換える。Obsidianのテンプレート機能を使う場合は、テンプレートフォルダを `templates` に設定する。

### 情報の記録場所

- `datasets` に概要・公開元・ライセンス・配布ファイル名・配布URL・取得版を記録する。
- `models` に個別IFCのファイル名・スキーマ・サイズ・SHA-256を記録する。
- IFC直接配布の場合は、データセットの配布ファイル欄からモデルノートへリンクする。
- ZIPなどのアーカイブ配布の場合は、モデルノートの `archive_name` と `archive_path` で配布ファイルとの対応を示す。
- 圧縮ファイルのサイズは `datasets` の配布ファイル欄に記録する。

| 主なプロパティ | 内容 |
| --- | --- |
| `type` | `dataset` または `model`。保存フォルダと合わせて一覧の対象を判定 |
| `name` | データセットの名称（データセットノートのみ） |
| `source_url` / `license` | データセットの公開ページ、ライセンス |
| `ifc_schemas` | データセットのスキーマ一覧。公開元の記載か実測かを本文に明記 |
| `dataset` | IFCが属するデータセットへの内部リンク |
| `filename` | IFCファイルの実際の名前 |
| `archive_name` / `archive_path` | 元の配布アーカイブ名と、その内部での相対パス。内包アーカイブは `内包ZIPのパス!/IFCのパス` と記録。直接配布なら空欄 |
| `size_bytes` | 実物で確認したIFCのバイト数。モデルノートにのみ記録 |
| `ifc_schema` | 実物の `FILE_SCHEMA` で確認したスキーマ |
| `sha256` | 実物のSHA-256。`shasum -a 256 <ファイルのパス>` で計算可能 |
| `instance_count` | ファイル内のエンティティインスタンス総数 |
| `product_count` / `element_count` | `IfcProduct` / `IfcElement` の件数。派生型を含む |
| `property_set_count` / `property_count` | `IfcPropertySet` / `IfcProperty` の件数。派生型を含む |
| `quantity_set_count` / `quantity_count` | `IfcElementQuantity` / `IfcPhysicalQuantity` の件数。派生型を含む |
| `length_unit` / `length_unit_scale` | プロジェクトの長さ単位とメートルへの換算係数。未指定の場合は `METRE` と `1` |
| `projected_crs_name` | CRS名 |
| `checked_on` | 公開元・配布情報を確認した日（データセットノートのみ） |

## Python環境とIFCの集計

[uv](https://docs.astral.sh/uv/) でPython 3.12とIfcOpenShell 0.9.0の環境を作成する。

```sh
uv sync --locked
uv run python scripts/inspect_ifc.py local/example.ifc > local/example-summary.json
```
