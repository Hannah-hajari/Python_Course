Dortmund_events = {
    "Museumsnacht": "19.09.2026",
    "Football Museum": "19.09.2026",
    "Dortmunder U Light Show": "19.09.2026",
    "Concert at FZW": "25.09.2026"
}
print("Events on Night of Museums (19.09.2026):")

for name, date in Dortmund_events.items():
    if date == "19.09.2026":
        print("*", name)