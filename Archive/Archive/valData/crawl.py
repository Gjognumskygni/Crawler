from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
import json
import time

""" løgtingsval 2002 """
def Crawl2002():
    dataList = []
    yearList = []
    voteList = []
    partiesList = []
    paths = ["Valúrslit/2002/Argir_files/index.html",
    "Valúrslit/2002/Árnafjørður_files/index.html",
    "Valúrslit/2002/Bøur_files/index.html",
    "Valúrslit/2002/Dalur_files/index.html",
    "Valúrslit/2002/Eiði_files/index.html",
    "Valúrslit/2002/Elduvík_files/index.html",
    "Valúrslit/2002/Fámjin_files/index.html",
    "Valúrslit/2002/Fossanes_files/index.html",
    "Valúrslit/2002/Fuglafjørður_files/index.html",
    "Valúrslit/2002/Funningsfjørður_files/index.html",
    "Valúrslit/2002/Funningur_files/index.html",
    "Valúrslit/2002/Gásadalur_files/index.html",
    "Valúrslit/2002/Gjógv_files/index.html",
    "Valúrslit/2002/Gøta_files/index.html",
    "Valúrslit/2002/Haldórsvík_files/index.html",
    "Valúrslit/2002/Haraldssund_files/index.html",
    "Valúrslit/2002/Hattarvík_files/index.html",
    "Valúrslit/2002/Hellurnar_files/index.html",
    "Valúrslit/2002/Hestur_files/index.html",
    "Valúrslit/2002/Hósvík_files/index.html",
    "Valúrslit/2002/Hov_files/index.html",
    "Valúrslit/2002/Húsar_files/index.html",
    "Valúrslit/2002/Húsavík_files/index.html",
    "Valúrslit/2002/Hvalba_files/index.html",
    "Valúrslit/2002/Hvalvík_files/index.html",
    "Valúrslit/2002/Kaldbak_files/index.html",
    "Valúrslit/2002/Kirkja_files/index.html",
    "Valúrslit/2002/Klaksvík_files/index.html",
    "Valúrslit/2002/Kollafjørður_files/index.html",
    "Valúrslit/2002/Kunoy_files/index.html",
    "Valúrslit/2002/Kvívík_files/index.html",
    "Valúrslit/2002/Leirvík_files/index.html",
    "Valúrslit/2002/Lopra_files/index.html",
    "Valúrslit/2002/Miðvágur_files/index.html",
    "Valúrslit/2002/Mikladalur_files/index.html",
    "Valúrslit/2002/Mykines_files/index.html",
    "Valúrslit/2002/Nólsoy_files/index.html",
    "Valúrslit/2002/Norðradalur_files/index.html",
    "Valúrslit/2002/Oyndarfjørður_files/index.html",
    "Valúrslit/2002/Oyrarbakki_files/index.html",
    "Valúrslit/2002/Porkeri_files/index.html",
    "Valúrslit/2002/Runavík_files/index.html",
    "Valúrslit/2002/Saksun_files/index.html",
    "Valúrslit/2002/Sandavágur_files/index.html",
    "Valúrslit/2002/Sandur_files/index.html",
    "Valúrslit/2002/Sandvík_files/index.html",
    "Valúrslit/2002/Selatrað_files/index.html",
    "Valúrslit/2002/Skálafjørður_files/index.html",
    "Valúrslit/2002/Skálavík_files/index.html",
    "Valúrslit/2002/Skopun_files/index.html",
    "Valúrslit/2002/Skúvoy_files/index.html",
    "Valúrslit/2002/Sørvágur_files/index.html",
    "Valúrslit/2002/Strendur_files/index.html",
    "Valúrslit/2002/Sumba_files/index.html",
    "Valúrslit/2002/Svínoy_files/index.html",
    "Valúrslit/2002/Syðradalur K_files/index.html",
    "Valúrslit/2002/Tjørnuvík_files/index.html",
    "Valúrslit/2002/Toftir_files/index.html",
    "Valúrslit/2002/Tórshavn_files/index.html",
    "Valúrslit/2002/Tvøroyri_files/index.html",
    "Valúrslit/2002/Vágur_files/index.html",
    "Valúrslit/2002/Velbastaður_files/index.html",
    "Valúrslit/2002/Vestmanna_files/index.html",
    "Valúrslit/2002/Viðareiði_files/index.html",]

    for path in paths:
        with open(path) as fp:
            soup = BeautifulSoup(fp, 'html.parser')
            partiesList = []

            votePlace = (((soup.find('pre')).get_text()).split("\n"))[1]
            print(votePlace)
            
            totalvotes = soup.find('td', {'class': "FlkAtkvTils"}).get_text()

            registerdVoters = soup.find('td', {'class': "FlkValraett"}).get_text()

            date = (soup.find('div', style="text-align:center")).find('div').get_text()
            
            party0 = soup.find('table',{'class': "Listi0"})
            partyName = party0.find('td', {'class': "ListiFlokkurNavn"}).get_text()
            voteList0 = []
            voteList0.append({'Name': party0.find('td', {'class': "ListiListi"}).get_text(), 'Vote': party0.find('td', {'class': "ListiListaAtkv"}).get_text()})
            for person in party0.find_all('tr')[1:]:
                name = person.find('td', {'class': "ListiValevniNavn"})
                vote = person.find('td', {'class': "ListiValevniAtkv"})
                if(name != None and vote != None):
                    voteList0.append({'Name': name.get_text(), 'Vote': vote.get_text()})
            partiesList.append({'PartyName': partyName, 'PartyVotes': voteList0})

            party1 = soup.find('table',{'class': "Listi1"})
            partyName = party1.find('td', {'class': "ListiFlokkurNavn"}).get_text()
            voteList1 = []
            voteList1.append({'Name': party1.find('td', {'class': "ListiListi"}).get_text(), 'Vote': party1.find('td', {'class': "ListiListaAtkv"}).get_text()})
            for person in party1.find_all('tr')[1:]:
                name = person.find('td', {'class': "ListiValevniNavn"})
                vote = person.find('td', {'class': "ListiValevniAtkv"})
                if(name != None and vote != None):
                    voteList1.append({'Name': name.get_text(), 'Vote': vote.get_text()})
            partiesList.append({'PartyName': partyName, 'PartyVotes': voteList1})

            party2 = soup.find('table',{'class': "Listi2"})
            partyName = party2.find('td', {'class': "ListiFlokkurNavn"}).get_text()
            voteList2 = []
            voteList2.append({'Name': party2.find('td', {'class': "ListiListi"}).get_text(), 'Vote': party2.find('td', {'class': "ListiListaAtkv"}).get_text()})
            for person in party2.find_all('tr')[1:]:
                name = person.find('td', {'class': "ListiValevniNavn"})
                vote = person.find('td', {'class': "ListiValevniAtkv"})
                if(name != None and vote != None):
                    voteList2.append({'Name': name.get_text(), 'Vote': vote.get_text()})
            partiesList.append({'PartyName': partyName, 'PartyVotes': voteList2})

            party3 = soup.find('table',{'class': "Listi3"})
            partyName = party3.find('td', {'class': "ListiFlokkurNavn"}).get_text()
            voteList3 = []
            voteList3.append({'Name': party3.find('td', {'class': "ListiListi"}).get_text(), 'Vote': party3.find('td', {'class': "ListiListaAtkv"}).get_text()})
            for person in party3.find_all('tr')[1:]:
                name = person.find('td', {'class': "ListiValevniNavn"})
                vote = person.find('td', {'class': "ListiValevniAtkv"})
                if(name != None and vote != None):
                    voteList3.append({'Name': name.get_text(), 'Vote': vote.get_text()})
            partiesList.append({'PartyName': partyName, 'PartyVotes': voteList3})
            
            party4 = soup.find('table',{'class': "Listi4"})
            partyName = party4.find('td', {'class': "ListiFlokkurNavn"}).get_text()
            voteList4 = []
            voteList4.append({'Name': party4.find('td', {'class': "ListiListi"}).get_text(), 'Vote': party4.find('td', {'class': "ListiListaAtkv"}).get_text()})
            for person in party4.find_all('tr')[1:]:
                name = person.find('td', {'class': "ListiValevniNavn"})
                vote = person.find('td', {'class': "ListiValevniAtkv"})
                if(name != None and vote != None):
                    voteList4.append({'Name': name.get_text(), 'Vote': vote.get_text()})
            partiesList.append({'PartyName': partyName, 'PartyVotes': voteList4})

            party5 = soup.find('table',{'class': "Listi5"})
            if(party5 != None):
                partyName = party5.find('td', {'class': "ListiFlokkurNavn"}).get_text()
                voteList5 = []
                voteList5.append({'Name': party5.find('td', {'class': "ListiListi"}).get_text(), 'Vote': party5.find('td', {'class': "ListiListaAtkv"}).get_text()})
                for person in party5.find_all('tr')[1:]:
                    name = person.find('td', {'class': "ListiValevniNavn"})
                    vote = person.find('td', {'class': "ListiValevniAtkv"})
                    if(name != None and vote != None):
                        voteList5.append({'Name': name.get_text(), 'Vote': vote.get_text()})
                partiesList.append({'PartyName': partyName, 'PartyVotes': voteList5})

            yearList.append({'VotePlace': votePlace, 'Date': date, 'Totalvotes': totalvotes, 'RegisterdVoters': registerdVoters, 'PartiesList': partiesList})
        fp.close()
    dataList.append({'Year': '2002', 'YearList': yearList})
    with open('valData2002.json', 'w', encoding='utf-8') as f:
        json.dump(dataList, f, ensure_ascii=False, indent=4)

