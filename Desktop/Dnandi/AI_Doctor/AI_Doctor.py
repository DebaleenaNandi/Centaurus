#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
import json
import os
from datetime import datetime
import pyttsx3

# Initialize speech engine
engine = pyttsx3.init()

# Function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Disease dictionary with treatment information
disease_dict = {
 
    "Acquired Immunodeficiency Syndrome (AIDS)": {
        "description": (
            "Acquired Immunodeficiency Syndrome (AIDS) is a disease caused by the Human Immunodeficiency Virus (HIV). "
            "HIV attacks the body's immune system, weakening it over time. The virus primarily targets CD4 cells, which are crucial for immunity. "
            "As HIV progresses, the body becomes more vulnerable to infections and certain cancers. "
            "HIV is transmitted through blood, semen, vaginal fluids, and breast milk. "
            "Without treatment, HIV can lead to AIDS, the final and most severe stage of HIV infection. "
            "At this stage, the immune system is severely damaged, and the person is at high risk for opportunistic infections. "
            "Common symptoms of AIDS include weight loss, chronic diarrhea, and fatigue. "
            "While there is no cure for AIDS, antiretroviral therapy (ART) can slow the progression of the disease. "
            "ART helps lower the amount of HIV in the blood, allowing people with HIV to live longer and healthier lives."
        ),
        "medicine": "Tenofovir",
        "dose": "300 mg once a day",
        "times_per_day": "Once a day",
        "body_weight": "Dose based on individual case, usually not weight-based",
        "lab_tests": [
            "CD4 count", "HIV RNA test"
        ],
        "side_effects": [
            "Nausea", "Headache", "Diarrhea", "Fatigue", "Liver damage"
        ]
    },
    "Asthma": {
        "description": (
            "Asthma is a chronic disease of the lungs that affects the airways. "
            "It causes inflammation and narrowing of the airways, leading to difficulty breathing. "
            "Common symptoms include wheezing, coughing, shortness of breath, and chest tightness. "
            "Asthma attacks can be triggered by various factors such as allergens, exercise, or respiratory infections. "
            "The severity of asthma symptoms can vary from mild to severe. "
            "Asthma is a lifelong condition, but it can be managed with medication. "
            "Inhalers containing bronchodilators or corticosteroids are commonly used to control symptoms. "
            "Avoiding triggers, such as dust or smoke, is crucial for managing asthma. "
            "While there is no cure for asthma, proper management allows individuals to lead active lives. "
            "Asthma management involves a combination of medication, lifestyle adjustments, and monitoring symptoms."
        ),
        "medicine": "Albuterol",
        "dose": "90 mcg per puff as needed",
        "times_per_day": "As needed for relief",
        "body_weight": "Not typically dose-adjusted based on body weight",
        "lab_tests": [
            "Spirometry", "Peak flow measurement"
        ],
        "side_effects": [
            "Tremors", "Nervousness", "Palpitations", "Headache", "Dizziness"
        ]
    },
    "Diabetes Mellitus Type 1": {
        "description": (
            "Diabetes Mellitus Type 1 is a chronic condition where the pancreas produces little or no insulin. "
            "Insulin is a hormone necessary for converting food into energy. Type 1 diabetes is usually diagnosed in children and young adults. "
            "The exact cause is unknown, but it's believed that the body's immune system mistakenly attacks and destroys the insulin-producing cells. "
            "Symptoms include frequent urination, extreme thirst, hunger, and unexplained weight loss. "
            "Treatment typically involves insulin injections and lifestyle changes."
        ),
        "medicine": "Insulin",
        "dose": "As prescribed based on blood glucose levels",
        "times_per_day": "Multiple times per day",
        "body_weight": "Insulin dosage may be adjusted based on body weight",
        "lab_tests": [
            "Blood glucose test", "HbA1c"
        ],
        "side_effects": [
            "Hypoglycemia (low blood sugar)", "Weight gain", "Injection site reactions"
        ]
    },
    "Diabetes Mellitus Type 2": {
        "description": (
            "Diabetes Mellitus Type 2 is a condition where the body becomes resistant to insulin or doesn't produce enough insulin. "
            "It is the most common form of diabetes and is often associated with obesity, sedentary lifestyle, and poor dietary habits. "
            "Symptoms include increased thirst, frequent urination, and fatigue. It can often be managed with lifestyle changes, oral medications, and sometimes insulin."
        ),
        "medicine": "Metformin",
        "dose": "500 mg once or twice daily",
        "times_per_day": "Once or twice a day",
        "body_weight": "Dose may be adjusted based on body weight",
        "lab_tests": [
            "Blood glucose test", "HbA1c"
        ],
        "side_effects": [
            "Gastrointestinal upset (nausea, diarrhea)", "Lactic acidosis (rare but serious)"
        ]
    },
    "Hypertension": {
        "description": (
            "Hypertension (high blood pressure) is a condition in which the blood pressure in the arteries is persistently elevated. "
            "It is a major risk factor for heart disease, stroke, and kidney damage. "
            "Symptoms can be subtle or absent, so regular monitoring of blood pressure is important for diagnosis. "
            "Lifestyle changes such as reducing salt intake, exercising, and taking antihypertensive medications are common treatments."
        ),
        "medicine": "Lisinopril",
        "dose": "10 mg once a day",
        "times_per_day": "Once a day",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Blood pressure monitoring", "Kidney function tests"
        ],
        "side_effects": [
            "Cough", "Dizziness", "Elevated potassium levels", "Fatigue", "Angioedema (rare but serious)"
        ]
    },
    "Tuberculosis": {
        "description": (
            "Tuberculosis (TB) is a bacterial infection that primarily affects the lungs but can also affect other parts of the body. "
            "It is transmitted through airborne droplets when an infected person coughs or sneezes. "
            "Common symptoms include a persistent cough, weight loss, fever, and night sweats. "
            "Treatment typically involves a course of antibiotics over several months."
        ),
        "medicine": "Isoniazid",
        "dose": "300 mg once a day",
        "times_per_day": "Once a day",
        "body_weight": "Dosage may vary based on individual case",
        "lab_tests": [
            "Chest X-ray", "Tuberculin skin test"
        ],
        "side_effects": [
            "Liver damage", "Peripheral neuropathy", "Rash", "Nausea"
        ]
    },
    "Influenza": {
        "description": (
            "Influenza (flu) is a contagious respiratory illness caused by influenza viruses. "
            "Symptoms include fever, chills, cough, sore throat, body aches, and fatigue. "
            "It spreads through respiratory droplets when an infected person coughs or sneezes. "
            "Vaccination is the most effective prevention, and antiviral medications may be prescribed for treatment."
        ),
        "medicine": "Oseltamivir",
        "dose": "75 mg twice daily for 5 days",
        "times_per_day": "Twice a day",
        "body_weight": "Standard dose for all adults",
        "lab_tests": [
            "Rapid influenza diagnostic test"
        ],
        "side_effects": [
            "Nausea", "Vomiting", "Headache", "Fatigue"
        ]
    },
    "Pneumonia": {
        "description": (
            "Pneumonia is an infection of the lungs caused by bacteria, viruses, or fungi. "
            "Common symptoms include cough, fever, shortness of breath, and chest pain. "
            "It can range from mild to severe, and treatment depends on the underlying cause of the infection."
        ),
        "medicine": "Amoxicillin",
        "dose": "500 mg three times a day",
        "times_per_day": "Three times a day",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Chest X-ray", "Blood cultures"
        ],
        "side_effects": [
            "Nausea", "Diarrhea", "Rash", "Yeast infections"
        ]
    },
    "Malaria": {
        "description": (
            "Malaria is a mosquito-borne infectious disease caused by Plasmodium parasites. "
            "It is transmitted through the bite of an infected female Anopheles mosquito. "
            "Symptoms include fever, chills, and flu-like illness. Malaria is treatable with antimalarial medications."
        ),
        "medicine": "Artemisinin-based combination therapy (ACT)",
        "dose": "As prescribed based on individual case",
        "times_per_day": "Typically once or twice a day for 3-7 days",
        "body_weight": "Dosage is adjusted based on body weight",
        "lab_tests": [
            "Blood smear", "Rapid diagnostic test"
        ],
        "side_effects": [
            "Nausea", "Vomiting", "Dizziness", "Headache"
        ]
    },
    "Cancer (General)": {
        "description": (
            "Cancer is a group of diseases characterized by uncontrolled cell growth. It can occur in any part of the body. "
            "Symptoms vary depending on the type of cancer but may include unexplained weight loss, fatigue, and lumps. "
            "Treatment may involve surgery, radiation therapy, chemotherapy, or immunotherapy."
        ),
        "medicine": "Varies depending on cancer type",
        "dose": "Varies based on cancer treatment plan",
        "times_per_day": "Varies",
        "body_weight": "Dosage may be adjusted based on body weight and type of cancer",
        "lab_tests": [
            "Biopsy", "CT scan", "MRI"
        ],
        "side_effects": [
            "Fatigue", "Nausea", "Hair loss", "Increased risk of infections", "Appetite loss"
        ]
    },
    "Cystic Fibrosis": {
        "description": (
            "Cystic Fibrosis is a genetic disorder that affects the lungs and digestive system. "
            "It leads to the production of thick, sticky mucus that can obstruct the airways, leading to breathing difficulties and lung infections."
        ),
        "medicine": "Ivacaftor",
        "dose": "150 mg twice a day",
        "times_per_day": "Twice a day",
        "body_weight": "Dose may be adjusted based on weight",
        "lab_tests": [
            "Sweat chloride test", "Genetic testing"
        ],
        "side_effects": [
            "Headache", "Sore throat", "Stomach pain", "Diarrhea"
        ]
    },
    "Multiple Sclerosis": {
        "description": (
            "Multiple sclerosis (MS) is a disease where the immune system attacks the protective covering of nerve fibers in the brain and spinal cord. "
            "Symptoms vary but may include fatigue, difficulty walking, numbness, and problems with coordination and vision."
        ),
        "medicine": "Interferon beta",
        "dose": "20 mcg once a week",
        "times_per_day": "Once a week",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "MRI", "Lumbar puncture"
        ],
        "side_effects": [
            "Flu-like symptoms", "Fatigue", "Injection site reactions"
        ]
    },
    "Osteoarthritis": {
        "description": (
            "Osteoarthritis is a degenerative joint disease that occurs when the protective cartilage in joints wears down over time. "
            "Common symptoms include pain, swelling, and stiffness in the affected joints."
        ),
        "medicine": "Acetaminophen",
        "dose": "500 mg every 4-6 hours as needed",
        "times_per_day": "As needed",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "X-ray", "Joint aspiration"
        ],
        "side_effects": [
            "Liver damage (with high doses)", "Stomach upset"
        ]
    },
    "Rheumatoid Arthritis": {
        "description": (
            "Rheumatoid arthritis is an autoimmune disease where the immune system attacks healthy joints, leading to inflammation. "
            "Symptoms include joint pain, swelling, and stiffness. Treatment typically includes disease-modifying antirheumatic drugs (DMARDs)."
        ),
        "medicine": "Methotrexate",
        "dose": "7.5-15 mg once a week",
        "times_per_day": "Once a week",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Rheumatoid factor", "C-reactive protein"
        ],
        "side_effects": [
            "Nausea", "Mouth sores", "Liver damage", "Bone marrow suppression"
        ]
    },

    "Gout": {
        "description": (
            "Gout is a form of arthritis characterized by sudden, severe pain, redness, and swelling in the joints, often starting in the big toe. "
            "It occurs when uric acid builds up in the blood and forms crystals in the joints."
        ),
        "medicine": "Allopurinol",
        "dose": "100-300 mg once a day",
        "times_per_day": "Once a day",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Serum uric acid level"
        ],
        "side_effects": [
            "Rash", "Gastrointestinal upset", "Liver dysfunction"
        ]
    },
    "Hepatitis B": {
        "description": (
            "Hepatitis B is a viral infection that affects the liver, causing inflammation and potential long-term liver damage. "
            "It is transmitted through blood or bodily fluids. "
            "Symptoms may include fatigue, jaundice, and abdominal pain."
        ),
        "medicine": "Tenofovir",
        "dose": "300 mg once a day",
        "times_per_day": "Once a day",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Hepatitis B surface antigen", "Liver function tests"
        ],
        "side_effects": [
            "Nausea", "Headache", "Diarrhea", "Fatigue"
        ]
    },
    "Hepatitis C": {
        "description": (
            "Hepatitis C is a viral infection that affects the liver, causing inflammation and potentially leading to liver cirrhosis or cancer. "
            "It is primarily spread through blood-to-blood contact."
        ),
        "medicine": "Sofosbuvir",
        "dose": "400 mg once a day",
        "times_per_day": "Once a day",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "HCV RNA test", "Liver function tests"
        ],
        "side_effects": [
            "Fatigue", "Headache", "Nausea"
        ]
    },

    "Apnea (Sleep Apnea)": {
        "description": (
            "Sleep apnea is a disorder where breathing repeatedly stops and starts during sleep, leading to daytime fatigue and other health issues."
            " Symptoms include loud snoring, choking, or gasping during sleep."
        ),
        "medicine": "CPAP therapy, Oral appliances, Surgery (e.g., Uvulopalatopharyngoplasty)",
        "dose": "CPAP: Use during sleep",
        "times_per_day": "Once nightly",
        "body_weight": "Not typically adjusted for body weight",
        "lab_tests": [
            "Polysomnography (Sleep study)", "Oximetry"
        ],
        "side_effects": [
            "Dry mouth", "Nasal congestion", "Discomfort from CPAP mask"
        ]
    },
    "Arrhythmia": {
        "description": (
            "Arrhythmia is an abnormal heart rhythm that can cause palpitations, dizziness, or even sudden cardiac arrest."
            " Types include atrial fibrillation, ventricular arrhythmias, and bradycardia."
        ),
        "medicine": "Antiarrhythmic drugs (e.g., Amiodarone, Beta-blockers), Pacemaker, Cardioversion",
        "dose": "Amiodarone: 200-400 mg daily",
        "times_per_day": "Once daily",
        "body_weight": "Not typically adjusted for body weight",
        "lab_tests": [
            "Electrocardiogram (ECG)", "Holter monitoring"
        ],
        "side_effects": [
            "Pulmonary toxicity", "Thyroid issues", "Bradycardia", "Liver damage"
        ]
    },
    "Asbestosis": {
        "description": (
            "Asbestosis is a lung disease caused by prolonged exposure to asbestos fibers, leading to scarring and difficulty breathing."
            " Symptoms include shortness of breath, persistent cough, and chest pain."
        ),
        "medicine": "Oxygen therapy, Pulmonary rehabilitation, Antioxidants",
        "dose": "Oxygen therapy: Adjust flow rate as needed",
        "times_per_day": "As required",
        "body_weight": "Not typically adjusted for body weight",
        "lab_tests": [
            "Chest X-ray", "Pulmonary function tests"
        ],
        "side_effects": [
            "Oxygen toxicity (with excessive use)", "Discomfort from oxygen masks"
        ]
    },

    "Atherosclerosis": {
        "description": (
            "Atherosclerosis is the buildup of plaque in the arteries, leading to reduced blood flow and increased risk of heart disease and stroke."
            " Symptoms may include chest pain or leg cramps."
        ),
        "medicine": "Statins (e.g., Atorvastatin), Antiplatelet drugs (e.g., Aspirin), Blood pressure medication",
        "dose": "Atorvastatin: 10-80 mg daily",
        "times_per_day": "Once daily",
        "body_weight": "Not typically adjusted for body weight",
        "side_effects": [
            "Muscle pain or weakness", "Liver enzyme abnormalities", "Increased risk of bleeding (Aspirin)"
        ],
        "lab_tests": [
            "Cholesterol levels", "Doppler ultrasound of arteries"
        ]
    },
    "Ataxia": {
        "description": (
            "Ataxia refers to a lack of muscle coordination that can affect movement, speech, and balance."
            " It may be caused by neurological disorders, genetic conditions, or other medical issues."
        ),
        "medicine": "Physical therapy, Occupational therapy, Medications (e.g., Baclofen, Anticonvulsants)",
        "dose": "Baclofen: 5-10 mg 3 times daily",
        "times_per_day": "3 times daily",
        "body_weight": "Not typically adjusted for body weight",
        "side_effects": [
            "Drowsiness", "Dizziness", "Weakness"
        ],
        "lab_tests": [
            "MRI of the brain", "Genetic testing"
        ]
    },
    "Atrial Fibrillation": {
        "description": (
            "Atrial fibrillation is a type of arrhythmia where the heart's upper chambers beat irregularly and rapidly, leading to symptoms like palpitations, fatigue, and dizziness."
        ),
        "medicine": "Anticoagulants (e.g., Warfarin), Beta-blockers (e.g., Metoprolol), Rate or rhythm control medications",
        "dose": "Warfarin: 2-5 mg daily, adjust based on INR",
        "times_per_day": "Once daily",
        "body_weight": "Adjusted based on INR",
        "side_effects": [
            "Increased risk of bleeding (Warfarin)", "Fatigue", "Dizziness (Beta-blockers)"
        ],
        "lab_tests": [
            "Electrocardiogram (ECG)", "INR (for Warfarin monitoring)"
        ]
    },
    "Autoimmune Hepatitis": {
        "description": (
            "Autoimmune hepatitis is a liver disease in which the body's immune system attacks liver cells, causing inflammation and potential liver damage."
            " Symptoms include jaundice, fatigue, and abdominal discomfort."
        ),
        "medicine": "Immunosuppressive drugs (e.g., Prednisone, Azathioprine)",
        "dose": "Prednisone: 20-40 mg daily, tapering based on response",
        "times_per_day": "Once daily",
        "body_weight": "Not typically adjusted for body weight",
        "side_effects": [
            "Increased blood sugar", "Osteoporosis", "Weight gain"
        ],
        "lab_tests": [
            "Liver function tests", "Liver biopsy"
        ]
    },
    "Autoimmune Vasculitis": {
        "description": (
            "Autoimmune vasculitis is a group of disorders where the immune system attacks blood vessels, causing inflammation and damage."
            " Symptoms vary depending on the affected vessels but may include fever, fatigue, and skin rashes."
        ),
        "medicine": "Immunosuppressive drugs (e.g., Cyclophosphamide, Prednisone)",
        "dose": "Cyclophosphamide: 1-2 mg/kg daily",
        "times_per_day": "Once daily",
        "body_weight": "Adjusted for body weight",
        "side_effects": [
            "Increased risk of infection", "Hair loss", "Nausea"
        ],
        "lab_tests": [
            "Blood tests (e.g., ANCA, CRP)", "Biopsy of affected tissue"
        ]
    },
    "Babesiosis": {
        "description": (
            "Babesiosis is a malaria-like parasitic infection transmitted by ticks, leading to symptoms like fever, chills, and anemia."
            " It can cause severe illness in immunocompromised individuals."
        ),
        "medicine": "Antiprotozoal drugs (e.g., Atovaquone, Azithromycin)",
        "dose": "Atovaquone: 750 mg every 8 hours for 7-10 days",
        "times_per_day": "3 times daily",
        "body_weight": "Not typically adjusted for body weight",
        "side_effects": [
            "Nausea", "Diarrhea", "Headache"
        ],
        "lab_tests": [
            "Blood smear", "PCR testing for Babesia"
        ]
    },
    "Bacterial Vaginosis": {
        "description": (
            "Bacterial vaginosis is an infection caused by an imbalance in the normal bacteria in the vagina."
            " Symptoms include abnormal vaginal discharge, fishy odor, and itching."
        ),
        "medicine": "Antibiotics (e.g., Metronidazole, Clindamycin)",
        "dose": "Metronidazole: 500 mg twice daily for 7 days",
        "times_per_day": "Twice daily",
        "body_weight": "Not typically adjusted for body weight",
        "side_effects": [
            "Nausea", "Metallic taste", "Vaginal irritation (if used topically)"
        ],
        "lab_tests": [
            "Vaginal swab for culture", "Microscopic examination"
        ]
    },
    "Basal Cell Carcinoma": {
        "description": (
            "Basal cell carcinoma is a type of skin cancer that typically appears as a small, raised bump on the skin, often in areas exposed to sunlight."
            " It is usually slow-growing and rarely spreads to other parts of the body."
        ),
        "medicine": "Surgical excision, Mohs micrographic surgery, Topical treatments (e.g., Imiquimod)",
        "dose": "Imiquimod: Apply once daily for 5 days a week",
        "times_per_day": "Once daily",
        "body_weight": "Not typically adjusted for body weight",
        "side_effects": [
            "Skin irritation", "Redness", "Itching"
        ],
        "lab_tests": [
            "Skin biopsy", "Dermatoscopy"
        ]
    },
    "Biliary Cirrhosis": {
        "description": (
            "Biliary cirrhosis is a liver disease caused by damage to the bile ducts, leading to a buildup of bile and liver damage."
            " Symptoms include fatigue, jaundice, and abdominal pain."
        ),
        "medicine": "Ursodeoxycholic acid, Immunosuppressive drugs (e.g., Prednisone)",
        "dose": "Ursodeoxycholic acid: 10-15 mg/kg daily",
        "times_per_day": "Once or twice daily",
        "body_weight": "Adjusted for body weight",
        "side_effects": [
            "Diarrhea", "Constipation", "Abdominal discomfort"
        ],
        "lab_tests": [
            "Liver function tests", "Liver biopsy"
        ]
    },
    "Binge Eating Disorder": {
        "description": (
            "Binge eating disorder involves episodes of eating large amounts of food in a short time, accompanied by feelings of loss of control."
            " Symptoms include eating rapidly, feeling uncomfortably full, and distress about eating behavior."
        ),
        "medicine": "Cognitive-behavioral therapy (CBT), Medications (e.g., Lisdexamfetamine, Antidepressants)",
        "dose": "Lisdexamfetamine: 30-70 mg once daily",
        "times_per_day": "Once daily",
        "body_weight": "Not typically adjusted for body weight",
        "side_effects": [
            "Loss of appetite", "Insomnia", "Increased heart rate"
        ],
        "lab_tests": [
            "Psychological evaluation", "Blood tests to rule out other conditions"
        ]
    },

    "Bipolar Affective Disorder": {
        "description": "Bipolar disorder is a mental health condition characterized by extreme mood swings, including manic episodes and depressive episodes. Symptoms include extreme highs (mania) and lows (depression).",
        "medicine": "Mood stabilizers (e.g., Lithium), Antipsychotics (e.g., Quetiapine), Antidepressants",
        "dose": "Lithium: 600-1200 mg daily",
        "times_per_day": "2-3 times daily",
        "body_weight": "Not typically adjusted for body weight",
        "lab_tests": [
            "Lithium blood levels", "Psychiatric evaluation"
        ],
        "side_effects": "Tremor, weight gain, hypothyroidism, kidney damage, gastrointestinal discomfort"
    },
    "Celiac Disease": {
        "description": "Celiac disease is an autoimmune disorder where the ingestion of gluten triggers immune system activity that damages the lining of the small intestine. This results in malabsorption of nutrients and various gastrointestinal and systemic symptoms. Symptoms can include diarrhea, abdominal pain, bloating, and fatigue. The only treatment is a strict gluten-free diet.",
        "medicine": "None (Gluten-free diet)",
        "dose": "N/A",
        "times_per_day": "N/A",
        "body_weight": "N/A",
        "lab_tests": [
            "Serology for tissue transglutaminase antibodies (tTG-IgA)", "Small bowel biopsy"
        ],
        "side_effects": "N/A (strict diet management, no medication)"
    },
    "Cervical Cancer": {
        "description": "Cervical cancer is a malignant tumor of the cervix, often caused by persistent infection with high-risk strains of the human papillomavirus (HPV). Early stages may have no symptoms, but advanced stages can cause abnormal bleeding, pain, or discharge. Vaccination and regular Pap smears can help prevent and detect cervical cancer early.",
        "medicine": "Cisplatin (chemotherapy)",
        "dose": "50 mg/m² IV once every 3 weeks",
        "times_per_day": "Once every 3 weeks",
        "body_weight": "Adjusted based on body surface area",
        "lab_tests": [
            "Pap smear", "HPV testing", "Biopsy"
        ],
        "side_effects": "Nausea, vomiting, kidney toxicity, hair loss, low blood cell counts"
    },
    "Chickenpox (Varicella)": {
        "description": "Chickenpox is a highly contagious viral infection caused by the varicella-zoster virus. It is characterized by itchy, red rashes and flu-like symptoms. The infection is usually mild in children but can be more severe in adults. Vaccination has significantly reduced its incidence.",
        "medicine": "Acyclovir (for severe cases)",
        "dose": "800 mg 5 times daily for 7 days",
        "times_per_day": "Five times a day",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Polymerase chain reaction (PCR) for varicella-zoster virus"
        ],
        "side_effects": "Nausea, vomiting, headache, dizziness, kidney dysfunction (rare)"
    },
    "Chlamydia": {
        "description": "Chlamydia is a sexually transmitted infection caused by the bacterium *Chlamydia trachomatis*. It often presents with mild or no symptoms but can lead to serious reproductive issues if left untreated.",
        "medicine": "Azithromycin",
        "dose": "1 g orally as a single dose",
        "times_per_day": "Once",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Urine test", "Swab culture"
        ],
        "side_effects": "Nausea, vomiting, diarrhea, abdominal pain, liver toxicity (rare)"
    },
    "Chronic Fatigue Syndrome": {
        "description": "Chronic fatigue syndrome (CFS) is a complex disorder characterized by persistent, unexplained fatigue that is not alleviated by rest. Symptoms also include cognitive impairment, sleep disturbances, and muscle pain.",
        "medicine": "Antidepressants (e.g., Duloxetine), Pain relievers (e.g., Ibuprofen)",
        "dose": "Duloxetine: 30-60 mg daily",
        "times_per_day": "Once a day",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Rule out other conditions", "Psychological assessment"
        ],
        "side_effects": "Nausea, dizziness, dry mouth, insomnia, increased blood pressure"
    },
    "Chronic Kidney Disease": {
        "description": "Chronic kidney disease (CKD) is the gradual loss of kidney function over time, often due to diabetes or hypertension. Symptoms may not appear until the disease is advanced, at which point individuals may experience fluid retention, fatigue, and nausea.",
        "medicine": "ACE inhibitors (e.g., Lisinopril), Diuretics",
        "dose": "Lisinopril: 10-40 mg daily",
        "times_per_day": "Once a day",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Serum creatinine", "Glomerular filtration rate (GFR)"
        ],
        "side_effects": "Cough, elevated potassium levels, low blood pressure, dizziness, fatigue"
    },
    "Chronic Obstructive Pulmonary Disease (COPD)": {
        "description": "COPD is a progressive lung disease that causes breathing difficulty, typically due to long-term exposure to irritants like cigarette smoke. It includes emphysema and chronic bronchitis, leading to symptoms like shortness of breath, chronic cough, and wheezing.",
        "medicine": "Salbutamol (for shortness of breath), Inhaled corticosteroids",
        "dose": "Salbutamol: 100-200 mcg as needed",
        "times_per_day": "As needed",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Spirometry", "Chest X-ray"
        ],
        "side_effects": "Tremors, tachycardia, headache, nervousness, throat irritation"
    },
    "Cirrhosis": {
        "description": "Cirrhosis is scarring of the liver caused by long-term liver damage, often due to chronic alcohol use or viral hepatitis. It can lead to liver failure, portal hypertension, and liver cancer.",
        "medicine": "Lactulose (for hepatic encephalopathy), Diuretics",
        "dose": "Lactulose: 30-45 mL orally 3 times a day",
        "times_per_day": "Three times a day",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Liver function tests", "Ultrasound"
        ],
        "side_effects": "Diarrhea, bloating, abdominal cramps, electrolyte imbalances"
    },
    "Cleft Lip and Palate": {
        "description": "Cleft lip and palate are congenital conditions where there are openings or gaps in the upper lip and/or the roof of the mouth (palate). These gaps occur during early fetal development and can cause feeding, speech, and hearing issues.",
        "medicine": "Surgical intervention (cleft repair surgery)",
        "dose": "N/A",
        "times_per_day": "N/A",
        "body_weight": "N/A",
        "lab_tests": [
            "Prenatal ultrasound", "Genetic testing"
        ],
        "side_effects": "N/A (post-surgical complications may include infection, swelling, or bleeding)"
    },
    "Clostridium Difficile Infection": {
        "description": "Clostridium difficile infection (C. difficile) is a bacterial infection that causes severe diarrhea, often after antibiotic use. It can lead to colitis and other complications if not treated.",
        "medicine": "Vancomycin",
        "dose": "125 mg orally 4 times a day for 10 days",
        "times_per_day": "Four times a day",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Stool culture", "PCR for C. difficile"
        ],
        "side_effects": "Nausea, abdominal pain, taste disturbances, diarrhea"
    },
    "Colorectal Cancer": {
        "description": "Colorectal cancer is cancer of the colon or rectum, often starting as polyps that may turn cancerous over time. Symptoms include changes in bowel habits, blood in the stool, and unexplained weight loss.",
        "medicine": "5-Fluorouracil (chemotherapy)",
        "dose": "400 mg/m² IV bolus on day 1, followed by 600 mg/m² continuous infusion for 46 hours",
        "times_per_day": "Once every 2 weeks",
        "body_weight": "Adjusted based on body surface area",
        "lab_tests": [
            "Colonoscopy", "CT scan"
        ],
        "side_effects": "Nausea, vomiting, diarrhea, low blood cell counts, mouth sores"
    },

    "Common Cold": {
        "description": "The common cold is a viral upper respiratory infection that can cause symptoms such as a runny nose, sore throat, and cough. It is caused by many different viruses, primarily rhinoviruses.",
        "medicine": "Decongestants (e.g., Pseudoephedrine), Pain relievers (e.g., Acetaminophen)",
        "dose": "Pseudoephedrine: 30-60 mg every 4-6 hours",
        "times_per_day": "As needed",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Clinical diagnosis", "Nasal swab for virus culture"
        ],
        "side_effects": "Increased heart rate, nervousness, dizziness, headache, stomach upset"
    },
    "Congestive Heart Failure": {
        "description": "Congestive heart failure occurs when the heart is unable to pump blood effectively, leading to fluid buildup in the lungs and other parts of the body. Symptoms include shortness of breath, edema, and fatigue.",
        "medicine": "Furosemide (diuretic), ACE inhibitors",
        "dose": "Furosemide: 20-80 mg orally once a day",
        "times_per_day": "Once a day",
        "body_weight": "Adjusted based on response",
        "lab_tests": [
            "Echocardiogram", "B-type natriuretic peptide (BNP)"
        ],
        "side_effects": "Dehydration, low blood pressure, dizziness, electrolyte imbalances, kidney dysfunction"
    },
    "Coronary Artery Disease": {
        "description": "Coronary artery disease (CAD) is caused by the buildup of plaque in the coronary arteries, leading to reduced blood flow to the heart. It can result in chest pain (angina) or heart attacks.",
        "medicine": "Aspirin, Statins (e.g., Atorvastatin)",
        "dose": "Atorvastatin: 10-80 mg daily",
        "times_per_day": "Once daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Stress test", "Coronary angiography"
        ],
        "side_effects": "Muscle pain, liver enzyme changes, digestive upset, headache"
    },
    "Crohn’s Disease": {
        "description": "Crohn’s disease is an inflammatory bowel disease that causes chronic inflammation in the gastrointestinal tract. Symptoms include abdominal pain, diarrhea, and weight loss. It can affect any part of the digestive tract.",
        "medicine": "Infliximab (biologic therapy), Steroids",
        "dose": "Infliximab: 5 mg/kg IV every 8 weeks after initial doses",
        "times_per_day": "Every 8 weeks",
        "body_weight": "Dosed based on body weight",
        "lab_tests": [
            "Colonoscopy", "C-reactive protein (CRP)"
        ],
        "side_effects": "Infusion reactions, headache, abdominal pain, fatigue, increased risk of infection"
    },
    "Cystic Fibrosis": {
        "description": "Cystic fibrosis is a genetic disorder that affects the lungs and digestive system, causing thick mucus buildup. Symptoms include chronic lung infections, digestive problems, and difficulty gaining weight.",
        "medicine": "Dornase alfa (for lungs), Pancreatic enzyme replacement",
        "dose": "Dornase alfa: 2.5 mg inhaled daily",
        "times_per_day": "Once a day",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Sweat chloride test", "Chest X-ray"
        ],
        "side_effects": "Voice alteration, throat irritation, cough, shortness of breath"
    },
    "Diphtheria": {
        "description": "Diphtheria is a bacterial infection caused by *Corynebacterium diphtheriae* that affects the mucous membranes of the throat and nose. Symptoms include a sore throat, fever, and a thick grey membrane covering the throat, which can lead to difficulty breathing.",
        "medicine": "Antitoxin, Erythromycin",
        "dose": "Erythromycin: 500 mg every 6 hours for 14 days",
        "times_per_day": "Four times a day",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Throat culture", "PCR for *Corynebacterium diphtheriae*"
        ],
        "side_effects": "Nausea, vomiting, diarrhea, abdominal pain"
    },
    "Diverticulitis": {
        "description": "Diverticulitis is the inflammation or infection of small pouches (diverticula) that can form in the walls of the colon. It causes symptoms like lower abdominal pain, fever, and changes in bowel movements.",
        "medicine": "Ciprofloxacin (for infections), Metronidazole",
        "dose": "Ciprofloxacin: 500 mg twice daily for 7-10 days",
        "times_per_day": "Twice a day",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "CT scan", "Complete blood count (CBC)"
        ],
        "side_effects": "Nausea, diarrhea, dizziness, headache, tendonitis"
    },
    "Down Syndrome": {
        "description": "Down syndrome is a genetic condition caused by the presence of an extra chromosome 21. It leads to developmental delays, intellectual disabilities, and may be associated with various health issues.",
        "medicine": "None (Management of symptoms and conditions)",
        "dose": "N/A",
        "times_per_day": "N/A",
        "body_weight": "N/A",
        "lab_tests": [
            "Karyotyping", "Ultrasound (during pregnancy)"
        ],
        "side_effects": "N/A"
    },
    "Eczema (Atopic Dermatitis)": {
        "description": "Eczema, also known as atopic dermatitis, is a chronic inflammatory skin condition characterized by dry, itchy, and red patches of skin. It is often triggered by allergens, irritants, or stress.",
        "medicine": "Topical corticosteroids (e.g., Hydrocortisone), Antihistamines (e.g., Cetirizine)",
        "dose": "Hydrocortisone: Apply to affected areas 1-2 times daily",
        "times_per_day": "Once or twice a day",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Skin biopsy", "Patch test for allergens"
        ],
        "side_effects": "Skin thinning, irritation, delayed wound healing, dry skin"
    },
    "Emphysema": {
        "description": "Emphysema is a type of chronic obstructive pulmonary disease (COPD) where the alveoli in the lungs are damaged, making it difficult to breathe. It is typically caused by long-term exposure to irritants like cigarette smoke.",
        "medicine": "Bronchodilators (e.g., Salmeterol), Inhaled corticosteroids",
        "dose": "Salmeterol: 50 mcg twice daily",
        "times_per_day": "Twice a day",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Spirometry", "Chest X-ray"
        ],
        "side_effects": "Tremors, tachycardia, headache, nervousness, throat irritation"
    },

