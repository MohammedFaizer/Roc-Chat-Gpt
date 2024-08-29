# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import PromptSerializer
# from django.conf import settings
# from openai import OpenAI
# from pydantic import BaseModel

# class PropertyEvent(BaseModel):
#     location: list[str]
#     min_price:  int
#     max_price: int
#     bedrooms: int
#     bathrooms: int
#     apartment_type: list[str] 


# class Roc_Properties_Views(APIView):

#     def post(self, request, *args, **kwargs):
#         serializer = PromptSerializer(data=request.data)
#         if serializer.is_valid():
#             prompt = serializer.validated_data['prompt']
#             client = OpenAI()
#             completion = client.beta.chat.completions.parse(
#             model="gpt-4o-2024-08-06",
#             messages=[
#             {"role": "system", 
#             "content": "Extract the Property related filter information.only with respect to context if not dont give answer. Caution : Don't fill with values leave blank"},
#             {"role": "user", "content": f"{prompt}"},
#             ],
#             response_format=PropertyEvent,
#             )
#             event = completion.choices[0].message.parsed
#             if event is not None:
#                 event_dict = event.dict()  
#                 return Response(event_dict, status=status.HTTP_200_OK)
#             else:
#                 return Response({"error": "No valid response parsed from the completion."}, status=status.HTTP_204_NO_CONTENT)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# #this is the currently working model
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import PromptSerializer
# from django.conf import settings
# from openai import OpenAI
# from typing import List, Union,Optional
# from enum import Enum
# from pydantic import BaseModel,model_validator,Field

# class Category(str, Enum):
#     rent = "rent"
#     sold = "sold"
#     sale = "sale"

# class Bedrooms(str, Enum):
#     any = "Any"
#     studio = "Studio"
#     one = "1"
#     two = "2"
#     three = "3"
#     four = "4"
#     five = "5+"

# class HomeType(str, Enum):
#     single_family = "Single Family"
#     condo = "Condo"
#     town_house = "Town House"
#     multifamily = "Multi Family"
#     land = "Land"
#     Others = "Others"
    

# class Bathrooms(str, Enum):
#     any = "Any"
#     one_plus = "1+"
#     one_and_half_plus = "1.5+"
#     two_plus = "2+"
#     three_plus = "3+"
#     four_plus = "4+"

# class SquareFeet(int,Enum):
#     _750 = 750
#     _1000 = 1000
#     _1100 = 1100
#     _1200 = 1200
#     _1300 = 1300
#     _1400 = 1400
#     _1500 = 1500
#     _1600 = 1600
#     _1700 = 1700
#     _1800 = 1800
#     _1900 = 1900
#     _2000 = 2000
#     _2250 = 2250
#     _2500 = 2500
#     _2750 = 2750
#     _3000 = 3000
#     _4000 = 4000
#     _5000 = 5000
#     _7500 = 7500
#     _10000 = 10000

# class LotSize(str,Enum):
#     _2000_SQFT = "2000 sqft"
#     _4500_SQFT = "4500 sqft"
#     _6500_SQFT = "6500 sqft"
#     _8000_SQFT = "8000 sqft"
#     _9500_SQFT = "9500 sqft"
#     _1_ACRE = "1 acres"
#     _0_5_ACRE = ".5 acres"
#     _0_25_ACRE = ".25 acres"
#     _2_ACRE = "2 acres"
#     _3_ACRE = "3 acres"
#     _4_ACRE = "4 acres"
#     _5_ACRE = "5 acres"
#     _10_ACRE = "10 acres"
#     _20_ACRE = "20 acres"
#     _40_ACRE = "40 acres"
#     _100_ACRE = "100 acres"

# class Stories(int,Enum):
#     ONE = 1
#     TWO = 2
#     THREE = 3
#     FOUR = 4
#     FIVE = 5
#     TEN = 10
#     FIFTEEN = 15
#     TWENTY = 20

# class YearBuilt(int, Enum):
#     YEAR_1920 = 1920
#     YEAR_1940 = 1940
#     YEAR_1960 = 1960
#     YEAR_1980 = 1980
#     YEAR_1990 = 1990
#     YEAR_2000 = 2000
#     YEAR_2005 = 2005
#     YEAR_2010 = 2010
#     YEAR_2014 = 2014
#     YEAR_2015 = 2015
#     YEAR_2016 = 2016
#     YEAR_2017 = 2017
#     YEAR_2018 = 2018
#     YEAR_2019 = 2019
#     YEAR_2020 = 2020
#     YEAR_2021 = 2021
#     YEAR_2022 = 2022
#     YEAR_2023 = 2023
#     YEAR_2024 = 2024



