import csv
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)
        
    def output_html(self):
        with open('output.csv', 'wb') as csvfile:
            fieldnames = ['url', 'name', 'title', 'sex', 'birthday', 'hometown', 'education']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for data in self.datas:
                #writer.writerow(data['url'].encode('GBK'), data['name'].encode('GBK'), data['title'].encode('GBK'), data['sex'].encode('GBK'), data['birthday'].encode('GBK')
                             #% data['hometown'].encode('GBK'), data['education'].encode('GBK'))
                writer.writerow({'url':data['url'].encode('GBK'), 'name':data['name'].encode('GBK'), 'title': data['title'].encode('GBK'), 'sex': data['sex'].encode('GBK'),
                                 'birthday':data['birthday'].encode('GBK'), 'hometown': data['hometown'].encode('GBK'), 'education':data['education'].encode('GBK')})
if __name__== "__main__":
    data = {'url': 'Wonderful', 'name':'haha','title': 'Spam'}
    print data['url']
    obj_spider = HtmlOutputer()
    obj_spider.collect_data(data)
    obj_spider.output_html()