"Epilepsy": {
    "description": (
        "Epilepsy is a neurological disorder characterized by recurrent, unprovoked seizures. "
        "Seizures can vary in type and severity, ranging from brief lapses in attention to full convulsions."
    ),
    "medicine": "Levetiracetam, Valproic acid",
    "dose": "Levetiracetam: 500-1500 mg daily",
    "side_effects": "Dizziness, fatigue, irritability, headache",
    "times_per_day": "Once or twice a day",
    "body_weight": "Not typically adjusted based on body weight",
    "lab_tests": [
        "EEG (electroencephalogram)", "MRI of the brain"
    ]
},
"Esophageal Cancer": {
    "description": (
        "Esophageal cancer is cancer that begins in the cells of the esophagus. Risk factors include smoking, alcohol consumption, and acid reflux disease. "
        "Symptoms may include difficulty swallowing, weight loss, and chest pain."
    ),
    "medicine": "Cisplatin, 5-Fluorouracil (chemotherapy)",
    "dose": "Cisplatin: 75 mg/m² IV every 3 weeks",
    "side_effects": "Nausea, vomiting, hair loss, kidney toxicity",
    "times_per_day": "Once every 3 weeks",
    "body_weight": "Adjusted based on body surface area",
    "lab_tests": [
        "Endoscopy", "Biopsy"
    ]
},
"Gallbladder Disease": {
    "description": (
        "Gallbladder disease refers to a range of conditions affecting the gallbladder, including gallstones, inflammation, and infection. "
        "It typically causes pain in the upper right abdomen, nausea, and indigestion."
    ),
    "medicine": "Ursodiol (for gallstones), Analgesics",
    "dose": "Ursodiol: 300 mg twice daily",
    "side_effects": "Diarrhea, nausea, headache, dizziness",
    "times_per_day": "Twice a day",
    "body_weight": "Not typically adjusted based on body weight",
    "lab_tests": [
        "Ultrasound of the abdomen", "Liver function tests"
    ]
},
"Gallstones": {
    "description": (
        "Gallstones are hardened deposits of bile that form in the gallbladder. They can block bile ducts, causing pain, nausea, and vomiting."
    ),
    "medicine": "Ursodiol, Surgery (cholecystectomy)",
    "dose": "Ursodiol: 300 mg twice daily",
    "side_effects": "Diarrhea, nausea, headache, dizziness",
    "times_per_day": "Twice a day",
    "body_weight": "Not typically adjusted based on body weight",
    "lab_tests": [
        "Ultrasound of the abdomen", "HIDA scan"
    ]
},
"Gout": {
    "description": (
        "Gout is a form of arthritis caused by an excess of uric acid in the blood, leading to the formation of crystals in joints. "
        "It causes intense pain, redness, and swelling, typically affecting the big toe."
    ),
    "medicine": "Allopurinol, Colchicine",
    "dose": "Allopurinol: 100-300 mg daily",
    "side_effects": "Rash, gastrointestinal discomfort, liver dysfunction",
    "times_per_day": "Once a day",
    "body_weight": "Not typically adjusted based on body weight",
    "lab_tests": [
        "Serum uric acid levels", "Joint fluid analysis"
    ]
},
"Guillain-Barré Syndrome": {
    "description": (
        "Guillain-Barré syndrome is a rare neurological disorder where the body's immune system attacks the peripheral nervous system. "
        "It can cause weakness, numbness, and paralysis, often starting in the legs."
    ),
    "medicine": "Intravenous immunoglobulin (IVIG), Plasma exchange",
    "dose": "IVIG: 0.4 g/kg daily for 5 days",
    "side_effects": "Headache, fever, chills, nausea, thrombosis",
    "times_per_day": "Once daily for 5 days",
    "body_weight": "Dosed based on weight",
    "lab_tests": [
        "Nerve conduction studies", "CSF analysis"
    ]
},
"Haemophilia": {
    "description": (
        "Haemophilia is a genetic disorder in which blood doesn't clot properly due to a deficiency in clotting factors. "
        "It leads to excessive bleeding and bruising."
    ),
    "medicine": "Factor VIII (for haemophilia A), Factor IX (for haemophilia B)",
    "dose": "Factor VIII: 25-40 IU/kg every 48 hours",
    "side_effects": "Allergic reactions, fever, headache, joint pain",
    "times_per_day": "As needed",
    "body_weight": "Dosed based on body weight",
    "lab_tests": [
        "Clotting factor levels", "PTT (Partial Thromboplastin Time)"
    ]
},
"Hay Fever (Allergic Rhinitis)": {
    "description": (
        "Hay fever is an allergic reaction to airborne allergens, such as pollen, that causes sneezing, runny nose, and itchy eyes. "
        "It often occurs seasonally."
    ),
    "medicine": "Antihistamines (e.g., Loratadine), Nasal corticosteroids",
    "dose": "Loratadine: 10 mg once daily",
    "side_effects": "Dry mouth, dizziness, headache, drowsiness",
    "times_per_day": "Once daily",
    "body_weight": "Not typically adjusted based on body weight",
    "lab_tests": [
        "Skin prick test", "Blood test for specific IgE antibodies"
    ]
},
"Headache (Migraine, Tension-Type)": {
    "description": (
        "Headaches can be caused by various factors, including tension, stress, or vascular issues. Migraines are often characterized by severe, throbbing pain, nausea, and light sensitivity."
    ),
    "medicine": "Triptans (e.g., Sumatriptan for migraines), NSAIDs (e.g., Ibuprofen for tension-type)",
    "dose": "Sumatriptan: 25-100 mg at onset of migraine",
    "side_effects": "Dizziness, nausea, drowsiness, chest tightness",
    "times_per_day": "As needed",
    "body_weight": "Not typically adjusted based on body weight",
    "lab_tests": [
        "Clinical diagnosis", "MRI (if persistent)"
    ]
},
"Heart Attack (Myocardial Infarction)": {
    "description": (
        "A heart attack occurs when blood flow to part of the heart is blocked, leading to damage to the heart muscle. "
        "Common symptoms include chest pain, shortness of breath, and sweating."
    ),
    "medicine": "Aspirin, Thrombolytics (e.g., Streptokinase)",
    "dose": "Aspirin: 325 mg once daily",
    "side_effects": "Gastrointestinal bleeding, upset stomach, allergic reactions",
    "times_per_day": "Once daily",
    "body_weight": "Not typically adjusted based on body weight",
    "lab_tests": [
        "ECG (Electrocardiogram)", "Cardiac enzyme levels"
    ]
},
"Heart Disease": {
    "description": (
        "Heart disease refers to various conditions that affect the heart, including coronary artery disease, heart failure, and arrhythmias. "
        "Symptoms can include chest pain, shortness of breath, and fatigue."
    ),
    "medicine": "ACE inhibitors, Beta-blockers",
    "dose": "Lisinopril: 10-40 mg daily",
    "side_effects": "Cough, dizziness, hyperkalemia, fatigue",
    "times_per_day": "Once a day",
    "body_weight": "Not typically adjusted based on body weight",
    "lab_tests": [
        "Echocardiogram", "Electrocardiogram (ECG)"
    ]
},
"Hepatitis A": {
    "description": (
        "Hepatitis A is a viral infection of the liver caused by the Hepatitis A virus, typically spread through contaminated food or water. "
        "Symptoms include jaundice, fatigue, and abdominal pain."
    ),
    "medicine": "None (supportive care)",
    "dose": "N/A",
    "side_effects": "N/A",
    "times_per_day": "N/A",
    "body_weight": "N/A",
    "lab_tests": [
        "Liver function tests", "Hepatitis A IgM antibodies"
    ]
},
"Hepatitis B": {
    "description": (
        "Hepatitis B is a viral infection that attacks the liver and can lead to chronic disease. It is transmitted through blood, semen, or bodily fluids. "
        "Symptoms include jaundice, fatigue, and abdominal pain."
    ),
    "medicine": "Tenofovir, Entecavir",
    "dose": "Tenofovir: 300 mg once daily",
    "side_effects": "Fatigue, headache, gastrointestinal discomfort, renal impairment",
    "times_per_day": "Once daily",
    "body_weight": "Not typically adjusted based on body weight",
    "lab_tests": [
        "Hepatitis B surface antigen", "Liver function tests"
    ]
},
"Hepatitis C": {
    "description": (
        "Hepatitis C is a viral infection that affects the liver and is primarily transmitted through blood-to-blood contact. "
        "It can lead to chronic liver disease, cirrhosis, and liver cancer."
    ),
    "medicine": "Sofosbuvir/Velpatasvir (combination therapy)",
    "dose": "Sofosbuvir/Velpatasvir: 400 mg/100 mg once daily for 12 weeks",
    "side_effects": "Fatigue, headache, nausea, liver enzyme elevations",
    "times_per_day": "Once daily",
    "body_weight": "Not typically adjusted based on body weight",
    "lab_tests": [
        "HCV RNA test", "Liver biopsy"
    ]
},
"Herpes Simplex Virus (HSV)": {
    "description": (
        "Herpes simplex virus (HSV) is a common virus that causes painful blisters or sores, often around the mouth (HSV-1) or genital region (HSV-2)."
    ),
    "medicine": "Acyclovir, Valacyclovir",
    "dose": "Acyclovir: 200 mg 5 times a day for 5 days",
    "side_effects": "Nausea, diarrhea, headache, kidney dysfunction",
    "times_per_day": "Five times a day",
    "body_weight": "Not typically adjusted based on body weight",
    "lab_tests": [
        "Viral culture", "PCR for HSV"
    ]
},

