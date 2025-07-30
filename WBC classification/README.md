# Exploring Deep Learning Models for White Blood Cell Classification

This project presents a comparative analysis of various deep learning architectures for the classification of White Blood Cells (WBCs) from microscopic images. The aim is to automate WBC subtype identification (neutrophils, lymphocytes, monocytes, eosinophils, and basophils) using Convolutional Neural Networks (CNNs) and assess the impact of preprocessing on model performance.

## Project Structure

The implementation is divided into two major parts based on whether image preprocessing is applied:

### With Preprocessing
- **WBC_CNN_GAN_ResNet_Preprocessed.ipynb**
- **WBC_VGG19_Preprocessed.ipynb**
- **WBC_MobileNet_Preprocessed.ipynb**

### Without Preprocessing
- **WBC_CNN_GAN_ResNet_Unprocessed.ipynb**
- **WBC_VGG19_Unprocessed.ipynb**
- **WBC_MobileNetV2_Unprocessed.ipynb**

---

## Dataset

- **Source**: BCCD White Blood Cell Image Dataset
- **Classes**: Basophil, Eosinophil, Lymphocyte, Monocyte, Neutrophil
- **Total Images**: 3,500 (700 per class)
- **Image Size**: 84x84 pixels
- **Balance**: No class imbalance

---

## Methodology

1. **Image Preprocessing Techniques** (applied to the “preprocessed” versions only):
   - Histogram Equalization
   - Gaussian Low-Pass and High-Pass Filtering

2. **Models Implemented**:
   - **Simple CNN**
   - **GAN + ResNet18**
   - **VGG19**
   - **MobileNetV2**

3. **Evaluation Metrics**:
   - Training Loss, Validation Loss, Test Accuracy
   - Accuracy vs. Epoch and Loss vs. Epoch plots

4. **Training Details**:
   - Loss Functions: `categorical_crossentropy`, `CrossEntropyLoss`, `BCEWithLogitsLoss`
   - Optimizer: `Adam`
   - Train/Test split using `train_test_split` from `sklearn`

---

## Results Summary

| Model                  | Preprocessing | Train Acc | Val Acc | Test Acc | Observations |
|------------------------|----------------|-----------|---------|----------|--------------|
| CNN                    | Yes         | 85.96%    | 87.29%  | 87.28%   | Good performance with enhanced features |
| CNN                    | No          | 86.46%    | 89.00%  | 88.99%   | Slightly better without preprocessing |
| GAN + ResNet           | Yes         | 94.57%    | 88.00%  | 89.14%   | Best preprocessed result |
| GAN + ResNet           | No          | 96.64%    | 94.28%  | **95.42%**   | **Top overall performer** |
| VGG19                  | Yes         | 74.55%    | 77.14%  | 74.57%   | Moderate performance |
| VGG19                  | No          | 80.27%    | 77.86%  | 80.71%   | Preprocessing slightly hurt performance |
| MobileNetV2            | Yes         | 18.84%    | -       | 20.00%   | Significantly underperformed |
| MobileNetV2            | No          | 96.46%    | -       | 94.29%   | Surprisingly high accuracy |

> **Conclusion**: The model combining **GAN + ResNet without preprocessing** achieved the best performance with a **test accuracy of 95.42%**. Preprocessing techniques did not always improve results and, in some cases (e.g., MobileNetV2), led to a significant drop in accuracy.

---

## Tech Stack

- **Language**: Python
- **Libraries**:
  - `TensorFlow`, `PyTorch`, `Keras`
  - `OpenCV`, `PIL`
  - `scikit-learn`, `NumPy`, `pandas`, `matplotlib`

---

## Key Insights

- Preprocessing using histogram equalization and Gaussian filters did not consistently enhance performance.
- Simpler models like CNN and VGG showed steady accuracy but were outperformed by GAN + ResNet.
- MobileNetV2 yielded unexpectedly strong results **without** preprocessing but was highly unstable when preprocessing was applied.

---

## Desired Outcome

This project demonstrates how CNN-based methods — especially hybrid architectures using GANs for augmentation — can automate and improve WBC classification. The insights help support better diagnostic tools in clinical practice by enabling more accurate, consistent, and faster analysis of blood cell imagery.

---

## Contact

For any queries or collaboration:

**Email**: varni.mulay@gmail.com  
**LinkedIn**: [Varnika Mulay](https://www.linkedin.com/in/varnika-mulay)

