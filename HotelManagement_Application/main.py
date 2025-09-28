from repository import Repository
from services import Services
from ui import UI

repository = Repository()
services = Services(repository)
ui = UI(services)

ui.start()
