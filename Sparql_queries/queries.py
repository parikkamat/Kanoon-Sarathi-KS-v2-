from SPARQLWrapper import SPARQLWrapper, JSON , CSV
import pandas as pd
import numpy as np

class get_data:

    def __init__(self):
        self.sparql = SPARQLWrapper('https://kanoonkg.herokuapp.com/kg/sparql')


    def nameOfCases(self):
        
        self.sparql.setQuery("""
       PREFIX nyon: <https://w3id.org/def/NyOn#>
       PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
       PREFIX foaf: <http://xmlns.com/foaf/0.1/>
       Select ?CaseName where
       {
    
          ?case nyon:hasCaseName ?CaseName.
       }


        """
        )
        
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        
        case_name = []
        for result in results["results"]["bindings"]:
              case_name.append( result["CaseName"]["value"])
             
    
        return case_name    



    def get_case_number(self,case_name_for_caseNo):
        query ="""
        PREFIX nyon: <https://w3id.org/def/NyOn#> 
        Select ?CaseNumber where
        {
    
               ?case nyon:hasCaseName \""""+case_name_for_caseNo+"""\"@en;
                     nyon:hasCaseNo ?CaseNumber.

        }
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        get_caseNo_of_case = []
        for result in results["results"]["bindings"]:
            get_caseNo_of_case.append( result["CaseNumber"]["value"])
            
        return get_caseNo_of_case


    def get_parties_of_cases(self,case_name_for_parties):
        
        query ="""
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX nyon: <https://w3id.org/def/NyOn#>
        select ?parties where
        {
          ?case nyon:hasCaseName \""""+case_name_for_parties+"""\"@en;
          nyon:hasParty ?peti.
          ?peti rdfs:label ?parties.    
         }
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        get_party_of_case = []
        for result in results["results"]["bindings"]:
            get_party_of_case.append( result["parties"]["value"])
            
        return get_party_of_case
   

    def get_petitioner_of_cases(self,case_name_for_petitioner):
        
        query ="""
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX nyon: <https://w3id.org/def/NyOn#>
        select ?petitioner where
        {
          ?case nyon:hasCaseName \""""+case_name_for_petitioner+"""\"@en;
          nyon:hasParty ?peti.
          ?peti rdfs:type nyon:Petitioner;
          rdfs:label ?petitioner .    
}
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        get_petitioner_of_case = []
        for result in results["results"]["bindings"]:
            get_petitioner_of_case.append( result["petitioner"]["value"])
            
        return get_petitioner_of_case


    def get_courtofficial_of_cases(self,case_name_for_courtofficial):
        
        query ="""
        PREFIX nyon: <https://w3id.org/def/NyOn#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        select ?CourtOfficial where
        {
         ?case nyon:hasCaseName  \""""+case_name_for_courtofficial+"""\"@en;
         nyon:hasCourtOfficial ?participants.
         ?participants rdfs:label ?CourtOfficial.
        }    
        """
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        
        get_CourtOfficial_of_case = []
        for result in results["results"]["bindings"]:
            get_CourtOfficial_of_case.append( result["CourtOfficial"]["value"])
            
        return get_CourtOfficial_of_case

    

       