"High Blood Pressure (Hypertension)": {
    "description": (
        "Hypertension is a condition in which the blood pressure in the arteries is consistently high. "
        "It increases the risk of heart disease, stroke, and kidney failure. Common symptoms are often absent, but it can cause headaches and dizziness."
    ),
    "medicine": "ACE inhibitors (e.g., Lisinopril), Calcium channel blockers (e.g., Amlodipine)",
    "dose": "Lisinopril: 10-40 mg once daily",
    "side_effects": "Cough, dizziness, hyperkalemia, fatigue",
    "times_per_day": "Once daily",
    "body_weight": "Not typically adjusted based on body weight",
    "lab_tests": [
        "Blood pressure monitoring", "Kidney function tests (e.g., serum creatinine)"
    ]
},
"Hodgkin's Lymphoma": {
    "description": (
        "Hodgkin's lymphoma is a type of cancer that starts in the lymphatic system, often presenting with swollen lymph nodes, fever, and weight loss. "
        "It is characterized by the presence of Reed-Sternberg cells."
    ),
    "medicine": "Chemotherapy (e.g., ABVD regimen), Radiation therapy",
    "dose": "Doxorubicin (Adriamycin): 25 mg/m² IV every 14 days",
    "side_effects": "Hair loss, nausea, vomiting, heart toxicity, immunosuppression",
    "times_per_day": "Once every 14 days",
    "body_weight": "Dosed based on body surface area",
    "lab_tests": [
        "CT scan", "Biopsy of lymph node"
    ]
},
"Huntington’s Disease": {
    "description": (
        "Huntington’s disease is a genetic neurodegenerative disorder that causes the progressive breakdown of nerve cells in the brain. "
        "It leads to movement abnormalities, cognitive decline, and psychiatric issues."
    ),
    "medicine": "Tetrabenazine (for movement symptoms), Antidepressants (for mood changes)",
    "dose": "Tetrabenazine: 12.5 mg twice daily",
    "side_effects": "Drowsiness, depression, akathisia, Parkinsonism",
    "times_per_day": "Twice a day",
    "body_weight": "Not typically adjusted based on body weight",
    "lab_tests": [
        "Genetic testing for HTT gene mutation", "MRI of the brain"
    ]
},
"Hyperthyroidism": {
    "description": (
        "Hyperthyroidism occurs when the thyroid gland produces too much thyroid hormone, leading to symptoms like weight loss, rapid heartbeat, and heat intolerance."
    ),
    "medicine": "Methimazole, Beta-blockers (e.g., Propranolol for symptoms)",
    "dose": "Methimazole: 15-30 mg daily",
    "side_effects": "Rash, joint pain, liver dysfunction, agranulocytosis",
    "times_per_day": "Once daily",
    "body_weight": "Not typically adjusted based on body weight",
    "lab_tests": [
        "TSH (Thyroid-stimulating hormone)", "Free T4"
    ]
},
"Hypothyroidism": {
    "description": (
        "Hypothyroidism is a condition where the thyroid gland does not produce enough thyroid hormone, leading to symptoms like fatigue, weight gain, and depression."
    ),
    "medicine": "Levothyroxine",
    "dose": "Levothyroxine: 25-300 mcg daily",
    "side_effects": "Palpitations, anxiety, weight loss, heat intolerance",
    "times_per_day": "Once daily",
    "body_weight": "Dosed based on body weight",
    "lab_tests": [
        "TSH", "Free T4"
    ]
},
"Impetigo": {
    "description": (
        "Impetigo is a highly contagious skin infection caused by *Streptococcus* or *Staphylococcus* bacteria, characterized by red sores and crusted blisters."
    ),
    "medicine": "Topical mupirocin or oral antibiotics (e.g., Cephalexin)",
    "dose": "Mupirocin: Apply 3 times a day for 5-7 days",
    "side_effects": "Burning, itching, dryness at application site",
    "times_per_day": "Three times a day",
    "body_weight": "Not typically adjusted based on body weight",
    "lab_tests": [
        "Skin swab culture", "Blood culture (if severe)"
    ]
},
"Influenza (Flu)": {
    "description": (
        "Influenza is a viral infection that affects the respiratory system, with symptoms such as fever, chills, cough, sore throat, and body aches."
    ),
    "medicine": "Oseltamivir (Tamiflu), Supportive care",
    "dose": "Oseltamivir: 75 mg twice daily for 5 days",
    "side_effects": "Nausea, vomiting, headache, dizziness",
    "times_per_day": "Twice daily",
    "body_weight": "Not typically adjusted based on body weight",
    "lab_tests": [
        "Rapid influenza diagnostic test (RIDT)", "PCR for influenza"
    ]
},
"Irritable Bowel Syndrome (IBS)": {
    "description": (
        "IBS is a chronic gastrointestinal disorder that causes symptoms like abdominal pain, bloating, and altered bowel movements (diarrhea or constipation)."
    ),
    "medicine": "Loperamide (for diarrhea), Fiber supplements (for constipation)",
    "dose": "Loperamide: 2 mg after each loose stool, up to 8 mg/day",
    "side_effects": "Constipation, bloating, abdominal discomfort",
    "times_per_day": "As needed",
    "body_weight": "Not typically adjusted based on body weight",
    "lab_tests": [
        "Stool tests (to rule out infections)", "Colonoscopy (if symptoms persist)"
    ]
},
"Ischemic Stroke": {
    "description": (
        "An ischemic stroke occurs when a blood clot blocks or narrows an artery leading to the brain, causing brain tissue damage. Symptoms include sudden numbness, confusion, or difficulty speaking."
    ),
    "medicine": "Aspirin, Thrombolytics (e.g., tPA if within a 3-4.5 hour window)",
    "dose": "Aspirin: 81 mg daily",
    "side_effects": "Gastrointestinal bleeding, upset stomach",
    "times_per_day": "Once daily",
    "body_weight": "Not typically adjusted based on body weight",
    "lab_tests": [
        "CT scan of the brain", "Blood tests for coagulation profile"
    ]
},
"Kawasaki Disease": {
    "description": (
        "Kawasaki disease is a rare childhood condition that causes inflammation in blood vessels, often affecting the coronary arteries. It leads to fever, rash, and swelling of hands and feet."
    ),
    "medicine": "Intravenous immunoglobulin (IVIG), Aspirin",
    "dose": "IVIG: 2 g/kg single infusion",
    "side_effects": "Fever, chills, headache, rash",
    "times_per_day": "Single infusion",
    "body_weight": "Dosed based on weight",
    "lab_tests": [
        "Echocardiogram", "CBC (Complete Blood Count)"
    ]
},
"Kidney Stones": {
    "description": (
        "Kidney stones are hard deposits of minerals and salts that form in the kidneys. They can cause severe pain, especially when passing through the urinary tract."
    ),
    "medicine": "Pain relievers (e.g., Ibuprofen), Alpha-blockers (e.g., Tamsulosin)",
    "dose": "Ibuprofen: 400-600 mg every 6-8 hours as needed for pain",
    "side_effects": "Gastrointestinal upset, renal impairment (with prolonged use)",
    "times_per_day": "As needed",
    "body_weight": "Not typically adjusted based on body weight",
    "lab_tests": [
        "CT scan of the abdomen", "Urinalysis"
    ]
},
"Klinefelter Syndrome": {
    "description": (
        "Klinefelter syndrome is a genetic condition in males caused by an extra X chromosome, leading to symptoms such as infertility, reduced testosterone, and learning disabilities."
    ),
    "medicine": "Testosterone replacement therapy",
    "dose": "Testosterone enanthate: 50-100 mg every 2-4 weeks",
    "side_effects": "Acne, mood changes, increased red blood cell count, gynecomastia",
    "times_per_day": "Once every 2-4 weeks",
    "body_weight": "Not typically adjusted based on body weight",
    "lab_tests": [
        "Karyotype analysis", "Serum testosterone levels"
    ]
},
"Laryngitis": {
    "description": (
        "Laryngitis is the inflammation of the larynx (voice box), usually caused by viral infections or overuse of the voice. It causes hoarseness or loss of voice."
    ),
    "medicine": "Rest for the voice, Hydration, Corticosteroids (if severe)",
    "dose": "Corticosteroids: Prednisone 20 mg daily for 5 days (if needed)",
    "side_effects": "Increased blood sugar, gastrointestinal irritation, insomnia",
    "times_per_day": "Once daily (if corticosteroids are prescribed)",
    "body_weight": "Not typically adjusted based on body weight",
    "lab_tests": [
        "Laryngoscopy", "Throat culture (if bacterial etiology is suspected)"
    ]
},

