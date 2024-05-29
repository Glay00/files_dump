from sqlalchemy.ext.asyncio import AsyncSession


class BaseController:
    """
    Initialize the class with the given AsyncSession.

    :param session: The AsyncSession to be assigned to self.session.
    :type session: AsyncSession
    """

    def __init__(self, session: AsyncSession):
        self.session = session


base_controller: BaseController = None  # noqa: RUF100


def get_base_controller():
    if base_controller is None:
        raise RuntimeError("BaseController is not initialized.")
    return base_controller
