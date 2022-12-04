from dash import Output, Input
from app.app_test import app
from app.pages import page_home

# logging.basicConfig(filename=f"{datetime.date.today()}_record.log", level=logging.DEBUG,
#                     format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    """
    Route l'utilisateur en fonction de l'URL
    """
    if pathname == "/":
        return page_home.layout()
    else:
        return "404"


if __name__ == '__main__':
    app.run_server(debug=True, port=5000, host="localhost", use_reloader=False)
