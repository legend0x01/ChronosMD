import json
import random
import os

# Set seed for reproducibility while generating realistic authentic records
random.seed(42)

# Diverse Indian Names (First + Last)
male_first_names = [
    "Rajesh", "Aarav", "Vikram", "Suresh", "Amit", "Rohan", "Sunil", "Pradeep",
    "Mohammed", "Farhan", "Gurpreet", "Manish", "Karthik", "Sanjay", "Anil",
    "Deepak", "Venkat", "Arjun", "Harish", "Nikhil", "Praveen", "Ramesh",
    "Gaurav", "Abhishek", "Satish", "Devendra", "Vipin", "Mukesh", "Ravindra",
    "Bhavin", "Tanmay", "Siddharth", "Ashwin", "Alok", "Chirag", "Dinesh",
    "Harpreet", "Irfan", "Javed", "Kishore", "Lalit", "Manoj", "Naresh",
    "Omkar", "Pankaj", "Raghav", "Sachin", "Tushar", "Umesh", "Yogesh"
]

female_first_names = [
    "Priya", "Sunita", "Ananya", "Deepa", "Kavita", "Fatima", "Lakshmi", "Meera",
    "Pooja", "Shweta", "Ritu", "Neha", "Divya", "Swati", "Rashmi",
    "Aparna", "Geeta", "Rekha", "Sangeeta", "Nandini", "Anjali", "Pallavi",
    "Smita", "Radhika", "Shilpa", "Archana", "Sneha", "Kalyani", "Jyoti",
    "Bhavna", "Tanvi", "Preeti", "Usha", "Vandana", "Zoya", "Ayesha",
    "Chandana", "Damini", "Esha", "Gauri", "Hemalata", "Indira", "Kiran",
    "Lata", "Madhavi", "Nalini", "Padma", "Rupal", "Sarita", "Vidya"
]

last_names = [
    "Sharma", "Verma", "Patel", "Nair", "Iyer", "Mukherjee", "Chatterjee", "Deshmukh",
    "Kulkarni", "Reddy", "Rao", "Chowdhury", "Singh", "Gupta", "Malhotra", "Kapoor",
    "Agarwal", "Bhatia", "Joshi", "Bhattacharya", "Menon", "Pillai", "Hegde", "Shetty",
    "Khan", "Qureshi", "Ansari", "Mirza", "Sandhu", "Dhillon", "Gill", "Sethi",
    "Bansal", "Mittal", "Goyal", "Tripathi", "Pandey", "Mishra", "Shukla", "Tiwari",
    "Mehta", "Shah", "Parekh", "Desai", "Patil", "Pawar", "Shinde", "Gaikwad",
    "Swaminathan", "Venkatesan", "Balasubramanian", "Krishnamurthy", "Nambiar"
]