"Leukemia (Acute and Chronic)": {
    "description": (
        "Leukemia is a type of cancer that affects blood and bone marrow. It leads to the overproduction of abnormal white blood cells, which can interfere with normal blood function."
    ),
    "medicine": "Chemotherapy, Bone marrow transplant",
    "dose": "Cytarabine: 100-200 mg/m² IV daily for 7 days",
    "side_effects": "Nausea, vomiting, hair loss, myelosuppression, risk of infections",
    "times_per_day": "Once or twice daily (depending on chemotherapy regimen)",
    "body_weight": "Dosed based on body surface area",
    "lab_tests": [
        "Complete blood count (CBC)", "Bone marrow biopsy"
    ]
},
"Liver Cancer": {
    "description": (
        "Liver cancer, or hepatocellular carcinoma, is a type of cancer that originates in the liver. It is often associated with chronic liver diseases such as cirrhosis and hepatitis."
    ),
    "medicine": "Sorafenib, Liver transplant",
    "dose": "Sorafenib: 400 mg twice daily",
    "side_effects": "Fatigue, diarrhea, hand-foot skin reaction, hypertension, liver toxicity",
    "times_per_day": "Twice daily",
    "body_weight": "Not typically adjusted based on body weight",
    "lab_tests": [
        "CT scan of the abdomen", "Liver biopsy"
    ]
},
"Lyme Disease": {
    "description": (
        "Lyme disease is an infectious disease caused by the bacterium *Borrelia burgdorferi*, transmitted by ticks. It can cause fever, rash, fatigue, and joint pain."
    ),
    "medicine": "Doxycycline, Amoxicillin",
    "dose": "Doxycycline: 100 mg twice daily for 14-21 days",
    "side_effects": "Nausea, vomiting, photosensitivity, dizziness, diarrhea",
    "times_per_day": "Twice daily",
    "body_weight": "Not typically adjusted based on body weight",
    "lab_tests": [
        "ELISA test for *Borrelia burgdorferi*", "Western blot test"
    ]
},
"Lupus": {
    "description": (
        "Lupus is an autoimmune disease where the body's immune system attacks its own tissues, causing inflammation and damage to various organs."
    ),
    "medicine": "Hydroxychloroquine, Corticosteroids, Immunosuppressants",
    "dose": "Hydroxychloroquine: 200-400 mg per day",
    "side_effects": "Retinal toxicity, gastrointestinal upset, skin rash, headaches",
    "times_per_day": "Once or twice a day",
    "body_weight": "Typically not adjusted based on body weight",
    "lab_tests": [
        "Antinuclear Antibody (ANA) Test", "Complete Blood Count (CBC)", "Urinalysis"
    ]
},
"Lymphoma": {
    "description": (
        "Lymphoma is a cancer of the lymphatic system, which includes the lymph nodes, spleen, and bone marrow. It can cause swollen lymph nodes, fever, and weight loss."
    ),
    "medicine": "Chemotherapy, Rituximab, Stem cell transplant",
    "dose": "Varies based on chemotherapy regimen",
    "side_effects": "Hair loss, nausea, fatigue, immunosuppression, increased risk of infection",
    "times_per_day": "Varies",
    "body_weight": "Chemotherapy doses are sometimes adjusted based on body weight",
    "lab_tests": [
        "Biopsy", "CT Scan", "PET Scan"
    ]
},
"Malaria": {
    "description": (
        "Malaria is a life-threatening disease caused by parasites transmitted through the bite of infected mosquitoes, causing fever, chills, and flu-like symptoms."
    ),
    "medicine": "Chloroquine, Artemisinin-based combination therapies (ACTs)",
    "dose": "Chloroquine: 250 mg once a week for prophylaxis",
    "side_effects": "Headache, nausea, vomiting, dizziness, visual disturbances",
    "times_per_day": "Once daily or weekly, depending on treatment",
    "body_weight": "May be adjusted based on weight for certain treatments",
    "lab_tests": [
        "Blood smear", "Rapid diagnostic test (RDT)"
    ]
},
"Melanoma": {
    "description": (
        "Melanoma is a type of skin cancer that develops from melanocytes, the cells that produce pigment. It can spread to other parts of the body."
    ),
    "medicine": "Immunotherapy, Chemotherapy, Targeted therapy",
    "dose": "Varies based on treatment regimen",
    "side_effects": "Fatigue, nausea, rash, diarrhea, liver toxicity, skin reactions",
    "times_per_day": "Varies",
    "body_weight": "Chemotherapy doses may be adjusted based on weight",
    "lab_tests": [
        "Skin biopsy", "CT Scan", "Lymph node biopsy"
    ]
},
"Menopause": {
    "description": (
        "Menopause is the natural biological process marking the end of a woman's menstrual cycles, typically occurring between ages 45 and 55."
    ),
    "medicine": "Hormone Replacement Therapy (HRT), Antidepressants, Vaginal Estrogen",
    "dose": "HRT: Typically 0.5-2 mg of estradiol per day",
    "side_effects": "Breast tenderness, headaches, nausea, mood swings, increased risk of blood clots",
    "times_per_day": "Once a day or as prescribed",
    "body_weight": "Not typically adjusted based on body weight",
    "lab_tests": [
        "Follicle-stimulating hormone (FSH) test", "Estradiol test"
    ]
},
"Meningitis": {
    "description": (
        "Meningitis is an inflammation of the protective membranes covering the brain and spinal cord, typically caused by infection."
    ),
    "medicine": "Antibiotics, Antivirals, Corticosteroids",
    "dose": "Varies based on the cause (bacterial, viral)",
    "side_effects": "Nausea, vomiting, rash, immune suppression (with corticosteroids)",
    "times_per_day": "Varies",
    "body_weight": "Doses adjusted based on weight for children",
    "lab_tests": [
        "Lumbar puncture", "Blood cultures", "CT scan"
    ]
},
"Mononucleosis": {
    "description": (
        "Mononucleosis, often called 'mono', is a viral infection caused by the Epstein-Barr virus (EBV), leading to fever, sore throat, and swollen lymph nodes."
    ),
    "medicine": "Supportive care, Antipyretics for fever",
    "dose": "Rest and fluids, acetaminophen or ibuprofen for symptoms",
    "side_effects": "Fatigue, headache, gastrointestinal upset (from pain relievers)",
    "times_per_day": "As needed for symptoms",
    "body_weight": "Not typically adjusted based on body weight",
    "lab_tests": [
        "Monospot test", "EBV antibody test"
    ]
},
"Multiple Sclerosis (MS)": {
    "description": (
        "Multiple sclerosis is an autoimmune disease where the immune system attacks the protective covering of nerve fibers in the central nervous system."
    ),
    "medicine": "Disease-modifying therapies (e.g., Interferons), Steroids for flare-ups",
    "dose": "Interferon: 30 mcg every other day",
    "side_effects": "Flu-like symptoms, injection site reactions, liver toxicity, depression",
    "times_per_day": "Once every other day",
    "body_weight": "Typically not adjusted based on body weight",
    "lab_tests": [
        "MRI of the brain and spinal cord", "Lumbar puncture"
    ]
},
"Muscular Dystrophy": {
    "description": (
        "Muscular dystrophy is a group of genetic diseases that cause progressive weakness and degeneration of skeletal muscles."
    ),
    "medicine": "Corticosteroids, Physical therapy",
    "dose": "Prednisone: 0.75 mg per pound of body weight",
    "side_effects": "Weight gain, osteoporosis, mood swings, gastrointestinal discomfort",
    "times_per_day": "Once daily",
    "body_weight": "Doses may be adjusted based on weight",
    "lab_tests": [
        "Creatine kinase (CK) test", "Genetic testing"
    ]
},
"Myasthenia Gravis": {
    "description": (
        "Myasthenia gravis is a chronic autoimmune disease that causes weakness in the skeletal muscles by blocking communication between nerves and muscles."
    ),
    "medicine": "Acetylcholinesterase inhibitors, Immunosuppressants, Thymectomy",
    "dose": "Pyridostigmine: 30-60 mg, 3-4 times per day",
    "side_effects": "Diarrhea, cramping, excessive salivation, muscle weakness",
    "times_per_day": "3-4 times daily",
    "body_weight": "Not typically adjusted based on body weight",
    "lab_tests": [
        "Acetylcholine receptor antibody test", "Electromyography (EMG)"
    ]
},

    "Nasal Polyps": {
        "description": "Nasal polyps are noncancerous growths in the lining of the nasal passages or sinuses, often caused by inflammation or chronic sinus infections.",
        "medicine": "Corticosteroid nasal sprays, Oral corticosteroids",
        "dose": "Fluticasone nasal spray: 2 sprays in each nostril once daily",
        "side_effects": ["Nasal irritation", "Nosebleeds", "Sore throat", "Headache", "Nasal dryness"],
        "times_per_day": "Once a day",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": ["Nasal endoscopy", "CT scan"]
    },
    "Narcolepsy": {
        "description": "Narcolepsy is a neurological disorder that affects the control of sleep and wakefulness, causing excessive daytime sleepiness.",
        "medicine": "Stimulants (e.g., Modafinil), Antidepressants, Sodium oxybate",
        "dose": "Modafinil: 100-200 mg once daily",
        "side_effects": ["Headache", "Nausea", "Anxiety", "Dizziness", "Insomnia", "Dry mouth"],
        "times_per_day": "Once daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": ["Polysomnography", "Multiple Sleep Latency Test (MSLT)"]
    },
    "Nephritis": {
        "description": "Nephritis is inflammation of the kidneys, which can be caused by infections, autoimmune diseases, or toxins.",
        "medicine": "Corticosteroids, Immunosuppressive drugs, Diuretics",
        "dose": "Prednisone: 0.5-2 mg/kg per day",
        "side_effects": ["Weight gain", "Fluid retention", "Increased blood sugar", "High blood pressure", "Osteoporosis", "Mood swings"],
        "times_per_day": "Once or twice a day",
        "body_weight": "Adjusted for children based on body weight",
        "lab_tests": ["Urinalysis", "Creatinine test", "Kidney biopsy"]
    },
    "Neurofibromatosis": {
        "description": "Neurofibromatosis is a genetic disorder that causes tumors to form on nerve tissue, leading to skin changes and bone deformities.",
        "medicine": "Pain management, Surgery for tumor removal",
        "dose": "Varies based on treatment",
        "side_effects": ["Varies depending on the specific pain management drug (e.g., opioids can cause sedation, constipation)"],
        "times_per_day": "As prescribed",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": ["Genetic testing", "MRI", "CT scan"]
    },
    "Obesity": {
        "description": "Obesity is a condition characterized by excessive body fat, which increases the risk of several health problems, including heart disease, diabetes, and hypertension.",
        "medicine": "Phentermine, Orlistat, Bariatric surgery",
        "dose": "Phentermine: 15-37.5 mg once daily",
        "side_effects": ["Increased heart rate", "Elevated blood pressure", "Insomnia", "Nervousness", "Dry mouth", "Constipation"],
        "times_per_day": "Once daily",
        "body_weight": "Adjusted based on the individual’s weight",
        "lab_tests": ["Body Mass Index (BMI)", "Lipid profile", "Glucose test"]
    },
    "Osteoarthritis": {
        "description": "Osteoarthritis is a degenerative joint disease that causes the cartilage in the joints to break down, leading to pain and stiffness.",
        "medicine": "NSAIDs (e.g., Ibuprofen), Corticosteroid injections, Physical therapy",
        "dose": "Ibuprofen: 200-400 mg every 4-6 hours as needed",
        "side_effects": ["Stomach irritation", "Ulcers", "Gastrointestinal bleeding", "Kidney damage", "Dizziness", "High blood pressure"],
        "times_per_day": "Every 4-6 hours as needed",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": ["X-ray", "MRI", "Joint fluid analysis"]
    },
    "Osteoporosis": {
        "description": "Osteoporosis is a condition in which bones become weak and brittle, increasing the risk of fractures.",
        "medicine": "Bisphosphonates (e.g., Alendronate), Calcium and Vitamin D supplements",
        "dose": "Alendronate: 70 mg once a week",
        "side_effects": ["Esophageal irritation", "Stomach pain", "Nausea", "Headache", "Musculoskeletal pain", "Jawbone problems"],
        "times_per_day": "Once weekly",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": ["Bone density test (DEXA)", "Calcium and vitamin D levels"]
    },
    "Otitis Media (Ear Infection)": {
        "description": "Otitis media is an infection or inflammation of the middle ear, commonly caused by bacteria or viruses.",
        "medicine": "Antibiotics (e.g., Amoxicillin), Pain relievers (e.g., Acetaminophen)",
        "dose": "Amoxicillin: 80-90 mg/kg/day divided into two doses",
        "side_effects": ["Diarrhea", "Rash", "Nausea", "Vomiting", "Allergic reactions (e.g., hives, swelling)"],
        "times_per_day": "Twice daily",
        "body_weight": "Adjusted for children based on body weight",
        "lab_tests": ["Tympanometry", "Otoscopy"]
    },
    "Parkinson's Disease": {
        "description": "Parkinson's disease is a neurodegenerative disorder that affects movement, causing tremors, stiffness, and difficulty with balance and coordination.",
        "medicine": "Levodopa, Dopamine agonists, MAO-B inhibitors",
        "dose": "Levodopa: 100-250 mg 2-3 times a day",
        "side_effects": ["Nausea", "Dizziness", "Low blood pressure", "Involuntary movements (dyskinesia)", "Hallucinations", "Confusion"],
        "times_per_day": "2-3 times daily",
        "body_weight": "Typically not adjusted based on body weight",
        "lab_tests": ["MRI", "Dopamine transporter scan"]
    },
    "Peptic Ulcer Disease": {
        "description": "Peptic ulcer disease refers to sores that develop on the lining of the stomach, small intestine, or esophagus, often caused by infection with H. pylori bacteria or long-term use of NSAIDs.",
        "medicine": "Proton pump inhibitors (e.g., Omeprazole), Antacids, Antibiotics (e.g., Amoxicillin)",
        "dose": "Omeprazole: 20 mg once a day",
        "side_effects": ["Headache", "Diarrhea", "Nausea", "Abdominal pain", "Increased risk of fractures", "Vitamin B12 deficiency"],
        "times_per_day": "Once daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": ["Endoscopy", "H. pylori breath test"]
    },
    "Pelvic Inflammatory Disease (PID)": {
        "description": "PID is an infection of the female reproductive organs, often caused by sexually transmitted infections like chlamydia or gonorrhea.",
        "medicine": "Antibiotics (e.g., Doxycycline, Ceftriaxone)",
        "dose": "Doxycycline: 100 mg twice a day",
        "side_effects": ["Nausea", "Vomiting", "Diarrhea", "Photosensitivity", "Esophageal irritation", "Yeast infections"],
        "times_per_day": "Twice daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": ["Pelvic ultrasound", "Laparoscopy", "Cervical cultures"]
    },
    "Pemphigus": {
        "description": "Pemphigus is a rare autoimmune disorder that causes blisters and sores on the skin and mucous membranes.",
        "medicine": "Corticosteroids, Immunosuppressants",
        "dose": "Prednisone: 1-2 mg/kg per day",
        "side_effects": ["Weight gain", "Fluid retention", "High blood sugar", "Osteoporosis", "Increased risk of infection", "Mood swings"],
        "times_per_day": "Once or twice daily",
        "body_weight": "Doses adjusted based on body weight",
        "lab_tests": ["Skin biopsy", "Direct immunofluorescence"]
    },
    "Peritonitis": {
        "description": "Peritonitis is an infection of the peritoneum, the lining of the abdominal cavity, typically caused by a bacterial or fungal infection.",
        "medicine": "Intravenous antibiotics, Surgery if necessary",
        "dose": "Ceftriaxone: 1-2 grams once daily",
        "side_effects": ["Diarrhea", "Nausea", "Allergic reactions (e.g., rash)", "Liver enzyme abnormalities", "Blood disorders"],
        "times_per_day": "Once daily",
        "body_weight": "Adjusted for body weight in children",
        "lab_tests": ["Abdominal ultrasound", "Blood cultures", "Peritoneal fluid analysis"]
    },

    "Rabies": {
        "description": "Rabies is a viral disease that affects the nervous system and is transmitted through the saliva of infected animals. It can be fatal if not treated promptly.",
        "medicine": "Rabies post-exposure prophylaxis (PEP), Rabies vaccine, Rabies immunoglobulin",
        "dose": "Rabies vaccine: 1 dose per day for 5 days",
        "times_per_day": "Once daily for 5 days",
        "body_weight": "Not typically adjusted based on body weight",
        "side_effects": [
            "Pain at injection site", "Swelling", "Fever", "Headache", "Fatigue"
        ],
        "lab_tests": [
            "Rabies virus test", "PCR"
        ]
    },

    "Raynaud’s Disease": {
        "description": "Raynaud’s disease is a condition that causes some areas of the body, usually fingers and toes, to feel numb and cold due to constricted blood vessels.",
        "medicine": "Calcium channel blockers (e.g., Nifedipine), Vasodilators",
        "dose": "Nifedipine: 30-60 mg once daily",
        "times_per_day": "Once daily",
        "body_weight": "Not typically adjusted based on body weight",
        "side_effects": [
            "Headache", "Dizziness", "Flushing", "Edema", "Palpitations"
        ],
        "lab_tests": [
            "Nailfold capillaroscopy", "Blood tests for autoimmune conditions"
        ]
    },

    "Rheumatic Fever": {
        "description": "Rheumatic fever is an inflammatory disease that can develop after a strep throat or scarlet fever infection, affecting the heart, joints, skin, and brain.",
        "medicine": "Penicillin, Aspirin, Corticosteroids",
        "dose": "Penicillin: 250 mg twice daily for 10 days",
        "times_per_day": "Twice daily",
        "body_weight": "Not typically adjusted based on body weight",
        "side_effects": [
            "Gastrointestinal upset", "Allergic reactions (rash, hives)", "Headache", "Fever"
        ],
        "lab_tests": [
            "Throat culture for Group A Streptococcus", "Echocardiogram"
        ]
    },

    "Rheumatoid Arthritis": {
        "description": "Rheumatoid arthritis is an autoimmune disease that causes chronic inflammation in the joints, leading to pain, stiffness, and deformities.",
        "medicine": "DMARDs (e.g., Methotrexate), NSAIDs, Biologics (e.g., Etanercept)",
        "dose": "Methotrexate: 7.5-25 mg once weekly",
        "times_per_day": "Once weekly",
        "body_weight": "Not typically adjusted based on body weight",
        "side_effects": [
            "Nausea", "Fatigue", "Liver toxicity", "Bone marrow suppression", "Increased risk of infections"
        ],
        "lab_tests": [
            "Rheumatoid factor test", "X-rays of affected joints"
        ]
    },

    "Roseola": {
        "description": "Roseola is a viral infection that primarily affects young children, characterized by a sudden high fever followed by a rash.",
        "medicine": "Antipyretics (e.g., Acetaminophen), Supportive care",
        "dose": "Acetaminophen: 10-15 mg/kg per dose",
        "times_per_day": "Every 4-6 hours as needed",
        "body_weight": "Adjusted based on body weight",
        "side_effects": [
            "Liver toxicity (with excessive use)", "Allergic reactions (rash, swelling)"
        ],
        "lab_tests": [
            "Clinical diagnosis", "PCR for human herpesvirus 6 (HHV-6)"
        ]
    },

    "Rubella": {
        "description": "Rubella, also known as German measles, is a viral infection that causes a rash, fever, and swollen lymph nodes. It can be serious in pregnant women.",
        "medicine": "Supportive care, Vaccination for prevention",
        "dose": "N/A for treatment (vaccination recommended for prevention)",
        "times_per_day": "N/A",
        "body_weight": "Not applicable",
        "side_effects": [
            "Mild fever", "Rash", "Joint pain"
        ],
        "lab_tests": [
            "Rubella IgG and IgM test"
        ]
    },

    "Salmonella Infection": {
        "description": "Salmonella infection is caused by *Salmonella* bacteria, typically from contaminated food or water. Symptoms include diarrhea, fever, and abdominal cramps.",
        "medicine": "Ciprofloxacin (if severe), Supportive care",
        "dose": "Ciprofloxacin: 500 mg twice daily for 5-7 days",
        "times_per_day": "Twice daily",
        "body_weight": "Not typically adjusted based on body weight",
        "side_effects": [
            "Nausea", "Diarrhea", "Tendinitis", "Rash", "Dizziness"
        ],
        "lab_tests": [
            "Stool culture", "Blood cultures (if septic)"
        ]
    },

    "Sarcoidosis": {
        "description": "Sarcoidosis is an inflammatory disease that typically affects the lungs, skin, and lymph nodes. It causes granulomas (clusters of inflammatory cells) to form in affected organs.",
        "medicine": "Corticosteroids (e.g., Prednisone), Immunosuppressants (e.g., Methotrexate)",
        "dose": "Prednisone: 20-40 mg daily",
        "times_per_day": "Once daily",
        "body_weight": "Not typically adjusted based on body weight",
        "side_effects": [
            "Weight gain", "Hyperglycemia", "Osteoporosis", "Mood changes", "Increased infection risk"
        ],
        "lab_tests": [
            "Chest X-ray", "Lung function tests", "Serum calcium levels"
        ]
    },

    "Scabies": {
        "description": "Scabies is a skin infestation caused by the mite *Sarcoptes scabiei*. It leads to intense itching and a rash. It is highly contagious.",
        "medicine": "Permethrin cream, Ivermectin (oral)",
        "dose": "Permethrin: Apply to all affected areas, leave on for 8-14 hours, repeat after 1 week",
        "times_per_day": "Once (for application)",
        "body_weight": "Ivermectin: Dosed based on weight (200 mcg/kg)",
        "side_effects": [
            "Skin irritation", "Itching", "Headache", "Dizziness", "Fatigue"
        ],
        "lab_tests": [
            "Skin scraping for mites", "Clinical diagnosis"
        ]
    },

    "Schizophrenia": {
        "description": "Schizophrenia is a chronic mental health disorder characterized by distorted thinking, hallucinations, and impaired functioning.",
        "medicine": "Antipsychotics (e.g., Olanzapine, Risperidone)",
        "dose": "Olanzapine: 5-20 mg daily",
        "times_per_day": "Once daily",
        "body_weight": "Dosage may require adjustment for weight-related side effects",
        "side_effects": [
            "Weight gain", "Sedation", "Tardive dyskinesia", "Metabolic changes", "Dry mouth"
        ],
        "lab_tests": [
            "Psychiatric evaluation", "Blood tests for side effects (e.g., glucose, lipid profile)"
        ]
    },

    "Scleroderma": {
        "description": "Scleroderma is an autoimmune disease that causes thickening and hardening of the skin and connective tissues. It may also affect internal organs like the lungs and heart.",
        "medicine": "Corticosteroids, Immunosuppressants (e.g., Methotrexate, Cyclophosphamide)",
        "dose": "Methotrexate: 10-25 mg weekly",
        "times_per_day": "Once weekly",
        "body_weight": "Not typically adjusted based on body weight",
        "side_effects": [
            "Nausea", "Fatigue", "Liver toxicity", "Bone marrow suppression", "Hair loss"
        ],
        "lab_tests": [
            "Autoantibody testing", "Chest X-ray", "Pulmonary function tests"
        ]
    },

    "Scurvy": {
        "description": "Scurvy is caused by a deficiency in Vitamin C, leading to symptoms like fatigue, swollen gums, joint pain, and skin bruising.",
        "medicine": "Vitamin C supplements",
        "dose": "Vitamin C: 500 mg daily",
        "times_per_day": "Once daily",
        "body_weight": "Not typically adjusted based on body weight",
        "side_effects": [
            "Stomach upset", "Diarrhea (if taken in excessive amounts)"
        ],
        "lab_tests": [
            "Serum vitamin C levels"
        ]
    },

    "Sepsis": {
        "description": "Sepsis is a life-threatening condition caused by the body's response to an infection, leading to widespread inflammation and organ failure.",
        "medicine": "IV antibiotics (e.g., Piperacillin-Tazobactam), IV fluids",
        "dose": "Piperacillin-Tazobactam: 3.375 g every 6 hours",
        "times_per_day": "Four times a day",
        "body_weight": "Dosed based on weight, especially for pediatric cases",
        "side_effects": [
            "Allergic reactions (rash, fever)", "Diarrhea", "Increased risk of infections"
        ],
        "lab_tests": [
            "Blood cultures", "Complete blood count (CBC)", "Lactate levels"
        ]
    },

    "Shingles": {
        "description": "Shingles (Herpes Zoster) is caused by the reactivation of the chickenpox virus. It leads to a painful rash and blisters, often on one side of the body.",
        "medicine": "Acyclovir, Valacyclovir, Pain management",
        "dose": "Acyclovir: 800 mg five times daily for 7-10 days",
        "times_per_day": "Five times a day",
        "body_weight": "Not typically adjusted based on body weight",
        "side_effects": [
            "Nausea", "Diarrhea", "Headache", "Fatigue"
        ],
        "lab_tests": [
            "PCR for varicella-zoster virus", "Clinical diagnosis"
        ]
    },

    "Sickle Cell Anemia": {
        "description": "Sickle cell anemia is a genetic blood disorder characterized by abnormal hemoglobin, leading to misshapen red blood cells and reduced oxygen transport.",
        "medicine": "Hydroxyurea, Pain management, Blood transfusions",
        "dose": "Hydroxyurea: 15 mg/kg/day",
        "times_per_day": "Once daily",
        "body_weight": "Dosed based on body weight",
        "side_effects": [
            "Nausea", "Vomiting", "Low blood cell counts", "Hair loss", "Fatigue"
        ],
        "lab_tests": [
            "Hemoglobin electrophoresis", "CBC", "Reticulocyte count"
        ]
    },

    "Sinusitis": {
        "description": "Sinusitis is the inflammation or infection of the sinus cavities, causing symptoms like nasal congestion, headache, and facial pain.",
        "medicine": "Antibiotics (e.g., Amoxicillin), Nasal decongestants",
        "dose": "Amoxicillin: 500 mg three times daily for 10-14 days",
        "times_per_day": "Three times a day",
        "body_weight": "Not typically adjusted based on body weight",
        "side_effects": [
            "Gastrointestinal upset", "Rash", "Allergic reactions"
        ],
        "lab_tests": [
            "CT scan of sinuses", "Nasal swab culture"
        ]
    },

    "Smallpox": {
        "description": "Smallpox is a highly contagious viral disease characterized by fever and a distinctive skin rash. It has been eradicated but was historically a major public health threat.",
        "medicine": "Vaccination (before exposure), Supportive care (after exposure)",
        "dose": "One dose of the smallpox vaccine",
        "side_effects": [
            "Fever",
            "Redness or swelling at the injection site",
            "Headache",
            "Fatigue",
            "Rare: Serious allergic reactions"
        ],
        "times_per_day": "Once (for vaccination)",
        "body_weight": "Not applicable (for vaccination)",
        "lab_tests": [
            "PCR for variola virus", "Clinical diagnosis"
        ]
    },
    "Spina Bifida": {
        "description": "Spina bifida is a birth defect where the spinal cord and its covering don't form properly. It may lead to physical and intellectual disabilities.",
        "medicine": "Folic acid supplements (before and during pregnancy), Surgery",
        "dose": "Folic acid: 400-800 mcg daily (for prevention)",
        "side_effects": [
            "Rare: Allergic reactions",
            "Nausea (at high doses)",
            "Bloating",
            "Gas"
        ],
        "times_per_day": "Once daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Prenatal screening (e.g., maternal serum alpha-fetoprotein)"
        ]
    },
    "Spondylitis": {
        "description": "Spondylitis is an inflammatory disease that affects the spine, causing pain and stiffness. It is commonly associated with ankylosing spondylitis.",
        "medicine": "NSAIDs (e.g., Ibuprofen), TNF inhibitors (e.g., Etanercept)",
        "dose": "Ibuprofen: 400-800 mg every 6-8 hours as needed",
        "side_effects": [
            "Upset stomach",
            "Heartburn",
            "Dizziness",
            "Headache",
            "Risk of gastrointestinal bleeding (long-term use)"
        ],
        "times_per_day": "Three times a day (if needed)",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "X-ray of the spine", "HLA-B27 testing"
        ]
    },
    "Strep Throat": {
        "description": "Strep throat is a bacterial infection caused by *Streptococcus pyogenes*. It causes a sore throat, fever, and difficulty swallowing.",
        "medicine": "Penicillin or Amoxicillin",
        "dose": "Amoxicillin: 500 mg twice daily for 10 days",
        "side_effects": [
            "Nausea",
            "Vomiting",
            "Diarrhea",
            "Skin rash",
            "Rare: Severe allergic reactions (anaphylaxis)"
        ],
        "times_per_day": "Twice daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Rapid antigen test", "Throat culture"
        ]
    },
    "Streptococcus Infection": {
        "description": "Streptococcus infections can affect various body parts, including the throat, skin, and lungs. Symptoms depend on the location of the infection.",
        "medicine": "Penicillin, Cephalosporins (if resistant)",
        "dose": "Penicillin: 250 mg four times daily for 10 days",
        "side_effects": [
            "Nausea",
            "Vomiting",
            "Diarrhea",
            "Rash",
            "Rare: Severe allergic reactions"
        ],
        "times_per_day": "Four times a day",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Strep throat culture", "Blood culture (if systemic)"
        ]
    },
    "Stroke": {
        "description": "A stroke occurs when there is a sudden interruption of blood flow to part of the brain, causing tissue damage. Symptoms include paralysis, speech difficulties, and confusion.",
        "medicine": "Aspirin, Thrombolytics (e.g., tPA for ischemic stroke)",
        "dose": "Aspirin: 81 mg daily",
        "side_effects": [
            "Upset stomach",
            "Gastrointestinal bleeding",
            "Allergic reactions"
        ],
        "times_per_day": "Once daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "CT scan of the brain", "Blood tests for coagulation"
        ]
    },
    "Systemic Lupus Erythematosus (SLE)": {
        "description": "SLE is an autoimmune disease that affects multiple organs, leading to inflammation, joint pain, and skin rashes.",
        "medicine": "Hydroxychloroquine, Immunosuppressants (e.g., Azathioprine)",
        "dose": "Hydroxychloroquine: 200-400 mg daily",
        "side_effects": [
            "Nausea",
            "Diarrhea",
            "Headache",
            "Retinal damage (long-term use)"
        ],
        "times_per_day": "Once daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Antinuclear antibody (ANA) test", "Complete blood count (CBC)"
        ]
    },
    "Testicular Cancer": {
        "description": "Testicular cancer is a malignancy that originates in the testicles. It is one of the most treatable cancers with high survival rates.",
        "medicine": "Chemotherapy (e.g., Cisplatin), Surgery (orchiectomy)",
        "dose": "Cisplatin: 20-30 mg/m² daily for 3-5 days",
        "side_effects": [
            "Nausea and vomiting",
            "Kidney damage",
            "Hearing loss",
            "Fatigue"
        ],
        "times_per_day": "Once daily (during chemotherapy cycles)",
        "body_weight": "Dosed based on body surface area (BSA)",
        "lab_tests": [
            "Blood tumor markers (AFP, hCG, LDH)", "Ultrasound of testicles"
        ]
    },
    "Thalassemia": {
        "description": "Thalassemia is a group of inherited blood disorders that affect the production of hemoglobin, leading to anemia and other complications.",
        "medicine": "Blood transfusions, Iron chelation therapy (e.g., Deferasirox)",
        "dose": "Deferasirox: 20-40 mg/kg daily",
        "side_effects": [
            "Nausea",
            "Diarrhea",
            "Liver toxicity",
            "Kidney toxicity"
        ],
        "times_per_day": "Once daily",
        "body_weight": "Dosed based on body weight",
        "lab_tests": [
            "Hemoglobin electrophoresis", "Iron studies", "CBC"
        ]
    },
    "Thyroid Cancer": {
        "description": "Thyroid cancer is a malignancy that arises from the thyroid gland. It can be classified into different types, such as papillary, follicular, and anaplastic.",
        "medicine": "Surgery (thyroidectomy), Radioactive iodine therapy, Thyroid hormone replacement",
        "dose": "Levothyroxine: 1.6-1.8 mcg/kg daily",
        "side_effects": [
            "Hyperthyroidism (if overdosed)",
            "Weight loss",
            "Increased heart rate",
            "Nervousness"
        ],
        "times_per_day": "Once daily",
        "body_weight": "Dosed based on body weight",
        "lab_tests": [
            "Thyroid function tests (TSH, T4, T3)", "Ultrasound of thyroid"
        ]
    },
    "Tinnitus": {
        "description": "Tinnitus is the perception of ringing or other sounds in the ears in the absence of external sound. It can be caused by various factors such as hearing loss or exposure to loud noise.",
        "medicine": "Sound therapy, Antidepressants, Antianxiety medications",
        "dose": "Amitriptyline: 10-25 mg at bedtime",
        "side_effects": [
            "Drowsiness",
            "Dry mouth",
            "Blurred vision",
            "Weight gain"
        ],
        "times_per_day": "Once daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Audiometry", "Tympanometry"
        ]
    },
    "Tuberculosis (TB)": {
        "description": "Tuberculosis is a bacterial infection caused by *Mycobacterium tuberculosis*, typically affecting the lungs but can affect other organs.",
        "medicine": "Antitubercular drugs (e.g., Isoniazid, Rifampin, Pyrazinamide, Ethambutol)",
        "dose": "Isoniazid: 5 mg/kg daily, Rifampin: 10 mg/kg daily",
        "side_effects": [
            "Liver toxicity",
            "Peripheral neuropathy",
            "Nausea",
            "Red-orange discoloration of urine",
            "GI upset"
        ],
        "times_per_day": "Once daily",
        "body_weight": "Dosed based on body weight",
        "lab_tests": [
            "Chest X-ray", "Sputum culture for acid-fast bacilli (AFB)"
        ]
    },
    "Tuberous Sclerosis": {
        "description": "Tuberous sclerosis is a genetic disorder that causes non-cancerous tumors to form in various organs, including the brain, kidneys, and lungs.",
        "medicine": "Antiepileptic drugs, mTOR inhibitors (e.g., Everolimus)",
        "dose": "Everolimus: 2.5 mg twice daily",
        "side_effects": [
            "Mouth ulcers",
            "Diarrhea",
            "Headache",
            "Fatigue"
        ],
        "times_per_day": "Twice daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Brain MRI", "Kidney function tests", "Genetic testing"
        ]
    },
    "Turner Syndrome": {
        "description": "Turner syndrome is a genetic condition affecting females, caused by the partial or complete absence of one X chromosome. It can result in short stature, infertility, and various health issues.",
        "medicine": "Growth hormone therapy, Estrogen replacement therapy",
        "dose": "Growth hormone: 0.3-0.6 mg/kg weekly (subcutaneous injection)",
        "side_effects": [
            "Headache",
            "Limb pain",
            "Swelling",
            "Increased blood sugar levels"
        ],
        "times_per_day": "Once daily (for growth hormone)",
        "body_weight": "Dosed based on body weight",
        "lab_tests": [
            "Chromosome analysis", "Growth monitoring", "Thyroid function tests"
        ]
    },

    "Yellow Fever": {
        "description": "Yellow fever is a viral hemorrhagic disease transmitted by mosquitoes. It causes fever, jaundice, and bleeding in severe cases.",
        "medicine": "Vaccination (prevention), Supportive care (for severe cases)",
        "dose": "Yellow fever vaccine: One dose",
        "times_per_day": "Once (for vaccination)",
        "body_weight": "Not applicable (for vaccination)",
        "lab_tests": [
            "Serology for yellow fever virus", "Liver function tests"
        ],
        "side_effects": "Mild fever, soreness at the injection site, headache, and fatigue. Rare side effects include allergic reactions."
    },
    "Zika Virus": {
        "description": "Zika virus is transmitted by mosquitoes and typically causes mild symptoms, such as rash, fever, and joint pain. It can be dangerous for pregnant women due to the risk of birth defects.",
        "medicine": "Supportive care, Antipyretics for fever",
        "dose": "Acetaminophen: 500-1000 mg every 4-6 hours as needed",
        "times_per_day": "As needed",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Serology for Zika virus", "PCR for Zika virus"
        ],
        "side_effects": "Possible side effects of acetaminophen include liver damage (with prolonged high doses), allergic reactions, and gastrointestinal upset."
    },
    "Achondroplasia": {
        "description": "Achondroplasia is a genetic disorder that results in dwarfism due to abnormal bone growth, affecting the long bones, leading to short stature.",
        "medicine": "Growth hormone therapy (off-label), Surgical intervention for skeletal deformities",
        "dose": "Growth hormone: 0.03 mg/kg daily (in some cases)",
        "times_per_day": "Once daily (if prescribed)",
        "body_weight": "Dosed based on body weight",
        "lab_tests": [
            "Genetic testing for FGFR3 mutation", "Bone age assessment"
        ],
        "side_effects": "Possible side effects of growth hormone include joint pain, swelling, headache, and increased risk of diabetes or fluid retention."
    },
    "Acute Lymphoblastic Leukemia (ALL)": {
        "description": "ALL is a type of cancer that affects the blood and bone marrow, characterized by the overproduction of immature lymphocytes (a type of white blood cell).",
        "medicine": "Chemotherapy (e.g., Vincristine, Methotrexate), Targeted therapy (e.g., Imatinib)",
        "dose": "Vincristine: 1.5 mg/m² weekly (during induction phase)",
        "times_per_day": "Once weekly (for chemotherapy)",
        "body_weight": "Dosed based on body surface area (BSA)",
        "lab_tests": [
            "CBC with differential", "Bone marrow biopsy", "Flow cytometry"
        ],
        "side_effects": "Vincristine may cause nerve damage (peripheral neuropathy), constipation, hair loss, and bone marrow suppression."
    },
    "Acute Myeloid Leukemia (AML)": {
        "description": "AML is a type of cancer that affects the blood and bone marrow, characterized by the rapid growth of abnormal myeloid cells that interfere with normal blood cell production.",
        "medicine": "Chemotherapy (e.g., Cytarabine, Daunorubicin), Stem cell transplant (in some cases)",
        "dose": "Cytarabine: 100-200 mg/m² daily for 7 days (during induction)",
        "times_per_day": "Once or twice daily (during chemotherapy cycles)",
        "body_weight": "Dosed based on body surface area (BSA)",
        "lab_tests": [
            "CBC with differential", "Bone marrow biopsy", "Cytogenetic analysis"
        ],
        "side_effects": "Cytarabine can cause nausea, vomiting, bone marrow suppression, and liver toxicity."
    },
    "Acute Respiratory Distress Syndrome (ARDS)": {
        "description": "ARDS is a severe lung condition where the air sacs in the lungs become inflamed and filled with fluid, leading to difficulty breathing and low blood oxygen levels.",
        "medicine": "Mechanical ventilation, Oxygen therapy, Sedation",
        "dose": "Sedation: Propofol 5-50 mcg/kg/min (for comfort during ventilation)",
        "times_per_day": "As needed (for sedation)",
        "body_weight": "Dosed based on body weight",
        "lab_tests": [
            "Arterial blood gas (ABG)", "Chest X-ray", "Pulmonary function tests"
        ],
        "side_effects": "Propofol can cause hypotension, respiratory depression, allergic reactions, and pain at the injection site."
    },
    "Adult-onset Diabetes": {
        "description": "Adult-onset diabetes, commonly known as Type 2 diabetes, is a metabolic disorder characterized by insulin resistance and impaired insulin secretion.",
        "medicine": "Oral hypoglycemics (e.g., Metformin), Insulin (if necessary)",
        "dose": "Metformin: 500 mg twice daily",
        "times_per_day": "Twice daily",
        "body_weight": "Dosed based on kidney function and tolerance",
        "lab_tests": [
            "Fasting blood glucose", "HbA1c", "Kidney function tests"
        ],
        "side_effects": "Metformin can cause gastrointestinal issues like nausea, diarrhea, and, rarely, lactic acidosis."
    },
    "Albinism": {
        "description": "Albinism is a genetic condition characterized by a lack of melanin pigment in the skin, hair, and eyes, leading to pale skin, light-colored hair, and visual impairments.",
        "medicine": "Sunscreen, Protective eyewear, Monitoring for skin cancer",
        "dose": "Sunscreen: SPF 50 or higher, apply every 2 hours in sun",
        "times_per_day": "As needed",
        "body_weight": "Not applicable for medication",
        "lab_tests": [
            "Genetic testing", "Eye exams"
        ],
        "side_effects": "Sunscreen may cause skin irritation, although severe side effects are rare."
    },
    "Alport Syndrome": {
        "description": "Alport syndrome is a genetic condition that affects the kidneys, ears, and eyes, often leading to kidney failure and hearing and vision problems.",
        "medicine": "ACE inhibitors (e.g., Enalapril), Kidney transplant (in severe cases)",
        "dose": "Enalapril: 5-10 mg daily",
        "times_per_day": "Once daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Urine protein levels", "Kidney function tests", "Genetic testing"
        ],
        "side_effects": "Enalapril can cause dizziness, hyperkalemia, hypotension, and kidney dysfunction."
    },

    "Alport Syndrome": {
        "description": "Alport syndrome is a genetic condition that affects the kidneys, ears, and eyes, often leading to kidney failure and hearing and vision problems.",
        "medicine": "ACE inhibitors (e.g., Enalapril), Kidney transplant (in severe cases)",
        "dose": "Enalapril: 5-10 mg daily",
        "times_per_day": "Once daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": ["Urine protein levels", "Kidney function tests", "Genetic testing"],
        "side_effects": ["Dizziness", "Cough", "Elevated potassium levels", "Low blood pressure", "Headache", "Fatigue"]
    },
    "Amyotrophic Lateral Sclerosis (ALS)": {
        "description": "ALS, also known as Lou Gehrig's disease, is a progressive neurodegenerative disease that affects motor neurons, leading to muscle weakness and atrophy.",
        "medicine": "Riluzole, Supportive care (e.g., physical therapy, breathing support)",
        "dose": "Riluzole: 50 mg twice daily",
        "times_per_day": "Twice daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": ["Electromyography (EMG)", "MRI of the brain and spinal cord"],
        "side_effects": ["Nausea", "Fatigue", "Liver enzyme abnormalities", "Dizziness", "Headache", "Anorexia"]
    },
    "Anaplastic Thyroid Cancer": {
        "description": "Anaplastic thyroid cancer is a rare and aggressive form of thyroid cancer characterized by rapid growth and poor prognosis.",
        "medicine": "Surgery (thyroidectomy), Radiation therapy, Chemotherapy",
        "dose": "Doxorubicin: 60 mg/m² every 21 days (chemotherapy)",
        "times_per_day": "Once every 21 days",
        "body_weight": "Dosed based on body surface area (BSA)",
        "lab_tests": ["Thyroid function tests", "Fine needle aspiration biopsy", "CT scan"],
        "side_effects": ["Nausea", "Vomiting", "Hair loss", "Fatigue", "Heart damage", "Lowered blood cell counts", "Mouth sores"]
    },
    "Aortic Aneurysm": {
        "description": "An aortic aneurysm is a bulge in the wall of the aorta, which can be life-threatening if it ruptures.",
        "medicine": "Blood pressure control (e.g., Beta-blockers), Surgical repair (for large aneurysms)",
        "dose": "Metoprolol: 25-100 mg daily",
        "times_per_day": "Once daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": ["CT scan or MRI of the chest/abdomen", "Echocardiogram"],
        "side_effects": ["Fatigue", "Dizziness", "Low blood pressure", "Slow heart rate", "Shortness of breath", "Cold hands/feet"]
    },
    "Aortic Dissection": {
        "description": "Aortic dissection is a tear in the inner layer of the aortic wall, leading to severe chest pain and risk of rupture.",
        "medicine": "Antihypertensive medications (e.g., Labetalol), Surgery",
        "dose": "Labetalol: 10-20 mg IV every 10 minutes as needed",
        "times_per_day": "As needed (IV administration)",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": ["CT angiography", "Echocardiogram", "MRI of the aorta"],
        "side_effects": ["Dizziness", "Fatigue", "Low blood pressure", "Shortness of breath", "Nausea", "Slow heart rate"]
    },
    "Apnea (Sleep Apnea)": {
        "description": "Sleep apnea is a sleep disorder where breathing repeatedly stops and starts during sleep, leading to disrupted sleep and daytime fatigue.",
        "medicine": "CPAP (Continuous Positive Airway Pressure), Surgery (in severe cases)",
        "dose": "CPAP: Continuous use during sleep",
        "times_per_day": "Nightly",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": ["Polysomnography (sleep study)", "Pulse oximetry"],
        "side_effects": ["Dry mouth", "Nasal congestion", "Bloating", "Skin irritation", "Discomfort from mask"]
    },
    "Arrhythmia": {
        "description": "Arrhythmia refers to abnormal heart rhythms, which can cause palpitations, dizziness, and, in severe cases, can be life-threatening.",
        "medicine": "Antiarrhythmic medications (e.g., Amiodarone), Rate control medications (e.g., Beta-blockers)",
        "dose": "Amiodarone: 200 mg daily",
        "times_per_day": "Once daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": ["Electrocardiogram (ECG)", "Holter monitor"],
        "side_effects": ["Nausea", "Fatigue", "Thyroid problems", "Lung toxicity", "Liver damage", "Eye issues", "Photosensitivity"]
    },
    "Asbestosis": {
        "description": "Asbestosis is a lung disease caused by inhaling asbestos fibers, leading to scarring of the lung tissue and difficulty breathing.",
        "medicine": "Oxygen therapy, Pulmonary rehabilitation, Bronchodilators",
        "dose": "Oxygen: As prescribed based on oxygen saturation levels",
        "times_per_day": "As needed for oxygen therapy",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": ["Chest X-ray", "Pulmonary function tests", "CT scan"],
        "side_effects": ["Dry or bloody nose", "Fatigue", "Irritation of the airways", "Headache (if used excessively)"]
    },
    "Atherosclerosis": {
        "description": "Atherosclerosis is a condition where the arteries become narrowed and hardened due to the buildup of plaque, increasing the risk of heart disease and stroke.",
        "medicine": "Statins (e.g., Atorvastatin), Antiplatelet therapy (e.g., Aspirin)",
        "dose": "Atorvastatin: 10-80 mg daily",
        "times_per_day": "Once daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": ["Lipid profile", "Blood pressure monitoring", "ECG"],
        "side_effects": ["Muscle pain", "Liver enzyme abnormalities", "Digestive issues", "Increased blood sugar", "Memory problems"]
    },
    "Ataxia": {
        "description": "Ataxia is a neurological disorder characterized by loss of coordination and balance due to damage to the cerebellum or its pathways.",
        "medicine": "Symptom management (e.g., Anticonvulsants for seizures, Physical therapy)",
        "dose": "Gabapentin: 100-300 mg daily",
        "times_per_day": "Once to three times daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": ["MRI of the brain", "Genetic testing (in some cases)"],
        "side_effects": ["Dizziness", "Fatigue", "Peripheral edema", "Weight gain", "Nausea", "Blurred vision"]
    },
    "Atrial Fibrillation": {
        "description": "Atrial fibrillation is a common heart arrhythmia that can increase the risk of stroke and heart failure.",
        "medicine": "Anticoagulants (e.g., Warfarin), Rate control medications (e.g., Beta-blockers)",
        "dose": "Warfarin: 2-5 mg daily",
        "times_per_day": "Once daily",
        "body_weight": "Adjusted based on INR levels",
        "lab_tests": ["Electrocardiogram (ECG)", "INR monitoring"],
        "side_effects": ["Bleeding", "Bruising", "Nausea", "Liver damage", "Purple toe syndrome", "Hair loss"]
    },
    "Autoimmune Hepatitis": {
        "description": "Autoimmune hepatitis is a chronic liver disease in which the body's immune system attacks liver cells, causing inflammation and damage.",
        "medicine": "Immunosuppressive therapy (e.g., Prednisone, Azathioprine)",
        "dose": "Prednisone: 40-60 mg daily (initial dose)",
        "times_per_day": "Once daily (during flare-up)",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": ["Liver function tests", "Autoantibodies (ANA, ASMA)", "Liver biopsy (if needed)"],
        "side_effects": ["Weight gain", "Osteoporosis", "High blood sugar", "Mood swings", "Increased risk of infections"]
    },
    "Autoimmune Vasculitis": {
        "description": "Autoimmune vasculitis is a group of disorders characterized by inflammation of blood vessels, which can lead to organ damage.",
        "medicine": "Immunosuppressive drugs (e.g., Cyclophosphamide, Methotrexate)",
        "dose": "Cyclophosphamide: 0.5-1.0 g/m² every 1-3 weeks",
        "times_per_day": "Once every 1-3 weeks",
        "body_weight": "Dosed based on body surface area (BSA)",
        "lab_tests": ["Complete blood count (CBC)", "Renal function tests", "Urinalysis"],
        "side_effects": ["Hair loss", "Nausea", "Increased risk of infections", "Bladder irritation", "Liver toxicity"]
    },

    "Babesiosis": {
        "description": "Babesiosis is a malaria-like parasitic infection transmitted by ticks, leading to flu-like symptoms and, in severe cases, organ failure.",
        "medicine": "Antiprotozoal drugs (e.g., Atovaquone, Azithromycin)",
        "dose": "Atovaquone: 750 mg twice daily, Azithromycin: 500 mg daily for 7-10 days",
        "times_per_day": "Twice daily for Atovaquone, Once daily for Azithromycin",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Blood smear for Babesia parasites", "PCR for Babesia"
        ],
        "side_effects": [
            "Nausea", "Headache", "Diarrhea", "Rash", "Liver enzyme abnormalities"
        ]
    },

    "Bacterial Vaginosis": {
        "description": "Bacterial vaginosis is an imbalance in the natural bacteria of the vagina, leading to symptoms like discharge, odor, and irritation.",
        "medicine": "Metronidazole, Clindamycin",
        "dose": "Metronidazole: 500 mg twice a day for 7 days",
        "times_per_day": "Twice daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Vaginal pH test", "Wet mount microscopy", "Culture for Gardnerella"
        ],
        "side_effects": [
            "Metallic taste", "Nausea", "Headache", "Diarrhea", "Vaginal irritation"
        ]
    },

    "Basal Cell Carcinoma": {
        "description": "Basal cell carcinoma is the most common type of skin cancer, originating from the basal cells in the skin, usually caused by long-term sun exposure.",
        "medicine": "Excision, Mohs surgery, Topical treatments (e.g., Imiquimod)",
        "dose": "Imiquimod: Apply once daily for 5 days per week for 6 weeks",
        "times_per_day": "Once daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Skin biopsy", "Dermatoscopy"
        ],
        "side_effects": [
            "Skin irritation", "Redness", "Itching", "Swelling", "Burning sensation"
        ]
    },

    "Biliary Cirrhosis": {
        "description": "Biliary cirrhosis is a chronic liver disease where the bile ducts become damaged, leading to liver scarring and impaired liver function.",
        "medicine": "Ursodeoxycholic acid, Immunosuppressants",
        "dose": "Ursodeoxycholic acid: 13-15 mg/kg per day",
        "times_per_day": "Once to twice daily",
        "body_weight": "Dosed based on body weight",
        "lab_tests": [
            "Liver function tests", "Ultrasound", "Liver biopsy"
        ],
        "side_effects": [
            "Diarrhea", "Constipation", "Nausea", "Stomach pain", "Fatigue"
        ]
    },

    "Binge Eating Disorder": {
        "description": "Binge eating disorder is characterized by recurrent episodes of eating large quantities of food in a short time, often with feelings of loss of control.",
        "medicine": "Antidepressants (e.g., Fluoxetine), Cognitive-behavioral therapy (CBT)",
        "dose": "Fluoxetine: 20-60 mg once daily",
        "times_per_day": "Once daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Psychological assessment", "Blood tests to assess metabolic health"
        ],
        "side_effects": [
            "Nausea", "Insomnia", "Sexual dysfunction", "Appetite changes", "Weight changes"
        ]
    },

    "Bipolar Affective Disorder": {
        "description": "Bipolar disorder is a mental health condition characterized by extreme mood swings that include emotional highs (mania) and lows (depression).",
        "medicine": "Mood stabilizers (e.g., Lithium), Antipsychotics, Antidepressants",
        "dose": "Lithium: 600-1200 mg per day in divided doses",
        "times_per_day": "2-3 times daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Lithium blood levels", "Thyroid function tests", "Electrolyte levels"
        ],
        "side_effects": [
            "Tremors", "Weight gain", "Thirst", "Increased urination", "Thyroid problems"
        ]
    },

    "Bladder Infection": {
        "description": "Bladder infections, or urinary tract infections (UTIs), are common infections of the bladder, often caused by bacteria like E. coli.",
        "medicine": "Antibiotics (e.g., Nitrofurantoin, Trimethoprim-sulfamethoxazole)",
        "dose": "Nitrofurantoin: 100 mg twice a day for 5-7 days",
        "times_per_day": "Twice daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Urinalysis", "Urine culture"
        ],
        "side_effects": [
            "Nausea", "Headache", "Dizziness", "Stomach upset", "Urine discoloration"
        ]
    },

    "Blount's Disease": {
        "description": "Blount's disease is a growth disorder of the shin bone (tibia) that causes the lower leg to bow outward.",
        "medicine": "Orthotics, Bracing, Surgery (in severe cases)",
        "dose": "N/A (No specific medication for this condition)",
        "times_per_day": "N/A",
        "body_weight": "Not applicable",
        "lab_tests": [
            "X-rays", "MRI"
        ],
        "side_effects": [
            "No specific medication-related side effects"
        ]
    },

    "Bone Cancer (Osteosarcoma)": {
        "description": "Osteosarcoma is a rare and aggressive form of bone cancer that most commonly occurs in the long bones of the arms and legs.",
        "medicine": "Chemotherapy (e.g., Methotrexate, Doxorubicin), Surgery",
        "dose": "Methotrexate: 12-15 mg/kg per week",
        "times_per_day": "Weekly",
        "body_weight": "Adjusted for body weight",
        "lab_tests": [
            "X-ray", "MRI", "Biopsy"
        ],
        "side_effects": [
            "Hair loss", "Nausea", "Vomiting", "Fatigue", "Low blood cell counts", "Mouth sores"
        ]
    },

    "Bowel Obstruction": {
        "description": "Bowel obstruction occurs when there is a blockage in the intestines, which can be caused by a variety of factors including tumors, adhesions, or impacted stool.",
        "medicine": "Bowel rest, IV fluids, Surgery if necessary",
        "dose": "N/A",
        "times_per_day": "N/A",
        "body_weight": "Not applicable",
        "lab_tests": [
            "Abdominal X-ray", "CT scan"
        ],
        "side_effects": [
            "No specific medication-related side effects"
        ]
    },

    "Brucellosis": {
        "description": "Brucellosis is an infectious disease caused by bacteria from animals, leading to flu-like symptoms such as fever, joint pain, and fatigue.",
        "medicine": "Antibiotics (e.g., Doxycycline, Rifampin)",
        "dose": "Doxycycline: 100 mg twice daily for 6 weeks",
        "times_per_day": "Twice daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Blood cultures", "Brucella antibody test"
        ],
        "side_effects": [
            "Nausea", "Dizziness", "Photosensitivity", "Stomach upset", "Loss of appetite"
        ]
    },

    "Bullous Pemphigoid": {
        "description": "Bullous pemphigoid is a rare autoimmune blistering skin disorder, causing large, fluid-filled blisters.",
        "medicine": "Corticosteroids (e.g., Prednisone), Immunosuppressants",
        "dose": "Prednisone: 0.5-1 mg/kg per day",
        "times_per_day": "Once or twice daily",
        "body_weight": "Dosed based on body weight",
        "lab_tests": [
            "Skin biopsy", "Direct immunofluorescence"
        ],
        "side_effects": [
            "Weight gain", "Mood changes", "High blood sugar", "Osteoporosis", "Increased risk of infections"
        ]
    },

    "Cardiomyopathy": {
        "description": "Cardiomyopathy refers to diseases of the heart muscle that can lead to heart failure, arrhythmias, and other cardiovascular issues.",
        "medicine": "ACE inhibitors (e.g., Enalapril), Beta-blockers (e.g., Metoprolol), Diuretics",
        "dose": "Enalapril: 2.5-20 mg twice daily",
        "times_per_day": "Twice daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Echocardiogram", "Electrocardiogram (ECG)", "Cardiac MRI"
        ],
        "side_effects": [
            "Dizziness", "Fatigue", "Low blood pressure", "Cough (with ACE inhibitors)", "Elevated potassium levels"
        ]
    },

    "Carpal Tunnel Syndrome": {
        "description": "Carpal tunnel syndrome occurs when the median nerve is compressed at the wrist, causing symptoms such as numbness, tingling, and weakness in the hand.",
        "medicine": "NSAIDs (e.g., Ibuprofen), Corticosteroid injections, Surgery",
        "dose": "Ibuprofen: 200-400 mg every 4-6 hours as needed",
        "times_per_day": "Up to 4 times daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Nerve conduction studies", "Electromyography (EMG)"
        ],
        "side_effects": [
            "Gastrointestinal upset", "Stomach irritation", "Dizziness", "Rash"
        ]
    },

    "Celiac Disease": {
        "description": "Celiac disease is an autoimmune disorder where the ingestion of gluten leads to damage to the small intestine lining.",
        "medicine": "Gluten-free diet (primary treatment), Nutritional supplements",
        "dose": "N/A (Dietary change is key)",
        "times_per_day": "N/A",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Serology tests for tTG-IgA", "Endoscopy with biopsy"
        ],
        "side_effects": [
            "No medication-related side effects (dietary changes required)"
        ]
    },
    "Central Nervous System Infections": {
        "description": "CNS infections can involve the brain, spinal cord, or meninges, and include conditions such as meningitis and encephalitis.",
        "medicine": "Antibiotics (e.g., Ceftriaxone), Antivirals (e.g., Acyclovir)",
        "dose": "Ceftriaxone: 1-2 grams once or twice daily",
        "times_per_day": "Once or twice daily",
        "body_weight": "Adjusted for pediatric cases",
        "lab_tests": [
            "CSF analysis", "Blood cultures", "MRI"
        ],
        "side_effects": {
            "Ceftriaxone": [
                "Diarrhea",
                "Allergic reactions (rash, anaphylaxis)",
                "Liver enzyme abnormalities",
                "Thrombophlebitis at injection site",
                "Risk of superinfection"
            ],
            "Acyclovir": [
                "Nausea",
                "Headache",
                "Renal dysfunction (if not hydrated)",
                "Rash"
            ]
        }
    },

    "Charcot-Marie-Tooth Disease": {
        "description": "Charcot-Marie-Tooth disease is a group of inherited disorders that affect the peripheral nerves, leading to muscle weakness and sensory loss.",
        "medicine": "No specific cure, Symptomatic treatments (e.g., Physical therapy)",
        "dose": "N/A",
        "times_per_day": "N/A",
        "body_weight": "Not applicable",
        "lab_tests": [
            "Genetic testing", "Nerve conduction studies"
        ],
        "side_effects": {
            "Physical Therapy": "No pharmaceutical side effects"
        }
    },

    "Chickenpox": {
        "description": "Chickenpox is a highly contagious viral infection characterized by itchy, red blisters and fever, caused by the varicella-zoster virus.",
        "medicine": "Antihistamines (e.g., Diphenhydramine), Calamine lotion, Antiviral medication (e.g., Acyclovir) in severe cases",
        "dose": "Acyclovir: 800 mg five times a day for 5 days (in severe cases)",
        "times_per_day": "Five times daily for severe cases",
        "body_weight": "Adjusted for children based on weight",
        "lab_tests": [
            "Clinical diagnosis", "PCR for varicella-zoster virus"
        ],
        "side_effects": {
            "Diphenhydramine": [
                "Drowsiness",
                "Dry mouth",
                "Urinary retention",
                "Blurred vision",
                "Constipation"
            ],
            "Calamine lotion": [
                "Skin irritation",
                "Dryness"
            ],
            "Acyclovir": [
                "Nausea",
                "Headache",
                "Renal dysfunction (if not hydrated)",
                "Rash"
            ]
        }
    },

    "Cholangitis": {
        "description": "Cholangitis is an infection of the bile ducts, often caused by a bacterial infection, which can lead to fever, jaundice, and abdominal pain.",
        "medicine": "Antibiotics (e.g., Piperacillin-tazobactam), ERCP for bile duct drainage",
        "dose": "Piperacillin-tazobactam: 3.375 grams every 6-8 hours",
        "times_per_day": "Every 6-8 hours",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Liver function tests", "Ultrasound", "Endoscopic retrograde cholangiopancreatography (ERCP)"
        ],
        "side_effects": {
            "Piperacillin-tazobactam": [
                "Diarrhea",
                "Allergic reactions (rash, anaphylaxis)",
                "Liver enzyme abnormalities",
                "Thrombocytopenia"
            ]
        }
    },

    "Chronic Sinusitis": {
        "description": "Chronic sinusitis is long-term inflammation of the sinuses, leading to symptoms such as nasal congestion, facial pain, and reduced sense of smell.",
        "medicine": "Decongestants, Nasal corticosteroids, Antibiotics (if bacterial infection present)",
        "dose": "Fluticasone nasal spray: 1 spray in each nostril once daily",
        "times_per_day": "Once daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Nasal endoscopy", "Sinus CT scan"
        ],
        "side_effects": {
            "Fluticasone": [
                "Nasal irritation",
                "Headache",
                "Sore throat",
                "Epistaxis (nosebleeds)",
                "Potential growth suppression in children with long-term use"
            ]
        }
    },

    "Circulatory Shock": {
        "description": "Circulatory shock occurs when there is inadequate blood flow to tissues and organs, which can be caused by various factors like heart failure, severe blood loss, or infection.",
        "medicine": "IV fluids, Vasopressors (e.g., Norepinephrine), Antibiotics (if septic)",
        "dose": "Norepinephrine: 0.05-2 mcg/kg/min as a continuous infusion",
        "times_per_day": "Continuous infusion until stabilized",
        "body_weight": "Adjusted for body weight in pediatric cases",
        "lab_tests": [
            "Arterial blood gas (ABG)", "Lactate levels", "Blood cultures"
        ],
        "side_effects": {
            "Norepinephrine": [
                "Hypertension",
                "Arrhythmias",
                "Headache",
                "Anxiety",
                "Tissue necrosis at injection site"
            ]
        }
    },

    "Colitis": {
        "description": "Colitis is inflammation of the colon, which can be caused by infections, inflammatory bowel disease (e.g., Crohn’s disease), or ischemia.",
        "medicine": "Corticosteroids (e.g., Prednisone), Antibiotics (for infection), Aminosalicylates (e.g., Mesalamine)",
        "dose": "Prednisone: 40-60 mg daily, tapering over time",
        "times_per_day": "Once daily, taper as prescribed",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Colonoscopy", "Stool culture", "CT scan"
        ],
        "side_effects": {
            "Prednisone": [
                "Weight gain",
                "Hyperglycemia",
                "Increased risk of infections",
                "Mood changes",
                "Osteoporosis with long-term use"
            ],
            "Mesalamine": [
                "Nausea",
                "Diarrhea",
                "Abdominal pain",
                "Headache",
                "Possible renal dysfunction"
            ]
        }
    },

    "Crohn’s Disease": {
        "description": "Crohn's disease is a chronic inflammatory bowel disease that can affect any part of the gastrointestinal tract, leading to symptoms like abdominal pain, diarrhea, and weight loss.",
        "medicine": "Corticosteroids (e.g., Prednisone), Immunosuppressants (e.g., Azathioprine), Biologics (e.g., Infliximab)",
        "dose": "Prednisone: 40-60 mg daily, tapering",
        "times_per_day": "Once daily for induction phase, tapering as prescribed",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Colonoscopy", "Fecal calprotectin", "Blood tests for inflammation"
        ],
        "side_effects": {
            "Prednisone": [
                "Weight gain",
                "Hyperglycemia",
                "Increased risk of infections",
                "Mood changes",
                "Osteoporosis with long-term use"
            ],
            "Azathioprine": [
                "Nausea",
                "Liver toxicity",
                "Bone marrow suppression",
                "Increased risk of infection"
            ],
            "Infliximab": [
                "Infusion reactions (fever, chills)",
                "Increased risk of infections",
                "Liver enzyme abnormalities",
                "Allergic reactions"
            ]
        }
    },

    "Cystitis": {
        "description": "Cystitis is an inflammation of the bladder, often caused by a urinary tract infection (UTI), leading to symptoms such as painful urination and frequent urination.",
        "medicine": "Antibiotics (e.g., Nitrofurantoin, Trimethoprim-sulfamethoxazole)",
        "dose": "Nitrofurantoin: 100 mg twice daily for 5-7 days",
        "times_per_day": "Twice daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Urine culture", "Urinalysis"
        ],
        "side_effects": {
            "Nitrofurantoin": [
                "Nausea",
                "Vomiting",
                "Diarrhea",
                "Pulmonary toxicity (rare)",
                "Peripheral neuropathy (with long-term use)",
                "Brown-colored urine"
            ]
        }
    },

    "Deep Vein Thrombosis": {
        "description": "Deep vein thrombosis (DVT) is the formation of a blood clot in a deep vein, typically in the legs, which can cause pain, swelling, and can lead to a pulmonary embolism.",
        "medicine": "Anticoagulants (e.g., Heparin, Warfarin, Rivaroxaban)",
        "dose": "Rivaroxaban: 15 mg twice daily for 3 weeks, then 20 mg once daily",
        "times_per_day": "Twice daily for 3 weeks, then once daily",
        "body_weight": "Adjusted for weight in pediatric cases",
        "lab_tests": [
            "Ultrasound", "D-dimer", "CT pulmonary angiography (if suspected PE)"
        ],
        "side_effects": {
            "Rivaroxaban": [
                "Bleeding (including gastrointestinal, intracranial)",
                "Anemia",
                "Liver enzyme abnormalities",
                "Nausea"
            ]
        }
    },

    "Dystonia": {
        "description": "Dystonia is a movement disorder that causes muscles to contract uncontrollably, leading to abnormal postures or twisting movements.",
        "medicine": "Anticholinergics (e.g., Benztropine), Botulinum toxin injections, Muscle relaxants",
        "dose": "Benztropine: 0.5-2 mg once or twice daily",
        "times_per_day": "Once or twice daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Neurological examination", "MRI", "Genetic testing"
        ],
        "side_effects": {
            "Benztropine": [
                "Dry mouth",
                "Constipation",
                "Blurred vision",
                "Urinary retention",
                "Confusion (especially in elderly)"
            ]
        }
    },

    "Endometriosis": {
        "description": "Endometriosis is a condition where tissue similar to the lining inside the uterus grows outside it, leading to pelvic pain, heavy menstruation, and infertility.",
        "medicine": "Hormonal therapies (e.g., Birth control pills, GnRH agonists), Pain relievers (e.g., NSAIDs)",
        "dose": "GnRH agonists (e.g., Leuprolide): 3.75 mg monthly injection",
        "times_per_day": "Once monthly",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Pelvic ultrasound", "Laparoscopy"
        ],
        "side_effects": {
            "Leuprolide": [
                "Hot flashes",
                "Mood swings",
                "Decreased bone density (with long-term use)",
                "Vaginal dryness"
            ]
        }
    },

    "Epiglottitis": {
        "description": "Epiglottitis is an infection that causes inflammation of the epiglottis, which can block the airway and cause difficulty breathing.",
        "medicine": "Antibiotics (e.g., Ceftriaxone), Airway management",
        "dose": "Ceftriaxone: 1-2 grams once or twice daily",
        "times_per_day": "Once or twice daily",
        "body_weight": "Adjusted for pediatric cases",
        "lab_tests": [
            "Laryngoscopy", "Blood cultures", "X-ray (neck)"
        ],
        "side_effects": {
            "Ceftriaxone": [
                "Diarrhea",
                "Allergic reactions (rash, anaphylaxis)",
                "Liver enzyme abnormalities",
                "Thrombophlebitis at injection site",
                "Risk of superinfection"
            ]
        }
    },

    "Erythropoietic Protoporphyria": {
        "description": "Erythropoietic protoporphyria is a genetic disorder that causes sensitivity to sunlight and a build-up of protoporphyrin in red blood cells.",
        "medicine": "Beta-carotene",
        "dose": "15-30 mg per day",
        "times_per_day": "Once daily",
        "body_weight": "Adjusted for children based on weight",
        "lab_tests": [
            "Blood tests for porphyrins", "Liver function tests"
        ],
        "side_effects": {
            "Beta-carotene": [
                "Yellow-orange skin discoloration",
                "Nausea",
                "Mild gastrointestinal upset"
            ]
        }
    },

    "Bipolar Disorder": {
        "description": "Bipolar disorder is a mental health condition characterized by extreme mood swings that include emotional highs (mania or hypomania) and lows (depression).",
        "medicine": "Mood stabilizers (e.g., Lithium), Antipsychotics (e.g., Olanzapine), Antidepressants (e.g., SSRIs)",
        "dose": "Lithium: 600-1200 mg daily",
        "times_per_day": "Once or twice daily",
        "body_weight": "Adjusted for pediatric cases",
        "lab_tests": [
            "Lithium blood levels", "Thyroid function tests", "Kidney function tests"
        ],
        "side_effects": {
            "Lithium": [
                "Weight gain",
                "Tremors",
                "Thirst",
                "Polyuria",
                "Thyroid and kidney dysfunction",
                "Nausea"
            ],
            "Olanzapine": [
                "Weight gain",
                "Sedation",
                "Metabolic changes (increased cholesterol, glucose)",
                "Extrapyramidal symptoms"
            ],
            "SSRIs": [
                "Weight changes",
                "Sexual dysfunction",
                "Nausea",
                "Insomnia",
                "Dizziness"
            ]
        }
    },

    "Major Depressive Disorder": {
        "description": "Major depressive disorder is a mood disorder that causes persistent feelings of sadness, loss of interest, and various emotional and physical problems.",
        "medicine": "SSRIs (e.g., Sertraline), SNRIs, Psychotherapy (e.g., CBT, IPT)",
        "dose": "Sertraline: 50-200 mg daily",
        "times_per_day": "Once daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Depression screening questionnaires"
        ],
        "side_effects": {
            "SSRIs": [
                "Weight gain",
                "Sexual dysfunction",
                "Nausea",
                "Insomnia",
                "Dizziness"
            ]
        }
    },

    "Generalized Anxiety Disorder": {
        "description": "Generalized anxiety disorder involves excessive and uncontrollable worry about everyday matters.",
        "medicine": "SSRIs, Benzodiazepines (e.g., Lorazepam)",
        "dose": "Lorazepam: 0.5-1 mg as needed",
        "times_per_day": "Short-term use",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Clinical evaluation", "Screening questionnaires"
        ],
        "side_effects": {
            "SSRIs": [
                "Weight gain",
                "Sexual dysfunction",
                "Nausea",
                "Insomnia",
                "Dizziness"
            ],
            "Lorazepam": [
                "Drowsiness",
                "Dizziness",
                "Tolerance",
                "Dependence",
                "Cognitive impairment"
            ]
        }
    },

    "Obsessive-Compulsive Disorder": {
        "description": "Obsessive-compulsive disorder is characterized by unwanted repetitive thoughts (obsessions) and/or behaviors (compulsions).",
        "medicine": "SSRIs (e.g., Fluoxetine), Cognitive-behavioral therapy (CBT)",
        "dose": "Fluoxetine: 20-60 mg daily",
        "times_per_day": "Once daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Screening questionnaires"
        ],
        "side_effects": {
            "SSRIs": [
                "Weight gain",
                "Sexual dysfunction",
                "Nausea",
                "Insomnia",
                "Dizziness"
            ]
        }
    },

    "Schizophrenia": {
        "description": "Schizophrenia is a chronic brain disorder characterized by hallucinations, delusions, and cognitive disturbances.",
        "medicine": "Antipsychotics (e.g., Risperidone), Antidepressants (if comorbid)",
        "dose": "Risperidone: 2-6 mg daily",
        "times_per_day": "Once or twice daily",
        "body_weight": "Adjusted for pediatric cases",
        "lab_tests": [
            "Mental status exam", "MRI of the brain"
        ],
        "side_effects": {
            "Risperidone": [
                "Weight gain",
                "Sedation",
                "Extrapyramidal symptoms (tremors, rigidity)",
                "Metabolic syndrome"
            ]
        }
    },

    "Post-Traumatic Stress Disorder": {
        "description": "Post-traumatic stress disorder develops after exposure to traumatic events and involves symptoms like flashbacks, nightmares, and hypervigilance.",
        "medicine": "SSRIs, Therapy (CBT, EMDR)",
        "dose": "SSRI (e.g., Sertraline): 50-200 mg daily",
        "times_per_day": "Once daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Clinical interview"
        ],
        "side_effects": {
            "SSRIs": [
                "Weight gain",
                "Sexual dysfunction",
                "Nausea",
                "Insomnia",
                "Dizziness"
            ]
        }
    },

    "Panic Disorder": {
        "description": "Panic disorder is characterized by recurrent and unexpected panic attacks, often with physical symptoms like chest pain and shortness of breath.",
        "medicine": "SSRIs, Benzodiazepines (e.g., Lorazepam)",
        "dose": "Lorazepam: 0.5-1 mg as needed",
        "times_per_day": "Short-term use",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Clinical evaluation", "Screening questionnaires"
        ],
        "side_effects": {
            "SSRIs": [
                "Weight gain",
                "Sexual dysfunction",
                "Nausea",
                "Insomnia",
                "Dizziness"
            ],
            "Lorazepam": [
                "Drowsiness",
                "Dizziness",
                "Tolerance",
                "Dependence",
                "Cognitive impairment"
            ]
        }
    },

    "Attention-Deficit Hyperactivity Disorder": {
        "description": "ADHD is characterized by inattention, hyperactivity, and impulsivity that affect daily functioning.",
        "medicine": "Stimulants (e.g., Methylphenidate), Non-stimulants (e.g., Atomoxetine)",
        "dose": "Methylphenidate: 5-20 mg twice daily",
        "times_per_day": "Twice daily",
        "body_weight": "Adjusted for weight in children",
        "lab_tests": [
            "Clinical evaluation"
        ],
        "side_effects": {
            "Methylphenidate": [
                "Appetite suppression",
                "Insomnia",
                "Weight loss",
                "Increased heart rate",
                "Anxiety"
            ],
            "Atomoxetine": [
                "Decreased appetite",
                "Dry mouth",
                "Insomnia",
                "Mood swings"
            ]
        }
    },

    "Eating Disorders": {
        "description": "Eating disorders include anorexia nervosa, bulimia nervosa, and binge eating disorder, characterized by abnormal eating behaviors and preoccupation with body weight.",
        "medicine": "SSRIs, Psychotherapy (CBT, family-based therapy)",
        "dose": "Fluoxetine (for bulimia): 60 mg daily",
        "times_per_day": "Once daily",
        "body_weight": "Adjusted for pediatric cases",
        "lab_tests": [
            "Mental status exam", "Blood tests (electrolytes, liver function)"
        ],
        "side_effects": {
            "SSRIs": [
                "Weight gain",
                "Sexual dysfunction",
                "Nausea",
                "Insomnia",
                "Dizziness"
            ]
        }
    },

    "Borderline Personality Disorder": {
        "description": "Borderline personality disorder is characterized by intense emotions, impulsivity, and unstable relationships.",
        "medicine": "SSRIs, Mood stabilizers",
        "dose": "SSRIs (e.g., Sertraline): 50-200 mg daily",
        "times_per_day": "Once daily",
        "body_weight": "Not typically adjusted based on body weight",
        "lab_tests": [
            "Clinical evaluation"
        ],
        "side_effects": {
            "SSRIs": [
                "Weight gain",
                "Sexual dysfunction",
                "Nausea",
                "Insomnia",
                "Dizziness"
            ]
        }
    },

    "Autism Spectrum Disorder": {
        "description": "Autism spectrum disorder is a developmental disorder affecting communication, behavior, and social interaction.",
        "medicine": "Therapies (ABA, Speech Therapy)",
        "dose": "N/A",
        "times_per_day": "N/A",
        "body_weight": "Not applicable",
        "lab_tests": [
            "Developmental screenings", "Genetic testing"
        ],
        "side_effects": {
            "Therapies": "No pharmaceutical side effects"
        }
    },

        "Dementia": {
        "description": "Dementia is a decline in cognitive function that affects memory, thinking, and daily functioning.",
        "medicine": "Cholinesterase inhibitors (e.g., Donepezil), Memantine",
        "dose": "Donepezil: 5-10 mg daily",
        "times_per_day": "Once daily",
        "side_effects": {
            "Donepezil": ["Diarrhea", "Nausea", "Dizziness", "Insomnia"],
            "Memantine": ["Dizziness", "Confusion", "Headache", "Constipation"]
        },
        "lab_tests": ["Mental status exam", "MRI of the brain"]
    }
    # Add more diseases here...
}

