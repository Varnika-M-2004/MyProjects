# Exploring Disease Similarity Using NLP

This project investigates disease similarity by analyzing textual information such as symptoms, causes, and treatments using Natural Language Processing (NLP) techniques. The core idea is to identify diseases that share common medical features — helping predict the likelihood of co-occurring or related conditions.

## Features

### Data Preparation
- Extracted disease names and corresponding descriptions from medical sources.
- Processed texts to focus on **keywords** like symptoms, treatments, and causes.

### Similarity Detection
- Applied **Jaccard Similarity** to compare disease pairs based on extracted keyword sets.
- Constructed a **similarity matrix** to quantify and visualize semantic overlap.

### Inference Logic
- If a patient is diagnosed with a particular disease, the model identifies other diseases that share high similarity scores.
- Helps uncover **comorbidities**, potential misdiagnoses, or secondary risk conditions based on symptom overlap.

### Visualization
- Tabular display and heatmaps for top similar diseases.
- Supports easier medical analysis and interpretation of semantic closeness.

## Tech Stack

- **Programming Language**: Python
- **Libraries Used**:
  - `pandas`, `numpy` – Data processing
  - `nltk`, `re` – Text preprocessing
  - `sklearn.metrics` – Jaccard similarity computation
  - `matplotlib`, `seaborn` – Data visualization

## Desired Outcome

The goal of this project is to:
- **Model disease similarity** using NLP and keyword-based comparison.
- **Support diagnostic reasoning** by suggesting related diseases based on overlapping medical features.
- Provide a foundation for **intelligent clinical decision systems**, especially for early detection of related or sequential illnesses.

## Example Use Case

If a user inputs *Disease A*, the model analyzes its symptoms and treatments, and returns a ranked list of diseases (*Disease B, C, D...*) with high similarity — aiding in **risk prediction**, **screening**, or **secondary diagnosis**.

## Contact

For questions or collaborations:

**Email**: varni.mulay@gmail.com  
**LinkedIn**: [Varnika Mulay](https://www.linkedin.com/in/varnika-mulay)
