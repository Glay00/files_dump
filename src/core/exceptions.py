from fastapi import HTTPException, status


class APIException(HTTPException):
    """
    Initialize the object with the provided status code, detail, and headers.

    Parameters:
        status_code (int | None): The status code for the response.
        detail (str | None): The detail message for the response.
        headers (dict[str, str] | None): The headers for the response.

    Returns:
        None
    """

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "A server error occurred."

    def __init__(
        self,
        status_code: int | None = None,
        detail: str | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        if detail is None:
            detail = self.default_detail
        if status_code is None:
            status_code = self.status_code

        super().__init__(status_code=status_code, detail=detail, headers=headers)
