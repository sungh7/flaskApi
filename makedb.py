import csv, sqlite3

col = ['Page',
    'MANUFACTURER_AND_DISTRIBUTOR',
    'Date_Released',
    'Date_Available',
    'NAME_OF_DEVICE',
    'DESCRIPTION',
    'MATERIALS',
    'GENERAL_USE',
    'SPECIFIC_INDICATIONS',
    'SPECIFIC_FEATURES',
    'SIZES_AVAILABLE',
    'INSTRUMENTATION',
    'SPECIAL_REMARKS',
    'REFERENCES_',
    'SPECIAL_FEATURES',]

con = sqlite3.connect('./test5.db')
cur = con.cursor()
cur.execute("CREATE TABLE if not exists test1 (Page TEXT, MANUFACTURER_AND_DISTRIBUTOR TEXT, Date_Released TEXT, Date_Available TEXT, NAME_OF_DEVICE TEXT, DESCRIPTION TEXT, MATERIALS TEXT, GENERAL_USE TEXT, SPECIFIC_INDICATIONS TEXT, SPECIFIC_FEATURES TEXT, SIZES_AVAILABLE, INSTRUMENTATION TEXT, SPECIAL_REMARKS TEXT, REFERENCES_ TEXT, SPECIAL_FEATURES TEXT);")

with open('./Orthopaedic_Edvice_Reference2.csv', 'r', encoding='utf-8-sig') as f:
    dr = csv.DictReader(f)
    to_db = [(i[col[0]], i[col[1]], i[col[2]], i[col[3]], i[col[4]], i[col[5]], i[col[6]],i[col[7]], i[col[8]], i[col[9]], i[col[10]], i[col[11]], i[col[12]], i[col[13]], i[col[14]]) for i in dr]

cur.executemany("INSERT INTO test1 (Page, MANUFACTURER_AND_DISTRIBUTOR, Date_Released, Date_Available, NAME_OF_DEVICE, DESCRIPTION, MATERIALS, GENERAL_USE, SPECIFIC_INDICATIONS, SPECIFIC_FEATURES, SIZES_AVAILABLE, INSTRUMENTATION, SPECIAL_REMARKS, REFERENCES_, SPECIAL_FEATURES) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()