""" løgtingsval 2004 """
def Crawl2004():
    dataList = []
    yearList = []
    voteList = []
    partiesList = []
    paths = ["Valúrslit/2004/Argir_files/index.html",
    "Valúrslit/2004/Árnafjørður_files/index.html",
    "Valúrslit/2004/Bøur_files/index.html",
    "Valúrslit/2004/Dalur_files/index.html",
    "Valúrslit/2004/Eiði_files/index.html",
    "Valúrslit/2004/Elduvík_files/index.html",
    "Valúrslit/2004/Fámjin_files/index.html",
    "Valúrslit/2004/Fossanes_files/index.html",
    "Valúrslit/2004/Fuglafjørður_files/index.html",
    "Valúrslit/2004/Funningsfjørður_files/index.html",
    "Valúrslit/2004/Funningur_files/index.html",
    "Valúrslit/2004/Gásadalur_files/index.html",
    "Valúrslit/2004/Gjógv_files/index.html",
    "Valúrslit/2004/Gøta_files/index.html",
    "Valúrslit/2004/Haldórsvík_files/index.html",
    "Valúrslit/2004/Haraldssund_files/index.html",
    "Valúrslit/2004/Hattarvík_files/index.html",
    "Valúrslit/2004/Hellurnar_files/index.html",
    "Valúrslit/2004/Hestur_files/index.html",
    "Valúrslit/2004/Hósvík_files/index.html",
    "Valúrslit/2004/Hov_files/index.html",
    "Valúrslit/2004/Húsar_files/index.html",
    "Valúrslit/2004/Húsavík_files/index.html",
    "Valúrslit/2004/Hvalba_files/index.html",
    "Valúrslit/2004/Hvalvík_files/index.html",
    "Valúrslit/2004/Kaldbak_files/index.html",
    "Valúrslit/2004/Kirkja_files/index.html",
    "Valúrslit/2004/Klaksvík_files/index.html",
    "Valúrslit/2004/Kollafjørður_files/index.html",
    "Valúrslit/2004/Kunoy_files/index.html",
    "Valúrslit/2004/Kvívík_files/index.html",
    "Valúrslit/2004/Leirvík_files/index.html",
    "Valúrslit/2004/Lopra_files/index.html",
    "Valúrslit/2004/Miðvágur_files/index.html",
    "Valúrslit/2004/Mikladalur_files/index.html",
    "Valúrslit/2004/Mykines_files/index.html",
    "Valúrslit/2004/Nólsoy_files/index.html",
    "Valúrslit/2004/Norðradalur_files/index.html",
    "Valúrslit/2004/Oyndarfjørður_files/index.html",
    "Valúrslit/2004/Oyrarbakki_files/index.html",
    "Valúrslit/2004/Porkeri_files/index.html",
    "Valúrslit/2004/Runavík_files/index.html",
    "Valúrslit/2004/Saksun_files/index.html",
    "Valúrslit/2004/Sandavágur_files/index.html",
    "Valúrslit/2004/Sandur_files/index.html",
    "Valúrslit/2004/Sandvík_files/index.html",
    "Valúrslit/2004/Selatrað_files/index.html",
    "Valúrslit/2004/Skálafjørður_files/index.html",
    "Valúrslit/2004/Skálavík_files/index.html",
    "Valúrslit/2004/Skopun_files/index.html",
    "Valúrslit/2004/Skúvoy_files/index.html",
    "Valúrslit/2004/Sørvágur_files/index.html",
    "Valúrslit/2004/Strendur_files/index.html",
    "Valúrslit/2004/Sumba_files/index.html",
    "Valúrslit/2004/Svínoy_files/index.html",
    "Valúrslit/2004/Syðradalur K_files/index.html",
    "Valúrslit/2004/Tjørnuvík_files/index.html",
    "Valúrslit/2004/Toftir_files/index.html",
    "Valúrslit/2004/Tórshavn_files/index.html",
    "Valúrslit/2004/Tvøroyri_files/index.html",
    "Valúrslit/2004/Vágur_files/index.html",
    "Valúrslit/2004/Velbastaður_files/index.html",
    "Valúrslit/2004/Vestmanna_files/index.html",
    "Valúrslit/2004/Viðareiði_files/index.html",]

    for path in paths:
        with open(path) as fp:
            soup = BeautifulSoup(fp, 'html.parser')
            partiesList = []

            votePlace = (((soup.find('pre')).get_text()).split("\n"))[1]
            print(votePlace)
            
            totalvotes = soup.find('td', {'class': "FlkAtkvTils"}).get_text()

            registerdVoters = soup.find('td', {'class': "FlkValraett"}).get_text()

            date = (soup.find('div', style="text-align:center")).find('div').get_text()
            
            party0 = soup.find('table',{'class': "Listi0"})
            partyName = party0.find('td', {'class': "ListiFlokkurNavn"}).get_text()
            voteList0 = []
            voteList0.append({'Name': party0.find('td', {'class': "ListiListi"}).get_text(), 'Vote': party0.find('td', {'class': "ListiListaAtkv"}).get_text()})
            for person in party0.find_all('tr')[1:]:
                name = person.find('td', {'class': "ListiValevniNavn"})
                vote = person.find('td', {'class': "ListiValevniAtkv"})
                if(name != None and vote != None):
                    voteList0.append({'Name': name.get_text(), 'Vote': vote.get_text()})
            partiesList.append({'PartyName': partyName, 'PartyVotes': voteList0})

            party1 = soup.find('table',{'class': "Listi1"})
            partyName = party1.find('td', {'class': "ListiFlokkurNavn"}).get_text()
            voteList1 = []
            voteList1.append({'Name': party1.find('td', {'class': "ListiListi"}).get_text(), 'Vote': party1.find('td', {'class': "ListiListaAtkv"}).get_text()})
            for person in party1.find_all('tr')[1:]:
                name = person.find('td', {'class': "ListiValevniNavn"})
                vote = person.find('td', {'class': "ListiValevniAtkv"})
                if(name != None and vote != None):
                    voteList1.append({'Name': name.get_text(), 'Vote': vote.get_text()})
            partiesList.append({'PartyName': partyName, 'PartyVotes': voteList1})

            party2 = soup.find('table',{'class': "Listi2"})
            partyName = party2.find('td', {'class': "ListiFlokkurNavn"}).get_text()
            voteList2 = []
            voteList2.append({'Name': party2.find('td', {'class': "ListiListi"}).get_text(), 'Vote': party2.find('td', {'class': "ListiListaAtkv"}).get_text()})
            for person in party2.find_all('tr')[1:]:
                name = person.find('td', {'class': "ListiValevniNavn"})
                vote = person.find('td', {'class': "ListiValevniAtkv"})
                if(name != None and vote != None):
                    voteList2.append({'Name': name.get_text(), 'Vote': vote.get_text()})
            partiesList.append({'PartyName': partyName, 'PartyVotes': voteList2})

            party3 = soup.find('table',{'class': "Listi3"})
            partyName = party3.find('td', {'class': "ListiFlokkurNavn"}).get_text()
            voteList3 = []
            voteList3.append({'Name': party3.find('td', {'class': "ListiListi"}).get_text(), 'Vote': party3.find('td', {'class': "ListiListaAtkv"}).get_text()})
            for person in party3.find_all('tr')[1:]:
                name = person.find('td', {'class': "ListiValevniNavn"})
                vote = person.find('td', {'class': "ListiValevniAtkv"})
                if(name != None and vote != None):
                    voteList3.append({'Name': name.get_text(), 'Vote': vote.get_text()})
            partiesList.append({'PartyName': partyName, 'PartyVotes': voteList3})
            
            party4 = soup.find('table',{'class': "Listi4"})
            partyName = party4.find('td', {'class': "ListiFlokkurNavn"}).get_text()
            voteList4 = []
            voteList4.append({'Name': party4.find('td', {'class': "ListiListi"}).get_text(), 'Vote': party4.find('td', {'class': "ListiListaAtkv"}).get_text()})
            for person in party4.find_all('tr')[1:]:
                name = person.find('td', {'class': "ListiValevniNavn"})
                vote = person.find('td', {'class': "ListiValevniAtkv"})
                if(name != None and vote != None):
                    voteList4.append({'Name': name.get_text(), 'Vote': vote.get_text()})
            partiesList.append({'PartyName': partyName, 'PartyVotes': voteList4})

            party5 = soup.find('table',{'class': "Listi5"})
            partyName = party5.find('td', {'class': "ListiFlokkurNavn"}).get_text()
            voteList5 = []
            voteList5.append({'Name': party5.find('td', {'class': "ListiListi"}).get_text(), 'Vote': party5.find('td', {'class': "ListiListaAtkv"}).get_text()})
            for person in party5.find_all('tr')[1:]:
                name = person.find('td', {'class': "ListiValevniNavn"})
                vote = person.find('td', {'class': "ListiValevniAtkv"})
                if(name != None and vote != None):
                    voteList5.append({'Name': name.get_text(), 'Vote': vote.get_text()})
            partiesList.append({'PartyName': partyName, 'PartyVotes': voteList5})

            party6 = soup.find('table',{'class': "Listi6"})
            if(party6 != None):
                partyName = party6.find('td', {'class': "ListiFlokkurNavn"}).get_text()
                voteList6 = []
                voteList6.append({'Name': party6.find('td', {'class': "ListiListi"}).get_text(), 'Vote': party6.find('td', {'class': "ListiListaAtkv"}).get_text()})
                for person in party6.find_all('tr')[1:]:
                    name = person.find('td', {'class': "ListiValevniNavn"})
                    vote = person.find('td', {'class': "ListiValevniAtkv"})
                    if(name != None and vote != None):
                        voteList6.append({'Name': name.get_text(), 'Vote': vote.get_text()})
                partiesList.append({'PartyName': partyName, 'PartyVotes': voteList6})

            yearList.append({'VotePlace': votePlace, 'Date': date, 'Totalvotes': totalvotes, 'RegisterdVoters': registerdVoters, 'PartiesList': partiesList})
        fp.close()
    dataList.append({'Year': '2004', 'YearList': yearList})
    with open('valData2004.json', 'w', encoding='utf-8') as f:
        json.dump(dataList, f, ensure_ascii=False, indent=4)

