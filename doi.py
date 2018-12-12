import requests


pages=["https://bmcmusculoskeletdisord.biomedcentral.com/articles/10.1186/s12891-017-1675-1",
       "https://onlinelibrary.wiley.com/doi/abs/10.1046/j.1532-5415.2001.49178.x",
       "http://www.onlinejacc.org/content/45/2/252",
       "https://www.sciencedirect.com/science/article/pii/S000287030110147X"
       ]




for x in pages:
           
    page=requests.get(x).text
    begin=page.find('doi.org')
    end=page[begin:].find('"')
    doi=page[begin:begin+end]
    print(doi)

