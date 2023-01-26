from core import load_modules

triggers = load_modules("triggers")
monitors = load_modules("monitors")


while True:
    for m in monitors:
        m.on_update(triggers)