# class PropertyEvent(BaseModel):
#     category: Category
#     minimum_price: Optional[int]
#     maximum_price: Optional[int]
#     bedrooms: Bedrooms
#     bathrooms:Bathrooms
#     home_type:list[HomeType]
#     minimum_square_feet:Optional[SquareFeet]
#     maximum_square_feet: Optional[SquareFeet]
#     minimum_lot_size: Optional[LotSize]
#     maximum_lot_size: Optional[LotSize]
#     minimum_year_built: Optional[YearBuilt]
#     maximum_year_built: Optional[YearBuilt]
#     minimum_stories: Optional[Stories]
#     maximum_stories: Optional[Stories]
#     location: Optional[str]
                    
#     @model_validator(mode='after')
#     def set_minimum_price(cls, values):
#         if values.minimum_price is None:  
#             if values.category == Category.rent:
#                 values.minimum_price = 200
#             elif values.category == Category.sold:
#                 values.minimum_price = 50000
#             elif values.category == Category.sale:
#                 values.minimum_price = 50000
#         return values

#     @model_validator(mode='after')
#     def set_maximum_price(cls, values):
#         if values.maximum_price is None:  
#             if values.category == Category.rent:
#                 values.maximum_price = 5000
#             elif values.category == Category.sold:
#                 values.maximum_price = 5000000
#             elif values.category == Category.sale:
#                 values.maximum_price = 5000000
#         return values


# class Roc_Properties_Views(APIView):

#     def post(self, request, *args, **kwargs):
#         serializer = PromptSerializer(data=request.data)
#         if serializer.is_valid():
#             prompt = serializer.validated_data['prompt']
#             client = OpenAI()
#             completion = client.beta.chat.completions.parse(
#             model="gpt-4o-2024-08-06",
#             messages=[
#             {"role": "system", 
#             "content": 
#             """
# You are an AI assistant designed to help users find properties based on their preferences. You will be provided with a prompt describing a real estate situation. Your task is to extract and fill in the property-related filter fields, including details such as location, size, number of bedrooms, bathrooms, home type, price, and other relevant information.

# Key Guidelines:

# Focus solely on extracting information relevant to real estate property details from the prompt.
# Fill out as many relevant fields as possible, but only if the context provides clear information.
# If the prompt does not contain specific details for a field, leave it blank.
# Avoid including any personal or sensitive information.
# Ensure that the extracted information aligns with the expected response type.
#             """},
#             {"role": "user", "content": f"{prompt}"},
#             ],
#             response_format=PropertyEvent,
#             )
#             event = completion.choices[0].message.parsed
#             if event is not None:
#                 event_dict = event.dict()
               
#                 return Response(event_dict, status=status.HTTP_200_OK)
#             else:
#                 return Response({"error": "No valid response parsed from the completion."}, status=status.HTTP_204_NO_CONTENT)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#Second level code
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import PromptSerializer
# from django.conf import settings
# from openai import OpenAI
# from typing import List, Union,Optional
# from enum import Enum
# from pydantic import BaseModel,model_validator,Field
# import requests
# import json
# import openai
# class PropertyEvent(BaseModel):
    
#     location: Optional[str]
#     polygon_id: Optional[str]
#     state_code: Optional[str]
#     type: Optional[str]


# class Roc_Properties_Views(APIView):

#     def post(self, request, *args, **kwargs):
#         serializer = PromptSerializer(data=request.data)
#         if serializer.is_valid():

#             prompt = serializer.validated_data['prompt']
#             client = OpenAI()
            
#             completion = client.chat.completions.create(
            
#             model="gpt-4o-2024-08-06",
#             messages=[
#             {"role": "system", "content": "fetch the location fields from the prompt given by the user with respect to response type"},
#             {"role": "user", "content": f"{prompt}"},
#             ],
            
#             tools = [
#                 {
#                     "type": "function",
#                     "function": {
#                         "name": "get_location_details",
#                         "strict": True,
#                         "description": "Get the location details for the user. if users gives the location, call this function and use this tool example 'i live in chennai'",
#                         "parameters": {
#                             "type": "object",
#                             "properties": {
#                                 "location": {
#                                     "type": "string",
#                                     "description": "User given location",
#                                 },
#                             },
#                             "required": ["location"],
#                             "additionalProperties": False,
#                         },
#                     }
#                 }],
              
                
#             )
#             tool_call = completion.choices[0].message.tool_calls[0]
#             arguments = json.loads(tool_call.function.arguments)
#             location = arguments.get('location')
#             location_details = self.get_location_details(location)

