{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3e8062fe-c880-494d-87b8-29e51a3c6011",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'datasets/symtoms_df.csv'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 13\u001b[0m\n\u001b[0;32m      8\u001b[0m app \u001b[38;5;241m=\u001b[39m Flask(\u001b[38;5;18m__name__\u001b[39m)\n\u001b[0;32m     12\u001b[0m \u001b[38;5;66;03m# load databasedataset===================================\u001b[39;00m\n\u001b[1;32m---> 13\u001b[0m sym_des \u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mread_csv(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdatasets/symtoms_df.csv\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m     14\u001b[0m precautions \u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mread_csv(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdatasets/precautions_df.csv\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m     15\u001b[0m workout \u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mread_csv(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdatasets/workout_df.csv\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\parsers\\readers.py:1026\u001b[0m, in \u001b[0;36mread_csv\u001b[1;34m(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, date_format, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, encoding_errors, dialect, on_bad_lines, delim_whitespace, low_memory, memory_map, float_precision, storage_options, dtype_backend)\u001b[0m\n\u001b[0;32m   1013\u001b[0m kwds_defaults \u001b[38;5;241m=\u001b[39m _refine_defaults_read(\n\u001b[0;32m   1014\u001b[0m     dialect,\n\u001b[0;32m   1015\u001b[0m     delimiter,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m   1022\u001b[0m     dtype_backend\u001b[38;5;241m=\u001b[39mdtype_backend,\n\u001b[0;32m   1023\u001b[0m )\n\u001b[0;32m   1024\u001b[0m kwds\u001b[38;5;241m.\u001b[39mupdate(kwds_defaults)\n\u001b[1;32m-> 1026\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m _read(filepath_or_buffer, kwds)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\parsers\\readers.py:620\u001b[0m, in \u001b[0;36m_read\u001b[1;34m(filepath_or_buffer, kwds)\u001b[0m\n\u001b[0;32m    617\u001b[0m _validate_names(kwds\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnames\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m))\n\u001b[0;32m    619\u001b[0m \u001b[38;5;66;03m# Create the parser.\u001b[39;00m\n\u001b[1;32m--> 620\u001b[0m parser \u001b[38;5;241m=\u001b[39m TextFileReader(filepath_or_buffer, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwds)\n\u001b[0;32m    622\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m chunksize \u001b[38;5;129;01mor\u001b[39;00m iterator:\n\u001b[0;32m    623\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m parser\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\parsers\\readers.py:1620\u001b[0m, in \u001b[0;36mTextFileReader.__init__\u001b[1;34m(self, f, engine, **kwds)\u001b[0m\n\u001b[0;32m   1617\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhas_index_names\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m=\u001b[39m kwds[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhas_index_names\u001b[39m\u001b[38;5;124m\"\u001b[39m]\n\u001b[0;32m   1619\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles: IOHandles \u001b[38;5;241m|\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[1;32m-> 1620\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_engine \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_make_engine(f, \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mengine)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\parsers\\readers.py:1880\u001b[0m, in \u001b[0;36mTextFileReader._make_engine\u001b[1;34m(self, f, engine)\u001b[0m\n\u001b[0;32m   1878\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb\u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;129;01min\u001b[39;00m mode:\n\u001b[0;32m   1879\u001b[0m         mode \u001b[38;5;241m+\u001b[39m\u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m-> 1880\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles \u001b[38;5;241m=\u001b[39m get_handle(\n\u001b[0;32m   1881\u001b[0m     f,\n\u001b[0;32m   1882\u001b[0m     mode,\n\u001b[0;32m   1883\u001b[0m     encoding\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mencoding\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m),\n\u001b[0;32m   1884\u001b[0m     compression\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcompression\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m),\n\u001b[0;32m   1885\u001b[0m     memory_map\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmemory_map\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mFalse\u001b[39;00m),\n\u001b[0;32m   1886\u001b[0m     is_text\u001b[38;5;241m=\u001b[39mis_text,\n\u001b[0;32m   1887\u001b[0m     errors\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mencoding_errors\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstrict\u001b[39m\u001b[38;5;124m\"\u001b[39m),\n\u001b[0;32m   1888\u001b[0m     storage_options\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstorage_options\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m),\n\u001b[0;32m   1889\u001b[0m )\n\u001b[0;32m   1890\u001b[0m \u001b[38;5;28;01massert\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[0;32m   1891\u001b[0m f \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles\u001b[38;5;241m.\u001b[39mhandle\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\common.py:873\u001b[0m, in \u001b[0;36mget_handle\u001b[1;34m(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)\u001b[0m\n\u001b[0;32m    868\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(handle, \u001b[38;5;28mstr\u001b[39m):\n\u001b[0;32m    869\u001b[0m     \u001b[38;5;66;03m# Check whether the filename is to be opened in binary mode.\u001b[39;00m\n\u001b[0;32m    870\u001b[0m     \u001b[38;5;66;03m# Binary mode does not support 'encoding' and 'newline'.\u001b[39;00m\n\u001b[0;32m    871\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m ioargs\u001b[38;5;241m.\u001b[39mencoding \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb\u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;129;01min\u001b[39;00m ioargs\u001b[38;5;241m.\u001b[39mmode:\n\u001b[0;32m    872\u001b[0m         \u001b[38;5;66;03m# Encoding\u001b[39;00m\n\u001b[1;32m--> 873\u001b[0m         handle \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mopen\u001b[39m(\n\u001b[0;32m    874\u001b[0m             handle,\n\u001b[0;32m    875\u001b[0m             ioargs\u001b[38;5;241m.\u001b[39mmode,\n\u001b[0;32m    876\u001b[0m             encoding\u001b[38;5;241m=\u001b[39mioargs\u001b[38;5;241m.\u001b[39mencoding,\n\u001b[0;32m    877\u001b[0m             errors\u001b[38;5;241m=\u001b[39merrors,\n\u001b[0;32m    878\u001b[0m             newline\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    879\u001b[0m         )\n\u001b[0;32m    880\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m    881\u001b[0m         \u001b[38;5;66;03m# Binary mode\u001b[39;00m\n\u001b[0;32m    882\u001b[0m         handle \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mopen\u001b[39m(handle, ioargs\u001b[38;5;241m.\u001b[39mmode)\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'datasets/symtoms_df.csv'"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, render_template, jsonify  # Import jsonify\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import pickle\n",
    "\n",
    "\n",
    "# flask app\n",
    "app = Flask(__name__)\n",
    "\n",
    "\n",
    "\n",
    "# load databasedataset===================================\n",
    "sym_des = pd.read_csv(\"datasets/symtoms_df.csv\")\n",
    "precautions = pd.read_csv(\"datasets/precautions_df.csv\")\n",
    "workout = pd.read_csv(\"datasets/workout_df.csv\")\n",
    "description = pd.read_csv(\"datasets/description.csv\")\n",
    "medications = pd.read_csv('datasets/medications.csv')\n",
    "diets = pd.read_csv(\"datasets/diets.csv\")\n",
    "\n",
    "\n",
    "# load model===========================================\n",
    "svc = pickle.load(open('models/svc.pkl','rb'))\n",
    "\n",
    "\n",
    "#============================================================\n",
    "# custome and helping functions\n",
    "#==========================helper funtions================\n",
    "def helper(dis):\n",
    "    desc = description[description['Disease'] == dis]['Description']\n",
    "    desc = \" \".join([w for w in desc])\n",
    "\n",
    "    pre = precautions[precautions['Disease'] == dis][['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']]\n",
    "    pre = [col for col in pre.values]\n",
    "\n",
    "    med = medications[medications['Disease'] == dis]['Medication']\n",
    "    med = [med for med in med.values]\n",
    "\n",
    "    die = diets[diets['Disease'] == dis]['Diet']\n",
    "    die = [die for die in die.values]\n",
    "\n",
    "    wrkout = workout[workout['disease'] == dis] ['workout']\n",
    "\n",
    "\n",
    "    return desc,pre,med,die,wrkout\n",
    "\n",
    "symptoms_dict = {'itching': 0, 'skin_rash': 1, 'nodal_skin_eruptions': 2, 'continuous_sneezing': 3, 'shivering': 4, 'chills': 5, 'joint_pain': 6, 'stomach_pain': 7, 'acidity': 8, 'ulcers_on_tongue': 9, 'muscle_wasting': 10, 'vomiting': 11, 'burning_micturition': 12, 'spotting_ urination': 13, 'fatigue': 14, 'weight_gain': 15, 'anxiety': 16, 'cold_hands_and_feets': 17, 'mood_swings': 18, 'weight_loss': 19, 'restlessness': 20, 'lethargy': 21, 'patches_in_throat': 22, 'irregular_sugar_level': 23, 'cough': 24, 'high_fever': 25, 'sunken_eyes': 26, 'breathlessness': 27, 'sweating': 28, 'dehydration': 29, 'indigestion': 30, 'headache': 31, 'yellowish_skin': 32, 'dark_urine': 33, 'nausea': 34, 'loss_of_appetite': 35, 'pain_behind_the_eyes': 36, 'back_pain': 37, 'constipation': 38, 'abdominal_pain': 39, 'diarrhoea': 40, 'mild_fever': 41, 'yellow_urine': 42, 'yellowing_of_eyes': 43, 'acute_liver_failure': 44, 'fluid_overload': 45, 'swelling_of_stomach': 46, 'swelled_lymph_nodes': 47, 'malaise': 48, 'blurred_and_distorted_vision': 49, 'phlegm': 50, 'throat_irritation': 51, 'redness_of_eyes': 52, 'sinus_pressure': 53, 'runny_nose': 54, 'congestion': 55, 'chest_pain': 56, 'weakness_in_limbs': 57, 'fast_heart_rate': 58, 'pain_during_bowel_movements': 59, 'pain_in_anal_region': 60, 'bloody_stool': 61, 'irritation_in_anus': 62, 'neck_pain': 63, 'dizziness': 64, 'cramps': 65, 'bruising': 66, 'obesity': 67, 'swollen_legs': 68, 'swollen_blood_vessels': 69, 'puffy_face_and_eyes': 70, 'enlarged_thyroid': 71, 'brittle_nails': 72, 'swollen_extremeties': 73, 'excessive_hunger': 74, 'extra_marital_contacts': 75, 'drying_and_tingling_lips': 76, 'slurred_speech': 77, 'knee_pain': 78, 'hip_joint_pain': 79, 'muscle_weakness': 80, 'stiff_neck': 81, 'swelling_joints': 82, 'movement_stiffness': 83, 'spinning_movements': 84, 'loss_of_balance': 85, 'unsteadiness': 86, 'weakness_of_one_body_side': 87, 'loss_of_smell': 88, 'bladder_discomfort': 89, 'foul_smell_of urine': 90, 'continuous_feel_of_urine': 91, 'passage_of_gases': 92, 'internal_itching': 93, 'toxic_look_(typhos)': 94, 'depression': 95, 'irritability': 96, 'muscle_pain': 97, 'altered_sensorium': 98, 'red_spots_over_body': 99, 'belly_pain': 100, 'abnormal_menstruation': 101, 'dischromic _patches': 102, 'watering_from_eyes': 103, 'increased_appetite': 104, 'polyuria': 105, 'family_history': 106, 'mucoid_sputum': 107, 'rusty_sputum': 108, 'lack_of_concentration': 109, 'visual_disturbances': 110, 'receiving_blood_transfusion': 111, 'receiving_unsterile_injections': 112, 'coma': 113, 'stomach_bleeding': 114, 'distention_of_abdomen': 115, 'history_of_alcohol_consumption': 116, 'fluid_overload.1': 117, 'blood_in_sputum': 118, 'prominent_veins_on_calf': 119, 'palpitations': 120, 'painful_walking': 121, 'pus_filled_pimples': 122, 'blackheads': 123, 'scurring': 124, 'skin_peeling': 125, 'silver_like_dusting': 126, 'small_dents_in_nails': 127, 'inflammatory_nails': 128, 'blister': 129, 'red_sore_around_nose': 130, 'yellow_crust_ooze': 131}\n",
    "diseases_list = {15: 'Fungal infection', 4: 'Allergy', 16: 'GERD', 9: 'Chronic cholestasis', 14: 'Drug Reaction', 33: 'Peptic ulcer diseae', 1: 'AIDS', 12: 'Diabetes ', 17: 'Gastroenteritis', 6: 'Bronchial Asthma', 23: 'Hypertension ', 30: 'Migraine', 7: 'Cervical spondylosis', 32: 'Paralysis (brain hemorrhage)', 28: 'Jaundice', 29: 'Malaria', 8: 'Chicken pox', 11: 'Dengue', 37: 'Typhoid', 40: 'hepatitis A', 19: 'Hepatitis B', 20: 'Hepatitis C', 21: 'Hepatitis D', 22: 'Hepatitis E', 3: 'Alcoholic hepatitis', 36: 'Tuberculosis', 10: 'Common Cold', 34: 'Pneumonia', 13: 'Dimorphic hemmorhoids(piles)', 18: 'Heart attack', 39: 'Varicose veins', 26: 'Hypothyroidism', 24: 'Hyperthyroidism', 25: 'Hypoglycemia', 31: 'Osteoarthristis', 5: 'Arthritis', 0: '(vertigo) Paroymsal  Positional Vertigo', 2: 'Acne', 38: 'Urinary tract infection', 35: 'Psoriasis', 27: 'Impetigo'}\n",
    "\n",
    "# Model Prediction function\n",
    "def get_predicted_value(patient_symptoms):\n",
    "    input_vector = np.zeros(len(symptoms_dict))\n",
    "    for item in patient_symptoms:\n",
    "        input_vector[symptoms_dict[item]] = 1\n",
    "    return diseases_list[svc.predict([input_vector])[0]]\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "# creating routes========================================\n",
    "\n",
    "\n",
    "@app.route(\"/\")\n",
    "def index():\n",
    "    return render_template(\"index.html\")\n",
    "\n",
    "# Define a route for the home page\n",
    "@app.route('/predict', methods=['GET', 'POST'])\n",
    "def home():\n",
    "    if request.method == 'POST':\n",
    "        symptoms = request.form.get('symptoms')\n",
    "        # mysysms = request.form.get('mysysms')\n",
    "        # print(mysysms)\n",
    "        print(symptoms)\n",
    "        if symptoms ==\"Symptoms\":\n",
    "            message = \"Please either write symptoms or you have written misspelled symptoms\"\n",
    "            return render_template('index.html', message=message)\n",
    "        else:\n",
    "\n",
    "            # Split the user's input into a list of symptoms (assuming they are comma-separated)\n",
    "            user_symptoms = [s.strip() for s in symptoms.split(',')]\n",
    "            # Remove any extra characters, if any\n",
    "            user_symptoms = [symptom.strip(\"[]' \") for symptom in user_symptoms]\n",
    "            predicted_disease = get_predicted_value(user_symptoms)\n",
    "            dis_des, precautions, medications, rec_diet, workout = helper(predicted_disease)\n",
    "\n",
    "            my_precautions = []\n",
    "            for i in precautions[0]:\n",
    "                my_precautions.append(i)\n",
    "\n",
    "            return render_template('index.html', predicted_disease=predicted_disease, dis_des=dis_des,\n",
    "                                   my_precautions=my_precautions, medications=medications, my_diet=rec_diet,\n",
    "                                   workout=workout)\n",
    "\n",
    "    return render_template('index.html')\n",
    "\n",
    "\n",
    "\n",
    "# about view funtion and path\n",
    "@app.route('/about')\n",
    "def about():\n",
    "    return render_template(\"about.html\")\n",
    "# contact view funtion and path\n",
    "@app.route('/contact')\n",
    "def contact():\n",
    "    return render_template(\"contact.html\")\n",
    "\n",
    "# developer view funtion and path\n",
    "@app.route('/developer')\n",
    "def developer():\n",
    "    return render_template(\"developer.html\")\n",
    "\n",
    "# about view funtion and path\n",
    "@app.route('/blog')\n",
    "def blog():\n",
    "    return render_template(\"blog.html\")\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "\n",
    "    app.run(debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e5bff481-4667-435e-9847-bc8a5f7abbdf",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