# File to store patient data
patient_data_file = "patient_data.json"

# Function to load patient data from a file
def load_patient_data():
    if os.path.exists(patient_data_file):
        with open(patient_data_file, "r") as file:
            return json.load(file)
    return None

# Function to save patient data to a file
def save_patient_data(data):
    with open(patient_data_file, "w") as file:
        json.dump(data, file)

# Function to simulate login process
def on_login():
    username = entry_username.get()
    password = entry_password.get()
    
    stored_username = "Andromeda"  # Example username
    stored_password = "Galaxy"  # Example password

    if username == stored_username and password == stored_password:
        speak("Welcome back, dear patient. It’s so good to have you here today. Your login was successful.")
        speak("Ownership of data is completely yours. We respect your privacy")
        speak("Before we move on, there is a small payment of $10 to be made via Google Pay to leena.nandi@gmail.com.")
        speak("Once you’ve completed tht, please let me know and we can continue with the next steps.")
        payment_frame.pack(pady=20)
        login_frame.pack_forget()
    else:
        speak("Oh no! It seems like the username or password you entered might be incorrect. Please take your time and double-check. I’m here to help you.")



# Function to confirm payment
def confirm_payment():
    speak("Thank you for your payment. Let’s continue.")
    payment_frame.pack_forget()
    main_feed.pack(pady=20)
    patient_data = load_patient_data()
    if patient_data:
        entry_patient_name.insert(0, patient_data["name"])
        entry_patient_age.insert(0, patient_data["age"])
        entry_patient_weight.insert(0, patient_data["weight"])
        entry_patient_height.insert(0, patient_data["height"])
        entry_patient_dob.insert(0, patient_data["dob"])
        entry_patient_address.insert(0, patient_data["address"])
        entry_patient_blood_group.insert(0, patient_data["blood_group"])
        entry_patient_email.insert(0, patient_data["email"])