""" løgtingsval 2008 """
def Crawl2008():
    dataList = []
    yearList = []
    voteList = []
    partiesList = []
    paths = ["Valúrslit/2008/Argir_files/index.html",
    "Valúrslit/2008/Árnafjørður_files/index.html",
    "Valúrslit/2008/Bøur_files/index.html",
    "Valúrslit/2008/Dalur_files/index.html",
    "Valúrslit/2008/Eiði_files/index.html",
    "Valúrslit/2008/Elduvík _files/index.html",
    "Valúrslit/2008/Fámjin_files/index.html",
    "Valúrslit/2008/Fossanes_files/index.html",
    "Valúrslit/2008/Fuglafjørður_files/index.html",
    "Valúrslit/2008/Funningsfjørður _files/index.html",
    "Valúrslit/2008/Funningur_files/index.html",
    "Valúrslit/2008/Gásadalur_files/index.html",
    "Valúrslit/2008/Gjógv _files/index.html",
    "Valúrslit/2008/Gøta_files/index.html",
    "Valúrslit/2008/Haldórsvík_files/index.html",
    "Valúrslit/2008/Haraldssund_files/index.html",
    "Valúrslit/2008/Hattarvík_files/index.html",
    "Valúrslit/2008/Hellurnar_files/index.html",
    "Valúrslit/2008/Hestur_files/index.html",
    "Valúrslit/2008/Hósvík_files/index.html",
    "Valúrslit/2008/Hov_files/index.html",
    "Valúrslit/2008/Húsar _files/index.html",
    "Valúrslit/2008/Húsavík _files/index.html",
    "Valúrslit/2008/Hvalba_files/index.html",
    "Valúrslit/2008/Hvalvík_files/index.html",
    "Valúrslit/2008/Kaldbak_files/index.html",
    "Valúrslit/2008/Kirkja_files/index.html",
    "Valúrslit/2008/Klaksvík_files/index.html",
    "Valúrslit/2008/Kollafjørður_files/index.html",
    "Valúrslit/2008/Kunoy_files/index.html",
    "Valúrslit/2008/Kvívík_files/index.html",
    "Valúrslit/2008/Leirvík_files/index.html",
    "Valúrslit/2008/Lopra_files/index.html",
    "Valúrslit/2008/Miðvágur_files/index.html",
    "Valúrslit/2008/Mikladalur_files/index.html",
    "Valúrslit/2008/Mykines_files/index.html",
    "Valúrslit/2008/Nólsoy_files/index.html",
    "Valúrslit/2008/Oyndarfjørður_files/index.html",
    "Valúrslit/2008/Oyrarbakki_files/index.html",
    "Valúrslit/2008/Porkeri_files/index.html",
    "Valúrslit/2008/Runavík_files/index.html",
    "Valúrslit/2008/Sandavágur_files/index.html",
    "Valúrslit/2008/Sandur_files/index.html",
    "Valúrslit/2008/Sandvík_files/index.html",
    "Valúrslit/2008/Selatrað_files/index.html",
    "Valúrslit/2008/Skálafjørður_files/index.html",
    "Valúrslit/2008/Skálavík_files/index.html",
    "Valúrslit/2008/Skáli_files/index.html",
    "Valúrslit/2008/Skopun_files/index.html",
    "Valúrslit/2008/Skúvoy_files/index.html",
    "Valúrslit/2008/Sørvágur_files/index.html",
    "Valúrslit/2008/Strendur_files/index.html",
    "Valúrslit/2008/Sumba_files/index.html",
    "Valúrslit/2008/Svínoy_files/index.html",
    "Valúrslit/2008/Tjørnuvík_files/index.html",
    "Valúrslit/2008/Toftir_files/index.html",
    "Valúrslit/2008/Tórshavn_files/index.html",
    "Valúrslit/2008/Tvøroyri_files/index.html",
    "Valúrslit/2008/Vágur_files/index.html",
    "Valúrslit/2008/Velbastaður_files/index.html",
    "Valúrslit/2008/Vestmanna_files/index.html",
    "Valúrslit/2008/Viðareiði_files/index.html",]

    for path in paths:
        with open(path) as fp:
            soup = BeautifulSoup(fp, 'html.parser')
            partiesList = []

            votePlace = soup.find_all('td', {"class":"Headline"})
            votePlace = votePlace[2].get_text()

            voteInfo = soup.find('table', {'class': "RammaAlt", 'style': "width:100%"})
            tr = voteInfo.find_all('tr')
            
            totalvotesTd = tr[8].find_all('td')
            totalvotes = totalvotesTd[1].get_text()

            registerdVotersTd = tr[9].find_all('td')
            registerdVoters = registerdVotersTd[1].get_text()

            date = (soup.find('td', {"class":"Headline", "style": "text-align:center"})).get_text()
            
            for party in (soup.find_all('td', style="width:48%"))[:-1]:
                voteList = []
                partyName = party.find('td', {'class': "RammaBottom", 'style': "width:60%;background-color:#CCCCCC"}).get_text()
                for person in (party.find_all('tr'))[1:]:
                    personInfo = person.find_all('td')
                    name = (personInfo[1]).get_text()
                    vote = (personInfo[2]).get_text()
                    voteList.append({'Name': name, 'Vote': vote})
                partiesList.append({'PartyName': partyName, 'PartyVotes': voteList})
            yearList.append({'VotePlace': votePlace, 'Date': date, 'Totalvotes': totalvotes, 'RegisterdVoters': registerdVoters, 'PartiesList': partiesList})
        fp.close()
    dataList.append({'Year': '2008', 'YearList': yearList})
    with open('valData2008.json', 'w', encoding='utf-8') as f:
        json.dump(dataList, f, ensure_ascii=False, indent=4)

