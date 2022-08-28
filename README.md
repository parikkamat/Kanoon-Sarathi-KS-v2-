# Interface of Kanoon-Sarathi Based on An Indian Court Decision Annotated Corpus and Knowledge Graph Construction

An annotated Indian Court Decision Document Corpus consisting of 
16 coarse-grained classes and 41 fine-grained classes as a 
benchmark dataset for constructing the knowledge graph. 
Indian Court Case Documents’ knowledge graph constructed by 
utilizing a rule-based approach for Named Entity Recognition (NER) 
and Relation Extraction (RE).

## Indian Court Decision Annotated Corpus
The legal documents for creating the corpus were collected from 
’[Indian Kanoon](https://indiankanoon.org/)’, an online search engine
for Indian legal documents. The data from the text files were split 
into sentences, tokenized word by word and annotated with POS 
tags using SPACY. Named Legal Entities were identified manually 
from these tokens and were tagged with domain specific tags using 
CoNLL-2003 format. The dataset is provided in three different encoding schemes of the CoNLL-2003
An Indian Court Decision Annotated Corpus and KG Construction 7
format, namely BILOU ((B-Beginning, I-Internal, L-Last, O-outside,U-Unit),
IOB (I-Inside, O-Outside, B-Beginning) and IOBES (I-Inside, O-Outside, B-
Beginning, E-End, S-Single). The dataset is published using FigShare with CC by 4.0 licence with the DOI:
https://doi.org/10.6084/m9.figshare.19719088.v1
## Knowledge Graph Construction
The two major steps for the construction of the knowledge graph are Named
Entity Recognition (NER) and Relation Extraction (RE). Various legal entities
identified from the corpus by referring to the [NyOn](https://github.com/semintelligence/NyOn) Ontology are combined together with the relations extracted for the construction of the Knowledge Graph
(KG). 

### Triple Construction

The Triples were formed by annotating the entities obtained from NER with the relations exrtracted in the RE phase.
The constructed triples were stored in a triple store (Apache Jena Fuseki) by manualy converting it to turtle(.ttl) format  and visualized using GraphDb.
An example of the manualy constructed RDf(.ttl) file and knowledge graph visualized through GraphDb are given below.

```
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix dc: <http://purl.org/dc/elements/1.1/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix schema: <http://schema.org/> .
@prefix : <http://example.org/#> .

:Case a schema:Thing ;
   dc:hasCaseName :case1, :case2 ;
.

:case2
          a schema:KT_Varghese_Ors_VS_State_of_Kerala ;
          rdfs:label "K.T. Varghese & Ors VS. State of Kerala & Ors. on 24/01/2008" ;                                
          dc:hasParty :case2P1, :case2P2;
 rdfs:hasAppealNo "Appeal No.547/1998";
 rdfs:hasCaseNo "Appeal (civil) 6456 of 2001";
 rdfs:hasCaseType "civil";
 rdfs:hasDate "24/01/2008";
 rdfs:hasAuthor :case2Judge2;
          rdfs:hasCourtDecision "Appeal is Allowed" ;
          dc:hasCourtOfficial :case2Judge1, :case2Judge2, :case2Judge3 ;
         
.

:case2P1 a schema:Petitioner, foaf:Person ;
            rdfs:hasName "K.T. Varghese & Ors" ;
.

:case2P2 a schema:Respondent, foaf:Person ;
            rdfs:hasName "State of Kerala & Ors" ;
.
```

![Knowledge Graph](https://github.com/semintelligence/KING/blob/main/kg%20ttl%20file/kg.jpg "Knowledge Graph visualized through GraphDB")
## Competency Questions and SPARQL Query
The triples formed where tested against competency questions with the help of SPARQL queries.
Screenshots of the competency questions, corresponnding SPARQL queries and outputs are attached below.

1. List all court officials that come under 'K.T. Varghese & Ors VS. State of Kerala & Ors.'
![Query 1](https://github.com/semintelligence/KING/blob/main/query/query1.JPG "Query 1")
![Output 1](https://github.com/semintelligence/KING/blob/main/output/output1.JPG)

2. What is the case number of case 'K.T. Varghese & Ors VS. State of Kerala & Ors.'
![Query 2](https://github.com/semintelligence/KING/blob/main/query/query2.JPG "Query 2")
![Output 2](https://github.com/semintelligence/KING/blob/main/output/output2.JPG)

3. Who is the Petitioner of 'K.T. Varghese & Ors VS. State of Kerala & Ors.'?
![Query 3](https://github.com/semintelligence/KING/blob/main/query/query3.JPG "Query 3")
![Output 3](https://github.com/semintelligence/KING/blob/main/output/output3.JPG)

4. List all the parties that come under case 'K.T. Varghese & Ors VS. State of Kerala & Ors.'
![Query 4](https://github.com/semintelligence/KING/blob/main/query/query4.JPG "Query 4")
![Output 4](https://github.com/semintelligence/KING/blob/main/output/output4.JPG)

## Using Django Framework and SPARQL Endpoint to Develop GUI

First you need to create the SPARQL endpoint for this work, by the help of HEROKU platform to complete this task so what you need to do is just create one account on heroku and follow this [steps](https://github.com/semintelligence/Tutorials/tree/main/Creating%20SPARQL%20endpoint) and then you done with this task then use this endpoint in DJango to fire the SPARQL Query and show your result in frontend.

```
from SPARQLWrapper import SPARQLWrapper, JSON , CSV
import pandas as pd
import numpy as np

class get_data:

    def __init__(self):
        self.sparql = SPARQLWrapper('https://kanoon.herokuapp.com/LegalCase/sparql')

    def case2_judge_name(self):
        
        self.sparql.setQuery("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
        PREFIX dc: <http://purl.org/dc/elements/1.1/> 
        PREFIX foaf: <http://xmlns.com/foaf/0.1/> 
        PREFIX schema: <http://schema.org/> 
        PREFIX : <http://example.org/#> 
        SELECT ?JudgesofCase2
        WHERE {
        ?Case dc:hasInstance :case2.
        :case2  dc:hasCourtOfficial ?Judges .
        ?Judges  rdfs:hasName ?JudgesofCase2 .
        }
        """
        )
        
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        
        judge = []
        for result in results["results"]["bindings"]:
              judge.append( result["JudgesofCase2"]["value"])
             
    
        return judge
```

As shown in this above code snippet sparqlwrapper is the api which you are using to pass the sparl endpoint url and then next step is write the query in seperate functions and call this function in views.py and by the help of ginger syntax you can show your result in your GUI.

# UI For Legal Text Extraction With Help Of Django

I am using Heroku freehosting site for creation or hosting the website so [Kanoon-Sarathi](https://kanoon-sarathi.herokuapp.com/) is the website that will take the queries and then extract result using SPARQL. 
