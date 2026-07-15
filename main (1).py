


from fastapi import FastAPI



from database import (

    Base,

    engine

)



from routers import (

    integrations,

    events,

    files

)





Base.metadata.create_all(

    bind=engine

)





app=FastAPI(


    title=
    "Cloud Integration Hub",


    description=

    """
    Enterprise SaaS Integration Platform

    Features:
    - Async webhook processing
    - SaaS API integrations
    - Cloud storage workflows
    - Event driven architecture

    """,


    version="1.0"

)





app.include_router(

    integrations.router

)



app.include_router(

    events.router

)



app.include_router(

    files.router

)






@app.get("/")

def home():


    return {


        "status":

        "Cloud Integration Hub Running"

    }