#             function_call_result_message = {
#     "role": "tool",
#     "content": json.dumps({
#         "location": location,
#         "location_details": location_details
#     }),
#     "tool_call_id": completion.choices[0].message.tool_calls[0].id
# }
           
#             completion_payload = {
#                 "model": "gpt-4o-2024-08-06",
#     "messages": [
#         {"role": "system", "content": "fill all the necessary field in the response format from the information "},
#             {"role": "user", "content": f"{prompt}"},
#         completion.choices[0].message,  
#         function_call_result_message
#     ]
# }
#             response = client.beta.chat.completions.parse(
#             model=completion_payload["model"],
#             messages=completion_payload["messages"],
#             response_format=PropertyEvent,
#             )
#             event = response.choices[0].message.parsed
#             if event is not None:
#                 event_dict = event.dict()  
#                 return Response(event_dict, status=status.HTTP_200_OK)
            
#             return Response(response, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def get_location_details(self,location: str):
#         api_url = f"https://roc-staging-api.cyces.co/web/property/search/meta?search={location}"
#         response = requests.get(api_url)

#         if response.status_code == 200:
#             return response.json()  # Return the JSON response from the API
#         else:
#             return {"error": f"Failed to retrieve data for location {location}. Status code: {response.status_code}"}









#pleaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PromptSerializer
from django.conf import settings
from openai import OpenAI
from typing import List, Union,Optional
from enum import Enum
from pydantic import BaseModel,model_validator,Field
import requests
import json
import openai


class Category(str, Enum):
    rent = "rent"
    sold = "sold"
    sale = "sale"

class Bedrooms(str, Enum):
    any = "Any"
    studio = "Studio"
    one = "1"
    two = "2"
    three = "3"
    four = "4"
    five = "5+"

class HomeType(str, Enum):
    single_family = "Single Family"
    condo = "Condo"
    town_house = "Townhouse"
    multifamily = "Multifamily"
    land = "Land"
    Others = "Others"
    

class Bathrooms(str, Enum):
    any = "Any"
    one_plus = "1"
    one_and_half_plus = "1.5"
    two_plus = "2"
    three_plus = "3"
    four_plus = "4"

class SquareFeet(int,Enum):
    _750 = 750
    _1000 = 1000
    _1100 = 1100
    _1200 = 1200
    _1300 = 1300
    _1400 = 1400
    _1500 = 1500
    _1600 = 1600
    _1700 = 1700
    _1800 = 1800
    _1900 = 1900
    _2000 = 2000
    _2250 = 2250
    _2500 = 2500
    _2750 = 2750
    _3000 = 3000
    _4000 = 4000
    _5000 = 5000
    _7500 = 7500
    _10000 = 10000

class LotSize(str,Enum):
    _2000_SQFT = "2000 sqft"
    _4500_SQFT = "4500 sqft"
    _6500_SQFT = "6500 sqft"
    _8000_SQFT = "8000 sqft"
    _9500_SQFT = "9500 sqft"
    _1_ACRE = "1 acres"
    _0_5_ACRE = ".5 acres"
    _0_25_ACRE = ".25 acres"
    _2_ACRE = "2 acres"
    _3_ACRE = "3 acres"
    _4_ACRE = "4 acres"
    _5_ACRE = "5 acres"
    _10_ACRE = "10 acres"
    _20_ACRE = "20 acres"
    _40_ACRE = "40 acres"
    _100_ACRE = "100 acres"

