import re
from collections import defaultdict
 
PATTERNS={
    'DISEASE':r'\b(diabetes|hypertension|cancer|pneumonia|fever|asthma|stroke)\b',
    'MEDICATION':r'\b(aspirin|metformin|insulin|paracetamol|ibuprofen|warfarin)\b',
    'DOSAGE':r'\b\d+\s*(?:mg|ml|mcg|units?)\b',
    'DATE':r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b',
    'AGE':r'\b(\d{1,3})\s*(?:year|yr)s?\s*(?:old)?\b'
}
 
def extract_entities(text):
    ents=defaultdict(list)
    for lbl,pat in PATTERNS.items():
        for m in re.finditer(pat,text,re.I): ents[lbl].append(m.group())
    return dict(ents)
 
def extract_relations(text):
    rels=[]
    for m in re.finditer(r'(\w+)\s+diagnosed\s+with\s+(\w+)',text,re.I):
        rels.append(('DIAGNOSED_WITH',m.group(1),m.group(2)))
    for m in re.finditer(r'prescribed\s+(\w+)\s+(\d+\s*mg)',text,re.I):
        rels.append(('PRESCRIBED',m.group(1),m.group(2)))
    return rels
 
records=[
    "Patient 65yr old diagnosed with diabetes. Prescribed metformin 500mg on 12/01/2024.",
    "Fever 38.5C and hypertension noted. aspirin 100mg prescribed. History of stroke."
]
for r in records:
    print("Entities:",extract_entities(r))
    print("Relations:",extract_relations(r)); print()
