# Automated Nutritional Analysis: Object Detection for Balanced Meal Evaluation According to 4 Sehat 5 Sempurna
### Andromeda Group's Startup Campus Final Project

## Project Description
Final project untuk program Startup Campus pada track Artificial Intelligence. Proyek ini bertujuan untuk mengembangkan aplikasi Automated Nutritional Analysis: Object Detection for Balanced Meal Evaluation According to 4 Sehat 5 Sempurna. Aplikasi ini menggunakan model deteksi objek berbasis Convolutional Neural Networks (CNN) untuk menganalisis komposisi makanan dan mengevaluasi keseimbangan gizi berdasarkan prinsip 4 Sehat 5 Sempurna. Proyek ini dirancang untuk mendukung edukasi gizi masyarakat dengan teknologi berbasis AI. Mendeteksi tingkat nutrisi dan gizi pada sepiring makanan menggunakan Object Detection dan berpatok pada 4 Sehat 5 Sempurna.

## Fitur Utama
- Deteksi dan klasifikasi makanan menggunakan CNN.
- Tampilan interaktif dengan anotasi visual objek makanan.
- Evaluasi keseimbangan nutrisi secara otomatis.
- Dukungan data lokal untuk prinsip 4 Sehat 5 Sempurna.
  
## Teknologi yang Digunakan:
- Python
- TensorFlow/Keras
- OpenCV
- Dataset makanan dan minuman

Please describe your Startup Campus final project here. You may should your <b>model architecture</b> in JPEG or GIF.

## Contributor
| Full Name | Affiliation | Email | LinkedIn | Role |
| --- | --- | --- | --- | --- |
| Mochamad Faisal Akbar | Universitas Sebelas Maret | faisalzogg022@gmail.com | [Profile Linkedln](https://www.linkedin.com/in/m-faisal-akbar) | Team Lead |
| Firman Sanjaya | Politeknik Harapan Bersama | firmansanjaya2301@gmail.com | [Profile Linkedln](https://www.linkedin.com/in/firman-sanjaya-ab5001332) | Team Member |
| Nasywa Raichanah | Universitas Sebelas Maret | nasywaraichanah15.2@gmail.com | [Profile Linkedln](https://www.linkedin.com/in/nasywaraichanah/) |Team Member |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
| Nicholas Dominic | Startup Campus, AI Track | nic.dominic@icloud.com | [Profile Linkedln](https://linkedin.com/in/nicholas-dominic) | Supervisor |

## Setup
### Prerequisite Packages (Dependencies)
- pandas==2.1.0
- openai==0.28.0
- google-cloud-aiplatform==1.34.0
- google-cloud-bigquery==3.12.0
- ...
- ...

### Environment
| | |
| --- | --- |
| CPU | 12th Gen Intel(R) Core(TM) i7-1260P (16 CPUs), ~2.1GHz |
| GPU | Laptop: Intel(R) Iris(R) Xe Graphics , Kaggle: Nvidia P100 (x1) |
| ROM | 476,92 GB SSD |
| RAM | 16 GB |
| OS | Microsoft Windows 11 Home Single Language |

## Dataset
Describe your dataset information here. Provide a screenshot for some of your dataset samples (for example, if you're using CIFAR10 dataset, then show an image for each class).
- Link: [Dataset 4 Sehat 5 Sempurna](https://www.kaggle.com/datasets/andromedagroup05/data-4-sehat-5-sempurna)

## Results
### Model Performance
Describe all results found in your final project experiments, including hyperparameters tuning and architecture modification performances. Put it into table format. Please show pictures (of model accuracy, loss, etc.) for more clarity.

#### 1. Metrics
Inform your model validation performances, as follows:
- For classification tasks, use **Precision and Recall**.
- For object detection tasks, use **Precision and Recall**. Additionaly, you may also use **Intersection over Union (IoU)**.
- For image retrieval tasks, use **Precision and Recall**.
- For optical character recognition (OCR) tasks, use **Word Error Rate (WER) and Character Error Rate (CER)**.
- For adversarial-based generative tasks, use **Peak Signal-to-Noise Ratio (PNSR)**. Additionally, for specific GAN tasks,
  - For single-image super resolution (SISR) tasks, use **Structural Similarity Index Measure (SSIM)**.
  - For conditional image-to-image translation tasks (e.g., Pix2Pix), use **Inception Score**.

Feel free to adjust the columns in the table below.

| model | epoch | learning_rate | batch_size | optimizer | val_loss | val_precision | val_recall | ... |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vit_b_16 | 110 |  0.0001 | 16 | Adam | 0.093 | 88.34% | 84.15% | ... |
| vit_l_32 | 110 | 0.001 | 16 | Adam | 0.041 | 90.19% | 87.55% | ... |
| ... | ... | ... | 16 | Adam | ... | ... | ... | ... | 

<!-- | model | epoch | learning_rate | batch_size | optimizer | val_loss | val_precision | val_recall | ... |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vit_b_16 | 1000 |  0.0001 | 32 | Adam | 0.093 | 88.34% | 84.15% | ... |
| vit_l_32 | 2500 | 0.00001 | 128 | SGD | 0.041 | 90.19% | 87.55% | ... |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |  -->

#### 2. Ablation Study
Any improvements or modifications of your base model, should be summarized in this table. Feel free to adjust the columns in the table below.

| model | layer_A | layer_B | layer_C | ... | top1_acc | top5_acc |
| --- | --- | --- | --- | --- | --- | --- |
| vit_b_16 | Conv(3x3, 64) x2 | Conv(3x3, 512) x3 | Conv(1x1, 2048) x3 | ... | 77.43% | 80.08% |
| vit_b_16 | Conv(3x3, 32) x3 | Conv(3x3, 128) x3 | Conv(1x1, 1028) x2 | ... | 72.11% | 76.84% |
| ... | ... | ... | ... | ... | ... | ... |

#### 3. Training/Validation Curve
Insert an image regarding your training and evaluation performances (especially their losses). The aim is to assess whether your model is fit, overfit, or underfit.
 
### Testing
Show some implementations (demos) of this model. Show **at least 10 images** of how your model performs on the testing data.

### Deployment (Optional)
Describe and show how you deploy this project (e.g., using Streamlit ), if any.

## Supporting Documents
### Presentation Deck
- Link: https://...

### Business Model Canvas
Provide a screenshot of your Business Model Canvas (BMC). Give some explanations, if necessary.

### Short Video
Provide a link to your short video, that should includes the project background and how it works.
- Link: https://...

## References
Provide all links that support this final project, i.e., papers, GitHub repositories, websites, etc.
- Link: https://...
- Link: https://...
- Link: https://...

## Additional Comments
Provide your team's additional comments or final remarks for this project. For example,
1. ...
2. ...
3. ...

## How to Cite
If you find this project useful, we'd grateful if you cite this repository:
```
@article{
...
}
```

## License
For academic and non-commercial use only.

## Acknowledgement
This project entitled <b>"YOUR PROJECT TITLE HERE"</b> is supported and funded by Startup Campus Indonesia and Indonesian Ministry of Education and Culture through the "**Kampus Merdeka: Magang dan Studi Independen Bersertifikasi (MSIB)**" program.