""" løgtingsval 2011 """
def Crawl2011():
    dataList = []
    yearList = []
    voteList = []
    partiesList = []
    paths = ["Valúrslit/2011/Argir_files/index.html",
    "Valúrslit/2011/Árnafjørður_files/index.html",
    "Valúrslit/2011/Bøur_files/index.html",
    "Valúrslit/2011/Dalur_files/index.html",
    "Valúrslit/2011/Eiði_files/index.html",
    "Valúrslit/2011/Elduvík_files/index.html",
    "Valúrslit/2011/Fámjin_files/index.html",
    "Valúrslit/2011/Fossanes_files/index.html",
    "Valúrslit/2011/Fuglafjørður_files/index.html",
    "Valúrslit/2011/Funningsfjørður_files/index.html",
    "Valúrslit/2011/Funningur_files/index.html",
    "Valúrslit/2011/Gásadalur_files/index.html",
    "Valúrslit/2011/Giljanes_files/index.html",
    "Valúrslit/2011/Gjógv_files/index.html",
    "Valúrslit/2011/Gøtugjógv_files/index.html",
    "Valúrslit/2011/Haldarsvík_files/index.html",
    "Valúrslit/2011/Haraldssund_files/index.html",
    "Valúrslit/2011/Hattarvík_files/index.html",
    "Valúrslit/2011/Hellur_files/index.html",
    "Valúrslit/2011/Hestur_files/index.html",
    "Valúrslit/2011/Hósvík_files/index.html",
    "Valúrslit/2011/Hov_files/index.html",
    "Valúrslit/2011/Húsar_files/index.html",
    "Valúrslit/2011/Húsavík_files/index.html",
    "Valúrslit/2011/Hvalba_files/index.html",
    "Valúrslit/2011/Hvalvík_files/index.html",
    "Valúrslit/2011/Kaldbak_files/index.html",
    "Valúrslit/2011/Kirkja_files/index.html",
    "Valúrslit/2011/Klaksvík_files/index.html",
    "Valúrslit/2011/Kollafjørður_files/index.html",
    "Valúrslit/2011/Kunoy_files/index.html",
    "Valúrslit/2011/Kvívík_files/index.html",
    "Valúrslit/2011/Leirvík_files/index.html",
    "Valúrslit/2011/Lopra_files/index.html",
    "Valúrslit/2011/Mikladalur_files/index.html",
    "Valúrslit/2011/Mykines_files/index.html",
    "Valúrslit/2011/Nólsoy_files/index.html",
    "Valúrslit/2011/Oyndarfjørður_files/index.html",
    "Valúrslit/2011/Oyrabakki_files/index.html",
    "Valúrslit/2011/Porkeri_files/index.html",
    "Valúrslit/2011/Rúnavík_files/index.html",
    "Valúrslit/2011/Sandur_files/index.html",
    "Valúrslit/2011/Sandvík_files/index.html",
    "Valúrslit/2011/Skálabotnur_files/index.html",
    "Valúrslit/2011/Skálavík_files/index.html",
    "Valúrslit/2011/Skáli_files/index.html",
    "Valúrslit/2011/Skopun_files/index.html",
    "Valúrslit/2011/Skúvoy_files/index.html",
    "Valúrslit/2011/Sørvágur_files/index.html",
    "Valúrslit/2011/Strendur_files/index.html",
    "Valúrslit/2011/Sumba_files/index.html",
    "Valúrslit/2011/Svínoy_files/index.html",
    "Valúrslit/2011/Tjørnuvík_files/index.html",
    "Valúrslit/2011/Toftir_files/index.html",
    "Valúrslit/2011/Tórshavn_files/index.html",
    "Valúrslit/2011/Tvøroyri_files/index.html",
    "Valúrslit/2011/Vágur_files/index.html",
    "Valúrslit/2011/Velbastaður_files/index.html",
    "Valúrslit/2011/Vestmanna_files/index.html",
    "Valúrslit/2011/Viðareiði_files/index.html",]
    for path in paths:
        with open(path) as fp:
            soup = BeautifulSoup(fp, 'html.parser')
            partiesList = []

            votePlace = (soup.find('h2')).get_text()

            """ totalvotes = asd.find_all('td', style="text-align:right;border-top:1px solid black")[1].get_text()
            print("totalvotes",totalvotes) """

            """registerdVoters = asd.find_all('td', style="text-align:right")[15].get_text()
            print("registerdVoters",registerdVoters)"""

            date = (soup.find('title')).get_text()
            
            for party in soup.find_all('div', style="width:350px; overflow:auto; float:left"):
                voteList = []
                partyName = party.find('div', style="float:left").get_text()
                for personLinel in party.find_all('div', {"class": "linel"}):
                    name = (personLinel.find('div', {"class": "navn"})).get_text()
                    vote = (personLinel.find('div', {"class": "minisum"})).get_text()
                    voteList.append({'name': name, 'vote': vote})
                for personLined in party.find_all("div", {"class": "lined"}):
                    name = (personLined.find('div', {"class": "navn"})).get_text()
                    vote = (personLined.find('div', {"class": "minisum"})).get_text()
                    voteList.append({'name': name, 'vote': vote})
                partiesList.append({'partyName': partyName, 'partyVotes': voteList})
            for party in soup.find_all('div', style="width:350px; overflow:auto; float:right"):
                voteList = []
                partyName = party.find('div', style="float:left").get_text()
                for personLinel in party.find_all('div', {"class": "linel"}):
                    name = personLinel.find('div', {"class": "navn"}).get_text()
                    vote = personLinel.find('div', {"class": "minisum"}).get_text()
                    voteList.append({'name': name, 'vote': vote})
                for personLinel in party.find_all("div", {"class": "lined"}):
                    name = personLinel.find('div', {"class": "navn"}).get_text()
                    vote = personLinel.find('div', {"class": "minisum"}).get_text()
                    voteList.append({'name': name, 'vote': vote})
                partiesList.append({'partyName': partyName, 'partyVotes': voteList})
            yearList.append({'votePlace': votePlace, 'date': date, 'PartiesList': partiesList})
        fp.close()
    dataList.append({'year': '2011', 'yearList': yearList})
    with open('valData2011.json', 'w', encoding='utf-8') as f:
        json.dump(dataList, f, ensure_ascii=False, indent=4)