# Function to submit patient data
def submit_patient_data():
    patient_data = {
        "name": entry_patient_name.get(),
        "age": entry_patient_age.get(),
        "weight": entry_patient_weight.get(),
        "height": entry_patient_height.get(),
        "dob": entry_patient_dob.get(),
        "address": entry_patient_address.get(),
        "blood_group": entry_patient_blood_group.get(),
        "email": entry_patient_email.get(),
        "date_of_visit": datetime.today().strftime('%Y-%m-%d')
    }
    
    save_patient_data(patient_data)
    speak("Thank you so much for sharing your information. It’s been successfully saved. You’re doing wonderfully! Please take your time and relax while I prepare the next steps for you.")
    speak("Now, if you’d like, I can provide you with detailed information about your treatment options and any medical advice you might need.")
    
    disease_input.pack(pady=10)
    disease_info_button.pack(pady=10)

# Function to show treatment information for the selected disease
def show_treatment_info():
    selected_disease = disease_var.get()
    
    if selected_disease in disease_dict:
        disease_info = disease_dict[selected_disease]
        
        # Construct the treatment info text with labels
        treatment_info_text = f"**Disease: {selected_disease}**\n\n"
        treatment_info_text += f"**Description of Disease**: {disease_info['description']}\n\n"
        
        # Dose
        treatment_info_text += f"**Dose**: {disease_info['dose']}\n"
        
        # Times per day
        treatment_info_text += f"**Times per Day**: {disease_info['times_per_day']}\n"
        
        # Side effects
        treatment_info_text += f"**Side Effects**: {disease_info['side_effects']}\n"
        
        # Lab tests
        treatment_info_text += "**Recommended Lab Tests**:\n"
        for test in disease_info['lab_tests']:
            treatment_info_text += f"- {test}\n"
        
        # Display the treatment information in the label
        treatment_label.config(text=treatment_info_text)
        treatment_label.grid(row=11, column=0, columnspan=2, pady=10)

        # Speak the treatment information empathetically
        speak(f"Now, let me explain the treatment information for {selected_disease}:")
        speak(f"Here’s a brief overview: {disease_info['description']}")
        speak(f"Your prescribed dose is {disease_info['dose']}. This will be taken {disease_info['times_per_day']} times a day.")
        speak(f"Please follow the prescribed duration: {disease_info['duration']}.")
        speak(f"Be aware that there could be some side effects like {', '.join(disease_info['side_effects'])}.")
        speak("The recommended lab tests include:")
        for test in disease_info['lab_tests']:
            speak(f"- {test}")

        speak("Would you be interested in sharing your experience with others on social media? It helps others who may be going through similar challenges. Of course, this is entirely up to you.")


