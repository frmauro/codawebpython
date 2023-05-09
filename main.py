from beautifulSoupService import SoupService
from codaService import CodaService
from flask import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form["url"]
        # assign URL
        #url_to_scrape = "https://www.estadao.com.br/"
        url_to_scrape = url

        soupService = SoupService(url_to_scrape)
        soup = SoupService.getSoupDocument(soupService)
        # print(soup.title)
        # print(soup.get_text())

        codaService = CodaService(url_to_scrape, soup.title)
        resColumn = CodaService.getColumnValue(url_to_scrape)
        #print(resColumn)
        #print(len(resColumn["items"]))

        itemsLenght = len(resColumn["items"])

        if itemsLenght == 0:
            print("Não foi encontrado nenhuma url com essa valor")
            res = CodaService.createRow(codaService)
            print(f'Inserted 1 row')


        if itemsLenght > 0:
            #print("foi encontrado a url com essa valor")
            res = CodaService.updateTitle(codaService)
            #print(f'Updated row {res["id"]}')
        #print(request.form["url"])
        return render_template("home.html", result = url)
    return render_template("home.html", result = "")

if __name__ == "__main__":
    app.run()