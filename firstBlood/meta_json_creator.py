from sql_decl import Base, Block, Bundle, Teacher
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json

engine = create_engine('sqlite:///sched.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

blocks_dict={}
query_blocks = session.query(Block.name, Block.id)
for block_name, block_id in query_blocks:
    blocks_dict[block_name] = block_id
    #print(f"{block_name}:{block_id}")

with open('blocks.json','w') as f:
    json.dump(blocks_dict, f)


bundles_dict={}
query_bundles = session.query(Bundle.name, Bundle.id)
for bundle_name, bundle_id in query_bundles:
    bundles_dict[bundle_name] = bundle_id
    #print(f"{bundle_name}:{bundle_id}")

with open('bundles.json','w') as f:
    json.dump(bundles_dict, f)


teachers_dict={}
query_teachers = session.query(Teacher.name,Teacher.id)
for teacher_name, teacher_id in query_teachers:
    teachers_dict[teacher_name] = teacher_id
    #print(f"{teacher_name}:{teacher_id}")

with open('teachers.json','w') as f:
    json.dump(teachers_dict, f)

blocks_dict.clear()

with open('blocks.json', 'r') as f:
    blocks_dict = json.load(f)

for block in blocks_dict:
    print(f"{block} : {blocks_dict[block]}")

bundles_dict.clear()

with open('bundles.json', 'r') as f:
    bundles_dict = json.load(f)

for bundle in bundles_dict:
    print(f"{bundle} : {bundles_dict[bundle]}")

teachers_dict.clear()

with open('teachers.json', 'r') as f:
    teachers_dict = json.load(f)

for teacher in teachers_dict:
    print(f"{teacher} : {teachers_dict[teacher]}")