# Function to toggle full screen mode
def toggle_fullscreen(event=None):
    global is_fullscreen
    is_fullscreen = not is_fullscreen
    root.attributes('-fullscreen', is_fullscreen)

# Initialize the Tkinter window
root = tk.Tk()
root.title("Health Assistant")

# Set the window to full screen initially
is_fullscreen = True
root.attributes('-fullscreen', is_fullscreen)

# Option to toggle full screen when pressing the Escape key
root.bind("<Escape>", toggle_fullscreen)

# Font settings for the UI components
font_settings = ("Arial", 12)

# Create login frame
login_frame = tk.Frame(root)
login_frame.pack(pady=20)

# Username and password entry
entry_username = tk.Entry(login_frame, font=font_settings)
entry_username.pack(pady=5)

entry_password = tk.Entry(login_frame, font=font_settings, show="*")
entry_password.pack(pady=5)

# Login button
login_button = tk.Button(login_frame, text="Login", command=on_login, font=font_settings)
login_button.pack(pady=5)

# Payment frame
payment_frame = tk.Frame(root)
payment_label = tk.Label(payment_frame, text="Please make a $10 payment via Google Pay to leena.nandi@gmail.com", font=font_settings)
payment_label.pack(pady=10)
payment_confirm_button = tk.Button(payment_frame, text="Payment Confirmed", command=confirm_payment, font=font_settings)
payment_confirm_button.pack(pady=10)