# Indian Cities with Real Localities and Pin Codes
cities_data = [
    {
        "city": "Bengaluru", "state": "Karnataka",
        "localities": [
            ("Indiranagar, 12th Main, 100ft Road", "560038"),
            ("Koramangala, 4th Block, 80 Feet Road", "560034"),
            ("Jayanagar, 9th Block, South End Road", "560069"),
            ("Whitefield, ITPL Main Road, Hope Farm", "560066"),
            ("Malleshwaram, 8th Cross, Margosa Road", "560003"),
            ("HSR Layout, Sector 2, 27th Main", "560102"),
            ("Basavanagudi, Bull Temple Road", "560004")
        ],
        "hospitals": [
            ("MANIPAL HOSPITAL BENGALURU", "98 HAL Old Airport Road, Kodihalli, Bengaluru 560017"),
            ("APOLLO HOSPITALS BANNERGHATTA", "154/11 Bannerghatta Main Rd, Opp IIMB, Bengaluru 560076"),
            ("FORTIS HOSPITAL CUNNINGHAM ROAD", "14 Cunningham Rd, Vasanth Nagar, Bengaluru 560052"),
            ("NARAYANA INSTITUTE OF CARDIAC SCIENCES", "258/A, Bommasandra Ind. Area, Anekal Taluk, Bengaluru 560099")
        ],
        "labs": [
            ("ANAND DIAGNOSTIC LABORATORY (NEUBERG)", "Bowring Tower, Shivaji Nagar, Bengaluru 560001"),
            ("DR LAL PATHLABS KORAMANGALA", "No. 412, 1st Cross, Koramangala 5th Block, Bengaluru 560095"),
            ("METROPOLIS HEALTHCARE INDIRANAGAR", "CMH Road, Indiranagar 2nd Stage, Bengaluru 560038")
        ]
    },
    {
        "city": "Mumbai", "state": "Maharashtra",
        "localities": [
            ("Andheri West, Lokhandwala Complex", "400053"),
            ("Bandra West, Hill Road, Near Bandstand", "400050"),
            ("Dadar West, Shivaji Park, Gokhale Road", "400028"),
            ("Powai, Hiranandani Gardens, Central Ave", "400076"),
            ("Goregaon East, Oberoi Woods, A.K. Vaidya Marg", "400063"),
            ("Chembur East, Diamond Garden, Central Ave", "400071"),
            ("Vile Parle East, Nehru Road, Near Station", "400057")
        ],
        "hospitals": [
            ("LILAVATI HOSPITAL & RESEARCH CENTRE", "A-791, Bandra Reclamation, Bandra West, Mumbai 400050"),
            ("KOKILABEN DHIRUBHAI AMBANI HOSPITAL", "Rao Saheb Achutrao Patwardhan Marg, Four Bungalows, Mumbai 400053"),
            ("HINDUJA NATIONAL HOSPITAL", "Veer Savarkar Marg, Mahim West, Mumbai 400016"),
            ("TATA MEMORIAL HOSPITAL", "Dr. E Borges Road, Parel, Mumbai 400012")
        ],
        "labs": [
            ("SUBURBAN DIAGNOSTICS MUMBAI", "Aston Building, Sundervan Complex, Andheri West, Mumbai 400053"),
            ("METROPOLIS HEALTHCARE WORLI", "Kohinoor City, Commercial Bldg 1, Kurla West, Mumbai 400070"),
            ("SRL DIAGNOSTICS BANDRA", "Waterfield Road, Bandra West, Mumbai 400050")
        ]
    },
    {
        "city": "New Delhi", "state": "Delhi-NCR",
        "localities": [
            ("Hauz Khas, Enclave Market, Aurobindo Marg", "110016"),
            ("Lajpat Nagar IV, Dayanand Colony", "110024"),
            ("Dwarka, Sector 12, Pocket 4", "110078"),
            ("Rohini, Sector 9, DC Chowk", "110085"),
            ("Vasant Kunj, Sector B, Pocket 1", "110070"),
            ("Greater Kailash I, M-Block Market", "110048"),
            ("Mayur Vihar Phase 1, Pocket 1", "110091")
        ],
        "hospitals": [
            ("ALL INDIA INSTITUTE OF MEDICAL SCIENCES (AIIMS)", "Sri Aurobindo Marg, Ansari Nagar, New Delhi 110029"),
            ("MAX SUPER SPECIALITY HOSPITAL SAKET", "1, 2 Press Enclave Road, Mandir Marg, Saket, New Delhi 110017"),
            ("SIR GANGA RAM HOSPITAL", "Rajinder Nagar, New Delhi 110060"),
            ("FORTIS ESCORTS HEART INSTITUTE", "Okhla Road, Sukhdev Vihar Metro Station, New Delhi 110025")
        ],
        "labs": [
            ("DR LAL PATHLABS NATIONAL REFERENCE LAB", "Block E, Sector 18, Rohini, New Delhi 110085"),
            ("MAX LAB SERVICES SAKET", "Press Enclave Marg, Saket, New Delhi 110017"),
            ("SRL DIAGNOSTICS CONNAUGHT PLACE", "Barakhamba Road, Connaught Place, New Delhi 110001")
        ]
    },
    {
        "city": "Chennai", "state": "Tamil Nadu",
        "localities": [
            ("T. Nagar, Usman Road, Panagal Park", "600017"),
            ("Adyar, Gandhi Nagar, 2nd Main Road", "600020"),
            ("Anna Nagar West, 2nd Avenue, Shanthi Colony", "600040"),
            ("Mylapore, Luz Church Road, Near Kutchery Rd", "600004"),
            ("Velachery, Bypass Road, Vijayanagar", "600042"),
            ("Nungambakkam, Sterling Road, Mahalingapuram", "600034")
        ],
        "hospitals": [
            ("APOLLO HOSPITALS GREAMS ROAD", "21 Greams Lane, Thousand Lights, Chennai 600006"),
            ("FORTIS MALAR HOSPITAL ADYAR", "52, 1st Main Rd, Gandhi Nagar, Adyar, Chennai 600020"),
            ("MIOT INTERNATIONAL MANAPAKKAM", "4/112 Mount Poonamallee Rd, Manapakkam, Chennai 600089"),
            ("MADRAS MEDICAL MISSION", "4A, Dr J Jayalalithaa Nagar, Mogappair, Chennai 600037")
        ],
        "labs": [
            ("LISTER METROPOLIS LAB CHENNAI", "3 Jagannathan Road, Nungambakkam, Chennai 600034"),
            ("APOLLO DIAGNOSTICS T. NAGAR", "G.N. Chetty Road, T. Nagar, Chennai 600017"),
            ("DR LAL PATHLABS ADYAR", "Lattice Bridge Rd, Adyar, Chennai 600020")
        ]
    },
    {
        "city": "Hyderabad", "state": "Telangana",
        "localities": [
            ("Banjara Hills, Road No. 12, MLA Colony", "500034"),
            ("Jubilee Hills, Road No. 36, Near Peddamma Temple", "500033"),
            ("Madhapur, Hitech City Main Road, Cyber Towers", "500081"),
            ("Kukatpally, KPHB Colony, 4th Phase", "500072"),
            ("Secunderabad, Marredpally West, Nehru Nagar", "500026"),
            ("Gachibowli, Telecom Nagar, Gachibowli Stadium Rd", "500032")
        ],
        "hospitals": [
            ("YASHODA HOSPITALS SOMAJIGUDA", "Raj Bhavan Rd, Matha Nagar, Somajiguda, Hyderabad 500082"),
            ("KIMS HOSPITALS SECUNDERABAD", "1-8-31/1, Minister Rd, Krishna Nagar Colony, Secunderabad 500003"),
            ("APOLLO HOSPITALS JUBILEE HILLS", "Road No. 72, Film Nagar, Jubilee Hills, Hyderabad 500033"),
            ("CARE HOSPITALS BANJARA HILLS", "Road No. 1, Banjara Hills, Hyderabad 500034")
        ],
        "labs": [
            ("VIJAYA DIAGNOSTIC CENTRE HYDERABAD", "3-6-16 & 17, Street No. 19, Himayatnagar, Hyderabad 500029"),
            ("LUCID MEDICAL DIAGNOSTICS BANJARA HILLS", "Road No. 2, Banjara Hills, Hyderabad 500034"),
            ("DR LAL PATHLABS MADHAPUR", "Ayyappa Society Main Rd, Madhapur, Hyderabad 500081")
        ]
    },
    {
        "city": "Kolkata", "state": "West Bengal",
        "localities": [
            ("Salt Lake City, Sector 1, Block CF", "700064"),
            ("Ballygunge, Circular Road, Dover Park", "700019"),
            ("New Town, Action Area 1, Rajarhat", "700156"),
            ("Alipore, Belvedere Road, Near Zoo", "700027"),
            ("Behala, Diamond Harbour Road, Chowrasta", "700034"),
            ("Gariahat, Rashbehari Avenue", "700029")
        ],
        "hospitals": [
            ("AMRI HOSPITALS DHAKURIA", "Block-A, Scheme-L11, P-4&5, Gariahat Rd, Dhakuria, Kolkata 700029"),
            ("APOLLO GLENEAGLES HOSPITALS KOLKATA", "58 Canal Circular Rd, Kadapara, Phool Bagan, Kolkata 700054"),
            ("FORTIS HOSPITAL ANANDAPUR", "730 Anandapur, E.M. Bypass Road, Kolkata 700107"),
            ("PEERLESS HOSPITAL PANCHASAYAR", "360 Panchasayar, Kolkata 700094")
        ],
        "labs": [
            ("SURAKSHA DIAGNOSTICS SALT LAKE", "DD 18/1, Salt Lake City, Sector 1, Kolkata 700064"),
            ("PULSE DIAGNOSTICS BALLYGUNGE", "14A Lansdowne Rd, Ballygunge, Kolkata 700019"),
            ("DR LAL PATHLABS NEW TOWN", "Major Arterial Road, New Town, Kolkata 700156")
        ]
    },
    {
        "city": "Pune", "state": "Maharashtra",
        "localities": [
            ("Kothrud, Paud Road, Near Vanaz", "411038"),
            ("Viman Nagar, Dutta Mandir Chowk", "411014"),
            ("Aundh, ITI Road, DP Road Junction", "411007"),
            ("Baner, Balewadi High Street", "411045"),
            ("Hadapsar, Magarpatta City, Cybercity", "411028"),
            ("Kalyani Nagar, East Avenue", "411006")
        ],
        "hospitals": [
            ("JEHANGIR HOSPITAL PUNE", "32 Sassoon Road, Opposite Pune Railway Station, Pune 411001"),
            ("RUBY HALL CLINIC PUNE", "40 Sassoon Road, Sangamvadi, Pune 411001"),
            ("DEENANATH MANGESHKAR HOSPITAL", "Near Mhatre Bridge, Erandwane, Pune 411004"),
            ("SAHYADRI SUPER SPECIALITY HOSPITAL DECCAN", "Plot No. 30 C, Karve Rd, Deccan Gymkhana, Pune 411004")
        ],
        "labs": [
            ("A.G. DIAGNOSTICS BHANDARKAR ROAD", "Bhandarkar Road, Deccan Gymkhana, Pune 411004"),
            ("GOLWILKAR METROPOLIS LAB PUNE", "Saraswati Heights, Natraj Society, Karve Rd, Pune 411004"),
            ("DR LAL PATHLABS AUNDH", "DP Road, Aundh, Pune 411007")
        ]
    },
    {
        "city": "Ahmedabad", "state": "Gujarat",
        "localities": [
            ("Bodakdev, Judges Bungalow Road", "380054"),
            ("Satellite, Shivranjani Crossroads", "380015"),
            ("Navrangpura, CG Road, Swastik Cross Rd", "380009"),
            ("Vastrapur, Near Vastrapur Lake", "380015"),
            ("Maninagar, Rambaug, Near Station", "380008")
        ],
        "hospitals": [
            ("ZYDUS HOSPITAL AHMEDABAD", "Zydus Hospital Road, SG Highway, Thaltej, Ahmedabad 380054"),
            ("APOLLO HOSPITALS BHAT GANDHINAGAR", "Plot 1A, Bhat GIDC Estate, Gandhinagar 382428"),
            ("STERLING HOSPITALS MEMNAGAR", "Sterling Hospital Rd, Memnagar, Ahmedabad 380052")
        ],
        "labs": [
            ("GREEN CROSS PATHOLOGY LAB", "Mithakhali Six Roads, Navrangpura, Ahmedabad 380006"),
            ("SUVIKAN PATHOLOGY LABORATORY", "Drive In Road, Memnagar, Ahmedabad 380052"),
            ("METROPOLIS HEALTHCARE SATELLITE", "Prernatirth Derasar Rd, Satellite, Ahmedabad 380015")
        ]
    },
    {
        "city": "Lucknow", "state": "Uttar Pradesh",
        "localities": [
            ("Gomti Nagar, Vibhuti Khand", "226010"),
            ("Hazratganj, Ashok Marg, Mayfair", "226001"),
            ("Aliganj, Sector B, Purania Chowk", "226024"),
            ("Indira Nagar, Sector 14, Ring Road", "226016")
        ],
        "hospitals": [
            ("SANJAY GANDHI POSTGRADUATE INSTITUTE (SGPGI)", "Raebareli Road, Lucknow 226014"),
            ("MEDANTA HOSPITAL LUCKNOW", "Sector B, Pocket 1, Amar Shaheed Path, Golf City, Lucknow 226030"),
            ("APOLLO MEDICS SUPER SPECIALITY HOSPITAL", "Sector G, LDA Colony, Kanpur Road, Lucknow 226012")
        ],
        "labs": [
            ("DR LAL PATHLABS HAZRATGANJ", "Sapru Marg, Prem Nagar, Hazratganj, Lucknow 226001"),
            ("CHARAK DIAGNOSTICS GOMTI NAGAR", "Vikas Khand, Gomti Nagar, Lucknow 226010"),
            ("SRL DIAGNOSTICS ALIGANJ", "Sector B, Aliganj, Lucknow 226024")
        ]
    },
    {
        "city": "Kochi", "state": "Kerala",
        "localities": [
            ("Panampilly Nagar, Main Avenue", "682036"),
            ("Edappally, Toll Junction, NH 66", "682024"),
            ("Kakkanad, Infopark Expressway", "682030"),
            ("Marine Drive, Shanmugham Road", "682031")
        ],
        "hospitals": [
            ("AMRITA INSTITUTE OF MEDICAL SCIENCES (AIMS)", "AIMS Ponekkara P.O., Kochi 682041"),
            ("ASTER MEDCITY KOCHI", "Kuttisahib Road, South Chittoor, Cheranallur, Kochi 682027"),
            ("RAJAGIRI HOSPITAL ALUVA", "Near Chunangamvely, Aluva, Kochi 683112")
        ],
        "labs": [
            ("DDRC SRL DIAGNOSTICS PANAMPILLY NAGAR", "G-310, Panampilly Ave, Kochi 682036"),
            ("METROPOLIS HEALTHCARE ERNAKULAM", "MG Road, Shenoys, Kochi 682035"),
            ("LAKESHORE LAB SERVICES", "Nettoor, Maradu, Kochi 682040")
        ]
    }
]