class Stories(int,Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    TEN = 10
    FIFTEEN = 15
    TWENTY = 20

class YearBuilt(int, Enum):
    YEAR_1920 = 1920
    YEAR_1940 = 1940
    YEAR_1960 = 1960
    YEAR_1980 = 1980
    YEAR_1990 = 1990
    YEAR_2000 = 2000
    YEAR_2005 = 2005
    YEAR_2010 = 2010
    YEAR_2014 = 2014
    YEAR_2015 = 2015
    YEAR_2016 = 2016
    YEAR_2017 = 2017
    YEAR_2018 = 2018
    YEAR_2019 = 2019
    YEAR_2020 = 2020
    YEAR_2021 = 2021
    YEAR_2022 = 2022
    YEAR_2023 = 2023
    YEAR_2024 = 2024


class Type(str, Enum):
    neighbourhood = "neighbourhood"
    city = "city"

# class PropertyEvent(BaseModel):
#     location: Optional[str]
#     type: Optional[Type]
#     polygon_id: Optional[str]
#     state_code: str
#     state:str
#     category: Category
#     minimum_price: Optional[int]
#     maximum_price: Optional[int]
#     bedrooms: Bedrooms
#     bathrooms:Bathrooms
#     home_type:list[HomeType]
#     minimum_square_feet:Optional[SquareFeet]
#     maximum_square_feet: Optional[SquareFeet]
#     minimum_lot_size: Optional[LotSize]
#     maximum_lot_size: Optional[LotSize]
#     minimum_year_built: Optional[YearBuilt]
#     maximum_year_built: Optional[YearBuilt]
#     minimum_stories: Optional[Stories]
#     maximum_stories: Optional[Stories]
#     latitude:str
#     longitude:str

class PropertyEvent(BaseModel):
    location: Optional[str]
    type: Optional[Type]
    polygon_id: Optional[str]
    state_code: Optional[str]
    state:Optional[str]
    category: Category
    minimum_price: Optional[int]
    maximum_price: Optional[int]
    bedrooms: Optional[Bedrooms]
    bathrooms:Optional[Bathrooms]
    home_type:Optional[list[HomeType]]
    minimum_square_feet:Optional[SquareFeet]
    maximum_square_feet: Optional[SquareFeet]
    minimum_lot_size: Optional[LotSize]
    maximum_lot_size: Optional[LotSize]
    minimum_year_built: Optional[YearBuilt]
    maximum_year_built: Optional[YearBuilt]
    minimum_stories: Optional[Stories]
    maximum_stories: Optional[Stories]
    latitude:Optional[str]
    longitude:Optional[str]
                    
    # @model_validator(mode='after')
    # def set_minimum_price(cls, values):
    #     if values.minimum_price is None:  
    #         if values.category == Category.rent:
    #             values.minimum_price = 200
    #         elif values.category == Category.sold:
    #             values.minimum_price = 50000
    #         elif values.category == Category.sale:
    #             values.minimum_price = 50000
    #     return values

    # @model_validator(mode='after')
    # def set_maximum_price(cls, values):
    #     if values.maximum_price is None:  
    #         if values.category == Category.rent:
    #             values.maximum_price = 5000
    #         elif values.category == Category.sold:
    #             values.maximum_price = 5000000
    #         elif values.category == Category.sale:
    #             values.maximum_price = 5000000
    #     return values


class Roc_Properties_Views(APIView):

    def post(self, request, *args, **kwargs):
        serializer = PromptSerializer(data=request.data)
        if serializer.is_valid():

            prompt = serializer.validated_data['prompt']
            client = OpenAI()
            
            completion = client.chat.completions.create(
            model="gpt-4o-2024-08-06",
            messages=[
            {"role": "system", "content": "fetch the location fields from the prompt given by the user with respect to response type"},
            # {"role": "system", "content": "Check wether the context is related to the property"},           
            {"role": "user", "content": f"{prompt}"},
            ], 
            tools = [
                {
                    "type": "function",
                    "function": {
                        "name": "get_location_details",
                        "strict": True,
                        "description": "Get the location details for the user. if users gives the location, call this function and use this tool example 'i live in chennai'",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "location": {
                                    "type": "string",
                                    "description": "User given location",
                                },
                            },
                            "required": ["location"],
                            "additionalProperties": False,
                        },
                    }
                }],    
            )
          
            completion_payload = {
                "model": "gpt-4o-2024-08-06",
                "messages": [
                    {"role": "system", "content": """
                    fill all the necessary field in the response format from the information provided by tools . fetch latitude and longitude for the given location from your knowledge base
                    if information is not subject to property set null for all values
                    answer only to context
                     """},
                        {"role": "user", "content": f"{prompt}"},
                ]

                }
            
            if (completion.choices[0].finish_reason == "tool_calls" ):
                tool_call = completion.choices[0].message.tool_calls[0]
                arguments = json.loads(tool_call.function.arguments)
                location = arguments.get('location')
                print(location)
                location_details = self.get_location_details(location)
                function_call_result_message = {
                                    "role": "tool",
                                    "content": json.dumps({
                                        "location": location,
                                        "location_details": location_details
                                    }),
                                    "tool_call_id": completion.choices[0].message.tool_calls[0].id
                                }
                completion_payload['messages'].append(completion.choices[0].message)
                completion_payload['messages'].append(function_call_result_message)
            
            response = client.beta.chat.completions.parse(
            model=completion_payload["model"],
            messages=completion_payload["messages"],
            response_format=PropertyEvent,
            )
            event = response.choices[0].message.parsed
            if event is not None:
                event_dict = event.dict()  
                return Response(event_dict, status=status.HTTP_200_OK)

            
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get_location_details(self,location: str):
        api_url = f"https://roc-staging-api.cyces.co/web/property/search/meta?search={location}"
        response = requests.get(api_url)

        if response.status_code == 200:
            return response.json()  # Return the JSON response from the API
        else:
            return {"error": f"Failed to retrieve data for location {location}. Status code: {response.status_code}"}





