# Lavers Timber Strength Properties: BRE Dataset & Interactive Web Explorer

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Static%20Web%20App-orange?style=flat-square&logo=github)](index.html)
[![Records](https://img.shields.io/badge/Records-447%20Test%20Conditions-success?style=flat-square)](#dataset-structure)

A high-fidelity digitized database and interactive web explorer for the physical and mechanical timber properties evaluated by the UK **Building Research Establishment (BRE)** / **Forest Products Research Laboratory (FPRL)**.

---

## 📚 Primary Literature & Original Documents

This repository digitizes two primary technical publications from the Building Research Establishment:

1. 📘 **1983 Master Report**:  
   [*The Strength Properties of Timber*](https://bregroup.com/store/bookshop/the-strength-properties-of-timber)  
   **BRE Report BR 241** (3rd Edition), by Gwendoline M. Lavers, revised by G.L. Moore. Garston, BRE, 1983.  
   *Contains standard small clear specimen ($20 \times 20\text{ mm}$) test data for 435 Green and Air-Dried test condition records across 223 timber species and growth location lots.*

2. 📙 **1997 Supplement**:  
   [*The Strength Properties of Timber: 1997 Supplement*](https://bregroup.com/store/bookshop/the-strength-properties-of-timber-1997-supplement)  
   **BRE Report BR 329**, by K.W. Maun & A.E. Coday. Watford, BRE, 1997. ISBN 1-86081-165-5.  
   *Adds standardized test data for 12 commercial and plantation-grown timber species tested in air-dried condition under BS 373:1957.*

---

## Key Stats

- **447 Total Test Condition Records**: Digitized with full statistical metrics (Mean, Standard Deviation, and Sample Count $n$) for all physical and mechanical properties.
- **191 Unique Common Species**: 186 original species from Lavers (1983) plus 5 new commercial species introduced in the 1997 Supplement (*Andiroba*, *Bintangor*, *Kamarare*, *Taun*, *Vitex*).
- **Explicit Source Metadata**: Every JSON record contains a dedicated `dataset_source` attribute identifying its origin publication (`"1983 BRE Report (Lavers)"` or `"1997 BRE Supplement (Maun & Coday)"`).

---

## 📂 Repository Structure

```text
├── index.html                           # Standalone static web application (HTML/CSS/JS + Chart.js)
├── master_lavers_1983.json              # 1983 Master Dataset (435 records)
├── maun_1997_supplement.json            # 1997 Supplement Dataset (12 records)
├── combined_lavers_maun_dataset.json    # Complete Combined Dataset with dataset_source metadata (447 records)
├── create_dashboard.py                  # Python generator script for index.html
└── README.md                            # Documentation & deployment guide
```

---

## 📊 Recorded Timber Properties

For each species and test condition (*Green* or *Air-Dried at 12% Moisture Content*), the following properties were recorded:

| Property | Symbol / Unit | Description |
| :--- | :--- | :--- |
| **Moisture Content** | `%` | Moisture content at time of testing |
| **Density** | $\text{kg/m}^3$ | Air-Dried (12% MC) or Green (50% MC) density |
| **Specific Gravity** | $-$ | Nominal specific gravity based on oven-dry mass |
| **Bending Strength (MOR)** | $\text{MPa}$ / $\text{N/mm}^2$ | Modulus of Rupture from static bending |
| **Bending Stiffness (MOE)** | $\text{MPa}$ / $\text{N/mm}^2$ | Modulus of Elasticity from static bending |
| **Work to Maximum Load** | $\text{mm N/mm}^3$ | Work done in bending up to maximum load |
| **Work Total Fracture** | $\text{mm N/mm}^3$ | Total work done in bending up to total fracture |
| **Impact Drop Height** | $\text{m}$ | Drop height of 22.7 kg hammer causing failure |
| **Compression Parallel** | $\text{MPa}$ / $\text{N/mm}^2$ | Maximum compressive strength parallel to grain |
| **Side Hardness** | $\text{N}$ | Load required to embed 11.28 mm steel ball to half-depth |
| **Shear Parallel** | $\text{MPa}$ / $\text{N/mm}^2$ | Maximum shearing strength parallel to grain |
| **Cleavage Strength** | $\text{N/mm}$ | Radial and Tangential resistance to splitting |

---

## 📜 Citation & References

- **Lavers, G. M. (revised by Moore, G. L.)** (1983). *The Strength Properties of Timber*. Building Research Establishment Report BR 241 (3rd Edition). Garston: BRE / HMSO.
- **Maun, K. W., & Coday, A. E.** (1997). *The Strength Properties of Timber: 1997 Supplement*. Building Research Establishment Report BR 329. Watford: BRE / CRC Ltd.
- **British Standards Institution** (1957). *Testing Small Clear Specimens of Timber*. British Standard BS 373:1957. London: BSI.