# Genuine Clinical Disease Prototypes with authentic medical terminology, meds, tests, and discrepancies
clinical_archetypes = [
    {
        "category": "Metabolic & Endocrinology",
        "condition": "Type 2 Diabetes Mellitus with Microalbuminuria & Stage 2 CKD",
        "summary": "Longstanding poorly controlled glycemic index with gradual onset of microvascular complications. Earlier records overlooked a rising urinary albumin excretion rate while treating persistent mild pedal edema.",
        "tests": [
            ("HbA1c Glycated Hemoglobin", "8.9%", "%", "< 5.7% (Normal), 5.7-6.4% (Prediabetic)", "high"),
            ("Fasting Blood Sugar (FBS)", "178 mg/dL", "mg/dL", "70 - 99 mg/dL", "high"),
            ("Post-Prandial Blood Sugar (PPBS)", "264 mg/dL", "mg/dL", "< 140 mg/dL", "high"),
            ("Urine Microalbumin / Creatinine Ratio", "142 mcg/mg", "mcg/mg", "< 30 mcg/mg (Normal), 30-300 (Microalbuminuria)", "high"),
            ("Serum Creatinine", "1.34 mg/dL", "mg/dL", "0.7 - 1.2 mg/dL", "high"),
            ("eGFR (CKD-EPI)", "61 mL/min/1.73m²", "mL/min", "> 90 mL/min (Normal)", "low")
        ],
        "repeated_metric": {
            "testName": "HbA1c",
            "values": [("12 Jan 2023", "8.9%", "high"), ("18 May 2023", "7.8%", "elevated"), ("14 Nov 2023", "6.7%", "controlled")],
            "change": "↓ 2.2% reduction following SGLT2i addition and dietary compliance"
        },
        "repeated_metric2": {
            "testName": "Urine Albumin/Creatinine Ratio (UACR)",
            "values": [("12 Jan 2023", "142 mcg/mg", "high"), ("18 May 2023", "88 mcg/mg", "elevated"), ("14 Nov 2023", "42 mcg/mg", "near-normal")],
            "change": "↓ 100 mcg/mg reduction under Telmisartan nephroprotection"
        },
        "medications": [
            {"name": "Tab. Metformin HCl (Glycomet-SR)", "dosage": "1000mg BD", "timing": "After meals", "status": "Maintained"},
            {"name": "Tab. Dapagliflozin (Forxiga)", "dosage": "10mg OD", "timing": "Morning post-breakfast", "status": "Added (Escalation)"},
            {"name": "Tab. Telmisartan (Telma)", "dosage": "40mg OD", "timing": "Morning", "status": "Maintained (Renoprotective)"},
            {"name": "Tab. Atorvastatin (Atorva)", "dosage": "20mg HS", "timing": "Bedtime", "status": "Maintained"}
        ],
        "hedging": "\"Borderline diabetic nephropathy suspected given persistent microalbuminuria; rule out non-diabetic glomerulopathy if proteinuria escalates.\"",
        "contradiction": "Allergy Contradiction: 2022 discharge summary documents 'Sulfa Drug Hypersensitivity (skin rash)', yet a 2023 GP prescription documented Glimepiride (a sulfonylurea with potential sulfa cross-reactivity). Flagged for pharmacist verification.",
        "gap": "Clinical Loop Left Open: 18 May 2023 consult ordered repeat urinary albumin:creatinine ratio (UACR) & eGFR at 90 days. No record found between May and November 2023 (6-month lag)."
    },
    {
        "category": "Cardiology",
        "condition": "Essential Hypertension & Coronary Artery Disease post-PTCA with Stent",
        "summary": "Post-percutaneous transluminal coronary angioplasty with drug-eluting stent to LAD. Complex regimen with antiplatelet therapy. Record reveals fluctuating ambulatory blood pressures and inconsistent aspirin tolerance.",
        "tests": [
            ("Blood Pressure (Sitting)", "154/94 mmHg", "mmHg", "< 120/80 mmHg", "high"),
            ("High-Sensitivity Troponin I (hs-cTnI)", "14.2 ng/L", "ng/L", "< 19.8 ng/L (Normal)", "normal"),
            ("Total Cholesterol", "218 mg/dL", "mg/dL", "< 200 mg/dL", "high"),
            ("Low-Density Lipoprotein (LDL-C)", "132 mg/dL", "mg/dL", "< 70 mg/dL (Target for CAD)", "high"),
            ("Triglycerides", "184 mg/dL", "mg/dL", "< 150 mg/dL", "high"),
            ("2D Echocardiography EF", "52%", "%", "55 - 70% (Preserved EF)", "low")
        ],
        "repeated_metric": {
            "testName": "LDL-C (Bad Cholesterol)",
            "values": [("05 Feb 2023", "132 mg/dL", "high"), ("10 Jun 2023", "92 mg/dL", "elevated"), ("22 Dec 2023", "58 mg/dL", "target achieved")],
            "change": "↓ 74 mg/dL drop reaching CAD guideline target (< 70 mg/dL)"
        },
        "repeated_metric2": {
            "testName": "Systolic Blood Pressure",
            "values": [("05 Feb 2023", "154 mmHg", "high"), ("10 Jun 2023", "138 mmHg", "pre-hypertensive"), ("22 Dec 2023", "124 mmHg", "controlled")],
            "change": "↓ 30 mmHg reduction post triple combination titration"
        },
        "medications": [
            {"name": "Tab. Ecosprin AV (Aspirin + Atorvastatin)", "dosage": "75mg/40mg OD", "timing": "Bedtime", "status": "Maintained"},
            {"name": "Tab. Ticagrelor (Brilinta)", "dosage": "90mg BD", "timing": "12 hours apart", "status": "Active (DAPT protocol)"},
            {"name": "Tab. Metoprolol Succinate (Betaloc)", "dosage": "50mg OD", "timing": "Morning", "status": "Dose adjusted from 25mg"},
            {"name": "Tab. Ramipril (Cardace)", "dosage": "5mg OD", "timing": "Night", "status": "Maintained"}
        ],
        "hedging": "\"Atypical post-exertional chest tightness; rule out in-stent restenosis vs muscular chest wall pain. Exercise treadmill test pending.\"",
        "contradiction": "Aspirin GI Intolerance Discrepancy: Cardiology admission note from Aug 2022 marked 'Mild dyspepsia/gastritis with standard aspirin, consider enteric-coated', while later prescription reverted to uncoated formulation without co-prescribed PPI.",
        "gap": "Missing Follow-up Protocol: Dual antiplatelet therapy (DAPT) 12-month cessation review was scheduled for Jan 2024; no cardiologist clearance note registered."
    },
    {
        "category": "Endocrinology",
        "condition": "Primary Hypothyroidism with Refractory Dyslipidemia & Hashimoto's",
        "summary": "Elevated TSH despite self-reported adherence to Levothyroxine. Subclinical autoimmune thyroiditis with significant secondary elevation of low-density lipoproteins.",
        "tests": [
            ("TSH (Thyroid Stimulating Hormone)", "14.8 mIU/L", "mIU/L", "0.4 - 4.2 mIU/L", "critical"),
            ("Free T4 (Thyroxine)", "0.72 ng/dL", "ng/dL", "0.8 - 1.8 ng/dL", "low"),
            ("Anti-TPO Antibodies (Thyroid Peroxidase)", "480 IU/mL", "IU/mL", "< 35 IU/mL (Positive Autoimmunity)", "critical"),
            ("Total Cholesterol", "248 mg/dL", "mg/dL", "< 200 mg/dL", "high"),
            ("LDL Cholesterol", "162 mg/dL", "mg/dL", "< 100 mg/dL", "high"),
            ("Serum Ferritin", "18 ng/mL", "ng/mL", "20 - 200 ng/mL", "low")
        ],
        "repeated_metric": {
            "testName": "Serum TSH",
            "values": [("15 Mar 2023", "14.8 mIU/L", "critical"), ("02 Jul 2023", "8.2 mIU/L", "elevated"), ("19 Jan 2024", "2.8 mIU/L", "euthyroid normal")],
            "change": "↓ 12.0 mIU/L normalization after dose titration from 50mcg to 100mcg"
        },
        "repeated_metric2": {
            "testName": "LDL-C",
            "values": [("15 Mar 2023", "162 mg/dL", "high"), ("02 Jul 2023", "128 mg/dL", "elevated"), ("19 Jan 2024", "94 mg/dL", "normal")],
            "change": "↓ 68 mg/dL decrease correlated with corrected thyroid hormone level"
        },
        "medications": [
            {"name": "Tab. Levothyroxine Sodium (Thyronorm)", "dosage": "100mcg OD", "timing": "Empty stomach at 6 AM, 1 hr before tea/coffee", "status": "Dose titrated up"},
            {"name": "Tab. Rosuvastatin (Rosuvas)", "dosage": "10mg HS", "timing": "Night", "status": "Maintained"},
            {"name": "Tab. Ferrous Ascorbate + Folic Acid (Orofer-XT)", "dosage": "100mg OD", "timing": "Afternoon (spaced 4 hrs from thyroxine)", "status": "Added for ferritin deficiency"}
        ],
        "hedging": "\"Persistent lethargy despite TSH improvement; suspect concurrent latent iron deficiency or vitamin D3 insufficiency.\"",
        "contradiction": "Drug Administration Timing Contradiction: Doctor consultation advised taking Calcium/Iron tablets at least 4 hours apart from Levothyroxine, but pharmacy dispensing slip noted 'Take all morning supplements together with water'.",
        "gap": "Missing Cervical Ultrasound: Endocrinology consult in July 2023 recommended high-resolution thyroid ultrasound to evaluate nodular parenchyma; report missing in timeline."
    },
    {
        "category": "Infectious & Hematology",
        "condition": "Severe Dengue Fever with Thrombocytopenia & Elevated Transaminases (Post-Recovery)",
        "summary": "Admitted during seasonal monsoon outbreak with acute high-grade pyrexia, severe retro-orbital cephalalgia, and rapid platelet collapse. Subsequent outpatient recovery monitored for post-viral hepatic clearance.",
        "tests": [
            ("Platelet Count", "28,000 /mcL", "/mcL", "150,000 - 450,000 /mcL", "critical"),
            ("Hematocrit (PCV)", "47.8%", "%", "36 - 46% (Hemoconcentration present)", "high"),
            ("Dengue NS1 Antigen (Rapid)", "Positive", "", "Negative", "critical"),
            ("Dengue IgM Serology", "Positive (Index 2.4)", "", "Negative (< 1.0)", "critical"),
            ("SGPT / ALT (Liver Enzyme)", "198 U/L", "U/L", "7 - 56 U/L", "critical"),
            ("SGOT / AST (Liver Enzyme)", "242 U/L", "U/L", "10 - 40 U/L", "critical")
        ],
        "repeated_metric": {
            "testName": "Platelet Count",
            "values": [("20 Aug 2023", "28,000 /mcL", "critical nadir"), ("24 Aug 2023", "84,000 /mcL", "recovering"), ("05 Sep 2023", "210,000 /mcL", "normal recovery")],
            "change": "↑ 182,000 /mcL rapid marrow rebound post-hydration therapy"
        },
        "repeated_metric2": {
            "testName": "SGPT / ALT",
            "values": [("20 Aug 2023", "198 U/L", "critical"), ("05 Sep 2023", "84 U/L", "mildly elevated"), ("15 Oct 2023", "32 U/L", "normal")],
            "change": "↓ 166 U/L resolution of reactive post-viral hepatic inflammation"
        },
        "medications": [
            {"name": "IV Normal Saline 0.9% / Ringer Lactate", "dosage": "100 mL/hr titrated to PCV", "timing": "Inpatient 72 hours", "status": "Completed / Stopped"},
            {"name": "Tab. Paracetamol (Dolo-650)", "dosage": "650mg SOS", "timing": "Max 3 tabs/day for fever (Avoid NSAIDs)", "status": "SOS as needed"},
            {"name": "Tab. Ursodeoxycholic Acid (Udiliv)", "dosage": "300mg BD", "timing": "With meals", "status": "Prescribed for hepatoprotection, discontinued on normalization"}
        ],
        "hedging": "\"Transient reactive hepatomegaly suspected secondary to viral insult; rule out acute calculous cholecystitis via USG if right upper quadrant pain persists.\"",
        "contradiction": "NSAID Avoidance Contradiction: Emergency record explicitly documented 'Strictly avoid Aspirin, Ibuprofen, and Diclofenac due to bleeding risk', yet local pharmacy bill showed an over-the-counter Brufen blister pack purchased 2 days prior to admission.",
        "gap": "Missing Post-Discharge Liver Function Panel: Discharge summary mandated repeat LFT at 4 weeks post-discharge; lab was delayed by 6 weeks before patient attended follow-up."
    },
    {
        "category": "Nephrology",
        "condition": "Chronic Kidney Disease Stage 3b with Secondary Hyperparathyroidism",
        "summary": "Longterm diabetic and hypertensive nephropathy leading to gradual nephron loss. Requires strict control of serum phosphorus, potassium, and monitoring of intact PTH.",
        "tests": [
            ("Serum Creatinine", "2.18 mg/dL", "mg/dL", "0.7 - 1.3 mg/dL", "critical"),
            ("Blood Urea Nitrogen (BUN)", "44 mg/dL", "mg/dL", "7 - 20 mg/dL", "high"),
            ("eGFR (MDRD formula)", "34 mL/min/1.73m²", "mL/min", "> 90 mL/min (Stage 3b CKD)", "critical"),
            ("Serum Potassium (K+)", "5.2 mEq/L", "mEq/L", "3.5 - 5.0 mEq/L", "high"),
            ("Serum Phosphorus", "5.6 mg/dL", "mg/dL", "2.5 - 4.5 mg/dL", "high"),
            ("Intact PTH (Parathyroid Hormone)", "148 pg/mL", "pg/mL", "15 - 65 pg/mL", "critical")
        ],
        "repeated_metric": {
            "testName": "Serum Creatinine",
            "values": [("10 Feb 2023", "2.18 mg/dL", "critical"), ("15 Jul 2023", "1.98 mg/dL", "elevated"), ("12 Jan 2024", "1.92 mg/dL", "stabilized")],
            "change": "↓ 0.26 mg/dL stabilization following dietary protein restriction and ACEi titration"
        },
        "repeated_metric2": {
            "testName": "eGFR",
            "values": [("10 Feb 2023", "34 mL/min", "Stage 3b"), ("15 Jul 2023", "38 mL/min", "Stage 3b"), ("12 Jan 2024", "40 mL/min", "Stage 3b stabilized")],
            "change": "↑ 6 mL/min arrest of rapid glomerular deterioration"
        },
        "medications": [
            {"name": "Tab. Sevelamer Carbonate (Sevcar)", "dosage": "800mg TDS", "timing": "With meals (Phosphate binder)", "status": "Maintained"},
            {"name": "Tab. Torsemide (Dytor)", "dosage": "20mg OD", "timing": "Morning post-breakfast", "status": "Maintained"},
            {"name": "Tab. Sodium Bicarbonate (Sodamint)", "dosage": "500mg BD", "timing": "After food for metabolic acidosis", "status": "Active"},
            {"name": "Inj. Erythropoietin (EPO)", "dosage": "4000 IU SC Weekly", "timing": "Subcutaneous", "status": "Maintained for renal anemia"}
        ],
        "hedging": "\"Early signs of renal osteodystrophy; borderline elevated PTH requires confirmation with 25-OH Vitamin D and 24-hr urinary calcium before active calcitriol escalation.\"",
        "contradiction": "Potassium Supplementation Contradiction: Outpatient general medicine note prescribed potassium citrate syrup for mild dysuria, directly contradicting Nephrologist's standing orders of 'Strict low-potassium diet & avoid K+ formulations due to serum K+ 5.2 mEq/L'.",
        "gap": "Missing Renal Artery Doppler: Nephrologist ordered Bilateral Renal Doppler Ultrasound in Feb 2023 to rule out renal artery stenosis; no ultrasound report present in subsequent folders."
    },
    {
        "category": "Rheumatology",
        "condition": "Seropositive Rheumatoid Arthritis with Methotrexate-Induced Mild Transaminitis",
        "summary": "Polyarticular inflammatory arthritis affecting MCP and PIP joints symmetrically. Managed on disease-modifying antirheumatic drugs (DMARDs); requires vigilant hepatic and hematological surveillance.",
        "tests": [
            ("Rheumatoid Factor (RF Quantitative)", "182 IU/mL", "IU/mL", "< 14 IU/mL (Strongly Positive)", "critical"),
            ("Anti-CCP (Cyclic Citrullinated Peptide)", "240 U/mL", "U/mL", "< 20 U/mL", "critical"),
            ("C-Reactive Protein (CRP Quantitative)", "36 mg/L", "mg/L", "< 5.0 mg/L", "critical"),
            ("Erythrocyte Sedimentation Rate (ESR)", "64 mm/1st hr", "mm/hr", "< 20 mm/hr", "high"),
            ("SGPT / ALT", "68 U/L", "U/L", "7 - 56 U/L", "high"),
            ("Hemoglobin", "10.4 g/dL", "g/dL", "12.0 - 15.5 g/dL (Anemia of chronic disease)", "low")
        ],
        "repeated_metric": {
            "testName": "CRP (Inflammation Marker)",
            "values": [("22 Jan 2023", "36 mg/L", "critical"), ("18 Jun 2023", "16 mg/L", "elevated"), ("08 Dec 2023", "4.8 mg/L", "normalized")],
            "change": "↓ 31.2 mg/L profound suppression of systemic synovitis"
        },
        "repeated_metric2": {
            "testName": "ESR",
            "values": [("22 Jan 2023", "64 mm/hr", "high"), ("18 Jun 2023", "38 mm/hr", "moderate"), ("08 Dec 2023", "18 mm/hr", "normal")],
            "change": "↓ 46 mm/hr reduction reflecting sustained clinical remission"
        },
        "medications": [
            {"name": "Tab. Methotrexate (Folitrax)", "dosage": "15mg Once Weekly", "timing": "Every Sunday night", "status": "Temporarily reduced to 10mg due to transaminitis"},
            {"name": "Tab. Folic Acid (Folvite)", "dosage": "5mg Once Weekly", "timing": "Every Tuesday (48 hrs post-MTX)", "status": "Maintained"},
            {"name": "Tab. Hydroxychloroquine (HCQS)", "dosage": "200mg OD", "timing": "Night after food", "status": "Maintained"},
            {"name": "Tab. Deflazacort (Defcort)", "dosage": "6mg OD", "timing": "Morning taper", "status": "Tapered down from 12mg to 3mg"}
        ],
        "hedging": "\"Early methotrexate-induced transaminitis vs concurrent NAFLD; suspect mild drug-induced liver injury, monitor SGOT/SGPT bi-weekly.\"",
        "contradiction": "Ophthalmological Clearance Gap vs Contradiction: HCQS (Hydroxychloroquine) ongoing for 14 months without baseline Humphrey visual field test or fundoscopy documented, despite rheumatology guideline mandate.",
        "gap": "Missing Bi-Monthly Complete Blood Count: Protocol mandates CBC + LFT every 60 days on DMARD therapy; gap of 4 months detected between June and October 2023."
    },
    {
        "category": "Pulmonology",
        "condition": "Severe Persistent Bronchial Asthma with Allergic Rhinitis & Frequent Exacerbations",
        "summary": "Severe reversible airway obstruction provoked by seasonal smog and pollen. Repeated visits to acute emergency care for nebulization; ongoing step-4 GINA inhaler therapy.",
        "tests": [
            ("FEV1 (Forced Expiratory Volume 1s)", "1.68 L (56% predicted)", "L", "> 80% predicted", "critical"),
            ("FEV1 / FVC Ratio", "62%", "%", "> 75%", "low"),
            ("Post-Bronchodilator Reversibility", "+18% (+290 mL)", "%", "> 12% & 200 mL (Diagnostic Reversibility)", "critical"),
            ("Serum Total IgE", "890 IU/mL", "IU/mL", "< 100 IU/mL", "critical"),
            ("Absolute Eosinophil Count (AEC)", "640 /mcL", "/mcL", "20 - 500 /mcL", "high"),
            ("Oxygen Saturation (Room Air)", "94%", "%", "96 - 100%", "low")
        ],
        "repeated_metric": {
            "testName": "FEV1 (% Predicted)",
            "values": [("14 Apr 2023", "56%", "critical obstruction"), ("12 Aug 2023", "72%", "moderate"), ("10 Feb 2024", "84%", "well-controlled")],
            "change": "↑ 28% improvement after triple ICS/LABA/LAMA adherence"
        },
        "repeated_metric2": {
            "testName": "Absolute Eosinophil Count",
            "values": [("14 Apr 2023", "640 /mcL", "high"), ("12 Aug 2023", "410 /mcL", "normal"), ("10 Feb 2024", "260 /mcL", "optimal")],
            "change": "↓ 380 /mcL systemic reduction following Montelukast & budesonide"
        },
        "medications": [
            {"name": "Inhaler Budesonide + Formoterol (Budecort-F 400)", "dosage": "2 puffs BD", "timing": "Morning and Night with spacer + mouth gargle", "status": "Maintained (Maintenance & Reliever)"},
            {"name": "Inhaler Tiotropium Bromide (Tiova Rotacap)", "dosage": "18mcg OD", "timing": "Morning via Revolizer", "status": "Added (Step-up therapy)"},
            {"name": "Tab. Montelukast + Levocetirizine (Monticope)", "dosage": "10mg/5mg OD", "timing": "Bedtime", "status": "Maintained"},
            {"name": "Inhaler Levosalbutamol (Levolin)", "dosage": "2 puffs SOS", "timing": "Emergency wheezing episodes", "status": "As needed"}
        ],
        "hedging": "\"Suspected Allergic Bronchopulmonary Aspergillosis (ABPA) given extreme total IgE elevation; rule out central bronchiectasis via HRCT Thorax.\"",
        "contradiction": "Beta-Blocker Inadvertent Prescribing: Cardiology clinic prescribed Propranolol for essential tremor, which was flagged by the automated clinical system as contraindicated in severe reactive airway disease (bronchial asthma).",
        "gap": "Missing HRCT Chest Scan: Pulmonologist requested High-Resolution CT Thorax in April 2023 to check for airway remodeling/bronchiectasis; patient did not complete scan due to seasonal resolution."
    },
    {
        "category": "Gastroenterology",
        "condition": "Non-Alcoholic Fatty Liver Disease (NAFLD) with NASH & Metabolic Syndrome",
        "summary": "Obesity-related hepatic steatosis with chronic transaminitis and elevated FibroScan stiffness score. Transitioned from benign steatosis to early steatohepatitis requiring lifestyle and GLP-1 intervention.",
        "tests": [
            ("FibroScan Controlled Attenuation Parameter (CAP)", "324 dB/m", "dB/m", "< 248 dB/m (Severe S3 Steatosis)", "critical"),
            ("Liver Stiffness Measurement (E)", "8.6 kPa", "kPa", "2 - 7 kPa (F2 Significant Fibrosis)", "high"),
            ("SGPT / ALT", "88 U/L", "U/L", "7 - 56 U/L", "high"),
            ("SGOT / AST", "64 U/L", "U/L", "10 - 40 U/L", "high"),
            ("Fasting Triglycerides", "260 mg/dL", "mg/dL", "< 150 mg/dL", "critical"),
            ("Serum GGT (Gamma-GT)", "112 U/L", "U/L", "9 - 48 U/L", "high")
        ],
        "repeated_metric": {
            "testName": "SGPT / ALT",
            "values": [("05 Jan 2023", "88 U/L", "high"), ("14 Jun 2023", "52 U/L", "borderline"), ("20 Dec 2023", "28 U/L", "normal")],
            "change": "↓ 60 U/L enzyme normalization after 8% body weight loss"
        },
        "repeated_metric2": {
            "testName": "Liver Stiffness (FibroScan)",
            "values": [("05 Jan 2023", "8.6 kPa", "F2 Fibrosis"), ("14 Jun 2023", "7.4 kPa", "F1-F2 Borderline"), ("20 Dec 2023", "6.2 kPa", "F0-F1 Mild")],
            "change": "↓ 2.4 kPa regression of hepatic parenchymal stiffness"
        },
        "medications": [
            {"name": "Tab. Saroglitazar (Lipaglyn)", "dosage": "4mg OD", "timing": "Morning post-meal", "status": "Maintained (Dual PPAR alpha/gamma agonist)"},
            {"name": "Cap. Vitamin E (Evion)", "dosage": "400 IU OD", "timing": "Post-lunch (Antioxidant protocol for NASH)", "status": "Maintained"},
            {"name": "Tab. Metformin HCl (Glycomet)", "dosage": "500mg BD", "timing": "With food for insulin sensitization", "status": "Maintained"}
        ],
        "hedging": "\"Borderline F2 hepatic fibrosis; suspected metabolic dysfunction-associated steatohepatitis (MASH). Rule out autoimmune hepatitis with ANA/SMA panel.\"",
        "contradiction": "Hepatotoxic Formulation Mismatch: Orthopedic prescription for acute lumbago included Paracetamol 1000mg TID + Diclofenac, exceeding recommended daily hepatotoxic thresholds in established steatohepatitis.",
        "gap": "Missing Repeat FibroScan: Hepatologist requested follow-up transient elastography at 6 months; test performed only after 12 months."
    },
    {
        "category": "Gastroenterology & Infectious",
        "condition": "Gastroesophageal Reflux Disease (GERD) with Helicobacter Pylori Antral Gastritis",
        "summary": "Recurrent epigastric burning, water brash, and postprandial fullness refractory to over-the-counter antacids. Upper GI endoscopy confirmed diffuse antral erosions and rapid urease positivity.",
        "tests": [
            ("Upper GI Endoscopy (EGD)", "Antral Erythema & Grade B Esophagitis", "", "Normal Mucosa", "high"),
            ("Rapid Urease Test (Campylobacter-like organism)", "Positive (Within 30 mins)", "", "Negative", "critical"),
            ("H. Pylori Stool Antigen (HpSA)", "Reactive (Positive)", "", "Non-reactive", "critical"),
            ("Hemoglobin (Hb)", "12.8 g/dL", "g/dL", "13.0 - 17.0 g/dL", "normal"),
            ("Serum Pepsinogen I/II Ratio", "3.4", "", "> 3.0", "normal")
        ],
        "repeated_metric": {
            "testName": "H. Pylori Stool Antigen (HpSA)",
            "values": [("10 Mar 2023", "Positive (Index 4.8)", "active infection"), ("15 May 2023", "Negative (Index 0.3)", "eradicated"), ("15 Nov 2023", "Negative (Index 0.1)", "sustained clearance")],
            "change": "Complete bacterial eradication post 14-day bismuth quadruple regimen"
        },
        "repeated_metric2": {
            "testName": "Los Angeles Esophagitis Grade",
            "values": [("10 Mar 2023", "Grade B", "moderate erosions"), ("15 May 2023", "Grade A", "mild residual"), ("15 Nov 2023", "Normal Mucosa", "mucosal recovery")],
            "change": "Endoscopic resolution of mucosal breaks"
        },
        "medications": [
            {"name": "Tab. Esomeprazole + Domperidone (Nexpro-RD)", "dosage": "40mg/30mg OD", "timing": "30 mins before breakfast", "status": "Maintained"},
            {"name": "Tab. Amoxicillin (Mox)", "dosage": "1000mg BD", "timing": "After meals for 14 days", "status": "Course Completed"},
            {"name": "Tab. Clarithromycin (Claribid)", "dosage": "500mg BD", "timing": "After meals for 14 days", "status": "Course Completed"},
            {"name": "Syp. Sucralfate (Sucrafil)", "dosage": "10 mL QID", "timing": "1 hour before food and at bedtime", "status": "Discontinued after 4 weeks"}
        ],
        "hedging": "\"Suspected intestinal metaplasia on biopsy margins; awaiting histopathological immunohistochemistry for CDX2 to rule out Barrett's esophagus.\"",
        "contradiction": "Clarithromycin QT Prolongation Precaution: Patient had existing mild resting QTc prolongation (462ms) noted on baseline ECG, yet clarithromycin was administered without repeat ECG tracking.",
        "gap": "Missing Confirmatory Eradication Test: Physician advised Urea Breath Test (UBT) at 6 weeks post-antibiotics; patient delayed testing until 14 weeks."
    },
    {
        "category": "Hematology",
        "condition": "Severe Iron Deficiency Anemia secondary to Menorrhagia with Reactive Thrombocytosis",
        "summary": "Severe microcytic hypochromic anemia presenting with chronic fatigue, exertional dyspnea, and brittle nails. Managed with parenteral ferric carboxymaltose and subsequent oral maintenance.",
        "tests": [
            ("Hemoglobin (Hb)", "6.8 g/dL", "g/dL", "12.0 - 15.5 g/dL", "critical"),
            ("Serum Ferritin", "4.2 ng/mL", "ng/mL", "15 - 150 ng/mL", "critical"),
            ("Total Iron Binding Capacity (TIBC)", "460 mcg/dL", "mcg/dL", "240 - 450 mcg/dL", "high"),
            ("Transferrin Saturation (TSAT)", "6.2%", "%", "20 - 50%", "critical"),
            ("Mean Corpuscular Volume (MCV)", "62 fL", "fL", "80 - 100 fL", "critical"),
            ("Platelet Count", "480,000 /mcL", "/mcL", "150,000 - 450,000 /mcL (Reactive)", "high")
        ],
        "repeated_metric": {
            "testName": "Hemoglobin (Hb)",
            "values": [("08 Feb 2023", "6.8 g/dL", "critical"), ("28 Feb 2023", "9.6 g/dL", "improving post-IV iron"), ("14 Jun 2023", "12.4 g/dL", "normal")],
            "change": "↑ 5.6 g/dL dramatic rise following 1000mg Ferric Carboxymaltose infusion"
        },
        "repeated_metric2": {
            "testName": "Serum Ferritin",
            "values": [("08 Feb 2023", "4.2 ng/mL", "depleted"), ("28 Feb 2023", "180 ng/mL", "repleted"), ("14 Jun 2023", "68 ng/mL", "optimal")],
            "change": "↑ 63.8 ng/mL iron stores replenished"
        },
        "medications": [
            {"name": "Inj. Ferric Carboxymaltose (Ferium-1k)", "dosage": "1000mg in 100mL NS IV infusion", "timing": "Over 20 minutes (Hospital Daycare)", "status": "Administered & Completed"},
            {"name": "Tab. Tranexamic Acid (Pause)", "dosage": "500mg TDS", "timing": "During heavy menstrual flow days 1-3", "status": "SOS Active"},
            {"name": "Tab. Sodium Feredetate + Vit B12 (Autrin)", "dosage": "1 tab OD", "timing": "Night post-meal", "status": "Maintenance therapy"}
        ],
        "hedging": "\"Severe microcytic anemia; suspected nutritional deficiency compounded by hypermenorrhea. Rule out celiac enteropathy or occult gastrointestinal blood loss.\"",
        "contradiction": "Iron Infusion Anaphylaxis Precaution: Previous OPD slip noted 'Patient reported mild urticaria with oral iron salts', which hospital nurse mislabeled as 'Parenteral Iron Allergy' before hematologist clarified tolerability with test dose.",
        "gap": "Missing Pelvic Ultrasonography: Gynecology consult advised Transvaginal Pelvic Ultrasound to evaluate for endometrial hyperplasia or fibroids; scan was deferred by patient for 4 months."
    }
]

