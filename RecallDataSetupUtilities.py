import pandas as pd
import re

#https://apps.tga.gov.au/Prod/sara/arn-report.aspx



'''
Function that is passed the appropriate product recall data and the specified country.
Function loops through the data and creates a table consisting of the number of remedy
instances for that specified country: i.e. (Refund, Recall, New Instructions, etc.)
Returned Table is used for visualization purposes and can be used for others as well.
'''


def createRecallRemedyCountryData(data, specific_country):
    remedy_count = [["REMEDY", "COUNT"]]
    country_data = data.loc[data['Manufactured In'] == specific_country]
    if country_data.size == 0: return
    for remedy in country_data['Remedy Type']:
        if pd.isna(remedy):
            continue
        if len(remedy.split(", ")) > 1:
            for split_remedy in remedy.split(", "):
                current_remedy_list = list(zip(*remedy_count))
                if split_remedy in current_remedy_list[0]:
                    occurence_index = current_remedy_list[0].index(split_remedy)
                    remedy_count[occurence_index][1] = (remedy_count[occurence_index][1] + 1)
        else:
            current_remedy_list = list(zip(*remedy_count))
            if remedy in current_remedy_list[0]:
                continue
            else:
                count = country_data['Remedy Type'].tolist().count(remedy)
                remedy_count.append([remedy, count])

    return remedy_count


'''
Function that is passed the appropriate product recall data and no other arguments available.
Function loops through the data and generates the number of occurrences for that countries instances i.e
how many occurrences the U.S.A or California has in the data-set. 
Returns a Table used for visualization purposed and can be used for other analysis as well. 
'''


def createOccurrencesCountries(data):
    country_calculations = [["COUNTRY", "COUNT"]]
    for countries in data['Manufactured In']:
        if pd.isna(countries):
            continue
        split_country = countries.split()
        if len(split_country) > 1:
            for countries_split in split_country:
                current_country_list = list(zip(*country_calculations))
                if countries_split in current_country_list[0]:
                    occurence_index = current_country_list[0].index(countries_split)
                    country_calculations[occurence_index][1] = (country_calculations[occurence_index][1] + 1)
                else:
                    continue
        else:
            current_country_list = list(zip(*country_calculations))
            if countries in current_country_list[0]:
                continue
            else:
                count = data['Manufactured In'].tolist().count(countries)
                country_calculations.append([countries, count])

    return country_calculations


def create_recall_action_breakdown_AUS(data):
    recall_type_breakdown = []
    for recall_type in data["Recall Action"]:
        if pd.isna(recall_type):
            continue
        count = data["Recall Action"].tolist().count(recall_type)
        recall_type_breakdown.append([recall_type, count])
    return pd.DataFrame(recall_type_breakdown, columns=['Recall Type', 'Count']).drop_duplicates()


def create_recall_action_level_breakdown_AUS(data):
    recall_type_level_breakdown = []
    for recall_type in data["Recall Action Level"]:
        if pd.isna(recall_type):
            continue
        count = data["Recall Action Level"].tolist().count(recall_type)
        recall_type_level_breakdown.append([recall_type, count])
    return pd.DataFrame(recall_type_level_breakdown, columns=['Recall Level Type', 'Count']).drop_duplicates()


def create_recall_product_type_breakdown_AUS(data):
    recall_product_type_level_breakdown = []
    for recall_type in data["Type of Product"]:
        if pd.isna(recall_type):
            continue
        count = data["Type of Product"].tolist().count(recall_type)
        recall_product_type_level_breakdown.append([recall_type, count])
    return pd.DataFrame(recall_product_type_level_breakdown, columns=['Type of Product', 'Count']).drop_duplicates()