# Main feed frame (hidden initially)
main_feed = tk.Frame(root)

# Patient information labels and entry fields
entry_patient_name = tk.Entry(main_feed, font=font_settings)
entry_patient_name.grid(row=0, column=1, pady=5)

entry_patient_age = tk.Entry(main_feed, font=font_settings)
entry_patient_age.grid(row=1, column=1, pady=5)

entry_patient_weight = tk.Entry(main_feed, font=font_settings)
entry_patient_weight.grid(row=2, column=1, pady=5)

entry_patient_height = tk.Entry(main_feed, font=font_settings)
entry_patient_height.grid(row=3, column=1, pady=5)

entry_patient_dob = tk.Entry(main_feed, font=font_settings)
entry_patient_dob.grid(row=4, column=1, pady=5)

entry_patient_address = tk.Entry(main_feed, font=font_settings)
entry_patient_address.grid(row=5, column=1, pady=5)

entry_patient_blood_group = tk.Entry(main_feed, font=font_settings)
entry_patient_blood_group.grid(row=6, column=1, pady=5)

entry_patient_email = tk.Entry(main_feed, font=font_settings)
entry_patient_email.grid(row=7, column=1, pady=5)

# Submit patient data button
submit_button = tk.Button(main_feed, text="Submit Data", command=submit_patient_data, font=font_settings)
submit_button.grid(row=8, column=0, columnspan=2, pady=10)

# Disease dropdown
disease_var = tk.StringVar()
disease_dropdown = tk.OptionMenu(main_feed, disease_var, *disease_dict.keys())
disease_dropdown.grid(row=9, column=0, pady=10)

# Button to show treatment information
disease_info_button = tk.Button(main_feed, text="Show Treatment Information", command=show_treatment_info, font=font_settings)
disease_info_button.grid(row=10, column=0, columnspan=2, pady=10)

# Label for treatment info
treatment_label = tk.Label(main_feed, text="", font=font_settings)
treatment_label.grid(row=11, column=0, columnspan=2, pady=10)

root.mainloop()



# In[3]:


import tkinter as tk
import json
import os
from datetime import datetime
import pyttsx3

# Initialize speech engine
engine = pyttsx3.init()

# Function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Disease dictionary with treatment information
disease_dict = {

    "Acquired Immunodeficiency Syndrome (AIDS)": {
        "description": (
            "Acquired Immunodeficiency Syndrome (AIDS) is a disease caused by the Human Immunodeficiency Virus (HIV). "
            "HIV attacks the body's immune system, weakening it over time. The virus primarily targets CD4 cells, which are crucial for immunity. "
            "As HIV progresses, the body becomes more vulnerable to infections and certain cancers. "
            "HIV is transmitted through blood, semen, vaginal fluids, and breast milk. "
            "Without treatment, HIV can lead to AIDS, the final and most severe stage of HIV infection. "
            "At this stage, the immune system is severely damaged, and the person is at high risk for opportunistic infections. "
            "Common symptoms of AIDS include weight loss, chronic diarrhea, and fatigue. "
            "While there is no cure for AIDS, antiretroviral therapy (ART) can slow the progression of the disease. "
            "ART helps lower the amount of HIV in the blood, allowing people with HIV to live longer and healthier lives."
        ),
        "medicine": "Tenofovir",
        "dose": "300 mg once a day",
        "times_per_day": "Once a day",
        "body_weight": "Dose based on individual case, usually not weight-based",
        "lab_tests": [
            "CD4 count", "HIV RNA test"
        ],
        "side_effects": [
            "Nausea", "Headache", "Diarrhea", "Fatigue", "Liver damage"
        ]
    },

    "Dementia": {
        "description": "Dementia is a decline in cognitive function that affects memory, thinking, and daily functioning.",
        "medicine": "Cholinesterase inhibitors (e.g., Donepezil), Memantine",
        "dose": "Donepezil: 5-10 mg daily",
        "times_per_day": "Once daily",
        "side_effects": {
            "Donepezil": ["Diarrhea", "Nausea", "Dizziness", "Insomnia"],
            "Memantine": ["Dizziness", "Confusion", "Headache", "Constipation"]
        },
        "lab_tests": ["Mental status exam", "MRI of the brain"]
    }
    # Add more diseases here...
}

# File to store patient data
patient_data_file = "patient_data.json"

# Function to load patient data from a file
def load_patient_data():
    if os.path.exists(patient_data_file):
        with open(patient_data_file, "r") as file:
            return json.load(file)
    return None

# Function to save patient data to a file
def save_patient_data(data):
    with open(patient_data_file, "w") as file:
        json.dump(data, file)

# Function to simulate login process
def on_login():
    username = entry_username.get()
    password = entry_password.get()
    
    stored_username = "Andromeda"  # Example username
    stored_password = "Galaxy"  # Example password

    if username == stored_username and password == stored_password:
        speak("Welcome back, dear patient. It’s so good to have you here today. Your login was successful.")
        speak("Ownership of data is completely yours. We respect your privacy")
        speak("Before we move on, there is a small payment of $10 to be made via Google Pay to leena.nandi@gmail.com.")
        speak("Once you’ve completed that, please let me know and we can continue with the next steps.")
        payment_frame.pack(pady=20)
        login_frame.pack_forget()
    else:
        speak("Oh no! It seems like the username or password you entered might be incorrect. Please take your time and double-check. I’m here to help you.")

# Function to confirm payment
def confirm_payment():
    speak("Thank you for your payment. Let’s continue.")
    payment_frame.pack_forget()
    main_feed.pack(pady=20)
    patient_data = load_patient_data()
    if patient_data:
        entry_patient_name.insert(0, patient_data["name"])
        entry_patient_age.insert(0, patient_data["age"])
        entry_patient_weight.insert(0, patient_data["weight"])
        entry_patient_height.insert(0, patient_data["height"])
        entry_patient_dob.insert(0, patient_data["dob"])
        entry_patient_address.insert(0, patient_data["address"])
        entry_patient_blood_group.insert(0, patient_data["blood_group"])
        entry_patient_email.insert(0, patient_data["email"])

# Function to submit patient data
def submit_patient_data():
    patient_data = {
        "name": entry_patient_name.get(),
        "age": entry_patient_age.get(),
        "weight": entry_patient_weight.get(),
        "height": entry_patient_height.get(),
        "dob": entry_patient_dob.get(),
        "address": entry_patient_address.get(),
        "blood_group": entry_patient_blood_group.get(),
        "email": entry_patient_email.get(),
        "date_of_visit": datetime.today().strftime('%Y-%m-%d')
    }
    
    save_patient_data(patient_data)
    speak("Thank you so much for sharing your information. It’s been successfully saved. You’re doing wonderfully! Please take your time and relax while I prepare the next steps for you.")
    speak("Now, if you’d like, I can provide you with detailed information about your treatment options and any medical advice you might need.")
    
    disease_input.pack(pady=10)
    disease_info_button.pack(pady=10)

# Function to show treatment information for the selected disease
def show_treatment_info():
    selected_disease = disease_var.get()
    
    if selected_disease in disease_dict:
        disease_info = disease_dict[selected_disease]
        
        # Construct the treatment info text with labels
        treatment_info_text = f"**Disease: {selected_disease}**\n\n"
        treatment_info_text += f"**Description of Disease**: {disease_info['description']}\n\n"
        
        # Dose
        treatment_info_text += f"**Dose**: {disease_info['dose']}\n"
        
        # Times per day
        treatment_info_text += f"**Times per Day**: {disease_info['times_per_day']}\n"
        
        # Side effects
        treatment_info_text += f"**Side Effects**: {', '.join(disease_info['side_effects'])}\n"
        
        # Lab tests
        treatment_info_text += "**Recommended Lab Tests**:\n"
        for test in disease_info['lab_tests']:
            treatment_info_text += f"- {test}\n"
        
        # Display the treatment information in the label
        treatment_label.config(text=treatment_info_text)
        treatment_label.grid(row=11, column=0, columnspan=2, pady=10)

        # Apply text wrapping and center alignment
        treatment_label.config(
            anchor="center",  # This centers the text within the label
            justify="left",  # This justifies the text to the left (wrapping within the label)
            wraplength=450,   # Wrap text after 450 pixels (~6 inches)
            font=("Arial", 12)  # Set the font for better readability
        )

        # Speak the treatment information empathetically
        speak(f"Now, let me explain the treatment information for {selected_disease}:")
        speak(f"Here’s a brief overview: {disease_info['description']}")
        speak(f"Your prescribed dose is {disease_info['dose']}. This will be taken {disease_info['times_per_day']} times a day.")
        speak(f"Please follow the prescribed duration: {disease_info['duration']}.")
        speak(f"Be aware that there could be some side effects like {', '.join(disease_info['side_effects'])}.")
        speak("The recommended lab tests include:")
        for test in disease_info['lab_tests']:
            speak(f"- {test}")

        speak("Would you be interested in sharing your experience with others on social media? It helps others who may be going through similar challenges. Of course, this is entirely up to you.")

# Function to toggle full screen mode
def toggle_fullscreen(event=None):
    global is_fullscreen
    is_fullscreen = not is_fullscreen
    root.attributes('-fullscreen', is_fullscreen)

# Initialize the Tkinter window
root = tk.Tk()
root.title("Health Assistant")

# Set the window to full screen initially
is_fullscreen = True
root.attributes('-fullscreen', is_fullscreen)

# Option to toggle full screen when pressing the Escape key
root.bind("<Escape>", toggle_fullscreen)

# Font settings for the UI components
font_settings = ("Arial", 12)

# Create login frame
login_frame = tk.Frame(root)
login_frame.pack(pady=20)

# Username and password entry
entry_username = tk.Entry(login_frame, font=font_settings)
entry_username.pack(pady=5)

entry_password = tk.Entry(login_frame, font=font_settings, show="*")
entry_password.pack(pady=5)

# Login button
login_button = tk.Button(login_frame, text="Login", command=on_login, font=font_settings)
login_button.pack(pady=5)

# Payment frame
payment_frame = tk.Frame(root)
payment_label = tk.Label(payment_frame, text="Please make a $10 payment via Google Pay to leena.nandi@gmail.com", font=font_settings)
payment_label.pack(pady=10)
payment_confirm_button = tk.Button(payment_frame, text="Payment Confirmed", command=confirm_payment, font=font_settings)
payment_confirm_button.pack(pady=10)

# Main feed frame (hidden initially)
main_feed = tk.Frame(root)

# Patient information labels and entry fields
label_patient_name = tk.Label(main_feed, text="Patient Name:", font=font_settings)
label_patient_name.grid(row=0, column=0, pady=5, sticky="e")

entry_patient_name = tk.Entry(main_feed, font=font_settings)
entry_patient_name.grid(row=0, column=1, pady=5)

label_patient_age = tk.Label(main_feed, text="Age:", font=font_settings)
label_patient_age.grid(row=1, column=0, pady=5, sticky="e")

entry_patient_age = tk.Entry(main_feed, font=font_settings)
entry_patient_age.grid(row=1, column=1, pady=5)

label_patient_weight = tk.Label(main_feed, text="Weight (kg):", font=font_settings)
label_patient_weight.grid(row=2, column=0, pady=5, sticky="e")

entry_patient_weight = tk.Entry(main_feed, font=font_settings)
entry_patient_weight.grid(row=2, column=1, pady=5)

label_patient_height = tk.Label(main_feed, text="Height (cm):", font=font_settings)
label_patient_height.grid(row=3, column=0, pady=5, sticky="e")

entry_patient_height = tk.Entry(main_feed, font=font_settings)
entry_patient_height.grid(row=3, column=1, pady=5)

label_patient_dob = tk.Label(main_feed, text="Date of Birth (YYYY-MM-DD):", font=font_settings)
label_patient_dob.grid(row=4, column=0, pady=5, sticky="e")

entry_patient_dob = tk.Entry(main_feed, font=font_settings)
entry_patient_dob.grid(row=4, column=1, pady=5)

label_patient_address = tk.Label(main_feed, text="Address:", font=font_settings)
label_patient_address.grid(row=5, column=0, pady=5, sticky="e")

entry_patient_address = tk.Entry(main_feed, font=font_settings)
entry_patient_address.grid(row=5, column=1, pady=5)

label_patient_blood_group = tk.Label(main_feed, text="Blood Group:", font=font_settings)
label_patient_blood_group.grid(row=6, column=0, pady=5, sticky="e")

entry_patient_blood_group = tk.Entry(main_feed, font=font_settings)
entry_patient_blood_group.grid(row=6, column=1, pady=5)

label_patient_email = tk.Label(main_feed, text="Email Address:", font=font_settings)
label_patient_email.grid(row=7, column=0, pady=5, sticky="e")

entry_patient_email = tk.Entry(main_feed, font=font_settings)
entry_patient_email.grid(row=7, column=1, pady=5)

# Submit patient data button
submit_button = tk.Button(main_feed, text="Submit Data", command=submit_patient_data, font=font_settings)
submit_button.grid(row=8, column=0, columnspan=2, pady=10)

# Disease dropdown
disease_var = tk.StringVar()
disease_dropdown = tk.OptionMenu(main_feed, disease_var, *disease_dict.keys())
disease_dropdown.grid(row=9, column=0, pady=10)

# Button to show treatment information
disease_info_button = tk.Button(main_feed, text="Show Treatment Information", command=show_treatment_info, font=font_settings)
disease_info_button.grid(row=10, column=0, columnspan=2, pady=10)

# Label for treatment info
treatment_label = tk.Label(main_feed, text="", font=font_settings)
treatment_label.grid(row=11, column=0, columnspan=2, pady=10)

root.mainloop()


# In[ ]:




