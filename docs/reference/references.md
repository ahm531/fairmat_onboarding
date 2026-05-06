# FAIRmat PI onboarding form reference

This reference describes the fields in the FAIRmat PI onboarding form and gives guidance and examples for completing each section.

## General information

| Field | What to enter | Example |
|---|---|---|
| **Full name** | Enter the PI’s first and last name. | `John Doe` |
| **Institution(s)** | List the institution or institutions the PI is affiliated with. | `Humboldt-Universität zu Berlin` |
| **Research group name or department** | Enter the name of the research group, chair, institute, or department. | `Functional Materials Group` |
| **Webpage** | Provide the URL of the research group or department webpage. | `https://www.example-university.de/materials-group` |
| **FAIRmat Area(s)** | Select the FAIRmat area or areas the PI is associated with. | `Area A - Synthesis`, `Area B - Experiment`, `Area C - Computation`, `Area D - Data modeling and interoperability`, `Area E - Digital infrastructure`, `Area F - Enabling data-driven science`, `Area G - Outreach`, `Area H - Management` |
| **Main contact person for data management / NOMAD administration** | Enter the person who can serve as the main contact for RDM or NOMAD-related questions in the group. | `Jane Doe` |
| **Role of contact person** | Enter the contact person’s role. | `Data steward`, `Lab manager`, 'IT adminstrator`, `Data curator`, `NOMAD Oasis admin` |
| **Email of contact person** | Enter the email address of the contact person. | `john.example@example.edu` |
| **Related projects or initiatives** | List related projects or initiatives. | `CRC 1234`, `NFFA-Europe`, `Battery 2030+`, `EXC 2089`, `RTG 531` |
| **Expectations from FAIRmat** | Briefly describe expectations from FAIRmat. | `Support for metadata standardization and NOMAD Oasis integration.` |

## Research Focus

| Field | What to enter | Example |
|---|---|---|
| **What best describes your research approach?** | Select whether the work is mainly experimental, computational, or both. | `3- Both` |
| **Main research topics** | List the main scientific topics or themes. | `Catalysis`, `Quantum materials`, `Energy storage` |
| **Main material systems studied** | List the main material systems studied by the group. | `Perovskites`, `2D materials`, `Oxide thin films` |
| **Main methods and techniques used** | List the main methods used by the group. | `DFT`, `XRD`, `Raman spectroscopy`, `Molecular dynamics` |
| **Brief description of the research focus of your group** | Summarize the main scientific questions and research directions. | `Our group studies structure–property relationships in oxide materials for energy applications.` |
| **How does your research connect to FAIRmat’s scientific scope?** | Describe the relation to FAIRmat domains, workflows, or NOMAD usage. | `Our work generates spectroscopy and simulation data that could be integrated into NOMAD workflows.` |

## Research Data Management

| Field | What to enter | Example |
|---|---|---|
| **How is research data currently stored?** | Select the storage solutions currently used. | `HPC storage`, `Local servers` |
| **Other storage solution** | If **Other** is selected, specify the solution. | `Institutional archive system` |
| **How is metadata documented?** | Select how metadata and research details are documented. | `Electronic lab notebooks`, `Spreadsheets` |
| **Other metadata documentation method** | If **Other** is selected, specify the method. | `Custom laboratory database` |
| **Are there existing standards or schemas used in your group?** | List standards, ontologies, or schemas used by the group. | `NeXus`, `CIF`, `custom JSON schemas` |

### Research Data subsection

Use this subsection to describe the main types of data generated, processed, or analyzed by the group. Add one subsection for each relevant data type.

| Field | What to enter | Example |
|---|---|---|
| **Name of data entry** | Provide a short descriptive name for the data type. | `DFT simulations of catalysts` |
| **Data type** | Select the option that best describes the data. | `1- DFT calculations` |
| **Other data type** | If **Other** is selected, specify the type. | `Neutron scattering data` |
| **Approximate data volume per year** | Estimate the yearly data volume. | `2 TB/year` |
| **Software or instruments used** | List software, instruments, or tools related to the data. | `VASP`, `Quantum ESPRESSO`, `Bruker D8 Advance` |
| **File formats** | List the main file formats used. | `CSV`, `HDF5`, `TIFF`, `XYZ` |

## NOMAD Usage

| Field | What to enter | Example |
|---|---|---|
| **Are you currently using NOMAD?** | Select the current NOMAD usage status. | `Planning to` |
| **NOMAD services currently used by your group** | Select the NOMAD services currently used. | `1- Central NOMAD`, `2- NOMAD Oasis` |
| **NOMAD plugins developed in your group** | Select plugin components developed by the group. | `6- Parsers`, `7- Schema packages` |
| **NOMAD plugin details** | Briefly describe plugins developed by the group. | `Parser for operando spectroscopy data: https://github.com/example/plugin` |
| **Which training topics are relevant for your group’s current or upcoming needs?** | Select relevant training topics. | `Plugin development`, `ELN usage` |
| **Other training topic** | If **Other** is selected, specify the topic. | `AI-ready metadata pipelines` |
| **What are the main challenges preventing deeper use of NOMAD today?** | Describe technical or organizational barriers. | `Limited personnel resources and lack of standardized metadata workflows.` |
| **What workflows would you like to integrate with NOMAD?** | Describe workflows that could benefit from NOMAD integration. | `Automated upload of spectroscopy measurements from laboratory instruments.` |

## Onboarding administration

This section is for the FAIRmat onboarding team only. PIs should not edit this section.

| Field | Purpose |
|---|---|
| **Interview status** | Tracks the onboarding interview status. |
| **Interview date** | Records the onboarding interview date. |
| **Interviewers** | Records the onboarding team members involved. |
| **Remarks** | Internal notes for the onboarding team. |
| **Letter of Commitment (LoC)** | Stores the signed Letter of Commitment. |