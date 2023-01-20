import glob


def load_modules(group: str):
    return list(
        map(
            lambda installable: installable(),
            map(
                lambda module: getattr(
                    getattr(__import__(f"{group}.{module}"), module), module
                ),
                map(
                    lambda path: path.replace("\\", ".")
                    .replace("/", ".")
                    .split(".")[1],
                    glob.glob(f"{group}/*.py"),
                ),
            ),
        )
    )
