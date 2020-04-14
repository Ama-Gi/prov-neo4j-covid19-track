from provdbconnector import ProvDb
from provdbconnector import Neo4jAdapter
import  os
import pkg_resources
import os

# Data is from: https://provenance.ecs.soton.ac.uk/store/documents/75490/


NEO4J_USER = os.environ.get('NEO4J_USERNAME', 'neo4j')
NEO4J_PASS = os.environ.get('NEO4J_PASSWORD', 'neo4jneo4j')
NEO4J_HOST = os.environ.get('NEO4J_HOST', 'localhost')
NEO4J_BOLT_PORT = os.environ.get('NEO4J_BOLT_PORT', '7687')



# Auth info
auth_info = {"user_name": NEO4J_USER,
             "user_password": NEO4J_PASS,
             "host": NEO4J_HOST + ":" + NEO4J_BOLT_PORT
             }


# create the api
prov_api = ProvDb(adapter=Neo4jAdapter, auth_info=auth_info)


for line in range(3, 44):
    os.system('cat csv1.csv | awk -v line='+str(line)+' -f tobindings.awk > bindings.json')
    os.system('provconvert -bindver 3 -infile template_block.provn -bindings bindings.json -outfile block.json')
    os.system('provconvert o-bindver 3 -infile template_block.provn -bindings bindings.json -outfile block'+str(line)+'.pdf')
# create the prov document from examples    prov_document_buffer = pkg_resources.resource_stream("examples", "block.json")
    prov_document_buffer = pkg_resources.resource_stream("examples", "block.json")
    print(line)
    # Save document
    document_id = prov_api.save_document(prov_document_buffer)
# This is similar to:
# prov_api.create_document_from_json(prov_document_buffer)

# get document
    print(prov_api.get_document_as_provn(document_id))