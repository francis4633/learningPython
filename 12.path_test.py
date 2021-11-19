import jsonpath
import  json

book_dict = '''{
    "store":{
        "book":[
            {"category": "reference",
             "author": "Nigel Rees",
             "title": "Saying of the Century",
             "price":9.85
            },
            {"category": "fiction",
             "author": "Evelyn Waugh",
             "title": "Sword of Honour",
             "price": 12.99
            },
            {"category": "fiction",
             "author": "Herman Melville",
             "title": "Moby Dick",
             "isbn": "0-553-21311-3",
             "price": 8.99
            },
            {"category": "fiction",
             "author": "J.R.R.Tolkien",
             "title": "The Lord of the Rings",
             "isbn": "0-359-19395-8",
             "price": 22.99
            } 
        ],
        "bicycle":{
            "color": "red",
            "price": 19.95
        }
    }
}'''

data = json.loads(book_dict)
#获取color的值   --->['red']
print(jsonpath.jsonpath(data, "$..color"))
#获取所有商品价格  --->[9.85, 12.99, 8.99, 22.99, 19.95]
print(jsonpath.jsonpath(data, "$..price"))



