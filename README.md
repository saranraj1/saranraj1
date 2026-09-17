<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/saranraj1/saranraj1/main/assets/hero-dark.gif">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/saranraj1/saranraj1/main/assets/hero-light.gif">
    <img alt="U Saran Raj — AI/ML Researcher" src="https://raw.githubusercontent.com/saranraj1/saranraj1/main/assets/hero-dark.gif" width="100%">
  </picture>
</div>

<p align="center">
  <b>AI/ML Researcher</b> &nbsp;·&nbsp; Responsible AI &nbsp;·&nbsp; Agent Reliability &nbsp;·&nbsp; Code Intelligence<br>
  <a href="https://saranraj-portfolio-two.vercel.app/"><b>Portfolio</b></a> &nbsp;·&nbsp;
  <a href="https://github.com/saranraj1?tab=repositories"><b>Repositories</b></a> &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/in/saranraj-u-663615352/"><b>LinkedIn</b></a> &nbsp;·&nbsp;
  <a href="mailto:saran17102005@gmail.com"><b>Contact</b></a>
</p>

---

### Research Statement

> *"I investigate where intelligent systems fail — and build tools to expose why."*

Most machine learning models are evaluated on aggregate benchmark averages. In production, however, they encounter distribution shifts, latent demographic leakage, and deceptive optimization dynamics that cause silent, high-impact failures.

My work treats neural models like complex physical systems: **probing their boundary decay, localizing causal faults, and verifying agent decision paths before deployment**.

---

### 01 / Research Map

A spatial topology connecting structural code analysis, empirical reliability bounds, and game-theoretic agent verification:

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/saranraj1/saranraj1/main/assets/map-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/saranraj1/saranraj1/main/assets/map-light.svg">
    <img alt="Research Topology Map" src="https://raw.githubusercontent.com/saranraj1/saranraj1/main/assets/map-dark.svg" width="100%">
  </picture>
</div>

---

### 02 / Flagship Systems

#### [01] [TITAN](https://github.com/saranraj1/Titan) · Change-Aware Code Intelligence
> *Predicting the semantic blast radius of code changes through AST proof trees and co-change graphs.*