#worrkkin
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import PromptSerializer
# from django.conf import settings
# from openai import OpenAI
# from typing import List, Union,Optional
# from enum import Enum
# from pydantic import BaseModel,model_validator,Field
# import requests
# import json
# import openai

# class Category(str, Enum):
#     rent = "rent"
#     sold = "sold"
#     sale = "sale"

# class Bedrooms(str, Enum):
#     any = "Any"
#     studio = "Studio"
#     one = "1"
#     two = "2"
#     three = "3"
#     four = "4"
#     five = "5+"

# class HomeType(str, Enum):
#     single_family = "Single Family"
#     condo = "Condo"
#     town_house = "Town House"
#     multifamily = "Multi Family"
#     land = "Land"
#     Others = "Others"
    

# class Bathrooms(str, Enum):
#     any = "Any"
#     one_plus = "1+"
#     one_and_half_plus = "1.5+"
#     two_plus = "2+"
#     three_plus = "3+"
#     four_plus = "4+"

# class SquareFeet(int,Enum):
#     _750 = 750
#     _1000 = 1000
#     _1100 = 1100
#     _1200 = 1200
#     _1300 = 1300
#     _1400 = 1400
#     _1500 = 1500
#     _1600 = 1600
#     _1700 = 1700
#     _1800 = 1800
#     _1900 = 1900
#     _2000 = 2000
#     _2250 = 2250
#     _2500 = 2500
#     _2750 = 2750
#     _3000 = 3000
#     _4000 = 4000
#     _5000 = 5000
#     _7500 = 7500
#     _10000 = 10000

# class LotSize(str,Enum):
#     _2000_SQFT = "2000 sqft"
#     _4500_SQFT = "4500 sqft"
#     _6500_SQFT = "6500 sqft"
#     _8000_SQFT = "8000 sqft"
#     _9500_SQFT = "9500 sqft"
#     _1_ACRE = "1 acres"
#     _0_5_ACRE = ".5 acres"
#     _0_25_ACRE = ".25 acres"
#     _2_ACRE = "2 acres"
#     _3_ACRE = "3 acres"
#     _4_ACRE = "4 acres"
#     _5_ACRE = "5 acres"
#     _10_ACRE = "10 acres"
#     _20_ACRE = "20 acres"
#     _40_ACRE = "40 acres"
#     _100_ACRE = "100 acres"

# class Stories(int,Enum):
#     ONE = 1
#     TWO = 2
#     THREE = 3
#     FOUR = 4
#     FIVE = 5
#     TEN = 10
#     FIFTEEN = 15
#     TWENTY = 20

# class YearBuilt(int, Enum):
#     YEAR_1920 = 1920
#     YEAR_1940 = 1940
#     YEAR_1960 = 1960
#     YEAR_1980 = 1980
#     YEAR_1990 = 1990
#     YEAR_2000 = 2000
#     YEAR_2005 = 2005
#     YEAR_2010 = 2010
#     YEAR_2014 = 2014
#     YEAR_2015 = 2015
#     YEAR_2016 = 2016
#     YEAR_2017 = 2017
#     YEAR_2018 = 2018
#     YEAR_2019 = 2019
#     YEAR_2020 = 2020
#     YEAR_2021 = 2021
#     YEAR_2022 = 2022
#     YEAR_2023 = 2023
#     YEAR_2024 = 2024



