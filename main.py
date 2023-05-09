from beautifulSoupService import SoupService
from codaService import CodaService
from flask import *
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    messageResult = ""
    if request.method == "GET":
        return render_template("home.html", result = "")

    if request.method == "POST":
        # assign URL
        #url_to_scrape = "https://www.estadao.com.br/"
        url_to_scrape = request.form["url"]
        url_to_scrape = url_to_scrape.strip()
        if  url_to_scrape == '':
            messageResult = "O campo URL é obrigatório"
            return render_template("home.html", result = messageResult)

        soupService = SoupService(url_to_scrape)
    try:
        soup = SoupService.getSoupDocument(soupService)
        # print(soup.title)
        # print(soup.get_text())

        codaService = CodaService(url_to_scrape, soup.title, soup.get_text())
        resColumn = CodaService.getColumnValue(url_to_scrape)
        #print(resColumn)
        #print(resColumn['items'])

        jsonResponse = json.dumps(resColumn['items'])
        #print(jsonResponse)
        data = json.loads('{"id":"i-l-7VewkOnH"}')
        rowid = data['id'] 
        # print(data)
        # print(data['id'])

        #print(len(resColumn["items"]))

        itemsLenght = len(resColumn["items"])

        if itemsLenght == 0:
            #print("Não foi encontrado nenhuma url com essa valor")
            res = CodaService.createRow(codaService)
            messageResult = "Inserção realizado com sucesso!"
            #print(f'Inserted 1 row')


        if itemsLenght > 0:
            #print("foi encontrado a url com essa valor")
            res = CodaService.update(codaService, rowid)
            messageResult = "Atualização realizado com sucesso!"
            #print(f'Updated row {res["id"]}')
            #print(request.form["url"])
        return render_template("home.html", result = messageResult)
    except:
        messageResult = "Ocorreu algum erro na requisição!"
        return render_template("home.html", result = messageResult)


if __name__ == "__main__":
    app.run()