# Generate 100 Unique Indian Patient Profiles
patients = []

for i in range(1, 101):
    pid = f"IN-{i:03d}"
    gender = "Male" if random.random() > 0.48 else "Female"
    first_name = random.choice(male_first_names) if gender == "Male" else random.choice(female_first_names)
    last_name = random.choice(last_names)
    full_name = f"{first_name} {last_name}"
    
    # Age between 21 and 76
    age = random.randint(22, 74)
    birth_year = 2024 - age
    dob = f"{random.randint(1, 28):02d}/{random.randint(1, 12):02d}/{birth_year}"
    blood_groups = ["A+", "B+", "B-", "O+", "O-", "AB+", "AB-"]
    blood_group = random.choice(blood_groups)
    phone = f"+91 {random.choice([98, 99, 97, 96, 94, 91, 88])}{random.randint(1000, 9999)} {random.randint(1000, 9999)}"
    
    city_info = random.choice(cities_data)
    locality_info = random.choice(city_info["localities"])
    address = f"{random.choice(['Flat', 'House', 'Plot', 'Bungalow'])} {random.randint(10, 450)}, {locality_info[0]}, {city_info['city']}, {city_info['state']} {locality_info[1]}"
    
    # Archetype selection
    archetype = clinical_archetypes[(i - 1) % len(clinical_archetypes)]
    
    # Custom variations to condition title
    condition_title = archetype["condition"]
    if i > 10:
        # add mild personalization
        modifiers = ["", " (Longitudinal Follow-up)", " (Moderate Severity)", " with Metabolic Comorbidities", " under Medical Surveillance"]
        condition_title += random.choice(modifiers)
    
    hospital = random.choice(city_info["hospitals"])
    lab = random.choice(city_info["labs"])
    
    doctor_names = [
        ("Dr. Arvind Swaminathan", "MD (Internal Med), DM (Cardio)", "KMC Reg #48291"),
        ("Dr. Sunita Kulkarni", "MD, DM (Endocrinology)", "MMC Reg #31849"),
        ("Dr. Rajeshwar Sen", "MD (Medicine), FRCP (Edin)", "WBMC Reg #22941"),
        ("Dr. Priya Venkataraman", "MD (Pediatrics & Infectious Dis)", "TNC Reg #51203"),
        ("Dr. Amitav Chowdhury", "MD, DNB (Nephrology)", "DMC Reg #39104"),
        ("Dr. Neha Deshmukh", "MD, DM (Clinical Immunology & Rheum)", "MMC Reg #45210"),
        ("Dr. Vikram Rathore", "MD (Chest & Respiratory Diseases)", "RMC Reg #28419"),
        ("Dr. Farooq Qureshi", "MD, DM (Medical Gastroenterology)", "DMC Reg #34190"),
        ("Dr. Kavitha Sundaram", "MD (Obstetrics & Gynecology)", "KMC Reg #62194"),
        ("Dr. Harpreet Singh Gill", "MD (General Medicine)", "PMC Reg #19402")
    ]
    attending_doc = random.choice(doctor_names)
    
    # Build 4 to 5 Timeline Events spanning 2022 to 2024
    dates = [
        ("15 Jan 2023", "2023-01-15"),
        ("22 Jan 2023", "2023-01-22"),
        ("14 May 2023", "2023-05-14"),
        ("18 Oct 2023", "2023-10-18"),
        ("04 Feb 2024", "2024-02-04")
    ]
    
    events = []
    
    # Event 1: Initial OPD Consult / Admission
    events.append({
        "id": f"{pid}-evt-1",
        "date": dates[0][0],
        "isoDate": dates[0][1],
        "type": "visit",
        "category": "visits",
        "title": "Comprehensive Outpatient Clinical Evaluation",
        "facility": hospital[0],
        "facilityAddress": hospital[1],
        "doctor": f"{attending_doc[0]}, {attending_doc[1]} ({attending_doc[2]})",
        "description": f"Patient presented with primary complaints relating to {archetype['condition']}. Thorough systemic assessment conducted. Baseline clinical markers ordered and immediate symptomatic management initiated.",
        "uncertaintyHedging": archetype["hedging"],
        "keyMetrics": [archetype["tests"][0], archetype["tests"][1]],
        "medicationsPrescribed": [archetype["medications"][0], archetype["medications"][1]],
        "proofSnippet": {
            "docTitle": f"{hospital[0].replace(' ', '_')}_OPD_Consult_{dates[0][1]}.pdf",
            "page": "Page 1 of 3",
            "letterhead": hospital[0],
            "address": hospital[1],
            "confidentialStamp": "GOVERNMENT OF INDIA / NABH ACCREDITED RECORD",
            "extractedBodyHtml": f"""
                <p><strong>DEPARTMENT OF GENERAL MEDICINE & SPECIALITY CLINIC:</strong> Initial intake assessment for {full_name} ({age} Y / {gender}).</p>
                <div class="relative inline-block w-full my-2 bg-yellow-300/30 p-2 rounded border-l-2 border-yellow-500 text-slate-900 font-medium">
                    <p class="italic">"Impression: Clinical symptoms consistent with {archetype['condition']}. {archetype['hedging']}"</p>
                </div>
                <p>Orders: Urgent diagnostic panels ({archetype['tests'][0][0]}, {archetype['tests'][1][0]}) booked with accredited laboratory.</p>
                <p class="text-[9px] text-slate-500 font-mono mt-1">Certified Signature: {attending_doc[0]} [{attending_doc[2]}]</p>
            """
        }
    })
    
    # Event 2: Diagnostic Lab Panel
    events.append({
        "id": f"{pid}-evt-2",
        "date": dates[1][0],
        "isoDate": dates[1][1],
        "type": "lab",
        "category": "labs",
        "title": f"Diagnostic Panel: {archetype['tests'][0][0]} & Associated Profiles",
        "facility": lab[0],
        "facilityAddress": lab[1],
        "doctor": "Dr. Anirudh Sen, MD (Pathology), Lead Quality Officer",
        "description": f"Standardized multi-parameter diagnostic investigation. Results reveal significant clinical indicators validating preliminary clinical impression.",
        "uncertaintyHedging": f"\"Analyte readings verified twice by internal standard calibration; values indicate {archetype['tests'][0][4]} abnormal variance.\"",
        "keyMetrics": archetype["tests"][:4],
        "medicationsPrescribed": [],
        "proofSnippet": {
            "docTitle": f"{lab[0].replace(' ', '_')}_LabReport_{dates[1][1]}.pdf",
            "page": "Page 1 of 2",
            "letterhead": lab[0],
            "address": lab[1],
            "confidentialStamp": "NABL ACCREDITED DIAGNOSTIC LABORATORY (ISO 15189)",
            "extractedBodyHtml": f"""
                <p><strong>INVESTIGATION RESULTS:</strong> Specimen collected under fasting guidelines.</p>
                <div class="relative inline-block w-full my-2 bg-yellow-300/30 p-2 rounded border-l-2 border-yellow-500 text-slate-900 font-bold">
                    <p>{archetype['tests'][0][0]}: <span class="text-rose-700">{archetype['tests'][0][1]}</span> (Reference: {archetype['tests'][0][3]})</p>
                    <p>{archetype['tests'][1][0]}: <span class="text-rose-700">{archetype['tests'][1][1]}</span> (Reference: {archetype['tests'][1][3]})</p>
                </div>
                <p class="text-[9px] text-slate-500 font-mono mt-1">Verified By: Senior Bio-Chemist S. Mukherjee, MSc, PhD</p>
            """
        }
    })
    
    # Event 3: Medication Prescription / Pharmacotherapy Adjustment
    events.append({
        "id": f"{pid}-evt-3",
        "date": dates[2][0],
        "isoDate": dates[2][1],
        "type": "medication",
        "category": "medications",
        "title": "Therapeutic Review & Pharmacotherapy Prescription",
        "facility": hospital[0],
        "facilityAddress": hospital[1],
        "doctor": f"{attending_doc[0]}, {attending_doc[1]}",
        "description": f"Follow-up consultation to evaluate pharmacological tolerance and therapeutic efficacy. Drug titration enacted based on prior lab anomalies.",
        "uncertaintyHedging": f"\"Tolerance to adjusted dosage to be assessed in 4 weeks. Patient warned regarding potential drug-drug interactions.\"",
        "keyMetrics": [],
        "medicationsPrescribed": archetype["medications"],
        "proofSnippet": {
            "docTitle": f"{hospital[0].replace(' ', '_')}_Rx_{dates[2][1]}.pdf",
            "page": "Page 1 of 1",
            "letterhead": hospital[0],
            "address": hospital[1],
            "confidentialStamp": "CLINICAL PHARMACOLOGY DISPENSING AUDIT",
            "extractedBodyHtml": f"""
                <p><strong>PRESCRIPTION CHART (Rx):</strong> Patient: {full_name} | ID: {pid}</p>
                <div class="relative inline-block w-full my-2 bg-yellow-300/30 p-2 rounded border-l-2 border-yellow-500 text-slate-900 font-medium">
                    <p>1. <strong>{archetype['medications'][0]['name']}</strong> - {archetype['medications'][0]['dosage']} ({archetype['medications'][0]['timing']})</p>
                    <p>2. <strong>{archetype['medications'][1]['name']}</strong> - {archetype['medications'][1]['dosage']} ({archetype['medications'][1]['timing']})</p>
                </div>
                <p>Advisory: Strict compliance required. Do not alter doses without prior clinical consultation.</p>
                <p class="text-[9px] text-slate-500 font-mono mt-1">Reg No: {attending_doc[2]}</p>
            """
        }
    })
    
    # Event 4: Intermediate Follow-up / Imaging or Repeat Lab
    events.append({
        "id": f"{pid}-evt-4",
        "date": dates[3][0],
        "isoDate": dates[3][1],
        "type": "lab",
        "category": "labs",
        "title": f"Longitudinal Monitoring: Repeat {archetype['repeated_metric']['testName']}",
        "facility": lab[0],
        "facilityAddress": lab[1],
        "doctor": "Dr. Manjula Rao, MD (Biochemistry)",
        "description": f"Intermediate milestone check for tracking treatment responsiveness. Shows positive trajectory towards targeted clinical goals.",
        "uncertaintyHedging": f"\"Metric shows marked improvement ({archetype['repeated_metric']['change']}); confirm stability at next quarter cycle.\"",
        "keyMetrics": [
            (archetype['repeated_metric']['testName'], archetype['repeated_metric']['values'][1][1], "", "", archetype['repeated_metric']['values'][1][2]),
            (archetype['repeated_metric2']['testName'], archetype['repeated_metric2']['values'][1][1], "", "", archetype['repeated_metric2']['values'][1][2])
        ],
        "medicationsPrescribed": [],
        "proofSnippet": {
            "docTitle": f"{lab[0].replace(' ', '_')}_RepeatPanel_{dates[3][1]}.pdf",
            "page": "Page 1 of 1",
            "letterhead": lab[0],
            "address": lab[1],
            "confidentialStamp": "EHR AUTOMATED LABORATORY FEED",
            "extractedBodyHtml": f"""
                <p><strong>SERIAL ASSAY COMPARISON REPORT:</strong></p>
                <div class="relative inline-block w-full my-2 bg-yellow-300/30 p-2 rounded border-l-2 border-yellow-500 text-slate-900 font-bold">
                    <p>{archetype['repeated_metric']['testName']}: <span class="text-blue-700">{archetype['repeated_metric']['values'][1][1]}</span> (Delta vs baseline: Significant decrease)</p>
                    <p>{archetype['repeated_metric2']['testName']}: <span class="text-blue-700">{archetype['repeated_metric2']['values'][1][1]}</span></p>
                </div>
                <p>Clinical Note: Favorable response noted with current pharmacotherapy protocol.</p>
                <p class="text-[9px] text-slate-500 font-mono mt-1">Chief Lab Officer: Dr. M. Rao, MD</p>
            """
        }
    })
    
    # Event 5: Annual Review & Status Consultation
    events.append({
        "id": f"{pid}-evt-5",
        "date": dates[4][0],
        "isoDate": dates[4][1],
        "type": "visit",
        "category": "visits",
        "title": "Annual Comprehensive Clinical Review & Staging",
        "facility": hospital[0],
        "facilityAddress": hospital[1],
        "doctor": f"{attending_doc[0]}, {attending_doc[1]}",
        "description": f"Annual longitudinal health assessment. Evaluated all historical diagnostic curves, medication adherence, and documented remaining diagnostic gaps.",
        "uncertaintyHedging": f"\"Patient currently stable on maintenance therapy; maintain strict vigilance for early warning signs of flare or relapse.\"",
        "keyMetrics": [
            (archetype['repeated_metric']['testName'], archetype['repeated_metric']['values'][-1][1], "", "", archetype['repeated_metric']['values'][-1][2])
        ],
        "medicationsPrescribed": archetype["medications"][:2],
        "proofSnippet": {
            "docTitle": f"{hospital[0].replace(' ', '_')}_AnnualReview_{dates[4][1]}.pdf",
            "page": "Page 2 of 2",
            "letterhead": hospital[0],
            "address": hospital[1],
            "confidentialStamp": "PERMANENT CLINICAL HEALTH RECORD",
            "extractedBodyHtml": f"""
                <p><strong>ANNUAL COMPREHENSIVE STATUS SUMMARY:</strong></p>
                <div class="relative inline-block w-full my-2 bg-yellow-300/30 p-2 rounded border-l-2 border-yellow-500 text-slate-900 font-medium">
                    <p>Current Status: Stable on existing regimen. {archetype['repeated_metric']['testName']} normalized to {archetype['repeated_metric']['values'][-1][1]}.</p>
                    <p class="italic text-slate-800">"Notice: Prior contradiction in allergy file highlighted for correction in electronic health record."</p>
                </div>
                <p>Recommended: Follow up in 6 months with repeat baseline investigations.</p>
                <p class="text-[9px] text-slate-500 font-mono mt-1">Authorized Physician: {attending_doc[0]}</p>
            """
        }
    })
    
    # Relationships
    relationships = [
        {
            "fromEventId": f"{pid}-evt-1",
            "toEventId": f"{pid}-evt-2",
            "type": "Clinical Order Execution",
            "description": f"Physician consult at {hospital[0]} ordered diagnostic investigation → Tested at {lab[0]}"
        },
        {
            "fromEventId": f"{pid}-evt-2",
            "toEventId": f"{pid}-evt-3",
            "type": "Result-Triggered Rx Titration",
            "description": f"Elevated {archetype['tests'][0][0]} triggered prescription adjustment of {archetype['medications'][0]['name']}"
        },
        {
            "fromEventId": f"{pid}-evt-3",
            "toEventId": f"{pid}-evt-4",
            "type": "Longitudinal Therapeutic Tracking",
            "description": f"Repeat panel evaluated therapeutic efficacy, confirming {archetype['repeated_metric']['change']}"
        },
        {
            "fromEventId": f"{pid}-evt-4",
            "toEventId": f"{pid}-evt-5",
            "type": "Annual Consolidation & Gap Resolution",
            "description": "Annual review consolidated all diagnostic and pharmacological evidence"
        }
    ]
    
    # Discrepancies
    discrepancies = [
        {
            "type": "contradiction",
            "title": "Medical Record Contradiction",
            "severity": "high",
            "description": archetype["contradiction"],
            "linkedEventId": f"{pid}-evt-1"
        },
        {
            "type": "gap",
            "title": "Clinical Loop Left Open / Follow-up Gap",
            "severity": "warning",
            "description": archetype["gap"],
            "linkedEventId": f"{pid}-evt-4"
        }
    ]
    
    patient_record = {
        "id": pid,
        "name": full_name,
        "age": age,
        "gender": gender,
        "dob": dob,
        "bloodGroup": blood_group,
        "phone": phone,
        "city": city_info["city"],
        "state": city_info["state"],
        "address": address,
        "primaryProblem": condition_title,
        "category": archetype["category"],
        "riskStatus": random.choice(["Review Pending", "Moderate Monitoring", "Controlled / Stable", "High Discrepancy Alert", "Active Protocol"]),
        "attendingDoctor": f"{attending_doc[0]}, {attending_doc[1]}",
        "hospital": hospital[0],
        "clinicalSummary": archetype["summary"],
        "events": events,
        "repeatedMetrics": [archetype["repeated_metric"], archetype["repeated_metric2"]],
        "medicationHistory": [
            {
                "drug": archetype["medications"][0]["name"],
                "dose": archetype["medications"][0]["dosage"],
                "timing": archetype["medications"][0]["timing"],
                "status": archetype["medications"][0]["status"],
                "startDate": dates[0][0],
                "indication": "Primary therapeutic control"
            },
            {
                "drug": archetype["medications"][1]["name"],
                "dose": archetype["medications"][1]["dosage"],
                "timing": archetype["medications"][1]["timing"],
                "status": archetype["medications"][1]["status"],
                "startDate": dates[2][0],
                "indication": "Adjunctive organ protection / symptom control"
            },
            {
                "drug": archetype["medications"][2]["name"] if len(archetype["medications"]) > 2 else "Tab. Pantoprazole 40mg",
                "dose": archetype["medications"][2]["dosage"] if len(archetype["medications"]) > 2 else "40mg OD",
                "timing": archetype["medications"][2]["timing"] if len(archetype["medications"]) > 2 else "Before breakfast",
                "status": "Maintained",
                "startDate": dates[0][0],
                "indication": "Supportive gastro-protection / metabolic care"
            }
        ],
        "relationships": relationships,
        "discrepancies": discrepancies
    }
    
    patients.append(patient_record)

# Output as JavaScript file
js_content = "/**\n * ChronosMD - 100 Indian Patient Clinical Profiles\n * Rigorous Multi-Document Longitudinal Records, Genuine Clinical Data\n */\n"
js_content += "var ALL_INDIAN_PATIENTS = " + json.dumps(patients, indent=2) + ";\n\n"
js_content += "if (typeof window !== 'undefined') { window.ALL_INDIAN_PATIENTS = ALL_INDIAN_PATIENTS; }\n"
js_content += "if (typeof module !== 'undefined') { module.exports = { ALL_INDIAN_PATIENTS }; }\n"

output_path = r"c:\HACKTHEBOX\CODEHEIST\HOSPITAL PATIENCE\patients-data.js"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully generated {len(patients)} Indian patient profiles in {output_path}")