# class PropertyEvent(BaseModel):
#     location: Optional[str]
#     type: Optional[str]
#     polygon_id: Optional[str]
#     state_code: str
#     state:str
#     category: Category
#     minimum_price: Optional[int]
#     maximum_price: Optional[int]
#     bedrooms: Bedrooms
#     bathrooms:Bathrooms
#     home_type:list[HomeType]
#     minimum_square_feet:Optional[SquareFeet]
#     maximum_square_feet: Optional[SquareFeet]
#     minimum_lot_size: Optional[LotSize]
#     maximum_lot_size: Optional[LotSize]
#     minimum_year_built: Optional[YearBuilt]
#     maximum_year_built: Optional[YearBuilt]
#     minimum_stories: Optional[Stories]
#     maximum_stories: Optional[Stories]
#     latitutde:Optional[str]
#     longitude:Optional[str]
                    
#     @model_validator(mode='after')
#     def set_minimum_price(cls, values):
#         if values.minimum_price is None:  
#             if values.category == Category.rent:
#                 values.minimum_price = 200
#             elif values.category == Category.sold:
#                 values.minimum_price = 50000
#             elif values.category == Category.sale:
#                 values.minimum_price = 50000
#         return values

#     @model_validator(mode='after')
#     def set_maximum_price(cls, values):
#         if values.maximum_price is None:  
#             if values.category == Category.rent:
#                 values.maximum_price = 5000
#             elif values.category == Category.sold:
#                 values.maximum_price = 5000000
#             elif values.category == Category.sale:
#                 values.maximum_price = 5000000
#         return values



# class Roc_Properties_Views(APIView):

#     def post(self, request, *args, **kwargs):
#         serializer = PromptSerializer(data=request.data)
#         if serializer.is_valid():

#             prompt = serializer.validated_data['prompt']
#             client = OpenAI()
            
#             completion = client.chat.completions.create(
#             model="gpt-4o-2024-08-06",
#             messages=[
#             {"role": "system", "content": "fetch the location fields from the prompt given by the user with respect to response type"},
#             {"role": "user", "content": f"{prompt}"},
#             ], 
#             tools = [
#                 {
#                     "type": "function",
#                     "function": {
#                         "name": "get_location_details",
#                         "strict": True,
#                         "description": "Get the location details for the user. if users gives the location, call this function and use this tool example 'i live in chennai'",
#                         "parameters": {
#                             "type": "object",
#                             "properties": {
#                                 "location": {
#                                     "type": "string",
#                                     "description": "User given location",
#                                 },
#                             },
#                             "required": ["location"],
#                             "additionalProperties": False,
#                         },
#                     }
#                 }],    
#             )
                
#             tool_call = completion.choices[0].message.tool_calls[0]
#             arguments = json.loads(tool_call.function.arguments)
#             location = arguments.get('location')
#             print(location)
#             location_details = self.get_location_details(location)
#             function_call_result_message = {
#                                 "role": "tool",
#                                 "content": json.dumps({
#                                     "location": location,
#                                     "location_details": location_details
#                                 }),
#                                 "tool_call_id": completion.choices[0].message.tool_calls[0].id
#                             }
#             completion_payload = {
#                 "model": "gpt-4o-2024-08-06",
#                 "messages": [
#                     {"role": "system", "content": """fill all the necessary field in the response format from the information provided by tools . fetch latitude and longitude for the given location from your knowledge base"""},
#                         {"role": "user", "content": f"{prompt}"},
#                         completion.choices[0].message,
#                         function_call_result_message
#                 ]
#                 }
            
#             response = client.beta.chat.completions.parse(
#             model=completion_payload["model"],
#             messages=completion_payload["messages"],
#             response_format=PropertyEvent,
#             )
#             event = response.choices[0].message.parsed
#             if event is not None:
#                 event_dict = event.dict()  
#                 return Response(event_dict, status=status.HTTP_200_OK)
            
#             return Response(response, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def get_location_details(self,location: str):
#         api_url = f"https://roc-staging-api.cyces.co/web/property/search/meta?search={location}"
#         response = requests.get(api_url)

#         if response.status_code == 200:
#             return response.json()  # Return the JSON response from the API
#         else:
#             return {"error": f"Failed to retrieve data for location {location}. Status code: {response.status_code}"}



#my BEST MODEL AFTER ALL THE TESTING
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import PromptSerializer
# from django.conf import settings
# from openai import OpenAI
# from typing import List, Union,Optional
# from enum import Enum
# from pydantic import BaseModel,model_validator,Field
# import requests
# import json
# import openai


