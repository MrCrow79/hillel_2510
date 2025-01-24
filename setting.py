import dynaconf

d_settings = dynaconf.Dynaconf(
    settings_files=["settings.ini", "secrets.ini"],
    environments=True,
    load_dotenv=True,
    envvar_prefix="DYNACONF",
)