""" løgtingsval 2015 """
def Crawl2015():
    dataList = []
    yearList = []
    voteList = []
    partiesList = []
    for x in range(1, 58):
        time.sleep(1)
        result = requests.get("https://kvf.fo/val-historik/lv2015/index.php?vs=" + str(x))
        src = result.content
        asd = BeautifulSoup(src, 'lxml')
        partiesList = []

        votePlace = (asd.find('h2', style="margin:0")).get_text()
        print(votePlace)

        totalvotes = asd.find_all('td', style="text-align:right;border-top:1px solid black")[1].get_text()
        print("totalvotes",totalvotes)

        registerdVoters = asd.find_all('td', style="text-align:right")[15].get_text()
        print("registerdVoters",registerdVoters)

        date = (asd.find('td', style="width:50%;text-align:right;font-style:italic")).get_text()
        print(date)

        detail = asd.find("table", style="width:100%;border-collapse:separate")
        for party in detail.find_all("td", style="vertical-align:top; border: solid #000 1px;padding-right:2px;padding-left:2px"):
            voteList = []
            partyName = ""
            for votes in party.find_all('tr'):
                name = votes.find('td', style="width:155px;font-weight:bold;")
                vote = votes.find('td', style="width:25px; text-align:right")
                asdName = votes.find('td', style="width:155px;;")
                asdVote = votes.find('td', style="width:25px; text-align:right")
                if(name != None and vote != None):
                    name = name.get_text()
                    vote = vote.get_text()
                elif(asdName != None and asdVote != None):
                    asdName = asdName.get_text()
                    asdVote = asdVote.get_text()
                else:
                    partyName = (party.find('td', colspan="3")).get_text()

                if(name != None and vote != None):
                    voteList.append({'name': name, 'vote': vote})
                elif(asdName != None and asdVote != None):
                    voteList.append({'name': asdName, 'vote': asdVote})

            partiesList.append({'partyName': partyName, 'partyVotes': voteList})

        yearList.append({'votePlace': votePlace, 'date': date, 'totalVotes': totalvotes, 'registerdVoters': registerdVoters, 'PartiesList': partiesList})
    dataList.append({'year': '2015', 'yearList': yearList})
    with open('valData2015.json', 'w', encoding='utf-8') as f:
        json.dump(dataList, f, ensure_ascii=False, indent=4)

