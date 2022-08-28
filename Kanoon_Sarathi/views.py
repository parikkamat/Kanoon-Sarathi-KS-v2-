from django.shortcuts import render,HttpResponse
from Sparql_queries.queries import get_data


def index(request):
    sparqlQueries = get_data()
    
    
    _context = {}
    data = {}

    N_cases = sparqlQueries.nameOfCases()
    #print(judges)
    _context = {
            "name1":N_cases,
            'flag':True,
            'suffix':'Casesss_',
            'title':'N Cases'
            
           }
    
    if(request.method=='POST'):
        
        
        casename = request.POST['Case_name']
        question = request.POST['Question']
        print(casename)
        print(question)

        
        if(question == 'List all the parties that come under the case?'):
            
            parties = sparqlQueries.get_parties_of_cases(casename)
            data = {
                "name":parties,
                'flag':True,
                'suffix':'parties',
                'title':'parties of Case'
                
             }

            data.update(_context)

            return render(request,'index.html', context = data)


        if(question == 'Who is the Petitioner of the case?'):
            
            petitioner = sparqlQueries.get_petitioner_of_cases(casename)
            data = {
                "name":petitioner,
                'flag':True,
                'suffix':'petitioner',
                'title':'petitioner of Case'
                
             }

            data.update(_context) 

            return render(request,'index.html', context = data)


        if(question == 'What is the Case No. of the case?'):
            
            judges = sparqlQueries.get_case_number(casename)
            print(judges)
            data = {
                "name":judges,
                'flag':True,
                'suffix':'judges',
                'title':'Judge of Case2'
                
             }

            data.update(_context) 

            return render(request,'index.html', context = data)    
        

        if(question == 'List all court officials that come under the case.'):
            
            courtofficial = sparqlQueries.get_courtofficial_of_cases(casename)
            #print(judges)
            data = {
                "name":courtofficial,
                'flag':True,
                'suffix':'courtofficial',
                'title':'courtofficial of Case2'
                
             }

            data.update(_context) 

            return render(request,'index.html', context = data) 
        
        
        
        
        
    
    
         

    return render(request,'index.html', context = _context)