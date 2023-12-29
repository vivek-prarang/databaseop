from io import StringIO
from threading import Thread
import csv
class CSV_Scraper:
    def get_csv_info(self,file_contents):   
        csv_reader = csv.reader(StringIO(file_contents))
        headers = next(csv_reader, [])
        row_count = sum(1 for row in csv_reader)
        return headers, row_count

    def scrape_titles(self,request):
        if request.method == 'POST':
            file = request.files['file']
            try:            
                file_contents = file.read().decode('utf-8')
                headers, row_count = self.get_csv_info(file_contents)
                return  headers, row_count
            except:
                return None, None
                
            

            
        
        