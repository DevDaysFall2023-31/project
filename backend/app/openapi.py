from fastapi.openapi.utils import get_openapi
from app.uwsgi import app
import json


print(
    json.dumps(
        get_openapi(
            title=app.title,
            version=app.version,
            openapi_version=app.openapi_version,
            description=app.description,
            routes=app.routes,
        ),
        indent=2,
    )
)
