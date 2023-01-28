from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status,permissions,viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .models import *
from .serializers import *
from django.db.models import Q
import os
import pandas as pd
import numpy as np
import json
import csv
import requests

import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

csv_path = os.path.join(BASE_DIR,"visualapp/Indian startups till 2022.csv")
df_full = pd.read_csv(csv_path)
df = df_full
junk_amount_index = []
df_digit_values = df['Amount ($)'].loc[(df['Amount ($)'] != 'Undisclosed') & (df['Amount ($)'] != 'undisclosed')].str.isdigit()
for index, data in df_digit_values.iteritems():
    if not data:
        junk_amount_index.append(index)
df = df.drop(junk_amount_index)
ud_amount_index = []
df_undisclosed_amount_companies = df.loc[(df['Amount ($)'] == 'Undisclosed') | (df['Amount ($)'] == 'undisclosed')]
for index in df_undisclosed_amount_companies.index:
    ud_amount_index.append(index)
df = df.drop(ud_amount_index)
df = df[df['Amount ($)'].notna()]
		
class csvfileinfo(APIView):
	def get(self,request):
		infoofcsv = df.isnull().sum()
		print(infoofcsv)
		print(df.columns)
		x = df.columns
		y = infoofcsv
		x_desc = df.describe()
		data ={'columns':x,'describe':x_desc}
		return Response(data)

class columndata(APIView):
	def get(self,request):
		x = df.columns
		return Response(x)

class Top25Fundedcompanybargraphapi(APIView):
	def get(self,request):
		x = request.GET.get('x')
		y = request.GET.get('y')
		df_top_25_funded_companies = df.sort_values('Amount ($)', ascending=False).head(25)
		#df_top_25_funded_companies = df_top_25_funded_companies.drop([956])
		data = {'x':df_top_25_funded_companies['Company/Brand'].head(5),'y':df_top_25_funded_companies['Amount ($)'].head(5)}
		return Response(data)

class statefundedcompanycountPIE(APIView):
	def get(self, request):
		df_comp_count_per_city = df_full['Headquarters'].value_counts().rename_axis('city').to_frame('count').head(15)
		df_comp_count_per_city_10 = df_comp_count_per_city.head(10)
		data = {'percent':df_comp_count_per_city_10['count'],'labels':df_comp_count_per_city_10.index,'radius':2.5}
		return Response(data)

class companycountpermonthBARAPI(APIView):
	def get(self,request):
		df_comp_count_per_month = df_full['Month'].value_counts().rename_axis('month').to_frame('count')
		x = [df_comp_count_per_month.index[8],df_comp_count_per_month.index[10],df_comp_count_per_month.index[6],df_comp_count_per_month.index[7],df_comp_count_per_month.index[11],df_comp_count_per_month.index[3],df_comp_count_per_month.index[1],df_comp_count_per_month.index[0],df_comp_count_per_month.index[4],df_comp_count_per_month.index[9],df_comp_count_per_month.index[5]]
		y = [df_comp_count_per_month['count'].iloc[8],df_comp_count_per_month['count'].iloc[10],df_comp_count_per_month['count'].iloc[6],df_comp_count_per_month['count'].iloc[7],df_comp_count_per_month['count'].iloc[11],df_comp_count_per_month['count'].iloc[3],df_comp_count_per_month['count'].iloc[1],df_comp_count_per_month['count'].iloc[0],df_comp_count_per_month['count'].iloc[4],df_comp_count_per_month['count'].iloc[9],df_comp_count_per_month['count'].iloc[5]]
		data = {'x':x,'y':y}
		return Response(data)

class monthwisefundingPIE(APIView):
	def get(self, request):
		df_comp_count_per_month = df_full['Month'].value_counts().rename_axis('month').to_frame('count')
		#df_comp_count_per_city_10 = df_comp_count_per_city.head(10)
		data = {'percent':df_comp_count_per_month['count'],'labels':df_comp_count_per_month.index,'radius':2.5}
		return Response(data)


class stagesectormixPIE(APIView):
	def get(self, request):
		df_comp_count_per_month = df['Sector'].value_counts().head(20).rename_axis('Sector').to_frame('count')
		df_stage_count = df['Stage'].value_counts().head(20).rename_axis('Stage').to_frame('count')

		data = {'percent_sector':df_comp_count_per_month['count'],'labels_sector':df_comp_count_per_month.index,'percent_stage':df_stage_count['count'],'labels_stage':df_stage_count.index}
		return Response(data)

class Fundingperregionbargraphapi(APIView):
	def get(self,request):
		funding_per_region= df.groupby(['Headquarters'])['Amount ($)'].sum().reset_index()
		funding_per_region = funding_per_region.sort_values('Amount ($)', ascending= False)
		funding_per_region = funding_per_region.head(20)
		#df_top_25_funded_companies = df_top_25_funded_companies.drop([956])
		x = [funding_per_region['Amount ($)'].iloc[2],funding_per_region['Amount ($)'].iloc[3],funding_per_region['Amount ($)'].iloc[9],funding_per_region['Amount ($)'].iloc[17],funding_per_region['Amount ($)'].iloc[19]]
		y = [funding_per_region['Headquarters'].iloc[2],funding_per_region['Headquarters'].iloc[3],funding_per_region['Headquarters'].iloc[9],funding_per_region['Headquarters'].iloc[17],funding_per_region['Headquarters'].iloc[19]]
		data = {'x':x,'y':y}
		return Response(data)

class codetoenglish(APIView):
	def post(self,request):
		API_URL = "https://api-inference.huggingface.co/models/describeai/gemini"
		headers = {"Authorization": f"Bearer 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"}

		text_input = request.POST.get('text')

		#text = "useEffect(()=> { alanBtn({key: '1cd1c991b78573fc8c9c034eaa1d05ef2e956eca572e1d8b807a3e2338fdd0dc/stage',})}, [])"
		text = text_input


		def query(payload):
		    response = requests.post(API_URL, headers=headers, json=payload)
		    return response.json()

		final_output = [] 

		lines = text.splitlines()
		for i in lines:
		    output = query({
		        "inputs": "explain"+ i + "to a 5 year old",
		    })
		    print(output)
		    final_output.append(output)

		return Response(final_output)          