""" løgtingsval 2019 """
def Crawl2019():
    dataList = []
    yearList = []
    voteList = []
    partiesList = []
    for x in range(1, 58):
        time.sleep(1)
        result = requests.get("https://kvf.fo/val-historik/lv2019/data/ps-" + str(x) + ".html")
        src = result.content
        asd = BeautifulSoup(src, 'lxml')
        print(asd)
        partiesList = []

        votePlace = (asd.find('h2', class_="topheader")).get_text()
        print(votePlace)

        date = (asd.find('td', class_="taright")).get_text()
        print(date)

        detail = asd.find('table', class_="detail")
        for party in detail.find_all("td", "partydetail"):
            voteList = []
            partyName = ""
            for votes in party.find_all('tr'):
                name = votes.find('td', class_='c2')
                vote = votes.find('td', class_='c3')
                if(name != None and vote != None):
                    name = name.get_text()
                    vote = vote.get_text()
                else:
                    partyName = (party.find('td', colspan="2")).get_text()
                
                if(name != None and vote != None):
                    voteList.append({'name': name, 'vote': vote})
            
            partiesList.append({'partyName': partyName, 'partyVotes': voteList})

        yearList.append({'votePlace': votePlace, 'date': date, 'PartiesList': partiesList})
    dataList.append({'year': '2019', 'yearList': yearList})
    with open('valData2019.json', 'w', encoding='utf-8') as f:
        json.dump(dataList, f, ensure_ascii=False, indent=4)