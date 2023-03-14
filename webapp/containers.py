from dependency_injector import containers, providers

from .database import Database
from .repositories import UserRepository, ProjectRepository
from .services import UserService, ProjectService


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=[".endpoints"])

    config = providers.Configuration(yaml_files=["config.yml"])

    db = providers.Singleton(Database, db_url=config.DATABASE_URL)

    user_repository = providers.Factory(
        UserRepository,
        session_factory=db.provided.session,
    )

    project_repository = providers.Factory(
        ProjectRepository,
        session_factory=db.provided.session,
    )

    user_service = providers.Factory(
        UserService,
        user_repository=user_repository,
    )

    project_service= providers.Factory(
         ProjectService,
         project_repository=project_repository,
    )