from django.shortcuts import render, redirect
from pyexcel_xls import get_data as xls_get
from pyexcel_xlsx import get_data as xlsx_get
from django.utils.datastructures import MultiValueDictKeyError
from .models import Candidate
from .forms import Upload_File
from django.views import View

class ParseExcel(View):

    def post(self, request, format=None):
        form = Upload_File(request.POST, request.FILES)
        if True:
            excel_file = request.FILES['upload_file']
            if (str(excel_file).split('.')[-1] == "xls"):
                data = xls_get(excel_file, column_limit=6)
            elif (str(excel_file).split('.')[-1] == "xlsx"):
                data = xlsx_get(excel_file, column_limit=6)
            else:
                return render(request, 'xltodb/upload.html', {'form' :form})

            candidates = data["addressSample"]
            if (len(candidates) > 1): 
                print('1')
                for a_candidate in candidates:
                    if (len(a_candidate) > 0): # The row is not blank
                        print('2')
                        if (a_candidate[0] != "Instruction ID"): # This is not header
                            print('3')
                            if (len(a_candidate) <= 6):
                                print('4')
                                i = len(a_candidate)
                                while (i <= 6):
                                    a_candidate.append("")
                                    i+=1
                                Candidate.objects.create(
                                    instruction_ID= a_candidate[0],
                                    case_ref_no= a_candidate[1],
                                    client_name= a_candidate[2],
                                    candidate_name= a_candidate[3],
                                    complete_address= a_candidate[4],
                                    period_od_stay= a_candidate[5]
                                )
        return render(request, 'xltodb/uploaded.html')
    
    def get(self, request):
        form  = Upload_File()
        return render(request, 'xltodb/upload.html', {'form' :form})
