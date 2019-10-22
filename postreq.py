# import requests
#
# # #get
# # req = requests.get("https://financialmodelingprep.com/api/v3/financials/income-statement/AAPL,FB,GOOG")
# # print(req.status_code)
#
# #post --endpoint , and data along with it
# url = "https://jsonplaceholder.typicode.com/posts"
# data = {
#     "title": 'foo',
#     "body": 'bar',
#     "userId": 1
# }
# req2=requests.post(url=url,data=data)
# print(req2.text)


itms = ["abce","ac","acd"]
itms2 = sorted(itms,key=len)
print(itms2)
itms.sort(key=len)
print(itms)