# class Category(str, Enum):
#     rent = "rent"
#     sold = "sold"
#     sale = "sale"

# class Bedrooms(str, Enum):
#     any = "Any"
#     studio = "Studio"
#     one = "1"
#     two = "2"
#     three = "3"
#     four = "4"
#     five = "5+"

# class HomeType(str, Enum):
#     single_family = "Single Family"
#     condo = "Condo"
#     town_house = "Townhouse"
#     multifamily = "Multifamily"
#     land = "Land"
#     Others = "Others"
    

# class Bathrooms(str, Enum):
#     any = "Any"
#     one_plus = "1"
#     one_and_half_plus = "1.5"
#     two_plus = "2"
#     three_plus = "3"
#     four_plus = "4"

# class SquareFeet(int,Enum):
#     _750 = 750
#     _1000 = 1000
#     _1100 = 1100
#     _1200 = 1200
#     _1300 = 1300
#     _1400 = 1400
#     _1500 = 1500
#     _1600 = 1600
#     _1700 = 1700
#     _1800 = 1800
#     _1900 = 1900
#     _2000 = 2000
#     _2250 = 2250
#     _2500 = 2500
#     _2750 = 2750
#     _3000 = 3000
#     _4000 = 4000
#     _5000 = 5000
#     _7500 = 7500
#     _10000 = 10000

# class LotSize(str,Enum):
#     _2000_SQFT = "2000 sqft"
#     _4500_SQFT = "4500 sqft"
#     _6500_SQFT = "6500 sqft"
#     _8000_SQFT = "8000 sqft"
#     _9500_SQFT = "9500 sqft"
#     _1_ACRE = "1 acres"
#     _0_5_ACRE = ".5 acres"
#     _0_25_ACRE = ".25 acres"
#     _2_ACRE = "2 acres"
#     _3_ACRE = "3 acres"
#     _4_ACRE = "4 acres"
#     _5_ACRE = "5 acres"
#     _10_ACRE = "10 acres"
#     _20_ACRE = "20 acres"
#     _40_ACRE = "40 acres"
#     _100_ACRE = "100 acres"

# class Stories(int,Enum):
#     ONE = 1
#     TWO = 2
#     THREE = 3
#     FOUR = 4
#     FIVE = 5
#     TEN = 10
#     FIFTEEN = 15
#     TWENTY = 20

# class YearBuilt(int, Enum):
#     YEAR_1920 = 1920
#     YEAR_1940 = 1940
#     YEAR_1960 = 1960
#     YEAR_1980 = 1980
#     YEAR_1990 = 1990
#     YEAR_2000 = 2000
#     YEAR_2005 = 2005
#     YEAR_2010 = 2010
#     YEAR_2014 = 2014
#     YEAR_2015 = 2015
#     YEAR_2016 = 2016
#     YEAR_2017 = 2017
#     YEAR_2018 = 2018
#     YEAR_2019 = 2019
#     YEAR_2020 = 2020
#     YEAR_2021 = 2021
#     YEAR_2022 = 2022
#     YEAR_2023 = 2023
#     YEAR_2024 = 2024


# class Type(str, Enum):
#     neighbourhood = "neighbourhood"
#     city = "city"

# # class PropertyEvent(BaseModel):
# #     location: Optional[str]
# #     type: Optional[Type]
# #     polygon_id: Optional[str]
# #     state_code: str
# #     state:str
# #     category: Category
# #     minimum_price: Optional[int]
# #     maximum_price: Optional[int]
# #     bedrooms: Bedrooms
# #     bathrooms:Bathrooms
# #     home_type:list[HomeType]
# #     minimum_square_feet:Optional[SquareFeet]
# #     maximum_square_feet: Optional[SquareFeet]
# #     minimum_lot_size: Optional[LotSize]
# #     maximum_lot_size: Optional[LotSize]
# #     minimum_year_built: Optional[YearBuilt]
# #     maximum_year_built: Optional[YearBuilt]
# #     minimum_stories: Optional[Stories]
# #     maximum_stories: Optional[Stories]
# #     latitude:str
# #     longitude:str

