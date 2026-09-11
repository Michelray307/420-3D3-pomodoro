from models.minuteur import Minuteur
from views.dashboard import Dashboard

donnes = Minuteur()

app = Dashboard(donnes)
app = app.mainloop()