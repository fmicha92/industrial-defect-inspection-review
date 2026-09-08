# Third-party notices

This website combines repository code, checked-in evidence metadata, bibliographic identifiers, and open-source software. Each component retains its applicable copyright and license conditions.

## Repository material

The repository uses a multi-license model:

- source code, scripts, and tests: MIT unless a file states otherwise;
- project documentation, schemas, exports, and graph annotations: Creative Commons Attribution 4.0 International unless a file states otherwise;
- vendored and third-party components: their respective upstream licenses;
- quotations, publication-derived material, and bibliographic content: rights remain with their authors and publishers;
- linked dataset archives: not distributed or relicensed by this website.

The repository-level **LICENSE**, **docs/licenses/**, and **THIRD_PARTY_NOTICES.md** files are authoritative. A notice attached to an individual file takes precedence.

## Runtime dependencies

Exact resolved versions are recorded in **pnpm-lock.yaml**.

| Package | Website role | License identifier |
|---|---|---|
| @react-sigma/core | React integration for Sigma graph views | MIT |
| clsx | Conditional class-name composition | MIT |
| d3 | Scientific chart and layout utilities | ISC |
| graphology | Graph data structures | MIT |
| graphology-layout-forceatlas2 | ForceAtlas2 graph layout | MIT |
| lucide-react | Interface icons | ISC |
| papaparse | CSV parsing | MIT |
| react | User-interface runtime | MIT |
| react-dom | Browser rendering | MIT |
| react-router-dom | Client-side routing | MIT |
| sigma | WebGL graph rendering | MIT |

## Development and verification dependencies

| Package | Website role | License identifier |
|---|---|---|
| @biomejs/biome | Formatting and static analysis | MIT OR Apache-2.0 |
| @testing-library/jest-dom | DOM test assertions | MIT |
| @testing-library/react | React component testing | MIT |
| @types/d3 | TypeScript declarations | MIT |
| @types/node | TypeScript declarations | MIT |
| @types/papaparse | TypeScript declarations | MIT |
| @types/react | TypeScript declarations | MIT |
| @types/react-dom | TypeScript declarations | MIT |
| @vitejs/plugin-react | React integration for Vite | MIT |
| jsdom | Test DOM implementation | MIT |
| tsx | TypeScript execution for maintenance scripts | MIT |
| typescript | Type checking and compilation | Apache-2.0 |
| vite | Development server and static build | MIT |
| vitest | Test runner | MIT |

Transitive dependencies are recorded in **pnpm-lock.yaml** and remain governed by their own license texts and notices.

## Icons, fonts, and imagery

Interface icons are provided by Lucide under the ISC license.

The website uses local system font stacks and does not require a runtime font CDN, stock photography, or AI-generated imagery. New research images may be added only when redistribution permission and required attribution are documented. Assets with unclear or incompatible permissions must be omitted.

## Publications and datasets

Publication and dataset names, identifiers, links, reported metrics, and short factual metadata are presented for scholarly evidence navigation.

The website does not redistribute:

- publication PDFs;
- extracted copyrighted full text;
- dataset archives;
- private note bodies.

A dataset being publicly accessible does not establish a license to copy or republish its files. Users must review the linked dataset terms and license before reuse.

## Website downloads

Files beneath **public/downloads/** are provided as reference tables. Their availability through the website does not transfer rights in referenced publications, datasets, trademarks, or third-party material.

## Repository citation

Use the repository’s **CITATION.cff** and release metadata for citation. Do not infer a DOI, archived-release URL, contributor list, or license grant that is not explicitly recorded there.
