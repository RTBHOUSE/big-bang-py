if __name__ == "__main__":
    # Your project configuration should be stored in the environment.
    # See: https://12factor.net/config
    #
    # This Cookiecutter proposes a setup, where the environment is
    # loaded dynamically at runtime from an .env file (see `load_envs`
    # function for the details).
    #
    # WARNING!
    # In this setup do not import or run anything before loading the ENVs!
    #
    # Naturally, you can manage ENVs however you want. A well known alternative
    # is to run your project on Docker and either have ENVs preconfigured
    # or simply pass them during running up the containers.
    from envs.loader import load_envs
    load_envs()

    # It is usually a good idea to configure the logging as soon as possible.
    import logging.config
    from {{ cookiecutter.project_source_code_dir }}.logging_config import DICT_CONFIG
    logging.config.dictConfig(DICT_CONFIG)

    # Example of logging
    logger = logging.getLogger("main")
    logger.info("logging: configured")

    # And finally... Your startup code goes below! :)
    # For instance:
    from {{ cookiecutter.project_source_code_dir }}.app import App
    app = App()
    app.run()