* **The Problem**: Incremental software refactors frequently trigger silent regressions because standard linters only check syntax, not semantic propagation across call graphs.
* **Approach**: Combines Tree-sitter AST parsing, Git commit co-change history, and Datalog relation queries to compute the exact impact radius of diffs before execution.
* **Tech Stack**: `Python` · `Tree-sitter` · `Datalog` · `Git API` · `NetworkX`
* **Repository**: [`github.com/saranraj1/Titan`](https://github.com/saranraj1/Titan)

---

#### [02] [DARA v2](https://github.com/saranraj1/DARA-v2) · Autonomous Software Repair
> *Closed-loop causal fault localization and patch synthesis with Docker sandbox verification.*

* **The Problem**: LLM coding agents often generate plausible-looking patches that pass basic tests while breaking subtle edge cases or introducing new security vulnerabilities.
* **Approach**: Multi-agent consensus loop that isolates failing traceframes, queries vector-indexed documentation, synthesizes minimal diffs, and verifies them inside isolated Docker containers.
* **Tech Stack**: `Python` · `Multi-Agent Orchestration` · `Docker SDK` · `Neo4j` · `Vector Retrieval`
* **Repository**: [`github.com/saranraj1/DARA-v2`](https://github.com/saranraj1/DARA-v2)

---

#### [03] [SILENTBIAS](https://github.com/saranraj1/SilentBias) · Latent Proxy Leakage & Fairness
> *Auditing hidden demographic reconstruction in sanitized representation spaces.*

* **The Problem**: Naively removing protected attributes (e.g. race, gender, zip code) does not prevent discrimination; deep models reconstruct protected targets from subtle latent proxy correlations.
* **Approach**: Trains adversarial shadow probes to quantify mutual information between latent embeddings and protected features, establishing provable fairness bounds.
* **Tech Stack**: `PyTorch` · `Scikit-learn` · `Information Theory` · `Representation Probing`
* **Repository**: [`github.com/saranraj1/SilentBias`](https://github.com/saranraj1/SilentBias)

---

#### [04] [AGENT-NOIR](https://github.com/saranraj1/AGENT-NOIR) · Deception & Multi-Agent Reliability
> *Eliminating strategic deceit in collaborative agent systems through deterministic verification protocols.*

* **The Problem**: In multi-step autonomous workflows, agents learn to optimize for verifier acceptance rather than genuine problem resolution.
* **Approach**: Formalizes interrogation as a game-theoretic verifier protocol where every agent claim must be backed by an immutable, deterministic audit trace.
* **Tech Stack**: `TypeScript` · `Python` · `Deterministic Simulation` · `Game Theory` · `Audit Logging`
* **Repository**: [`github.com/saranraj1/AGENT-NOIR`](https://github.com/saranraj1/AGENT-NOIR)

---

### 03 / The Failure Lab

An empirical testing loop designed to stress-test AI behavior at distribution boundaries:

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/saranraj1/saranraj1/main/assets/pipeline-dark.gif">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/saranraj1/saranraj1/main/assets/pipeline-light.gif">
    <img alt="Failure Lab Pipeline: DATA → SHIFT → FAILURE → AUDIT → EXPLANATION → VERIFICATION" src="https://raw.githubusercontent.com/saranraj1/saranraj1/main/assets/pipeline-dark.gif" width="100%">
  </picture>
</div>

| Experiment | Core Inquiry | Finding / Contribution |
| :--- | :--- | :--- |
| [`Data Decay`](https://github.com/saranraj1/data_decay) | Distribution Drift | Measures performance degradation rates over non-stationary temporal streams |
| [`OOD Explorer`](https://github.com/saranraj1/OOD-explorer) | Out-of-Distribution | Stress-tests decision boundaries under controlled covariate shifts |
| [`MissingnessMatter`](https://github.com/saranraj1/MissingnessMatter) | Informative Missingness | Separates MCAR, MAR, and MNAR patterns in tabular neural architectures |
| [`Fragility Index`](https://github.com/saranraj1/Fragility_index) | Model Brittleness | Computes the minimal feature perturbation vector required to flip predictions |
| [`XAI Lab`](https://github.com/saranraj1/XAI-Lab) | Explainability Auditing | Evaluates the alignment between feature attribution maps and causal impact |

---

### 04 / Verification Methodology

```python
# Causal verification: Bounding prediction uncertainty under distribution shift
def verify_system_invariant(model, spec, test_distribution):
    """
    Empirically bounds prediction error under semantic perturbation.
    Rejects hypotheses when uncertainty violates specification margin.
    """
    probes = test_distribution.generate_adversarial_perturbations()
    for probe in probes:
        prediction, uncertainty = model.predict_with_variance(probe)
        if not spec.is_admissible(prediction, uncertainty):
            raise VerificationFailure(
                f"Invariant violation: confidence={1 - uncertainty:.3f}, "
                f"margin={spec.delta(prediction):.4f}"
            )
    return VerificationProof(status="ADMISSIBLE", bounds=spec.bounds)
```

> **`RESEARCH NOTE // 001`**  
> *"I am interested in the gap between what an AI system predicts and what we can actually prove about it."*

---

### 05 / Tools & Runtime

* **Core Research**: Python · PyTorch · NumPy · SciPy · Scikit-learn · Tree-sitter · NetworkX
* **Systems & Infra**: TypeScript · FastAPI · Docker · PostgreSQL · Redis · Neo4j · GitHub Actions
* **Focus Areas**: Causal Inference · Representation Probing · AST Analysis · Multi-Agent Protocols · XAI

---

```
SARAN@RESEARCH-LAB
────────────────────────────────────────────────────────────
BUILD → INTERROGATE → VERIFY → REPEAT
```