# class PropertyEvent(BaseModel):
#     location: Optional[str]
#     type: Optional[Type]
#     polygon_id: Optional[str]
#     state_code: Optional[str]
#     state:Optional[str]
#     category: Category
#     minimum_price: Optional[int]
#     maximum_price: Optional[int]
#     bedrooms: Optional[Bedrooms]
#     bathrooms:Optional[Bathrooms]
#     home_type:Optional[list[HomeType]]
#     minimum_square_feet:Optional[SquareFeet]
#     maximum_square_feet: Optional[SquareFeet]
#     minimum_lot_size: Optional[LotSize]
#     maximum_lot_size: Optional[LotSize]
#     minimum_year_built: Optional[YearBuilt]
#     maximum_year_built: Optional[YearBuilt]
#     minimum_stories: Optional[Stories]
#     maximum_stories: Optional[Stories]
#     latitude:Optional[str]
#     longitude:Optional[str]
                    
#     # @model_validator(mode='after')
#     # def set_minimum_price(cls, values):
#     #     if values.minimum_price is None:  
#     #         if values.category == Category.rent:
#     #             values.minimum_price = 200
#     #         elif values.category == Category.sold:
#     #             values.minimum_price = 50000
#     #         elif values.category == Category.sale:
#     #             values.minimum_price = 50000
#     #     return values

#     # @model_validator(mode='after')
#     # def set_maximum_price(cls, values):
#     #     if values.maximum_price is None:  
#     #         if values.category == Category.rent:
#     #             values.maximum_price = 5000
#     #         elif values.category == Category.sold:
#     #             values.maximum_price = 5000000
#     #         elif values.category == Category.sale:
#     #             values.maximum_price = 5000000
#     #     return values


# class Roc_Properties_Views(APIView):

#     def post(self, request, *args, **kwargs):
#         serializer = PromptSerializer(data=request.data)
#         if serializer.is_valid():

#             prompt = serializer.validated_data['prompt']
#             client = OpenAI()
            
#             completion = client.chat.completions.create(
#             model="gpt-4o-2024-08-06",
#             messages=[
#             {"role": "system", "content": "fetch the location fields from the prompt given by the user with respect to response type"},
#             # {"role": "system", "content": "Check wether the context is related to the property"},           
#             {"role": "user", "content": f"{prompt}"},
#             ], 
#             tools = [
#                 {
#                     "type": "function",
#                     "function": {
#                         "name": "get_location_details",
#                         "strict": True,
#                         "description": "Get the location details for the user. if users gives the location, call this function and use this tool example 'i live in chennai'",
#                         "parameters": {
#                             "type": "object",
#                             "properties": {
#                                 "location": {
#                                     "type": "string",
#                                     "description": "User given location",
#                                 },
#                             },
#                             "required": ["location"],
#                             "additionalProperties": False,
#                         },
#                     }
#                 }],    
#             )
          
#             completion_payload = {
#                 "model": "gpt-4o-2024-08-06",
#                 "messages": [
#                     {"role": "system", "content": """
#                     fill all the necessary field in the response format from the information provided by tools . fetch latitude and longitude for the given location from your knowledge base
#                     if information is not subject to property set null for all values
#                     answer only to context
#                      """},
#                         {"role": "user", "content": f"{prompt}"},
#                 ]

#                 }
            
#             if (completion.choices[0].finish_reason == "tool_calls" ):
#                 tool_call = completion.choices[0].message.tool_calls[0]
#                 arguments = json.loads(tool_call.function.arguments)
#                 location = arguments.get('location')
#                 print(location)
#                 location_details = self.get_location_details(location)
#                 function_call_result_message = {
#                                     "role": "tool",
#                                     "content": json.dumps({
#                                         "location": location,
#                                         "location_details": location_details
#                                     }),
#                                     "tool_call_id": completion.choices[0].message.tool_calls[0].id
#                                 }
#                 completion_payload['messages'].append(completion.choices[0].message)
#                 completion_payload['messages'].append(function_call_result_message)
            
#             response = client.beta.chat.completions.parse(
#             model=completion_payload["model"],
#             messages=completion_payload["messages"],
#             response_format=PropertyEvent,
#             )
#             event = response.choices[0].message.parsed
#             if event is not None:
#                 event_dict = event.dict()  
#                 return Response(event_dict, status=status.HTTP_200_OK)

            
#             return Response(response, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def get_location_details(self,location: str):
#         api_url = f"https://roc-staging-api.cyces.co/web/property/search/meta?search={location}"
#         response = requests.get(api_url)

#         if response.status_code == 200:
#             return response.json()  # Return the JSON response from the API
#         else:
#             return {"error": f"Failed to retrieve data for location {location}. Status code: {response.status_code}"}

